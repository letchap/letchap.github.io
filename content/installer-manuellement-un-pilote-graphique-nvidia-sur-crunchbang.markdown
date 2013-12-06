Title: Installer manuellement un pilote graphique Nvidia sur Crunchbang
Date: 2013-06-05 22:02
Category: Crunchbang
Tags: Crunchbang, Nvidia, Terminal
Slug: installer-manuellement-un-pilote-graphique-nvidia-sur-crunchbang

La distribution Crunchbang est une distribution trés légére basée sur Debian. Lors de l'installation sur mon vieux PC, la partie inférieure de l'écran est inutilisable car la carte graphique est mal gérée. Il faut alors installer le pilote graphique propriétaire, Nvidia dans mon cas. Crunchbang, se voulant trés léger, il n'y a pas par défaut d'interface graphique pour installer le pilote, nous allons donc l'installer via le terminal.

Ce post est très largement inspiré du wiki Debian disponible [à cette adresse](http://wiki.debian.org/NvidiaGraphicsDrivers#NVIDIA_Proprietary_Driver "wiki Debian")

### Puis - je installer des pilotes non-libres ?

La première étape consiste à vérifier que nous pouvons installer des paquets non-libres, comme celui contenant le pilote nvidia qui nous intéresse. Par défaut, sur Crunchbang Waldorf, c'est le cas. Pour s'en assurer, il suffit de vérifier la présence de "non-free" dans la liste des sources. La commande :

	:::bash
    $ cat /etc/apt/sources.list

devrait vous renvoyer :

	## DEBIAN
    deb http://http.debian.net/debian/ wheezy main contrib non-free

S'il n'est pas présent, ajouter ces deux lignes en éditant le fichier :

	:::bash
    $ sudo nano /etc/apt/sources.list




### Quel pilote ?

La deuxième étape consiste à savoir quel pilote installer en fonction de sa carte graphique. Pour cela nous allons utiliser  nvidia-detect qui s'installe par synaptic ou à partir d'un terminal avec la commande `sudo apt-get install nvidia-detect`.

Ensuite, sur le terminal, la commande nvidia-detect vous renverra les informations sur la carte graphique et le pilote à installer.

	$ nvidia-detect
	Detected NVIDIA GPUs:
	01:00.0 VGA compatible controller [0300]: NVIDIA Corporation NV34M [GeForce FX Go5200 32M/64M] [10de:0328] (rev a1)
	Your card is only supported up to the 173.14 legacy drivers series.
	It is recommended to install the
		nvidia-glx-legacy-173xx
	package.


### J'installe mon pilote

Le pilote s'installe avec les deux commandes suivantes dans le terminal :

	:::bash
    $ sudo apt-get update
    $ sudo apt-get -r install linux-headers-$(uname -r|sed 's,[^-]*-[^-]*-,,') nvidia-kernel-legacy-173xx-dkms

Cela va également installer les dépendances, et notamment le paquet nvidia-glx-legacy-173xx.
    

### Mon pilote n'est pas détecté par défaut

La dernière étape consiste à faire reconnaître le pilote par le système, qui n'est pas détecté automatiquement par défaut. Pour cela, il faut créer un fichier de configuration :

	:::bash
    $ sudo nano /etc/X11/xorg.conf.d/20-nvidia.conf

et ajouter les lignes suivantes :

    Section "Device"
        Identifier     "Mon pilote graphique"
        Driver         "Nvidia"
        Option         "NoLogo" "1"
    EndSection
    
L'option NoLogo permet de supprimer l'affichage du logo nvidia au démarrage.

C'est fini, il ne reste plus qu'à redémarrer.
