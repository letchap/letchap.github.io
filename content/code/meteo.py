#!/usr/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------
# Créé par letchap
# meteo.py
#----------------------------------------------------
""" récupère les informations météo grace à l'API du site wunderground.com """ 

#import pour les infos meteo
import os.path
import urllib2
import json
import sys
# import pour le démon
import time
from daemon import runner

#=========================================================== 
#       La classe
#===========================================================        

class App(): 
    # Tout ça, c'est pour le démon
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null' # J'ai remplacé /dev/tty par dev/null pour éviter les plantages au démarrage par init.d
        self.stderr_path = '/dev/null' # J'ai remplacé /dev/tty par dev/null pour éviter les plantages au démarrage par init.d
        self.pidfile_path = '/tmp/meteo.pid'
        self.pidfile_timeout = 5
    
    # Bien appelé la fonction 'run' pour le démon
    def run(self): 
    
        
        while True: # C'est le début de ma boucle pour démoniser mon programme
        
            ###############################################
            #           Le corps du programme             #
            ###############################################
            try:
            # Je récupère les informations fournies par wunderground grâce à leur api, au format json,
            # en une seule fois (forecast et conditions), et en français
            # Un exemple de code est fourni sur le site wunderground
        
            # Je charge ma page meteo
                page_json = urllib2.urlopen('http://api.wunderground.com/api/macleapi/forecast/conditions/lang:FR/q/France/Paris.json?paris=I75003PA1')
                # Je lis la page
                json_string = page_json.read()
                # Je mets cette page dans un parseur
                parsed_json = json.loads(json_string)
                # Et je peux fermer ma page meteo, je n'en ai plus besoin
                page_json.close()
            except: 
                print 'Les informations météo ne sont pas accessibles sur le site wunderground.com' 
                sys.exit(2) # pour sortir du programme si la requête n'aboutit pas

            # Je récupère les informations du jour stokées sur le tag "current_observation"
            # Je fais attention à avoir des variables uniques dans le cas où je fais une recherche sur une chaîne de
            # caractère plus tard (avec un grep par exemple).

            city = parsed_json['current_observation']['display_location']['city'] # la ville
            last_observation = parsed_json['current_observation']['observation_time'] # l'heure dernière observation
            current_temp = parsed_json['current_observation']['temp_c'] # la température en °C
            current_weather = parsed_json['current_observation']['weather'] # le temps actuel
            humidity = parsed_json['current_observation']['relative_humidity'] # le taux d'humidité en %
            wind_kph = parsed_json['current_observation']['wind_kph'] # la vitesse du vent
            wind_dir = parsed_json['current_observation']['wind_dir'] # l'orientation du vent
            pressure_mb = parsed_json['current_observation']['pressure_mb'] # la pression atmosphérique
            pressure_trend = parsed_json['current_observation']['pressure_trend'] # l'evolution pression atmosphérique
            feelslike_c = parsed_json['current_observation']['feelslike_c'] # la température ressentie
            visibility = parsed_json['current_observation']['visibility_km'] # la visibilité en km
            UV = parsed_json['current_observation']['UV'] # l'indice UV
            
            # Un petit test sur l'indice UV qui peut être négatif
            if str(UV) == '-1':
                UV = 0
            
            # Une petite transformation de la tendance atmosphérique
            
            if pressure_trend == '-':
                pressure_trend = 'en baisse'
            elif pressure_trend == '+':
                pressure_trend = 'en hausse'
            else:
                pressure_trend = 'stable'
            
            # J'écris ces informations dans un fichier qui servira plus tard pour le conky meteo.
            # En ouvrant le fichier en mode 'w', j'écrase le fichier meteo.txt précédent 
            # Je transforme tous les chiffres en chaînes de caractères et j'encode tous les textes français en UTF8    
            # Je n'ai pas besoin de fermer le fichier en utilisant "with open"

            with open('/home/letchap/tmp/meteo.txt', 'w') as f: 
                f.write("Meteo = " + current_weather.encode('utf8') + "\n")
                f.write("Ville = " + city.encode('utf8') + "\n")
                f.write("Derniere_observation = " + last_observation.encode('utf8') + "\n")
                f.write("Temperature = " + str(current_temp) + " °C\n")
                f.write("Ressentie = " + str(feelslike_c) + " °C\n")
                f.write("Humidite = " + humidity + "\n")
                f.write("Vent = " + str(wind_kph) + " km/h\n")
                f.write("Dir_vent = " + wind_dir + "\n")
                f.write("Pression = " + str(pressure_mb) + " mb\n")
                f.write("Tend_pres = " + pressure_trend.encode('utf8') + "\n") #Ok, l'utf8 ne sert à rien là
                f.write("Visibilite = " + str(visibility) + " km\n")
                f.write("Indice_UV = " + str(UV) + "\n")
            
            
            
            # Je récupère les prévisions sous le tag "simpleforecast", en bouclant sur chacune des périodes
            forecast = parsed_json['forecast']['simpleforecast']['forecastday']
            for i in forecast:
                jour           = i['date']['day']        # jour
                mois           = i['date']['month']      # mois
                annee          = i['date']['year']       # année
                jour_sem       = i['date']['weekday']    # jour de la semaine
                period         = i['period']             # période
                tempmax        = i['high']['celsius']    # température maximale
                tempmin        = i['low']['celsius']     # température minimale
                condition      = i['conditions']         # conditions
                icon           = i['icon']               # icone en lien avec condition
                skyicon        = i['skyicon']            # le couverture nuagueuse
                pop            = i['pop']                # probabilité de précipitation
                hauteur_precip = i['qpf_allday']['mm']   # hauteur de précipitation pour la journée
                hauteur_neige  = i['snow_allday']['cm']  # hauteur de neige pour la journée
                vent           = i['avewind']['kph']     # vitesse moyenne du vent
                vent_dir       = i['avewind']['dir']     # direction du vent
                tx_humidite    = i['avehumidity']        # taux d'humidité

                # Je définis chacune de mes 4 périodes
                if period == 1:
                    date = 'jour1'
                elif period == 2:
                    date = 'jour2'
                elif period == 3:
                    date = 'jour3'
                elif period == 4:
                    date = 'jour4'
                
                # Encore un petit test pour les icones. Je combine icon et skyicon pour avoir la représentation graphique 
                # la plus proche de la réalité en particulier "partiellement couvert et pluvieux" qui n'existe pas
                # D'abord je définis 3 listes pour l'orage, la pluie et la neige
                orage = ['tstorms','chancetstorms','nt_tstorms', 'nt_chancetstorms']
                pluie = ['rain','chancerain','nt_rain', 'nt_chancerain', ]
                neige = ['snow','flurries','chancesnow','chanceflurries','nt_snow','nt_flurries','nt_chancesnow','nt_chanceflurries','sleet', 'nt_sleet','chancesleet','nt_chancesleet']
                # puis je définis mes icones
                if icon in orage:
                    icone = skyicon+"storm"
                elif icon in pluie:
                    icone = skyicon+"rain"
                elif icon in neige:
                    icone = skyicon+"snow"
                else:
                    icone = icon
                
                # J'écris à la suite, grâce à l'option 'a' append au lieu de 'w'
                with open('/home/letchap/tmp/meteo.txt', 'a') as f:
                    f.write(date + "_jour = "  + str(jour) + "\n")
                    f.write(date + "_mois = "  + str(mois) + "\n") 
                    f.write(date + "_annee = "  + str(annee) + "\n")     
                    f.write(date + "_jour_sem = "  + jour_sem.encode('utf8') + "\n")  # C'est du luxe, il n'y a pas d'accent dans les jours de la semaine
                    f.write(date + "_tempmax = "  + str(tempmax) + " °C\n")     
                    f.write(date + "_tempmin = "  + str(tempmin) + " °C\n")                              
                    f.write(date + "_conditions = " + condition.encode('utf8') + "\n")
                    f.write(date + "_icone = " + icone + "\n")
                    f.write(date + "_pop = "  + str(pop) + "%\n")            
                    f.write(date + "_hauteur_precip = "  + str(hauteur_precip) + " mm\n")            
                    f.write(date + "_hauteur_neige = "  + str(hauteur_neige) + " cm\n")            
                    f.write(date + "_vent = "  + str(vent) + " km/h\n")            
                    f.write(date + "_dir_vent = "  + vent_dir + "\n")             
                    f.write(date + "_tx_himidite = "  + str(tx_humidite) + "%\n")            
    
            ############################################
            #             Le fin du programme          #
            ############################################
            
            time.sleep(120) # C'est la fin de ma boucle de démonisation. La temporisation est de 120 secondes

# Toujours commencer la lecture d'un programme python par la fin. C'est là qu'on lance le démon
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
