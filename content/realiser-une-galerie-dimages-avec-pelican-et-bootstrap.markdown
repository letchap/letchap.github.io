Title: Réaliser une galerie d'images avec Pelican et Bootstrap
Date: 2013-12-11 11:54
Category: Pelican
Tags: Pelican, Bootstrap, lightbox, Markdown, Python
Slug: realiser-une-galerie-dimages-avec-pelican-et-bootstrap

Nous allons voir aujourd'hui comment afficher les images sous forme de diaporama sur un site généré avec Pelican. L'idée est de rendre cliquable une image qui s'affiche alors au-dessus du site, et de faire défiler les images sous la forme d'un diaporama pour une galerie d'images. Vous avez un petit exemple de ce que cela peut donner pour une image simple sur [un autre de mes billets]({filename}/lancer-un-programme-python-depuis-automator.markdown) ou pour [une galerie sur un autre billet ici]({filename}/virtualiser-mageia-2-sur-os-x-mountain-lion-avec-virtualbox.markdown)

Pour cela, nous avons besoin du plugin Lightbox pour Bootstrap ainsi que de la possibilité offerte par Pelican d'utiliser les extensions pour markdown de Python.

Cela ne s'applique que si vous utiliser la syntaxe Markdown pour rédiger vos billets. Je suppose que c'est également réalisable en syntaxe reStructuredTex.

### Installer le plugin lightbox

Le plugin lightbox pour bootstrap est disponible [à cette adresse](http://lokeshdhakar.com/projects/lightbox2/ "Lightbox V2"). 

Pour installer ligthbox dans votre thème pelican, il faut : 

* copier le répertoire img dans le répertoire `/static`
* copier les fichiers jquery-1.10.2.min.js et lightbox-2.6.min.js dans le répertoire `/static/js`
* copier lightbox.css dans le répertoire `/css`
* déclarer les scripts js et le fichier css dans le fichier base.hmtl

		:::HTML
		<script src="{{ SITEURL }}/theme/js/jquery-1.10.2.min.js"></script>
	    <script src="{{ SITEURL }}/theme/js/lightbox-2.6.min.js"></script>
		<link href="{{ SITEURL }}/theme/css/lightbox.css" rel="stylesheet" type="text/css"/>

La syntaxe html pour activer lightbox est la suivante : 

	:::HTML
	<a href="/path/to/monimage.png" data-lightbox="monimage" title="Mon Image"><img src="/path/to/monimage.png" alt="Mon Image" /></a>

Pour avoir une galerie d'image, il suffit de toutes les déclarer avec la même attribut data-lightbox.

Seulement, nous sommes sous Pelican, nous rédigeons en Markdown, nous n'allons pas insérer du code html dans notre fichier markdown quand même !!! Bien sûr, c'est tout à fait possible de le faire puisque markdown accepte du code html. Mais voyons comment tout faire en markdown.

### Les extensions Markdown Python

Pour un petit cours de rattrapage sur la syntaxe Markdown, [c'est ici.]({filename}/memo-markdown-en-francais.markdown "memo markdown")

Pour rédiger notre texte entièrement en Markdown, nous allons devoir résoudre deux problèmes :

* créer un lien sur une image
* ajouter un attribut data-lightbox sur notre lien, ce que n'autorise pas nativement Markdown


#### Créer un lien sur une image en Markdown

Pour créer un lien, la syntaxe Markdown est la suivante :

	[lien](http://example.com)
	ou sur Pelican pour un lien interne
	[lien]({filename}/path/to/monarticle.markdown)

Pour insérer une image :

	![alt text](/path/to/monimage.png)
	ou sur Pelican
	![alt text]({filename}/path/to/monimage.png)


Pour créer un lien sur une image, nous allons simplement combiner les deux 

	[![alt text]({filename}/path/to/monimage.png)]({filename}/path/to/monimage.png)
	
Ce qui nous donnera bien en sortie html :

	<a href="/path/to/monimage.png"><img src="path/to/monimage.png" alt="alt text" /></a>


#### Ajouter un attribut sur le lien

Comme je le disais en début d'article, il n'est pas possible nativement d'insérer un attribut sur un lien avec Markdown. Heureusement, les extensions Markdown pour Python offrent cette possibilité. Et Pelican inclus l'utilisation des extensions Markdown.

Pour plus d'information sur les extensions Markdown, vous pouvez vous rendre sur [la documentation Python](http://pythonhosted.org/Markdown/extensions/ "Markdown Python").

Pour insérer un ou plusieurs attributs dans un lien, il ne reste plus qu'à écrire les accolades suivantes, sans espace avec les parenthèses :

	[lien]({filename}/path/to/monimage.png){: data-lightbox="monimage" title="Mon Image" }

Ce qui se traduira par :

	<a href="path/to/monimage.png" data-lightbox="monimage" title="Mon Image">

	
#### On assemble le tout

Pour une image cliquable avec un effet diaporama, il faut donc écrire en Markdown :

	[![Mon Image]({filename}/path/to/monimage.png "Mon Image")]({filename}/path/to/monimage.png){: data-lightbox="monimage" title="Mon Image" }

Pour obtenir :

	:::html
	<a href="/path/to/monimage.png" data-lightbox="monimage" title="Mon Image"><img src="/path/to/monimage.png" alt="Mon Image" /></a>

Bon, d'accord, ce n'est pas beaucoup plus simple, mais c'est tellement plus gratifiant.
