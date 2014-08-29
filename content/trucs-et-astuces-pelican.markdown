Title: Trucs et astuces Pelican
Date: 2013-10-24 21:24
Category: Pelican
Tags: Pelican, Python, Bootstrap, CSS, Git
Slug: trucs-et-astuces-pelican


Me voilà donc sous Pelican ! Il m'a fallu un petit moment pour arriver à un résultat publiable, la version par défaut de Pelican ne me convenant pas. Finalement, j'ai effectué un certain nombre de modifications, que ce soit dans la présentation, dans le fichier de configuration, dans les plugins ou même sur la procédure de publication des pages sur Github. Pour la procédure d'installation, je vous renvoie à la documentation officielle.

Le plus compliqué pour moi a été la mise en forme des blocs de code avec pygments et le CSS associé pour que cela fontionne sur tous les navigateurs. J'ai fait beaucoup de modifications, si vous voulez plus de détails que ce qui est écrit, demandez moi !

Et maintenant, petit tour d'horizon de ma customisation de Pelican. Vous trouverez les sources de mon thème sur mon [compte github](https://github.com/letchap/letchap.github.io/tree/source/mon-theme).

Je suis parti sur la base du thème pelican-bootstrap3 qui se trouve dans le dépôt [pelican-theme](https://github.com/getpelican/pelican-themes). Ce thème est basé sur bootstrap, qui offre une mise en forme par défaut directement utilisable. J'ai choisi le thème spacelab disponible [à cette adresse sur bootswatch](http://bootswatch.com/spacelab/).


### Le fichier base.html

J'ai d'abord modifié le ficher base.html pour y ajouter le nom de l'auteur (le mien en l'occurrence) dans le head puisque je suis l'unique auteur et je me passe ainsi du tag author dans les fichiers markdown contenant les articles.

	:::html
	<meta name="author" content="{{ AUTHOR }}">

J'ai également ajouté un banner pour y mettre le nom du blog et un sous-titre avant la barre de navigation dans le corps de la page.

	:::html
	<body>
	<div class="container">
		<!-- Banner
		================================================== -->

			<div class="site-header" id="banner">
				<div class="row">
					<div class="col-lg-6">
						<h1><a href="{{ SITEURL }}">{{ SITENAME }}</a></h1>
						<p class="lead">{{ SITESUBTITLE }}</p>
					</div>
				</div>
			</div>



Enfin j'ai ajouté un formulaire de recherche basé sur google et la possibilité de s'abonner à un flux RSS (voir plus bas).


### Le fichier article.html

Du coup, j'ai aussi supprimé tout ce qui avait trait à l'auteur dans ce fichier.

### Disqus

Bon, alors, j'ai galèré un peu à cause de l'adresse URL relative. En hébergeant mon site sur les pages Github, je suis obligé d'utiliser les URL relatives (j'ai essayé avec les URL absolues mais j'avais des liens bizarres). La conséquence est qu'il n'est pas possible de s'appuyer sur la variable SITEURL qui renvoie un `.` dans les fichiers html. Et là, deux possibilités, soit utiliser une variable qui va stocker l'adresse du site (la même que celle que je vais créer un peu plus bas pour google), soit utiliser uniquement le slug de l'article (au sens Disqus, c'est à dire dans mon cas avec la date, c'est ce que j'ai paramétré dans pelicanconf.py dans ARTICLE_URL) comme identifiant Disqus, comme ce que j'ai finalement choisi de faire.

	:::javascript
	<script type="text/javascript">
		/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
		var disqus_identifier = "{{ article.url }}";
		/* * * DON'T EDIT BELOW THIS LINE * * */
		(function () {
			var dsq = document.createElement('script');
			dsq.type = 'text/javascript';
			dsq.async = true;
			dsq.src = 'http://{{ DISQUS_SITENAME }}.disqus.com/embed.js';
			(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
		})();
	</script>

Par contre, attention, ce n'est pas très précis, et il ne faut pas avoir plusieurs discussions avec le même identifiant Disqus, ce qui peut arriver lors d'une migration de site, ou même, ce qui m'est arrivé, en testant le site localement en ayant activé Disqus. Pour avoir une base Disqus propre, j'ai finalement été obligé d'effacer entièrement mon compte Disqus et de tout réimporter. Un peu bourrin comme méthode mais efficace.

Je verrai par la suite si je suis contraint d'utiliser un identifiant plus discriminant que le slug de l'article. Pour l'instant, ça suffit.


### Les fichiers CSS

Par défaut, nous avons besoin de 3 fichiers CSS pour gérer le style bootstrap, les icones fontawesome et la coloration synthaxique :
- bootstrap.min.css
- fontawesome.min.css
- pygments.css

Toutes les modifications ou surcharges sont à faire dans un fichier spécifique qui est nommé style.css dans le thème bootstrap3 et que j'ai un peu adapté à mes besoins, surtout pour les insertions de blocs de code. Tous les commentaires sont dans le code.

{% code content/code/style.css %}
[Télécharger style.css]({filename}/code/style.css){: class="button radius tiny" title="Télécharger style.css" }

Une exception que je n'ai pas réussi à gérer dans style.css, j'ai supprimé dans le fichier bootstrap.css, pour la balise pre, la mise en forme word-wrap: word-break. Sinon, impossible d'avoir un ascenseur horizontal dans le bloc de code.


### RSS

J'ai commencé par paramétrer un flux RSS dans le fichier de configuration, que j'ai rendu accessible dans ma barre de navigation. Je n'ai pas vraiment suivi les recommandations de la documentation, j'ai plutôt fait une adaptation à ma sauce.

Tout d'abord, dans le fichier pelicanconf.py, j'ai simplement ajouté une ligne, ce qui ne génèrera qu'un seul fichier atom.xml pour tous les posts, c'est largement suffisant, pas besoin de catégories ni de sous-dossier feed.

	FEED_ALL_ATOM = 'atom.xml'

**LE PLUS IMPORTANT** est dans le fichier base.html. Il ne faut surtout, surtout, surtout pas faire ce qui est écrit partout, à savoir paramétrer le lien RSS avec l'adresse du site comme ceci :

	:::html
	<li><a href="{{ SITEURL }}/{{ FEED_ALL_ATOM }}" type="application/atom+xml" rel="subscribe-rss"
		title="Subscribe via RSS"><i class="icon-rss"></i></a></li>

Il faut impérativement le paramètrer sans référence au site comme celà :

	:::html
	<li><a href="/{{ FEED_ALL_ATOM }}" type="application/atom+xml" rel="subscribe-rss"
		title="Subscribe via RSS"><i class="icon-rss"></i></a></li>

Sinon, le risque est d'avoir des liens vers les articles tous bizarres dans les aggrégateurs de flux.

### La recherche sur le site avec google

Le fichier de configuration est un outil magique car il permet de définir ses propres variables réutilisables dans les fichiers html. Je m'en suis servi pour créer deux variables permettant une recherche sur mon site grâce à google.

	SIMPLE_SEARCH = 'http://google.com/search'
	ABSURL = 'letchap.github.io'

Puis, j'ai ajouté un formulaire de recherche dans la barre de navigation en ajoutant les lignes suivantes dans le fichier base.html.

	:::html
	<ul class="nav navbar-nav navbar-right">
		<li><a href="{{ SITEURL }}/archives.html"><i class="icon-th-list"></i>Archives</a></li>
		<li><a href="{{ SITEURL }}/{{ FEED_ALL_RSS }}" type="application/atom+xml" rel="subscribe-rss"
			title="Subscribe via RSS"><i class="icon-rss"></i></a></li>
		<form class="navbar-form navbar-right" action="{{ SIMPLE_SEARCH }}" method="get">
			<fieldset role="search">
			<input type="hidden" name="q" value="site:{{ ABSURL }}" />  
			<input type="search" class="form-control col-lg-8" name="q" results="0" placeholder="Search" />  
			</fieldset>
		</form>  
	</ul>

### Les plugins

La liste des plugins est disponible sur [github](https://github.com/getpelican/pelican-plugins).

Je n'utilise qu'un seul plugin, celui permet d'insérer et de télécharger du code dont le petit nom est include_code.py. Il a un petit problème, il ne cause pas français, ou UTF-8 si vous préférez. J'ai donc été obligé de modifier légèrement le code à 3 endroits pour qu'il accepte les accents (d'djiou!).

J'ai ajouté `# -*- coding: utf-8 -*-` en tête du fichier

J'ai remplacé

	:::python
	code = open(code_path).read()

par

	:::python
	code = open(code_path).read().decode('utf8')

Enfin, j'ai remplacé

	:::python
    open_tag = ("<figure class='code'>\n<figcaption><span>{title}</span> "
                "<a href='{url}'>download</a></figcaption>".format(title=title,
                                                                   url=url))
    close_tag = "</figure>"

par

	:::python
    open_tag = u"<figure><figcaption class='well well-sm'><span style='text-align: left'>{title}\
                "</span><a style='float: right' href='{url}'>Télécharger</a></figcaption>".format(title=title,url=url)
    close_tag = "</figure>"

### La publication de mes pages Github et de mes sources

Le sujet méritait un billet dédié. Il est disponible [ici]({filename}/gerer-la-publication-et-les-sources-dun-site-pelican-sur-github.markdown "Gérer la publication et les sources d'un site Pelican sur Github").
