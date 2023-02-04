Title: Utilisation de Sass avec Pelican et Foundation
Date: 2014-11-29 15:27
Category: Foundation 
Tags: Foundation, Sass, Pelican
Slug: utilisation-de-sass-avec-pelican-et-foundation


Dans le dernier billet, nous avons vu comment nous mettre à l’aise avec Pelican et Foundation tout en nous préparant à utiliser Sass. Nous allons tirer profit de tout cela pour simplifier le fichier de configuration css personnel attaché au site.

Pour rappel, voici le fichier d’origine :

{% code content/code/style2.css %}


### Un peu de nettoyage

Première étape, avec la nouvelle version de Foundation, plus besoin de bidouille pour la barre de recherche dans la top-bar. Nous pouvons supprimer le code css dans la feuille de style

Deuxième étape : l’utilisation de pygments et de l’extension markdown. Je n’avais rien compris et j’avais monté une usine à gaz pour essayer d’avoir un tableau avec deux colonnes de largeur fixe et un texte qui pouvait déborder horizontalement en essayant de jouer avec la valeur witdh. Alors je ne sais pas si c’est la lib markdown de python et celle de pygments qui gère la table, mais dans tous les cas, il n’y a rien à faire pour gérer la largeur de la table de deux colonnes. Exit la bidouille sur la table.

Dernière étape : j’ai supprimé aussi la petite verrue .include que j’utilisais avec le plugin include que j’ai remplacé par ma propre extension markdown pour gérer les inclusions de code à partir d'un fichier.

Nous voilà avec un fichier un peu plus propre. Passons à Sass.

### Configuration avec Sass

Bon, passés tous ces préliminaires, attaquons l’utilisation de Sass proprement dite. Pour cela nous alors avoir besoin du fichier _setting.scss et de notre feuille perso _style.scss

Sass est très puissant, cependant, dans un premier temps, je ne vais utiliser que les possibilités offertes par les variables. Je définis une variable dans mon fichier _settings.scss et je l’utilise dans le fichier _style.scss.

Pour illustrer cela, prenons comme exemple la police de caractère des lignes de code.

Je vais commencer par définir dans _settings.sccs les polices de caractère que je souhaite utiliser sur l'ensemble du site. Pour cela, je copie la ligne 

	// $code-font-family: Consolas, 'Liberation Mono', Courier, monospace;

Je supprime la mise en commentaire et je mets définis les polices que je veux :

	$code-font-family: 'Source Code Pro', monospace, Consolas;

Il est important de dupliquer la ligne plutôt que de la modifier directement, afin de pouvoir retrouver facilement le paramétrage d'origine


Maintenant que j'ai défini ma police de caractère pour les blocs de code dans la variable $code-font-family, je vais pouvoir la réutiliser dans _style.scss pour définir le tag `<pre>`.

	pre {
	  font-family: $code-font-family;
	}


Le fichier après passage à la moulinette sass ressemblera alors à ça :

{% code content/code/_style.scss %}

Plus concis quand même.

	
### rem-calc

Petit détour sur la fonction rem-calc que l'on retrouve un peu partout dans foundation. Elle permet de ramener une valeur relative à une valeur en px :

Foundation définit une taille de police de base de 16px

	// This is the default html and body font-size for the base rem value.
	// $rem-base: 16px;


Quand je vais écrire font-size = 1rem, ma valeur sera de 16px, pour avoir une taille de 14px par exemple je devrais écrire font-size= 0.875rem. Pas super pratique. Pour éviter de s’embêter avec ça, on va faire comme si on écrivait directement la taille en px avec font-size=rem-calc(14), ce qui veut dire font-size=14px. Vous allez me dire, pourquoi ne pas écrire directement font-size=14px. Tout simplement car si on veut changer la taille de police de base, on n'aura à le faire qu'une seule fois. Petit extrait de _settings.scss:

	// Since the typical default browser font-size is 16px, that makes the calculation for grid size.
	// If you want your base font-size to be different and not have it affect the grid breakpoints,
	// set $rem-base to $base-font-size and make sure $base-font-size is a px value.
	// $base-font-size: 100%;


Hyper pratique !


