Title: Envoyer une notification au centre de notification de Mountain Lion avec Python
Date: 2013-08-29 21:20
Category: Mac OS X
Tags: PyObjC, Python, Mac OS X, Mountain Lion
Slug: envoyer-une-notification-au-centre-de-notification-de-mountain-lion-avec-python

[Dans mon dernier article]({filename}/demarrage-automatique-de-travaux-avec-launchd.markdown "Démarrage automatique de travaux avec launchd"), nous avons vu comment programmer le déclenchement périodique d'un programme dans Mountain Lion grace à l'utilitaire launchd. J'aimerais maintenant être averti de la bonne exécution de mon programme via le centre de notifciation de Mountain Lion.

Ce qui est décrit ci-dessous est librement inspiré de cet [article en anglais](http://dbader.org/blog/alfred-timer-extension "A countdown timer extension for Alfred").

Pour pouvoir envoyer un message dans le centre de notification de Mountain Lion et afficher une pop-up, il faut obligatoirement que l'application soit reconnu par Apple via le "bundle identifier". Pour mon petit programme Python à moi, je ne vais pas demander un identifiant, alors pour pouvoir malgré tout envoyer un message, je vais adopter la stratégie du coucou et emprunter un bundle identifier existant. Par exemple celui de du programme Python Launcher (puisque que je lance un programme Python). Je vais donc faire croire au centre de notification que c'est l'application Python Launcher qui envoie un message.

Tout d'abord, comment récupérer le bundler identifier? Avec la commande suivante dans le terminal :

    $ osascript -e 'id of app "Python Launcher"'
    org.python.PythonLauncher

Maintenant, décorons !

{% include_code decorateur.py %}

Le principe de base est de "décorer" la fonction renvoyant le bundle identifier, c'est à dire que nous affectons son comportement temporairement (mais sans la modifier), pour qu'elle renvoie l'identifiant que nous lui passons. Pour cela, nous utilisons un décorateur Python. Pour plus d'informations sur le fonctionnement des décorateurs, vous pouvez aller sur le [site du zéro](http://www.siteduzero.com/informatique/tutoriels/apprenez-a-programmer-en-python/les-decorateurs "Les décorateurs Python") ou sur [le blog de Sam et Max](http://sametmax.com/comprendre-les-decorateurs-python-pas-a-pas-partie-1/ "Les décorateurs Python première partie").

Ensuite dans la fonction notify(), nous envoyons un message au centre de notification de Mountain Lion qui pensera que c'est l'application Python Launcher qui envoie le flux. Colossale feinte de sioux !

Le résultat en image

![exemple notification]({filename}/images/notif.png)

Le tout s'appuie sur le projet PyObjC qui développe une passerelle entre Python et ObjC et dont vous trouverez la documentation [ici](http://pythonhosted.org/pyobjc/ "Python ObjC").

Contrairement au paquet pync (un wrapper Python de terminal-notifier qui permet d'envoyer des messages au centre de notification depuis le terminal) qui ne sait pas envoyer des messages hors d'une session du terminal, ici, il sera possible d'envoyer des notifications même si le programme est déclenché en mode batch par launchd.

Voilà, c'est tout pour Mac OS X pour le moment, la prochaine fois, retour sur Linux. 

Pour la petite histoire, ce qu'on vient de faire tient en trois lignes de code sous Linux grâce à la bibliothèque pynotify :
	
	#!python
    pynotify.init("Free.py")
    n = pynotify.Notification(
        "Titre\n", # Titre
        "Message", # Message
        "/home/letchap/Image/application_pdf.png") # Image
    n.show()

