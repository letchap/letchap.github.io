Title: Lancer anacron comme simple utilisateur
Date: 2013-10-25 16:44
Category: Terminal
Tags: cron, anacron, anacrontab, terminal
Slug: lancer-anacron-comme-simple-utilisateur

Sous Linux, il existe un utilitaire qui permet de déclencher des travaux de manière périodique. Il s'agit de cron. Cet utilitaire très pratique présente pour moi un énorme inconvient, il nécessite d'avoir un ordinateur constamment allumé. Heureusement, il existe un deuxième utilitaire anacron qui lui permet de lancer des travaux a posteriori si l'ordinateur était éteint au moment du déclenchement programmé. Et là, autre petit soucis, anacron ne se lance qu'en root (contrairement à cron qui se lance en mode utilisateur).

Heureusement, il est possible de créer un anacron non-root. Pour cela, il faut :

### 1) Créer un fichier anacrontab dans son répertoire personnel par exemple ~/user/etc/anacrontab, à l'image de celui présent dans /etc/anacrontab


	# /etc/anacrontab: configuration file for anacron

	# See anacron(8) and anacrontab(5) for details.

	SHELL=/bin/sh
	PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

	# These replace cron's entries
	@monthly	1	monprog    env DISPLAY=:0 python /home/letchap/bin/monprog.py >> /home/letchap/tmp/monprog.log 2>&1

Les 4 champs à renseigner sont :

- la période : ici, une fois par mois
- le délai : le temps d'attente après le démarrage de l'ordinateur avant de lancer les travaux
- la référence du travail (important pour le timestamp)
- la commande shell à lancer


### 2) Donner les droits utilisateur sur le répertoire contenant le "compteur" d'anacron, c'est à dire la date de dernière utilisation.

Pour cela, nous commençons par créer un group anacron dans /etc/group et nous y ajoutons notre user

	$ addgroup anacron
	$ adduser user anacron
	
Puis nous modifions les droits sur le fichier /var/spool/anacron

	$ chown root.anacron /var/spool/anacron
	$ chmod g+w /var/spool/anacron
	
Comme nous sommes dans le groupe anacron, tout va bien.


### 3) Ne reste plus qu'à lancer notre anacron au démarrage de l'ordinateur

Cela se fait dans le fichier .profile de l'utlisateur en ajoutant la ligne suivante

	/usr/sbin/anacron -t $HOME/etc/anacrontab


Pour mémoire, la date à laquelle se déclenche le job mensuel se définie dans le fichier /etc/crontab/.

