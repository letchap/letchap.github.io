Title: Bien démarrer un projet Python
Date: 2014-08-07 21:42
Category: Python
Tags: Python, git, virtualenv, Pelican
Slug: bien-demarrer-un-projet-python

Après quelques mois de pratique de Python, je viens enfin de comprendre à quoi servent les environnements virtuels. C'est un peu toujours la même chose. On lit, on expérimente, on ne comprend pas bien pourquoi on fait telle action, et un jour, on a le déclic. Evidemment, j'ai bien lu un peu partout que les environnements virtuels c'est super, que ça permet d'isoler des sources, que cela ne pollue pas le reste du système, etc ... Jusqu'à présent, pour moi, cela ne restait que des mots. Et facta est lux.


### La création d'un projet dans un environnement virtuel avec un dépôt git

Quelque soit le projet, la méthode que je suis est désormais la suivante :

- je crée un répertoire
- je me positionne dans le répertoire et je crée un dépôt git
- je crée un environnement virtuel en choisissant ma version Python
- j'exclue les sources et bibliothèques de l'environnement virtuel de mon dépôt
- je fais un premier commit de mon dépôt
- je peux activer l'environnement virtuel et installer les sources dont j'ai besoin pour travailler

Ce qui nous donne :

	$ mkdir monprojet
	$ cd monprojet
	$ git init
	$ virtualenv ‐p python2.7 monprojet-env # par défaut, version de Python installé sur l'OS
	$ echo monprojet-env >> .gitignore
	$ echo "*.pyc" >> .gitignore
	$ git add .gitignore
	$ git commit ‐m "Création du projet en ignorant les bibliothèques Python installées"
	$ source monprojet-env/bin/activate
	$ pip install ...

Pour sortir d'un environnement virtuel, la commande est `deactivate`.

### D'accord, mais à quoi ça sert ?

Première chose, l'environnement virtuel ne va concerner que la bibliothèque standard python dans la version que vous aurez choisi au moment de faire `virtualenv` et les bibliothèques tierces que vous aurez installé via `pip install` par exemple. Un petit tour dans le dossier `monprojet-env` vous permettra de le constater. Ce qui veut dire (ça a l'air évident mais j'avais pas percuté tout de suite), qu'il ne contient rien d'autre, surtout pas les sources de votre projet ou les sources des autres langages de programmation, comme par exemple, au hasard, Ruby.

Et maintenant, place au cas pratique :

Mon site est généré grâce au CMS Pelican écrit en python. Actuellement il est en version 3.4 et tourne en Python 2.7. Les sources de Python et Pelican sont dans un environnement virtuel. Les sources du site sont dans un dépôt git. J'utilise également Ruby et notamment le gem Sass, qui eux sont installés sur le système.

Je veux tester la version 3.4 de Pelican en Python 3.3, sans toucher à l'existant, puis si l'essai est concluant, en faire la version de production.

Les différentes étapes vont être les suivantes :

- récuperer la liste des bibliothèques tierces installées sur l'environnement virtuel de départ
- bien mettre à jour le dépôt avec les sources du site
- cloner les sources du site dans un nouveau dossier
- créer un nouvel environnement virtuel
- y installer Python 3.3, Pelican 3.4 et les autres bibliothèques nécessaires au fonctionnement de Pelican
- faire les tests avec ce nouvel environnement, donc sans toucher à l'ancien
- si tout est bon, ça devient le nouvel environnement, vous pouvez suprimmer l'ancien

Ce qui nous donne

	$ cd blog2.7
	$ pip freeze > source.txt
	$ virtualenv ‐p python3.3 pelican3.4-env
	$ echo pelican3.4-env >> .gitignore
	$ git add .gitignore
	$ git commit ‐m "J'exclue les sources python 3.3 du dépôt"
	$ source pelican3.4-env/bin/activate
	$ pip install -r source.txt

Voilà, il ne reste plus qu'à tester le site sous ce nouvel environnement, et si vous êtes content du résultat, supprimer l'ancien environnement. Si vous n'êtes pas satisfait, il suffit de supprimer le nouvel environnement et d'annuler les modifications dans git.
