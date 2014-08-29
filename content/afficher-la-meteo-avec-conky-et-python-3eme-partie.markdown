Title: Afficher la meteo avec conky et python 3ème partie
Date: 2013-07-10 22:43
Category: Conky
Tags: Python, Wunderground, conky, Crunchbang
Slug: afficher-la-meteo-avec-conky-et-python-3eme-partie

Dans les deux premiers épisodes de ce tutoriel, [nous avons créé un programme python]({filename}/afficher-la-meteo-avec-conky-et-python-1ere-partie.markdown) récupérant les informations météo sur le site de [wunderground](http://www.wunderground.com/), puis nous avons automatisé ce script [afin qu'il se lance au démarrage de notre session]({filename}/afficher-la-meteo-avec-conky-et-python-2eme-partie.markdown). Il ne reste plus qu'à afficher les informations sur notre bureau.

Pour cela, nous allons devoir :

- créer un conky météo (plusieurs en fait)
- créer un petit programme bash de démarrage / arrêt du conky météo
- créer les entrées de ce petit programme, dans le fichier menu.xml pour le menu openbox, et dans le fichier rc.xml pour les touches de raccourcis



### Les icones

Je suis allé les chercher chez [merlinthered sur devianart](http://merlinthered.deviantart.com). Je les ai renommées en fonction du nom que je leur ai donné dans le programme python.

### Le conky

Conky va nous permettre d'afficher sur le bureau les informations meteo contenu dans le fichier texte alimenté par le programme python

Tout d'abord, il faut installer conky. Sur Crunchbang, il est installé par défaut, sinon `sudo apt-get install conky`

Ensuite, nous allons réaliser non pas un mais quatre script conky, un par jour de prévision. Conky ne sait pas gérer les colonnes, à moins de bidouiller avec la commande ${goto}. Donc nous allons coller quatre conky pour réaliser une jolie présentation.

Voilà, à la suite, les quatre fichiers. Ces fichiers sont à copier dans le répertoire /home/monuser/.conky/ :

{% code content/code/conkyrc_meteo %}
[Télécharger conkyrc_meteo]({filename}/code/conkyrc_meteo){: class="button radius tiny" title="Télécharger conkyrc_meteo" }

{% code content/code/conkyrc_meteo_jour2 %}
[Télécharger conkyrc_meteo_jour2]({filename}/code/conkyrc_meteo_jour2){: class="button radius tiny" title="Télécharger conkyrc_meteo_jour2" }

{% code content/code/conkyrc_meteo_jour3 %}
[Télécharger conkyrc_meteo_jour3]({filename}/code/conkyrc_meteo_jour3){: class="button radius tiny" title="Télécharger conkyrc_meteo_jour3" }

{% code content/code/conkyrc_meteo_jour4 %}
[Télécharger conkyrc_meteo_jour4]({filename}/code/conkyrc_meteo_jour4){: class="button radius tiny" title="Téléchargerconkyrc_meteo_jour4" }


Pour positionner les différentes informations, il faut jouer d'abord avec minimum_size, maximum_with, gap_x, gap_y pour les quatre fenêtres, puis avec alignr, alignc, goto et voffset pour le contenu de chacune des fenêtres.

La documentation conky est [ici](http://conky.sourceforge.net/documentation.html)

L'astuce pour récupérer les infos, je l'ai trouvé [sur ce forum](http://www.archlinux.fr/forum/viewtopic.php?t=9981&p=107541), le même qui m'avait permis de créer le squelette du programme python. Tout tient dans la ligne suivante :

	:::bash
    ${execp grep jour2_icone ~/tmp/meteo.txt | awk -F " " '{print "${image ~/images/icone_meteo/" $3 ".png -p 58,10 -s 64x64}"}'}

Cela me permet d'aller récupérer dans le fichier meteo.txt le nom de l'icone et de l'afficher dans mon conky. Pour bien comprendre cette ligne, il faut connaître les commandes grep, awk et les tubes. Vous trouverez une saine lecture concernant les commandes unix [chez framabook](http://framabook.org/unix-pour-aller-plus-loin-avec-la-ligne-de-commande/).

Nous voyons l'importance dans le programme python de ne pas générer de doublon dans le nom des informations, sinon cela interdit le bon fonctionnement de grep.

### L'appel et la fermeture du conky météo

Je ne souhaite pas avoir en permanence les informations météo affichées sur mon bureau mais uniquement à la demande. Pour cela nous allons créer un petit programme de démarrage/arrêt du conky et créer des raccourcis dans le menu openbox et dans celui définissant les touches de raccourcis.

Le programme le voici :

{% code content/code/startstopmeteo.sh %}
[Télécharger startstopmeteo.sh]({filename}/code/startstopmeteo.sh){: class="button radius tiny" title="startstopmeteo.sh" }


Il ne reste plus qu'à créer une entrée dans le fichier menu.xml, par exemple comme ci :

	:::xml
    <item label="Meteo">
        <action name="Execute">
            <command>
                startstopmeteo.sh
            </command>
        </action>
    </item>

Et une entrée dans le fichier rc.xml pour les touches de raccourcis, comme cela :

	:::xml
    <!-- Meteo -->
    <keybind key="W-A-m">
      <action name="Execute">
        <command>~/bin/startstopmeteo.sh</command>
      </action>
    </keybind>

Et voilà, c'est fini. Une météo en un clic !

Pour résumer, il vous faut :

- s'inscrire sur le site de wunderground
- créer un script python pour récupérer les informations de wunderground
- le démoniser
- le lancer au démarrage de l'ordinateur
- récupérer de jolies icones
- créer les conky
- créer un script arret/relance des conky
- créer les entrées pour ce script dans le menu et les touches de raccourcis
