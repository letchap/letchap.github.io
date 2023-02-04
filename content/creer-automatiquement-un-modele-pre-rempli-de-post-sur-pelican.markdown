Title: Créer automatiquement un modèle pré-rempli d'article sur Pelican
Date: 2014-01-09 22:25
Category: Pelican
Tags: Pelican, Octopress, Fabric, slug, slugify
Slug: creer-automatiquement-un-modele-pre-rempli-d-article-sur-pelican

Depuis mon passage d'Octopress à Pelican, un petit outil me manque : la possibilité de créer un squelette d'article automatiquement à partir du titre, et directement dans le bon répertoire. Sur Octopress, cela se fait par la commande `rake new_post['Mon super post!']`. Par cette commande, l'en-tête est renseignée avec un certain nombre d'informations comme le titre ou la date, le nom du fichier est généré automatiquement et "slugifié", tout ça dans le bon répertoire.

Jusqu'à présent, sur Pelican, pour créer un nouvel article, je faisais un copier-coller d'un ancien post, et je modifiais tout à la main. Pas terrible.

Qu'à cela ne tienne, nous allons faire notre propre script Python pour automatiser tout ça. Le script, le voici, les commentaires sont dedans :

{% addcode content/code/newpost.py %}
[Télécharger newpost.py]({static}/code/newpost.py){: class="button small" title="Télécharger newpost.py" }

En résumé, ce script, à partir d'un titre passé en paramètre va générer un nom de fichier "slugifié", c'est à dire sans caratère accentué, en minuscule et séparé par des tirets, ainsi que l'en-tête de notre fichier. Le fichier de sortie ressemblera à ça :

    :::
    Title: Mon super post!
    Date: 2014-01-10 23:40
    Category:
    Tags:
    Slug: mon-super-post

Ce script fonctionne pour un fichier markdown, et pour un article. Rien ne vous empêche de modifier le script à la marge pour une page et en ReST.

Dernière étape, comment lancer ce script ?

J'ai d'abord regardé du côté des outils fournis par Pelican, à savoir make et fabric. Malheureusement, il n'est pas possible de faire un `make newpost 'Mon super post!'` ou un `fab newpost:'Mon super post!'`.

En revanche, aucun problème pour faire `python newpost.py 'Mon super post!'`.

Le dernier petit truc pour pouvoir faire plus simplement `python newpost 'Mon super post!'`, il suffit de créer un répertoire `newpost` à la racine du blog, et de mettre notre script python dans ce répertoire en le nommant `__main__.py`.
