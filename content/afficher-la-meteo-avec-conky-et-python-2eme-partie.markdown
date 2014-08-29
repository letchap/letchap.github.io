Title: Afficher la meteo avec conky et python 2ème partie
Date: 2013-07-09 20:52
Category: Linux
Tags: Python, Wunderground, conky, Crunchbang
Slug: afficher-la-meteo-avec-conky-et-python-2eme-partie

Nous avons vu [dans le billet précédent]({filename}/afficher-la-meteo-avec-conky-et-python-1ere-partie.markdown) comment créer un programme python qui récupère les informations météo sur le site de wunderground. Nous avons "démonisé" ce script, c'est à dire que nous lui avons demandé de se déclencher à intervalle régulier.

Nous allons maintenant faire en sorte qu'il se lance automatiquement au démarrage de l'ordinateur.

Cette procédure est valable pour les distributions Linux se basant sur init.d comme Debian, et donc Crunchbang qui est la distribution sur laquelle a été fait cette automatisation.

Pour cela, il suffit de suivre les étapes suivantes :

### Sauver le programme python dans /usr/sbin

Dans le billet précédent, j'ai appelé mon script meteo.py. La copie du programme meteo.py dans `/usr./sbin` doit se faire en mode root par un `sudo cp meteo.py /usr/sbin`. Ne pas oublier au préalable de rendre le script exécutable par un `chmod +x meteo.py`.


### Créer un script de démarrage /etc/init.d

Le fichier `/etc/init.d/skeleton` est un fichier d'exemple pour la création d'un script de démarrage. Personnellement, j'en ai créé un beaucoup plus sommaire sur la base d'un tuto que [j'ai trouvé ici](http://www.gavinj.net/2012/06/building-python-daemon-process.html), puis que j'ai un peu customisé, et qui fonctionne très bien. Il faut le créé en mode root dans le répertoire `/etc/init.d/`, en faisant `$ sudo geany /etc/init.d/meteo` par exemple (remplacer geany par nano, vim, ... l'éditeur de votre choix).

{% code content/code/meteo %}
[Télécharger meteo]({filename}/code/meteo){: class="button radius tiny" title="Télécharger meteo" }

Ensuite, il ne faut pas oublier de rendre le script exécutable par :

	:::bash
    $ sudo chmod +x meteo

Pour tester si votre script fonctionne correctement, vous pouvez faire :

	:::bash
	$ service /etc/init.d/meteo start
	$ ps -ef | grep meteo
	root      2355     1  0 21:01 ?        00:00:00 python /usr/sbin/meteo.py start

Vous devriez voir votre service dans la liste des processus actifs.

Pour arrêter le service, il suffit de faire :

	:::bash
    $ service /etc/init.d/meteo stop


### Inclure le service au démarrage

Pour ajouter le script à la liste de démarrage, vous devez lancer la commande suivante à partir du répertoire /etc/init.d/

	:::bash
    $ sudo update-rc.d meteo defaults

Il ne reste plus qu'à rebooter et le programme python sera lancé automatiquement au démarrage.


### Petites astuces

Argh, ça ne marche pas ! ! ! Mais pourquoi ? Pas de panique, il y a forcément une explication. Voilà deux pistes.

#### Astuce 1

Si vous avez lu le premier billet sur le programme python, vous avez remarqué que j'ai changé la redirection des messages envoyés par le démon de /dev/tty vers /dev/null. En effet, si tout fonctionnait parfaitement avec le lancement du service via le terminal, le script python plantait au reboot car il cherchait un service tty qui n'était pas démarré.

Maintenant que tout part à la poubelle, je n'ai plus d'infos sur le démon, mais je n'ai plus de problème.

#### Astuce 2

Pour être sûr d'avoir paramétré correctement le script meteo dans /etc/init.d, , il faut savoir dans quel runlevel se lance Crunchbang.

	:::bash
    $ who -r
             niveau d'exécution 2 2013-07-09 21:01                   dernier=S

Nous voyons dans mon cas particulier que ma session démarre avec un runlevel 2. Ca tombe bien, c'est ce que j'ai défini sur la ligne `# Default-Start:     2 3 4 5`.

Et lorsque que j'ai lancé la commande update-rc.d, un lien s'est créé dans le répertoire /etc/rc2.d listant les services concernés par le runlevel 2, la lettre S signifiant Start (K voulant dire Kill), et le numéro 05 précisant que le service démarrera après tous ceux ayant un numéro inférieur.

	:::bash
    $ls -l /etc/rc2.d/
    lrwxrwxrwx 1 root root  15 juil.  5 21:45 S05meteo -> ../init.d/meteo


Pour plus d'information sur les runlevel, je vous invite à aller [à cette adresse](http://www.generation-linux.fr/?post/2009/01/22/Cours-Linux-%3A-les-runlevels "Tout ce que vous avez toujours voulu savoir sur les runlevel")

Dans le prochain billet, la troisème et dernière étape : [le conky météo]({filename}/afficher-la-meteo-avec-conky-et-python-3eme-partie.markdown)
