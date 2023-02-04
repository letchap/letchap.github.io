Title: Petite blague suite à la clean install Yosemite
Date: 2015-03-21 11:32
Category: Mac OS X
Tags: Yosemite, clean install, action de dossier, CPU
Slug: petite-blague-suite-a-la-clean-install-yosemite


Après une clean install de Yosemite sur mon iMac mi-2010, j'ai rencontré un problème de consommation excessive de CPU par le programme "Distributeur des actions de dossier".

La solution de contournenment pour retrouver un ordinateur qui fonctionne normalement est de décocher l'utilisation des actions de dossiers :

Dans le finder faire un clic droit sur un dossier, n'importe lequel.

![clic droit dossier]({static}/images/blagueyosemite/clicdroit.png)

Puis aller dans service et cliquer sur "configuration des actions de dossier"

![service]({static}/images/blagueyosemite/service.png)

Enfin décocher la case "Activer les actions de ce dossier"

![désactiver]({static}/images/blagueyosemite/desactiver.png)

Il ne reste plus qu'à redémarrer.

Mais l'intérêt est aussi de savoir pourquoi ce processus s'emballe. Je me note deux petites actions que j'ai faite sans bien être sûr de leur efficacité, néanmoins, ça a l'air de fonctionner :

- mettre à jour les caches partagés dyld (avec Onyx par exemple dans l'onglet automation)
- supprimer les fichiers .scpt inutilisés. A la suppression des certaines applications, je me suis aperçu que des fichiers applescript de ces applications n'étaient pas supprimés. Dans le terminal, un petit `locate *.scpt` fera l'affaire, puis `rm -rf /path/to/fichier.scpt`.



