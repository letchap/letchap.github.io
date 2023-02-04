Title: Ceci n'est pas un post sur pourquoi j'ai migré de Wordpress vers Octopress
Date: 2013-02-26 22:21
Category: Octopress
Tags: Octopress, Ruby, RVM, Github, SSH
Slug: ceci-nest-pas-un-post-sur-pourquoi-jai-migre-de-wordpress-vers-octopress

Bon, j'ai fait comme tout le monde, j'ai migré de Wordpress vers Octopress parce que ... parce que c'est mieux. Il existe des tutoriels en français et en anglais donc je ne m'étendrai pas sur l'installation d'Octopress, [le site d'Octopress](http://octopress.org/) lui-même est très détaillé sur la procédure à suivre. Je vais simplement revenir sur les trois petites difficultés que j'ai rencontré et qui ne sont pas forcément détaillées sur la toile.

### L'échange de clé sécurisé avec Github

J'ai choisi d'installer Octopress en hébergeant mes pages dans un dépôt Github. J'ai donc créé un compte et un dépôt pour mon site, en revanche, je ne savais pas qu'il était nécessaire d'échanger des clés ssh pour communiquer. La procédure est expliquée sur [le site de Github](https://help.github.com/articles/generating-ssh-keys "Générer un clé ssh").

### Setup des pages Github

Il se peut que la saisie de l'adresse URL du dépôt est été mal faite (avec des gros doigts, j'en parle parce que ça m'est arrivé) au moment du `rake setup_github_pages`.

Pour vérifier que l'on ne sait pas trompé :

	:::bash
    $ git remote -v
    origin	git@github.com:letchap/letchap.github.com.git (fetch)
    origin	git@github.com:letchap/letchap.github.com.git (push)

### RVM is not a function

Au moment de lancer `$ RVM use`, j'ai eu un message d'erreur indiquant `RVM is not a function`.

En fait, par défaut, les binaires sont installés dans $HOME/.rvm et ne sont pas accessibles via le terminal. Pour corriger cela, il faut ajouter les lignes suivantes dans le fichier /home/your-name/.bashrc.

    :::bash
	[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"


### Réinstallation de Ruby avec openssl

La dernière difficulté est survenue au moment du déploiement du site avec le message d'erreur suivant :

	:::bash
    $ require "openssl" # > LoadError: cannot load such file -- openssl


Je ne sais pas pourquoi Ruby ne peut pas utiliser mon openssl installé par défaut, la solution de contournement que j'ai trouvé sur le site [RVM](https://rvm.io/packages/openssl/) a été d'installer un nouveau paquet openssl et de réinstaller Ruby.

	:::bash
    $ rvm pkg install openssl
    $ rvm reinstall 1.9.3 --with-openssl-dir=$rvm_path/usr


