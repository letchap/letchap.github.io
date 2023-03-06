Title: Mon extension markdown pour inclure du code à partir d'un fichier
Date: 2014-04-05 10:51
Category: Python
Tags: Python, Pelican, Markdown
Slug: mon-extension-markdown-pour-inclure-du-code-a-partir-dun-fichier

*Article mis à jour le 8 Février 2023 pour prendre en compte la montée de version Pelican* 

J'adore mon Pelican. Comme il est écrit en Python, il est vraiment facile de le customizer pour l'adapter au maximum à mes besoins.

Sur mon blog, j'ai régulièrement besoin d'insérer des blocs de code. Pour que l'opération soit la plus simple pour la maintenance du site et pour le lecteur qui souhaiterait utiliser le code, je mets le code dans un fichier que je rends téléchargeable.

Malheureusement, il n'est pas possible avec la syntaxe Markdown d'intégrer le contenu d'un fichier source.

Jusqu'à présent, pour contourner ce problème, j'utilisais un plugin Pelican nommé liquid_tags, inspiré du plugin liquid d'Octopress.

Pour moi, cela restait une façon de contourner une absence de fonctionnalité de markdown par ailleurs offerte par ReStructered Text dans une de ces directives. Pourquoi markdown ne pourrait - il pas interpréter un tag comme par exemple {% include_code file.py %} ? La réponse est assez simple : ce n'est pas fait pour ça.

En revanche, avec un peu de python, ça va devenir possible ...

### Un petit détour par le module markdown de python.

Le module markdown de Python, en plus de pouvoir interpréter la syntaxe classique markdown, offre un certain nombre d'extensions comme par exemple la possibilité d'ajouter une coloration syntaxique sur un bloc de code. Par défaut, Pelican prend en compte ces extensions. Il est possible de les paramétrer plus finement dans le fichier pelicanconf.py.

    MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
J'utilise déjà ces extensions (l'extension attribute lists) pour ajouter un attribut dans des balises `<img>`, comme je le décris [dans ce post]({filename}/realiser-une-galerie-dimages-avec-pelican-et-bootstrap.markdown), chose que ne permet évidemment pas nativement markdown.

En plus de ces extensions "standard", il est possible de créer ces propres extensions markdown en python. C'est exactement ce que nous allons faire pour insérer le contenu d'un fichier source dans notre fichier markdown. Puis, une fois cette extension personnelle créée, nous allons la déclarer à Pelican.

### Créons notre extension markdown

Pour créer sa propre extension markdown, il est indispensable de se rendre sur le site python et [de lire le chapitre sur l'API](http://pythonhosted.org/Markdown/extensions/api.html).

La logique de mon extension est la suivante : "Avant de passer mon fichier au processeur markdown, je vais lire le contenu de mon fichier markdown, et dès que je tombe sur le tag {% addcode content/monfichier.py %}, je récupère le contenu du fichier source, que j'indente. Ensuite, je rends la main au processeur markdown".

Concrètement, en python, cela donne les quelques lignes suivantes, les commentaires sont dans le code.

{% addcode content/code/addcode.py %}
[Télécharger addcode.py]({static}/code/addcode.py){: class="button small" title="addcode.py" }

### Testons cette extension

Pour tester cette extension, vous pouvez lancer la commande suivante dans le terminal.

    markdown_py -x addcode montexte.txt > output.html

### Installons l'extension

Pour installer cette extension, il suffit de la copier dans le répertoire contenant les extensions markdown python.

### Utilisons cette extension avec Pelican

Pour installer cette extension avec Pelican, il suffit de la déclarer dans le fichier pelicanconf.py.

    MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.addcode': {},
        },
    'output_format': 'html5',
    }

### Cherry on ze cake

J'aimerais bien avoir un joli bouton pour télécharger mon fichier source. Nous allons donc utiliser l'extension attribute list dont nous parlions précédemment pour ajouter une classe bouton à notre lien html (en l'occurrence un bouton foundation) :

    [Télécharger monfichier.py]({filename}/content/monfichier.py){: class="button" title="Télécharger monfichier.py" }

Le tour est joué, plus besoin de plugin Pelican, l'extension sera disponible pour tous vos projets markdown.
