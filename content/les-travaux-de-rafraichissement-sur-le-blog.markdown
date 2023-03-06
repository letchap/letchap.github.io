Title: Les travaux de rafraîchissement sur le blog
Date: 2023-02-28 10:27
Category: Pelican
Tags: Pelican, Foundation, Pycharm, Github, CMS
Slug: les-travaux-de-rafraichissement-sur-le-blog

Après presque 8 ans sans avoir touché au blog, il était nécessaire de faire un peu de dépoussiérage. Toutes les sources ont 8 ans, autant dire une éternité. Pour le blog, j'utilise :
* le CMS Pelican
* le framework Foundation pour les feuilles de style
* Github pour la publication des pages

Pour remettre un petit coup de frais sur le blog, j'ai eu besoin de :
* récupérer les sources depuis Github
* faire la montée de version Pelican
* faire la montée de version de Foundation de la v5 vers la v6

### Récupérer les sources

Mon dernier article a été écrit sur un iMac qui a rendu l'âme. Fort heureusement, les sources sont toujours disponibles sur mon dépôt Github. Dans le dépôt source sont présents les articles et le template du site au format Foundation 5 (mais pas les sources Pelican).

Dans deux de mes articles précédents, j'avais expliqué comment travailler sur plusieurs ordinateurs différents grâce à Github et comment créer un environnement virtuel python pour bien gérer le projet en local. Cette fois, je me suis facilité la tâche en faisant les deux en même temps grâce à Pycharm. L'installation de Pycharm sur Ubuntu se fait à partir d'un dépôt snap. J'utlise la version community :

	:::bash
	sudo snap install pycharm-community --classic

Une fois dans Pycharm, je peux créer un projet en clonant le dépôt Github. Pycharm va vous demander de vous connecter à votre compte Github, de sélectionner le dépôt à cloner, puis va créer le projet à partir du clone.

[![Ecran pycham]({static}/images/pycharm.png "Ecran pycharm")]({static}/images/pycharm.png){: data-lightbox="pycharm" title="Ecran pycharm" }

Dans Pycharm, je vais donc avoir les pages sources du blog, et l'ancien thème Foundation dans sa version 5.

Je vais ensuite paramétrer un environnement virtuel avant d'installer la nouvelle version de Pelican. Pour cela je vais dans file/settings/projets/python interpreter, add interpreter et je choisis virtualenv environment.


### Installer la nouvelle version de Pelican

Je peux maintenant procéder à l'installation de Pelican
	
	:::bash
	python -m pip install pelican
	python -m pip install "pelican[markdown]"
	pelican-quickstart

Je lance le pelican-quickstart uniquement pour créer le squelette du site, je laisse les options par défaut. Je récupère mon ancien fichier de configuration pelican.conf pour écraser celui créer par pelican-quickstart

Ce que j'ai trouvé extraordinaire avec Pelican, c'est que je n'ai quasiment pas eu besoin de modifier mon fichier de configuration pour pouvoir lancer la fabrication du site. Seul le module markdown a évolué, j'ai modifié les lignes concernant uniquement markdown dans le fichier.

A titre d'exemple, mon fichier `pelicanconf.py` :

{% addcode content/code/pelicanconf.py %}
[Télécharger pelicanconf.py]({static}/code/pelicanconf.py){: class="button small" title="Télécharger pelicanconf.py" }


Dans le fichier conf, j'ai une petite ligne custom car j'ai créé une extension markdown personnelle qui me permet de récupérer le contenu d'un fichier script pour le mettre sous forme de bloc de code dans un article. Les explications sont [dans cet article]({filename}/mon-extension-markdown-pour-inclure-du-code-a-partir-dun-fichier.markdown) qui a été mis à jour pour l'occasion.

   .pipe(gulp.dest('static/css'))

### Installer la nouvelle version 6 de foundation et adapter le thème du site

Alors là, ce fut le gros morceau. Tout a changé en 7 ans : l'installation, les composants, ... L'enfer.

#### L'installation

En clonant mon dépôt github, j'ai récupéré le thème Foundation dans sa version 5. Je vais installer la version 6 de foundation à coté, dans mon projet Pelican. J'ai choisi la version basic car je n'ai pas besoin de javascript Foundation, je n'utilise pas de composant le requérant. L'installation m'a semblé plus simple que dans la version 5, 3 petites lignes suffisent pour l'installation, la quatrième permet de visualiser les modifications en temps réel. J'ai installé Foundation dans un répertoire que j'ai appelé F6-theme.

    git clone https://github.com/foundation/foundation-sites-template F6-theme
    cd F6-theme
    yarn install
    yarn start # pour voir les modifications sass

J'en ai profité pour faire l'adaptation de la structure du répertoire Foundation à celle de Pelican ([petit rappel ici]({filename}/utiliser-foundation-et-sass-avec-pelican.markdown)) en modifiant le fichier gulpfile.js pour que le fichier app.css se crée dans un répertoire `static/css` et non `css`


#### Les composants

Le plus gros changement concerne les composants de la version 6 de Foundation et il m'a fallu un bon moment pour adapter le site au format V5 en V6. Je vais faire un billet dédié sur les différents changements car il y en a beaucoup, en particulier, la gestion des grilles.



### Le nouveau site Pelican

Une fois que tout est installé la structure de mon projet Pelican comprend :
* les articles au format markdown récupéré de mon dépôt github dans le dossier content
* un répertoire newpost qui me permet de créer automatique un squelette d'article
* un répertoire F6-theme qui contient mon nouveau thème Foundation
* un répertoire output qui va se créer en lançant la génération du site par un `make html`
* un répertoire venv qui contient les sources Pelican et mon extension markdown pour insérer du code dans les articles

[![Ecran blog-pycharm]({static}/images/blog-pycharm.png "Ecran blog-pycharm")]({static}/images/blog-pycharm.png){: data-lightbox="blog-pycharm" title="blog-pycharm" }














