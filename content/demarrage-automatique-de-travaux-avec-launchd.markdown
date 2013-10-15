Title: Démarrage automatique de travaux avec launchd
Date: 2013-08-08 23:04
Category: Mac OS X
Tags: Mac OS X, launchd, launchctl, plist, cron, anacron
Slug: demarrage-automatique-de-travaux-avec-launchd

Aujourd'hui nous allons (temporairement) quitter le monde GNU/Linux pour celui de Mac OS X et voir comment réaliser l'équivalent de cron / anacron sur OS X avec l'utilitaire launchd. 

Le besoin de départ est de lancer tous les mois à date fixe un programme python, y compris au redémarrage du Mac si celui est éteint le jour du lancement programmé (ce dernier point n'est d'ailleurs pas permis nativement par le couple cron / anacron).

Pour rédiger cet article, je me suis inspiré d'une part de [ce post en anglais](http://nathangrigg.net/2012/07/schedule-jobs-using-launchd/ "Schedule jobs using launchd") et d'autre part de la [documentation apple sur launchd et la création d'agents](http://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html "Création de démons et d'agents sur OS X")

Le principe de fonctionnement est le suivant : au démarrage du Mac, l'utilitaire Mac OS X launchd liste l'ensemble des travaux faisant l'objet d'un lancement programmé. Et pour programmer un lancement automatique, il va nous falloir deux éléments :

* un agent permettant de déclencher le travail en question 
* puis ajouter notre agent à la liste des travaux programmés.

### L'agent : le fichier de configuration plist

L'agent va se définir dans un fichier xml avec une extension plist. Ce fichier contient des informations sur le programme à lancer avec ses éventuels paramètres de lancement ainsi que les informations sur la fréquence de déclenchement. 

Les fichiers plist que vous allez créer sont à stocker de préférence dans le répertoire ~/Library/LaunchAgents. Le gros avantage de les créer à cet endroit est que vos agents launchd seront pris en compte automatiquement au démarrage du Mac.

La convention de nommage d'un fichier plist est de prendre un nom de domaine à l'envers. Ici, comme mon programme python récupère les factures freebox, je l'ai simplement appelé fr.free.facture.plist.

Détaillons un peu le fichier plist :

	#!xml
	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
	<plist version="1.0">
	<dict>
		<key>Label</key>
		<string>fr.free.facture</string>
		<key>ProgramArguments</key>
		<array>
			<string>/usr/bin/python</string>
			<string>/usr/local/bin/free.py</string>
		</array>
		<key>StartCalendarInterval</key>
		<dict>
			<key>Hour</key>
			<integer>7</integer>
			<key>Minute</key>
			<integer>0</integer>
			<key>Day</key>
			<integer>6</integer>
		</dict>
	</dict>
	</plist>

Les 3 premières lignes sont des informations d'entête, en particulier, nous voyons que nous avons bien à faire à un format xml. Ces lignes d'entête peuvent être reprises sans modification.

La partie intéressante se situe après.

D'abord, en lignes 5 et 6  nous nommons notre agent (avec le même nom que le fichier, c'est plus simple).

Puis nous donnons des informations sur le programme à lancer. Et là : **ATTENTION !!!!** :

* Il faut absolument mettre les chemins sous forme absolue et non relative si vous ne voulez pas vous embêter avec le PATH de launchd,
* Il faut absolument lui donner le chemin vers l'interpréteur python.

Si vous ne faites pas ça, vous allez pouvoir lancer votre agent à la main depuis le terminal (ce que nous allons voir juste après) et cela va très bien se passer, et vous ne comprendrez pas pourquoi cela ne fonctionne pas au démarrage de l'ordinateur. Les chemins complets vers le programme et l'interpréteur vous éviterons quelques migraines.

Enfin, nous renseignons les éléments de périodicité. Dans cet exemple, nous déclenchons notre programme tous les 6 du mois à 7h00. Le fait que le mois ne soit pas renseigné signifie "tous les mois".

Il est possible de renseigner d'autres types de fréquence, par exemple tous les 90 secondes, ainsi que tout un tas d'options. Le plus simple est de se référer à la documentation apple sur launchd (voir le lien en début d'article).


### Ajout à la liste des travaux programmés

Il existe deux façons d'ajouter notre agent la liste des travaux pris en charge par launchd.

La première, que je ai déjà évoqué, est de placer le fichier plist dans le bon répertoire, à savoir ~/Library/LaunchAgents. La seule contrainte est de redémarrer l'ordinateur pour prise en compte de l'agent.

Si vous n'avez pas envie d'attendre jusqu'au prochain reboot, ou même si vous souhaitez tester votre agent, il existe un utilitaire disponible à partir du terminal et permettant de gérer ses agents, launchctl :

* `$ launchctl list` permet de lister les agents actifs
* `$ launchctl load /chemin/vers/monagent.plist` permet de charger l'agent dans la liste prise en compte par launchd, le programme sera alors démarrer avec la périodicité définie dans le fichier plist. Si vous avez le moindre message d'erreur au chargement, c'est que le fichier plist est mal formaté.
* `$ launchctl start monagent` permet de déclencher manuellement et immédiatement l'agent. Cela permet de tester son bon fonctionnement. Ici, c'est le nom de l'agent que nous donnons, pas le nom du fichier.

Maintenant que mon programme tourne tout seul sans que j'intervienne, j'aimerais qu'il m'envoie un petit message dans le centre de notification pour dire qu'il a bien travaillé, ce sera l'objet du prochain article, et après retour à GNU/Linux.




