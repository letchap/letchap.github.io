Title: Transférer des fichiers de Lubuntu vers Mountain Lion
Date: 2013-02-22 21:08
Category: Mac OS X
Tags: SFTP, Cyberduck, Lubuntu, Mountain Lion, NETATALK, openssh-server, OS X, Réseau
Slug: transferer-des-fichiers-de-lubuntu-vers-mountain-lion

Comme je l’expliquais dans l’article précédent, avec Lubuntu, il n’existe pas en natif de moyen simple de transférer des fichiers en FTP (il faut installer Filezilla).

De la même manière, il n’existe pas en natif de moyen simple de communiquer avec un système Mac OS X.

Il existe 2 solutions pour le faire, une compliquée et pas très rapide, mais pour la beauté du geste, je vais la décrire, une super simple et super rapide, ma préférée.

### 1) La solution compliquée et lente : utiliser le protocole de OS X AFP avec NETATALK

AFP est le protocole natif de transfert de fichier de Mac OS X. Par défaut, il n’est pas présent sur Lubuntu. Pour mettre son Mac et son PC en réseau, il faut utiliser NETATALK.

J’avais installé cette solution avant de découvrir SFTP. La procédure d’installation est assez complexe, mais j’ai trouvé un très bon tutoriel [ici](http://www.monnetamoi.net/articles.php?lng=fr&pg=81 "Installer netatalk"). Je l’ai un peu adapté à ma sauce, notamment en m’embêtant un peu moins avec les droits (je n’ai pas créé de répertoire spécial pour les transferts par exemple, et donc pas eu besoin de faire de chmod non plus), par défaut j’ai eu accès à l’ensemble du disque dur de mon PC depuis mon Mac. En même temps, seule la petite famille utilise ces deux ordinateurs donc tout le monde peut avoir accès à tout.

Cette solution ne fonctionne qu’avec les deux ordinateurs allumés et uniquement depuis le Mac. Le transfert peut se faire dans les deux sens.

En revanche, j’ai abandonné assez rapidement cette solution, en dehors du coté assez complexe de la mise en place, je trouve les transferts de fichiers assez lents et consommateur en ressources machine. Mais ça marche.

N’hésiter pas à me demander si vous voulez plus de détails.

### 2) La solution simple et rapide : SFTP et Cyberduck

Et puis, j’ai trouvé une solution beaucoup plus simple et beaucoup plus rapide en termes de temps de transfert : utiliser le protocole SFTP avec Cyberduck. SFTP, c’est du FTP sécurisé avec un échange de clé de sécurité. Dans mon exemple, cet échange de clé est transparent.

#### Sur Lubuntu

##### 1) Installer openssh-server

Le logiciel openssh-server vous permettra de transformer votre PC en serveur SFTP, et donc vous permettra de vous connecter depuis Mac OS X en SFTP.

Cela peut se faire à partir de l’installateur de paquet Synaptic.

Par défaut, le serveur sera allumé au démarrage de l’ordinateur.

##### 2) Récupérer l’adresse IP de l’ordinateur

Un simple clic droit sur l’icône de connexion réseau vous donnera l’information.

C’est tout sur Lubuntu.

#### Sur Mac OS X

J’ai fait cette installation avec la version Mountain Lion de OS X. Je pense que cela fonctionne avec les versions antérieures.

##### 1) Installer Cyberduck

Cyberduck est un logiciel FTP bien connu des Mac users. Il est disponible gratuitement sur le site de [Cyberduck](http://cyberduck.ch/ "Cyberduck") (payant sur le Mac App Store).

##### 2) Créer une nouvelle connexion SFTP en précisant

- L’adresse IP
- Le port : 22
- Les login et mot de passe de votre session Lubuntu

Dites Ok quand Cyberduck vous pose une question.

Et comme par magie, vous êtes connecté à Lubuntu, sur l’ensemble du disque dur.

Et c’est tout sur Mac OS X. Simple, non ?

Cette solution ne fonctionne qu’avec les deux ordinateurs allumés et uniquement depuis le Mac. Le transfert peut se faire dans les deux sens.

Encore une fois, cela reste très simple car je ne m’embête pas à gérer des droits utilisateurs, restant dans le cadre d’une utilisation familiale. Mais qu’est ce que c’est pratique ! Plus de copie sur clé USB, et en plus le transfert est hyper rapide.


