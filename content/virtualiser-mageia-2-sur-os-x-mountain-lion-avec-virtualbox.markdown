Title: Virtualiser Mageia 2 sur OS X Mountain Lion avec VirtualBox
Date: 2013-04-09 22:02
Category: VirtualBox
Tags: VirtualBox, OS X, Mountain Lion, Mageia, guest additions, virtualisation
Slug: virtualiser-mageia-2-sur-os-x-mountain-lion-avec-virtualbox

Malgré toute sa bonne volonté mon pauvre vieux PC de 2003 touche certaines limites. La plus génante concerne l'obsolescence de la carte graphique, il m'est par exemple impossible d'utiliser Kivy.

C'est l'occasion d'installer une distribution sur mon iMac. Et pour tester un univers que je ne connais pas et qui va me changer du monde Ubuntu, nous allons installer Mageia 2.

### Dual boot ou virtualisation ?

Pour ne pas perturber les autres membres de la famille avec le choix d'un OS de démarrage, je ne souhaite pas installer Mageia en double amorçage (dual boot) sur mon iMac. J'ai la flemme de partitionner, d'installer rEfit, tout ça pour avoir un écran moche au démarrage.

La solution : la virtualisation

La virtualisation permet de démarrer une session de n'importe quelle distribution Linux à l'intérieur de Mountain Lion :

- Ca ne prend pas de place (il faut compter 8 Go pour être tranquille),
- Ca tourne de manière fluide avec 512 Mo de RAM dédiée (j'ai mis 2 Go quand même pour Mageia 2),
- Ca ne touche pas à Mountain Lion, 
- Ca permet de partager des fichiers entre Mountain Lion et Mageia très facilement,
- Ca reconnaît les port usb,
- Ca se sauvegarde,
- Ca permet de tester très facilement toutes sortes de distributions.

Le principal intérêt de la virtualisation est de pouvoir essayer sereinement des distributions, mais j'ai décidé de tester la virtualisation aussi sur la durée, je voudrais savoir si cela peut être une solution pérenne en attendant de racheter un PC et de faire une vraie installation.


### L'installation

Il n'existe pas énormément de logiciel de virtualisation sur Max OS X, et le seul gratuit est VirtualBox. Les deux autres sont VMware et Parallel Desktop.

Pour virtualiser, j'ai donc utilisé le logiciel Virtualbox. Les différentes étapes sont :

- L'installation de Virtualbox 
- Le téléchargement de l'image disque Mageia 2
- L'installation de Mageia 2 dans VirtualBox
- L'installation des compléments (VirtualBox guest additions)
- L'installation des compléments (VirtualBox extension pack)


#### Installer Virtualbox. 

C'est une installation classique sur OS X par les paquets dmg. Il est disponible au téléchargement [ici](https://www.virtualbox.org/wiki/Downloads "VirtualBox")

#### Télécharger Mageia 2

Nous allons installer la dernière version de Mageia 2 en 64 bits, elle est disponible au téléchargement sur [cette page](http://www.mageia.org/fr/downloads/ "Mageia"). Personnellement j'utilise le torrent avec transmission, c'est plus rapide et plus sûr.

Dans le dossier que vous récupérez se trouve un fichier .iso, c'est de celui dont nous aurons besoin.

Tous les Mac récents tournent en 64 bits, pour vous en assurer, vous pouvez aller dans le moniteur d'activité, il doit être indiqué Intel (64bits) dans la colonne Type.
[![Moniteur d'activité]({filename}/images/virtualbox/moniteur.png "moniteur d'activité")]({filename}/images/virtualbox/moniteur.png){: data-lightbox="moniteur" title="moniteur d'activité }

La documentation VirtualBox précise qu'il est possible de virtualiser du 64 sur du 32, je n'ai pas essayé, je ne sais pas si cela fonctionne bien.

#### Démarrer VirtualBox et installer Mageia

Le vrai travail commence maintenant

Démarrer VirtaulBox et cliquer sur nouveau. Vous saisissez alors le nom de votre distribution, Mageia
[![VirtualBox nouveau]({filename}/images/virtualbox/vb-nouvelle.png "Etape 1 : créer une nouvelle distribution")]({filename}/images/virtualbox/vb-nouvelle.png){: data-lightbox="virtualbox" title="Etape 1 : créer une nouvelle distribution" }

Ensuite choisissez la taille de la mémoire qui sera utilisé pour faire fonctionner la machine virtuelle. La mémoire vive est partagé avec le système hôte, celle dédiée à VirtualBox ne peut pas être plus de la moitié de la taille totale. Ici, j'ai choisi 2Go.
[![VirtualBox mémoire]({filename}/images/virtualbox/vb-memoire.png "Etape 2 : choisir la taille de la mémoire vive")]({filename}/images/virtualbox/vb-memoire.png){: data-lightbox="virtualbox" title="Etape 2 : choisir la taille de la mémoire vive" }

La création d'un disque dur virtuel est proposée (laissez le paramétrage par défaut)
[![VirtualBox disque dur]({filename}/images/virtualbox/vb-disk.png "Etape 3 : choisir le disque dur virtuel")]({filename}/images/virtualbox/vb-disk.png){: data-lightbox="virtualbox" title="Etape 3 : choisir le disque dur virtuel" }

Il s'agit d'un disque virtuel avec une extension vdi qui permettra plus tard si besoin d'exporter la machine virtuelle
[![VirtualBox vdi]({filename}/images/virtualbox/vb-vdi.png "Etape 4 : choisir l'extension du disque")]({filename}/images/virtualbox/vb-vdi.png){: data-lightbox="virtualbox" title="Etape 4 : choisir l'extension du disque" }

Conserver le paramétrage de taille de disque dynamiquement allouée. Seul l'espace réellement utilisé sera présent sur le disque dur de la machine hôte. Pour des soucis de performance, il est possible de choisir une taille fixe, mais évidemment, cela prend plus d'espace. A vous de voir.
[![VirtualBox taille allouée]({filename}/images/virtualbox/vb-alloue.png "Etape 5 : choisir la taille dynamiquement allouée")]({filename}/images/virtualbox/vb-alloue.png){: data-lightbox="virtualbox" title="Etape 5 : choisir la taille dynamiquement allouée" }

8Go par défaut, c'est largement suffisant pour tester une distribution.
[![VirtualBox taille]({filename}/images/virtualbox/vb-taille.png "Etape 6 : choisir la taille du disque")]({filename}/images/virtualbox/vb-taille.png){: data-lightbox="virtualbox" title="Etape 6 : choisir la taille du disque" }

Une fois tous ces éléments paramétrés, il va falloir demander à la machine de démarrer sur l'image disque de Mageia. Pour cela, il faut se rendre dans l'onglet stockage.
[![VirtualBox stockage]({filename}/images/virtualbox/vb-stockage.png "Etape 6 : onglet stockage")]({filename}/images/virtualbox/vb-stockage.png){: data-lightbox="virtualbox" title="Etape 6 : onglet stockage" }

Vous cliquez sur l'icone du CD à coté de Lecteur CD/DVD.
[![VirtualBox CD]({filename}/images/virtualbox/vb-cd.png "Etape 7 : charger l'image iso")]({filename}/images/virtualbox/vb-cd.png){: data-lightbox="virtualbox" title="Etape 7 : charger l'image iso" }

Et vous choisissez votre fichier iso.
[![VirtualBox iso]({filename}/images/virtualbox/vb-iso.png "Etape 8 : charger l'image iso")]({filename}/images/virtualbox/vb-iso.png){: data-lightbox="virtualbox" title="Etape 8 : charger l'image iso" }

Vous cliquer alors sur démarrer et lancer l'installation normale de Mageia. Attention, ne télécharger pas les compléments d'installation durant cette étape. C'est très important pour un bon fonctionnement ultérieur de Mageia.

A la fin de l'installation, vous éteignez (power off) la machine virtuelle.
[![VirtualBox power off]({filename}/images/virtualbox/vb-off.png "Etape 9 : éteindre la machine")]({filename}/images/virtualbox/vb-off.png){: data-lightbox="virtualbox" title="Etape 9 : éteindre la machine" }

Puis, vous éjectez le fichier iso (pour ne pas redémarrer l'installation à chaque fois).
[![VirtualBox eject]({filename}/images/virtualbox/vb-eject.png "Etape 10 : éjecter le fichier iso")]({filename}/images/virtualbox/vb-eject.png){: data-lightbox="virtualbox" title="Etape 10 : éjecter le fichier iso" }

Vous pouvez alors redémarrer Mageia. Une fois sur Mageia, voici quelques petites astuces pour un fonctionnement optimal de la machine virtuelle :

#### Guest additions

Tout d'abord, installer les compléments de l'installation que nous avons mis de coté tout à l'heure. L'installation sera plus propre si vous le faites maintenant et évitera des dysfonctionnements de Mageia. Pour éviter d'être embêté avec le fichier iso, vous pouvez aller dans le Centre de Contrôle Mageia (CCM) pour paramétrer les sources des programmes et supprimer la mise à jour par CD.

Mageia va en même temps installer les VirtualBox guest additions qui permettent notamment de partager un répertoire avec le système hôte. Il n'est donc pas nécessaire d'installer spécifiquement ces guest additions, laissez le CCM faire.

Une petite astuce pour les répertoires partagés, n'oubliez pas d'ajouter votre utilisateur dans le groupe VirtualBox (là encore cela se passe dans le CCM).
[![CCM]({filename}/images/virtualbox/ccm.png "Partager un répertoire")]({filename}/images/virtualbox/ccm.png){: data-lightbox="CCM" title="CCM" }

#### Extension pack

Enfin, dernière astuce, installer le VirtualBox extension pack pour pouvoir accéder aux ports USB sur la machine invitée.

Bonne virtualisation !!
