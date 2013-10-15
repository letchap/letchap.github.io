Title: Cloner son site octopress pour bloguer depuis deux ordinateurs
Date: 2013-04-10 22:54
Category: Octopress
Tags: Octopress, git
Slug: cloner-son-site-octopress-pour-bloguer-depuis-deux-ordinateurs

Vous avez un nouvel ordinateur, ou vous avez écrasé vos fichiers, ou bien encore vous voulez bloguer à plusieurs, il existe tout un tas de bonnes raisons de vouloir mettre à jour son site Octopress depuis plusieurs ordinateurs.

Cela se fait de manière assez simple, et avant tout il faut bien comprendre le principe de mise à jour de son site sur Github.

### Le principe

Dans votre dépôt github qui contient votre site, vous allez trouver deux branches :
- une branche source qui contient les éléments servant à construire le blog. C'est là par exemple que sont créés les nouveaux posts, que sont stockés les fichiers de code ou les images, et bien sûr le fichier de config et le sass.
- une branche master qui contient le site en lui-même, et rien que le site. Sur l'ordinateur, cette branche se trouve dans le répertoire _deploy

Ces deux branches sont mises à jour séparément sur github par deux blocs d'instructions différents

La mise à jour de la branche source va se faire par :

	:::bash
    ~/octopress$ git add .
	~/octopress$ git commit -m 'mon message'
	~/octopress$ git push origin source

La mise à jour de la branche master se fera elle par :

	:::bash
	~/octopress$ rake generate
	~/octopress$ rake deploy

Il n'est pas nécessaire de mettre à jour la branche source sur github pour avoir un site à jour car il est généré à partir des fichiers sources présent sur l'ordinateur.

En conséquence, la première étape avant d'installer octopress sur le deuxième ordinateur et de bien mettre à jour à la fois la branche source et la branche master du dépôt github.

Si vous avez perdu les fichiers de ce premier ordinateur, vous repartirez de la dernière mise à jour du dépôt.

### L'installation sur le deuxième ordinateur

Maintenant que le dépôt sur ces deux branches source et master est à jour, nous allons pouvoir installer Octopress sur le deuxième ordinateur.

L'installation est exactement la même que celle d'un site vierge dont la procédure est décrite sur le site d'Octopress, à une seule différence près. Nous allons cloner notre site au lieu de cloner le site par défaut.

D'abord nous clonons notre branche source en créant au passage le répertoire octopress:
   
	:::bash
    $ git clone -b source git@github.com:monuser/monuser.github.com.git octopress

Ensuite, nous nous positionnons sur le répertoire octopress pour cloner la branche master dans le répertoire _deploy que nous créons au passage :
    
	:::bash
	$ git clone git@github.com:monuser/monuser.github.com.git _deploy
	
Tout le reste de la procédure est rigoureusement identique : l'installation de git, de rvm, des bundles, le paramétrage du compte github, ... tout je vous dis.

### Bloguer depuis deux ordinateurs

Pour passer d'un ordinateur à l'autre, il faut d'abord mettre à jour les deux branches avec les instructions vues plus haut à partir du premier ordinateur, puis sur le deuxième, récupérer les derniers fichiers source et master en les ramenant sur votre ordinateur (pull) :

	:::bash
    $ cd octopress
	$ git pull origin source
	$ cd _deploy
	$ git pull origin master


