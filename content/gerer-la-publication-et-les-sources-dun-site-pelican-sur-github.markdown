Title: Gérer la publication et les sources d'un site Pelican sur Github
Date: 2013-10-16 21:01
Category: Pelican
Tags: Pelican, Github 
Slug: gerer-la-publication-et-les-sources-dun-site-pelican-sur-github

Début d'une série de billets sur la création d'un site avec le générateur de site statique Pelican. Je commence par la fin. Comment publier son site sur github, ainsi que les sources ayant permis de créer le site ? Je traiterai de la création proprement dite du site avec Pelican dans un prochain billet.

Nous démarrons donc ce billet à partir du moment où vous avez finalisé le paramètrage de Pelican et que vous voulez publier vos pages.

Mon objectif était d'avoir une facilité de publication assez similaire à celle offerte par Octopress. A partir d'un même dépôt distant, je veux disposé d'une branche contenant le site à déployer et d'une branche content les sources de mon site. Cela est très utile pour blogger depuis plusieurs ordinateurs. Je veux pouvoir mettre à jour facilement ces deux branches, indépendemment l'une de l'autre, mais toujours à partir d'un unique dépôt local. Le tout doit être exécutable en un minimum de lignes de commande. 

Dernier élément, je veux conserver l'adresse letchap.github.io, ce qui m'oblige à passer par une publication de pages Github en mode "pages utilisateur"

C'est parti !

Je commence par me placer dans le répertoire contenant les sources et le site. Je l'ai appelé de manière très originale `blog`. Il doit contenir les répertoires content et output (obtenu par la commande `make html`)

	:::bash
	$ cd blog
	/blog$ ls -l
	drwxr-xr-x  6 letchap letchap 4096 oct.  16 21:00 content
	-rwxr-xr-x  1 letchap letchap 2073 août   3 21:58 develop_server.sh
	-rw-r--r--  1 letchap letchap 3076 août   3 21:58 Makefile
	drwxr-xr-x  4 letchap letchap 4096 oct.  15 23:16 mon-theme
	drwxr-xr-x 11 letchap letchap 4096 oct.  15 23:06 output
	-rw-r--r--  1 letchap letchap 1537 oct.  15 23:16 pelicanconf.py
	-rw-r--r--  1 letchap letchap 1625 oct.  10 21:33 pelicanconf.pyc
	-rw-r--r--  1 letchap letchap    5 oct.  12 15:57 pelican.pid
	drwxr-xr-x  3 letchap letchap 4096 oct.  15 22:50 plugins
	-rw-r--r--  1 letchap letchap  508 août   3 21:58 publishconf.py
	-rw-r--r--  1 letchap letchap    5 oct.  12 15:57 srv.pid

	

Sous mon identifiant sur le site github.com, je créé un dépôt `letchap.github.io`, avec comme nom obligatoirement monuser.github.io. Et je n'y touche plus.
	
Retour dans le terminal, où j'initialise mon dépôt local, que je lie ensuite au dépôt distant.
	
	:::bash
	$ git init
	$ git remote add origin git@github.com:letchap/letchap.github.io.git
	$ git config --global user.name "Your Name"
	$ git config --global user.email you@example.com


Je vais maintenant créer une branche source qui va contenir les sources de mon site, c'est à dire tout sauf le dossier output qui lui contient le site à déployer. Pour exclure le sous-dossier output, j'ai pris soin de créer un fichier .gitignore contenant le dossier output (plus quelques fichiers sans intérêt)

Contenu de .gitignore

	:::bash
	output
	*.pyc
	*.pid
	Makefile
	develop_server.sh

Pour créer ma branche source, j'utilise une procédure normalement pas très orthodoxe : je créé une branche master vide que je renomme en source, et je l'alimente avec tout le contenu de mon répertoire blog sauf le contenu de .gitignore. Je peux alors envoyer mes sources dans mon dépôt distant github sur une branche source.

	:::bash
	$ git commit --allow-empty -m "initial commit" #je crée master vide
	$ git branch -m master source #je renomme master en source
	$ git add .
	$ git commit -m 'creation du source' #j'alimente la branche source
	$ git push origin source #j'envoie les sources sur le dépôt distant

Maintenant le site proprement dit !

Rappelez - vous, toutes les pages sont contenues dans le dossier output. Pour créer et alimenter une branche gh-pages, nous allons utilisé l'utilitaire ghp-import qui s'installe par un `pip install ghp-import`. Je ne sais pas comment ça fonctionne mais cela créé ou met à jour une branche gh-pages avec le contenu du dossier output. Hyper pratique. Il ne reste plus qu'à pousser cette branche sur la branche master de notre dépôt distant(qui se créé à cette occasion).

	:::bash
	$ ghp-import output
	$ git push origin gh-pages:master

Voilà, l'installation est terminée ! Pour la suite de la vie du blog, la mise à jour des sources se fera par :
	
	:::bash
	$ git add .
	$ git commit -m 'message'
	$ git push origin source

et la mise à jour des pages du site se fera par :

	:::bash
	$ make html
	$ ghp-import output
	$ git push origin gh-pages:master

C'est magique !
