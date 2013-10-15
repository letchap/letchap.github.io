Title: Quelle distribution légère choisir pour une vieille configuration?
Date: 2013-06-02 13:09
Category: Linux
Tags: Lubuntu, Mageia, Bodhi Linux, Crunchbang
Slug: quelle-distribution-legere-choisir-pour-une-vieille-configuration

Ces dernières semaines, plusieurs distributions adaptées aux petites configurations ont été livrées ou mises à jour :

- Lubuntu est passé en version 13.04 Raring Ringtail, 
- Mageia qui existe en version LXDE a livré sa version 3, 
- Debian a livré sa version Wheezy sur laquelle se base la distribution légère Crunchbang, 
- une version E17 du bureau Enlightenment est arrivé sur Bodhi Linux.

Petite parenthèse : je mets hors catégorie Toutou Linux qui reste LA distribution sur les plus vieux PC, qui transforme un canasson en cheval de course, mais dont le look peut parfois étonner.

Chacune de ces distributions est supposée tourner sur un ordinosaure, mais qu'en est-il dans la vraie vie, quand il s'agit de les installer concrétement et de les utiliser au quotidien ?

J'ai installé ces 4 distributions sur mon portable Toshiba M40 de 2003 (1,4 GHz, 512Mo de RAM). Verdict :

### Lubuntu 13.04

Pendant très longtemps, Lubuntu 12.04 LTS a été la seule distribution sur mon PC. Consommation de CPU et de RAM réduite, prise en main facile pour des débutants, aussi bien lors de l'installation que dans une utilisation courante. Le bureau LXDE reste très adapté sur les anciennes configurations.

Est ce toujours le cas pour les suivantes, la 12.10 puis la 13.04 ?

La réponse tient en une seule phrase : ces versions sont inutilisables sur des machines non-pae comme la mienne car le kernel de Ubuntu 13.04 n'est livré qu'avec une version pae. Ce que je trouve regrettable car cela exclu de fait les plus anciennes machines de Lubuntu dont elles sont sensées être la cible.

Si vous voulez absolument utiliser Lubuntu, ce qui est légitime compte tenu des qualités d'ensemble de cette distribution, rester en 12.04. En téléchargement [à cette adresse](https://help.ubuntu.com/community/Lubuntu/GetLubuntu "Lubuntu").

### Mageia 3 LXDE

Contrairement à Lubuntu, les machines non-pae supportent très bien le passage de Mageia 2 vers Mageia 3. Mageia est une distribution très agréable à utiliser, en particulier grâce au son centre de contrôle qui permet de configurer facilement son ordinateur.

Le confort d'utilisation est en revanche assez sensiblement réduit avec la version 3 (il n'était déjà pas fameux avec Mageia 2 avec simplement 512Mo de RAM). La distribution "rame" même avec un bureau LXDE. Rien de rédhibitoire mais du coup, il y a mieux sur des vieilles machines.

C'est [ici pour le téléchargement](http://www.mageia.org/fr/downloads/ "Mageia").

### Bodhi Linux

Y a t-il un bug ? Voyant qu'il était possible de charger une version 32bits non-pae, je me suis dit "chouette, je vais pouvoir installer une jolie distribution sur mon PC". Ce que j'en avais vu en virtualisant m'avait donné envie d'en savoir plus sur le bureau Enlightenment. Et là, patatras, impossible de lancer le live USB, je bloque au moment du choix de la configuration du bureau. Tant pis!

Mais si cela fonctionne chez vous, vous pouvez le [trouver là](http://www.bodhilinux.com/downloads_desktop.php "Bodhi Linux").

### Crunchbang

Mon coup de coeur !

Crunchbang est une version dérivée de Debian, utilisant le bureau openbox. La consommation de CPU et de RAM est réduite, comparable à ceux que je pouvais avoir avec Lubuntu 12.04. L'utilisation est très fluide, même lorsque plusieurs applications sont ouvertes. La présentation de base est très sobre.

Cette distribution ne s'adresse pas aux débutants. Il faut avoir un peu de connaissances de Linux pour le paramétrage du système. Un seul petit exemple, la francisation complète se fait en ligne de commande par le terminal là où toutes les autres proposent des mises à jour par une interface graphique.

Par contre, ceux qui viennent de Lubuntu (comme moi) ne seront pas dépaysés par l'univers Debian/Ubuntu (paquets .deb, synaptic, ...) et les plus curieux pourront approfondir avec bonheur leurs connaissances de Linux.

En résumé, une utilisation très fluide et une incitation à ouvrir le capot, c'est le bonheur.

[A télécharger d'urgence là](http://crunchbang.org/download/ "Crunchbang").

En conclusion, pour avoir une distribution légère sur son PC, je recommenderais Lubuntu pour les débutants et Crunchbang pour les plus aventuriers.

