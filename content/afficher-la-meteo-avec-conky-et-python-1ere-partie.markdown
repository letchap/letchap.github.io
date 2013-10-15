Title: Afficher la meteo avec conky et python 1ère partie
Date: 2013-07-08 21:56
Category: Python
Tags: Python, Wunderground, conky, crunchbang
Slug: afficher-la-meteo-avec-conky-et-python-1ere-partie

Sur mon joli bureau openbox sur Crunchbang, j'aimerais pouvoir afficher à la demande les informations concernant la meteo au moyen d'un raccourci clavier ou d'un menu, puis refermer la fenêtre quand je n'en ai plus besoin. Evidemment, je veux des infos fraîches, avec un affichage sympa, et en consommant très peu de ressources machine.

Tout d'abord, le résultat final :
 
![memo markdown]({filename}/images/conky_meteo.png "écran conky")

Pour réaliser cela, nous allons mettre en oeuvre plusieurs élements :

- un programme python qui va recueillir les informations météo sur un site spécialisé et stocker les informations dans un fichier texte
- une automatisation de ce programme sous forme d'un démon qui se lancera au démarrage de l'ordinateur
- un conky pour afficher à la demande la météo et la mettre en forme sur la base des informations contenues dans le fichier texte

Le tutoriel sera découpé en chacune de ces trois parties et nous commençons cette première partie par le programme python.

### Wunderground

Wunderground sera notre fournisseur de données météorologiques. Pourquoi Wunderground, parce qu'il fournit une API, une sorte de clé, qui va nous permettre de récupérer facilement des informations météo complètes. En une seule requête, vous disposez de prévisions riches sur les quatre prochains jours.

Les informations ainsi récupérées sont disponibles dans un format xml ou json, facilement lisibles car balisées. Le programme a été écrit pour un format json, rien ne vous empêche de le transposer pour un format xml, les grands principes resteront les mêmes.

La première étape consiste à s'inscrire sur le site de wunderground [à cette adresse](http://www.wunderground.com/weather/api/d/login.html "S'inscrire sur Weather Underground") pour obtenir une clé pour l'API. En bonus, vous avez à votre disposition des outils pour tester une requête et des exemples de code dans différents langages, dont Python.

L'inscription est gratuite dans la limite d'une utilisation non commerciale et de 10 requêtes par minute. Parfait pour un usage privé.


### Le script

Le but de ce programme est de se connecter régulièrement au site wunderground, de récupérer les informations qui nous intéressent et de créer un fichier texte lisible par un conky. 

Ce script est largement inspiré d'une part du tutoriel python sur [full circle HS n°2](http://www.fullcirclemag.fr/?pages/Numéros) et sur [ce forum](http://www.archlinux.fr/forum/viewtopic.php?t=9981&p=107541).

Tous les commentaires sont dans le script.

{% include_code meteo.py %}

Pour mieux comprendre la façon dont sont récupérées les données, prenons un exemple avec un morceau de fichier json et le code Python correspondant. Nous allons récupérer l'information concernant la ville.

Le morceau du fichier JSON qui nous intéresse ressemble à çà :

	#!javascript
	"current_observation":  {
			"image":  {
			  "url": "http://icons-ak.wxug.com/graphics/wu2/logo_130x80.png",
			  "title": "Weather Underground",
			  "link": "http://www.wunderground.com"
			},
			"display_location":  {
			  "full": "Paris, France",
			  "city": "Paris",
			  "state": "",
			  "state_name": "France",
			  "country": "FR",
			  "country_iso3166": "FR",
			  "zip": "00000",
			  "latitude": "48.86666489",
			  "longitude": "2.33333302",
			  "elevation": "47.00000000"
			},

Pour trouver la bonne information, il suffit de suivre les branches de l'arbre. L'information "Paris" se trouve dans "city", qui se trouve dans "display_location" qui se trouve dans "current_observation". Ce qui se traduira en python par : 
	
	:::javascript
    city = parsed_json['current_observation']['display_location']['city']

Le fichier texte final ressemble à ça :
	
	Meteo = Ciel dégagé
	Ville = Paris
	Derniere_observation = Last Updated on juillet 9, 20:05 CEST
	Temperature = 27.1 °C
	Ressentie = 27.1 °C
	Humidite = 56%
	Vent = 14.5 km/h
	Dir_vent = NE
	Pression = 1020 mb
	Tend_pres = stable
	Visibilite = 10.0 km
	Indice_UV = 0
	jour1_jour = 9
	jour1_mois = juillet
	jour1_annee = 2013
	jour1_jour_sem = mardi
	jour1_tempmax = 29 °C
	jour1_tempmin = 20 °C
	jour1_conditions = Ciel dégagé
	jour1_icone = clear
	jour1_pop = 0%
	jour1_hauteur_precip = 0.0 mm
	jour1_hauteur_neige = 0 cm
	jour1_vent = 16 km/h
	jour1_dir_vent = NE
	jour1_tx_himidite = 57%
	jour2_jour = 10
	jour2_mois = juillet
	jour2_annee = 2013
	jour2_jour_sem = mercredi
	jour2_tempmax = 27 °C
	jour2_tempmin = 16 °C
	jour2_conditions = Ciel dégagé
	jour2_icone = clear
	jour2_pop = 0%
	jour2_hauteur_precip = 0.0 mm
	jour2_hauteur_neige = 0 cm
	jour2_vent = 18 km/h
	jour2_dir_vent = NNE
	jour2_tx_himidite = 61%
	jour3_jour = 11
	jour3_mois = juillet
	jour3_annee = 2013
	jour3_jour_sem = jeudi
	jour3_tempmax = 24 °C
	jour3_tempmin = 15 °C
	jour3_conditions = Ciel dégagé
	jour3_icone = clear
	jour3_pop = 0%
	jour3_hauteur_precip = 0.0 mm
	jour3_hauteur_neige = 0 cm
	jour3_vent = 18 km/h
	jour3_dir_vent = NNE
	jour3_tx_himidite = 55%
	jour4_jour = 12
	jour4_mois = juillet
	jour4_annee = 2013
	jour4_jour_sem = vendredi
	jour4_tempmax = 27 °C
	jour4_tempmin = 16 °C
	jour4_conditions = Ciel dégagé
	jour4_icone = clear
	jour4_pop = 0%
	jour4_hauteur_precip = 0.0 mm
	jour4_hauteur_neige = 0 cm
	jour4_vent = 16 km/h
	jour4_dir_vent = NNE
	jour4_tx_himidite = 57%


### Le démon

Afin de pouvoir interroger régulièrement le site Wunderground, nous allons "démoniser" le programme, c'est à dire que nous allons lui demander de se déclencher à intervalle régulier (dans le script 120 secondes)

Pour cela, il suffit de suivre l'exemple suivant, en ayant installé préalablement python-daemon par un `sudo apt-get install python-daemon`.

	#!python
	import time
	from daemon import runner

	class App(): 
		def __init__(self):
			self.stdin_path = '/dev/null'
			self.stdout_path = '/dev/null'
			self.stderr_path = '/dev/null'
			self.pidfile_path = '/tmp/meteo.pid'
			self.pidfile_timeout = 5
		
		def run(self): 
			
			while True:
				# Le corps du programme
				time.sleep(1200)

	app = App()
	daemon_runner = runner.DaemonRunner(app)
	daemon_runner.do_action()

Le programme ainsi démonisé se lance par :
	
	:::bash
    $ python meteo.py start

Vous voir le résultat par exemple par un :
	
	#!bash
    $ ps -ef | grep meteo
    root      2413     1  0 22:30 ?        00:00:00 python /usr/sbin/meteo.py start

Il s'arrête par :

    :::bash
	$ python meteo.py stop

Nous pouvons bientôt passer à la deuxième étape : [le lancement automatique du programme python au démarrage de l'ordinateur]({filename}/afficher-la-meteo-avec-conky-et-python-2eme-partie.markdown).
