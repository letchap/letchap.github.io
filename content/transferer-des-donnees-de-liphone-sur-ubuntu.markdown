Title: Transférer des données de l'iPhone sur Ubuntu
Date: 2023-02-09 18:52
Category: Linux
Tags: Linux, Ubuntu, iPhone
Slug: transferer-des-donnees-de-liphone-sur-ubuntu

Il est toujours compliqué de brancher un iPhone sur un ordinateur Linux. A chaque fois je me demande comment faire. Je me note donc la procédure une bonne fois pour toute.

Tout d'abord vérifier que les packages suivants sont bien installés :

	sudo apt install libimobiledevice6 libimobiledevice-utils
	sudo apt install ifuse

Puis créer un répertoire sur lequel monter l'iPhone :

	sudo mkdir /media/iPhone
	
Afin monter le téléphone :

	ifuse /media/iPhone

J'ai trouvé les informations sur [ce lien](https://www.maketecheasier.com/easily-mount-your-iphone-as-an-external-drive-in-ubuntu/)
