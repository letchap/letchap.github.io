Title: Comment installer Lubuntu 12.04
Date: 2013-02-19 23:18
Category: Lubuntu
Tags: 12.04, BIOS, Boot, Live CD, Live USB, Lubuntu, LXDE
Slug: comment-installer-lubuntu-12-dot-04

Le guide d’installation décrit ci-dessous concerne plus particulièrement la version 12.04 de Lubuntu, la version qui est installée sur mon ordinateur. Ne sont exposés que les principes généraux pour une installation réussie, principes qui peuvent s'appliquer à un très grand nombre de distributions, l'important est de comprendre ce que nous sommes en train de faire. Pour plus de détail, les guides d'installation de chacune des distributions sont généralement disponibles sur les sites des dites distributions ou sur des blogs.

Le principe général est le suivant :

- Je cherche la distribution qui me convient,
- Je récupère une image .iso de la distribution que je souhaite installer,
- Je créé un live CD ou un live USB,
- Je démarre (boot en anglais) sur le CD ou sur la clé USB,
- Je choisis de tester la distribution avant de l’installer ou je l’installe directement,
- Lors de l’installation je choisis ou non de conserver mon ancien système d’exploitation,
- Je découvre les joies de Lubuntu.

Avant de démarrer, nous avons besoin :

- d’un CDRom de 700Mo ou d’une clé USB de 1Go (pour la version 12.04 de Lubuntu c’est suffisant, pour certaines versions c'est largement insuffisant),
- d’un ordinateur avec une connexion internet pour télécharger une image disque,
- d’un ordinateur (ça peut être le même) pour graver l’image disque sur le CDRom ou pour la copier sur la clé USB,
- d’un ordinateur, (ça peut toujours être le même) capable de démarrer sur CDRom ou sur une clé USB.

Si vous n'avez rien de tout ça, il est possible d'acheter un CD tout prêt avec l'image disque auprès de l'éditeur de la distribution choisie.

C’est bon, vous avez tout ce qui figure sur la liste des courses, nous allons pouvoir commencer l’installation.

### 1) Je cherche la distribution qui me convient

Tout est expliqué [ici]({filename}/quel-linux-choisir.markdown "Quel Linux choisir ?").

### 2) Je récupère une image disque de la distribution que je souhaite installer

Mais bon sang, c’est quoi une image disque ?

Une image disque est un fichier .iso qui contient la distribution à installer. Pour une même distribution, il peut se trouver plusieurs fichiers .iso, en fonction des versions, des bureaux, ou du processeur (32 ou 64bits).

Il est aussi souvent possible de les télécharger soit en direct download soit par torrent. Si possible, il est préférable de télécharger par torrent, c’est plus stable et souvent plus rapide.

### 3) Je créé un live CD ou un live USB

Créer un live CD ou un live USB consiste à copier le fichier .iso sur le CD ou la clé USB.

#### Créer un live CD

Maintenant que j’ai récupéré l’image que je voulais, comment je la grave sur le CDRom ?

Vous êtes sous Windows : je ne sais pas, je n’ai pas Windows. Mais vous pourrez trouver des tutoriels un peu partout.

Vous êtes sous OS X : attention, pour graver l’image disque sur le CD, il convient de passer obligatoirement par l’utilitaire de disque et de ne surtout pas faire de clic droit ou cmd clic sur l’image disque pour la graver. Une fois sur l’utilitaire de disque, il n’y a plus qu’à sélectionner « graver une image disque » sur le CDRom.

Vous êtes déjà sous Linux : je n’ai jamais gravé une image disque sous Linux, je ne sais donc pas comment faire, car une fois sur Lubuntu, je suis rapidement passer à la clé USB.

#### Créer un live USB

Toute la procédure est décrite [ici]({filename}/fabriquer-une-cle-live-usb-depuis-nimporte-quelle-distribution-linux.markdown).

### 4) Je démarre (boot en anglais) sur le CD ou sur la clé USB

Pourquoi je dois démarrer sur le CDRom, et d’ailleurs ça veut dire quoi ?

Lorsque vous démarrez l’ordinateur, sa première action est de chercher sur quel support démarrer et de lancer le système d’exploitation qu’il trouve sur ce support. Cela se passe dans le BIOS du PC.

Par défaut, le PC va démarrer sur le disque dur pour lancer Windows.

Il est possible de changer les paramètres du BIOS afin qu’il démarre sur le CD ou la clé USB. Sur mon PC (Toshiba Satellite), il faut appuyer la touche F12 au démarrage, puis sélectionner le support. Chaque marque à sa propre façon d’entrer dans le BIOS. Avec une petite recherche sur internet vous trouverez celle de votre PC.

Attention, cette procédure n'est valable que pour les PC démarrant avec le BIOS. Elle n'est pas valable pour les PC les plus récents démarrant avec UEFI.

### 5) Je choisis de tester la distribution avant de l’installer ou je l’installe directement

Il est possible de tester une distribution avant de l’installer définitivement sur son ordinateur, sans toucher à son système d’exploitation. C'est ce qu'on appelle une session live. Que cela soit par CD ou clé USB, l’ordinateur va uniquement utiliser les composants matériel (processeur, mémoire vive, carte video, etc …) sans toucher au disque dur. Tous les accès au système d’exploitation se feront sur le CD ou la clé USB. Et une fois l’ordinateur éteint, c’est comme s’il ne s’était rien passé. Cela permet de tester dans des conditions réelles sa distribution, de se faire une idée de son fonctionnement avant de choisir une installation définitive.

L’installation définitive peut se faire à partir de cette même session live.

L’installation définitive peut se faire aussi sans test dès le départ au moment du boot, puisque c’est au début du démarrage sur clé ou CD qu’il est en général demandé soit de tester soit d’installer la distribution.

### 6) Lors de l’installation je choisis ou non de conserver mon ancien système d’exploitation

Personnellement, j’ai complètement écrasé l’ancien système, je n’ai donc pas partitionné le disque dur pour installer le nouveau système à coté de l’ancien, mais sachez qu’il est tout à fait possible de garder son ancien OS (et donc toutes ses données) à coté de Linux. Il vous sera alors demandé au redémarrage de choisir entre les deux systèmes celui sur lequel vous voulez démarrer.

Pour installer le nouveau système à coté de l’ancien, il faudra réserver une place sur le disque dur pour le petit nouveau. Cette action s’appelle partitionner le disque dur, c'est-à-dire créer deux (ou plus) espaces étanches pour chacun des deux OS. Je vous mets en garde si vous ne l'avais jamais fait, une fausse manipulation et vous risquez de tout perdre, donc pensez à sauvegarder avant.

### 7) Je découvre les joies de Lubuntu

Il ne reste plus qu’à suivre la procédure d’installation, avec une connexion internet c’est mieux (ainsi les compléments d’installation seront téléchargés au fur et à mesure du processus), redémarrer et goûter au plaisir de votre tout nouvel OS.

