Title: Installer Archlinux avec XFCE
Date: 2015-03-11 19:30
Category: Archlinux
Tags: Archlinux, XFCE, Virtualbox
Slug: installer-archlinux-avec-xfce

L'annonce de l'arrêt de Crunchbang, une distribution basée sur Debian et Openbox, ma distribution par défaut, m'a fait prendre conscience que j'avais tout intérêt à me monter tout seul la distribution qui me convient, avec une solution pérenne.

A partir de ce moment, je bute sur l'éternelle question : Que choisir ?

J'ai besoin d'une distribution légère, récente, pérenne. Je veux pouvoir installer uniquement ce dont j'ai besoin. 

J'ai refait un énième tour des disributions existantes, et j'ai choisi par élimination :

- Récente : je vais quitter un peu Debian qui a des cycles de livraison très espacés
- Pérenne : une distribution majeure : Debian, Fedora, OpenSUSE, Ubuntu, ...
- Une distribution légère : exit Mageia, Linux Mint, Centos, Ubuntu, Fedora, ...
- Un bureau léger : XFCE ou LXDE ou Openbox
- Joli : avec XFCE, j'ai un bureau uniforme avec des applications par défaut adaptés à l'environnement graphique de XFCE, pas besoin de me battre avec les différentes version de GTK ou QT. Et personnalisable à l'envie.
- Pas d'installation par défaut : Archlinux ou Gentoo pour pouvoir choisir et installer exactement ce dont j'ai besoin

Ce sera donc une Archlinux avec un bureau XFCE.

Archlinux, c'est quand même plus pour les barbus. Mais avec un peu de patience et de longueur de temps, rien n'est impossible. [La documentation d'installation en français est très bien faite](https://wiki.archilinux.fr/Installation 'Installation Archlinux en français'), il ne manque que très peu d'information pour y arriver même sans tout comprendre. Un minimum de connaissance de la ligne de commande est nécessaire malgré tout.

Je ne vais donc pas paraphraser ce qui est dans le guide d'installation qui est parfait, je vais simplement noter les quelques points sur lesquels j'ai butés et compléter avec l'installation sur virtualbox et avec le bureau xfce car le guide d'installation s'arrête juste avant l'installation du bureau.

### Trucs et astuces pendant l'installation

#### Partitionnement

Personnellement j'ai utilisé fdisk.

Il suffit d'un petit `fdisk /dev/sda`

Puis créer les nouvelles partitions avec la commande `n`

Laisser les choix par défaut et ne renseigner que la taille des partitions

Sauvegarder avec la commande `w`


#### Amorçage

J'ai utilisé GRUB, simplement parce que je le connais alors que je ne connais pas syslinux.


#### SOS installation

Une faute de frappe est si vite arrivée, en cas problème sur le système que vous venez de construire, il est toujours possible de redémarrer sur l'iso puis de monter la partition contenant le système et de "chrooter" dessus.

	mount /dev/sda3 /mnt
	arch-chroot /mnt

A partir de là, vous pouvez corriger les petites erreurs sans être obligé de tout reconstruire.


A la fin de la procédure d'installation, vous avez Archlinux installé avec un compte root et un utilisateur, sans environnement graphique. Il est temps d'installer xfce.


### Installation de l'environnement graphique

Au redémarrage, nous allons nous connecter en root pour les installations suivantes

#### Réseau

A la fin de la procédure d'installation, après le démarrage, il ne faut pas oublier de démarrer le service dhcpcd pour avoir accès au réseau.

	systemctl enable dhcpcd

#### Virtualbox

En toute logique, la première étape avant l'installation de Xfce, c'est d'installer le système graphique Xorg. Mais là, je vais utiliser une voie un peu détournée, je vais directement installer les additions invité de virtualbox qui embarque le serveur xorg. Il ne va prendre que les éléments dont il a besoin, sans installer tous les drivers video. De plus, pas besoin de monter l'iso des additions invité, cela se fait par l'installation de paquets. Vraiment hyper pratique

Avec un simple :

	pacman -S virtualbox-guest-utils

j'aurais mon serveur Xorg, mesa, virtualbox-guest-modules, etc...

J'ai buté par contre sur plusieurs petit trucs bêtes pour le partage de répertoire avec le host :

- il faut créer un répertoire /media qui n'existe pas à l'installation de Archlinux. C'est là que par défaut est monté le répertoire partagé
- pour un montage automatique, il faut démarrer le service virtualboxclient par un `systemctl enable virtualboxclient`

Pour le reste, il suffit de suivre [le wiki d'Archlinux sur virtualbox](https://wiki.archlinux.org/index.php/VirtualBox 'Wiki Archlinux sur VirtualBox en anglais).

#### Xfce

Le plus facile, installer xfce :

	pacman -S xfce4

puis pour le démarrer :

	startxfce4


	
### Un peu de confort

#### slim

J'ai installé un petit gestionnaire de démarrage pour lancer xfce tout seul. J'ai choisi slim, là encore parce que je le connais.

Pour l'installer : 
	
	pacman -S slim

Comme j'ai crée mon utilisateur avant d'installer xorg-init, je dois d'abord copier le fichier .xinitrc sur mon répertoire

	cp {/ect/skel,~/}.xinitrc

Ensuite, penser à décommenter la ligne dans $HOME/.xinitrc 

	exec startxfce4

Pour un login automatique, aller dans le fichier `/etc/slim.conf` et décommenter la ligne `auto_login` en remplaçant `no`par `yes`.


#### sudo

La commande sudo devient vite indispensable quand vous êtes connectés avec votre compte et que vous voulez installer des paquets.

Elle s'installe tout simplement avec :

	pacman -S sudo
	
Puis, il convient d'aller dans le fichier `/etc/sudoers` et d'ajouter la ligne suivante.

	monuser ALL=(ALL) ALL

Vous pouvez aussi installer gksu, très pratique si vous voulez lancer thunar en root.





