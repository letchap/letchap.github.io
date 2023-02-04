Title: Quel langage de programmation choisir pour débuter
Date: 2014-04-28 22:36
Category: Python
Tags: Python, Java, C++, Perl
Slug: quel-langage-de-programmation-choisir-pour-debuter

Il y a de cela un an et demi, après avoir installé mon premier Linux, j'ai cherché un langage de programmation pour débutant. Je voulais réaliser des petits programmes simples pour me faciliter certaines tâches comme récupérer des documents sur internet ou convertir des fichiers.

La toute première question que je me suis posé fut : "Mais quel langage je vais bien pouvoir choisir ?". Question d'autant plus ardue que je n'y connaissais vraiment rien.

Evidemment, j'avais entendu parlé de certains langages comme Java ou C++, mais dès les premières recherches, je lis qu'en Java, tout objet est une classe. Rédhibitoire pour moi, les classes, quand on n'a jamais fait de programmation, ce n'est pas instinctif.

De la même manière, je connaissais php de nom, mais rapidement, je me rends compte que c'est surtout utile pour monter un site web.

Le premier langage sur lequel je tombe alors est Perl. Et dès l'introduction, je lis la devise Perl qui décomplexe n'importe quel amateur "Il y a toujours plusieurs façons de faire". Je me dis alors que je suis sur la bonne voie. Malheureusement, je pense que pour un débutant, Perl est un peu aride car très condensé. En une seule ligne, il est possible d'effectuer beaucoup de tâches, du coup, la relecture du code est un peu complexe. Il y a un gros ticket d'entrée.

Et puis, au hasard d'une lecture, en l'occurrence full circle magazine, je tombe sur [un tutoriel pour Python](http://www.fullcirclemag.fr/?post/2012/06/07/Numéro-spécial-PYTHON%2C-volume-1). Le premier article d'une longue série concerne le programme "Hello world" qui tient dans la ligne suivante :

    print("Hello world!")

Difficile de faire plus simple.

A titre de comparaison, les "Hello world" en Perl, Java et C++ paraissent plus trapus.

    Perl
    print "Hello world!\n";

    Java
    public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        }
    }

    C++
    #include <iostream>

    int main()
    {
        std::cout << "Hello, new world!" << std::endl;
        return 0;
    }

Encore un petit exemple pour illustrer la facilité d'utilisation de Python : pour déclarer une variable, il suffit de faire :

    x='toto'

Nous avons déclaré la variable x en lui affectant la valeur `toto`. Un jeu d'enfant !

Python est un langage bien adapté pour les débutants car :

- comme nous venons de le voir, sa syntaxe est très simple,
- il n'exige pas l'utilisation de classes. Il est possible de très rapidement de faire un programme complet sans une seule classe,
- il est multi-plateforme. Pour moi qui travaille à la fois sur Linux et sur OSX, je n'ai pas besoin de réécrire de code, il tourne sur les deux systèmes (et sur Windows bien sûr même si je ne l'ai jamais expérimenté),
- il est très documenté. Il est toujours possible également d'attrappé de bouts de code à droite à gauche qui vont faire le travail sans avoir forcément tout compris au début,
- Il y a des informations partout, y compris en français, ce qui est plus facile pour démarrer, même si on est familier de la langue de Shakespeare,
- il est capable de tout faire : du web, des maths, des interfaces, ... rien ne lui est interdit.

Pour vous donner un petit exemple, en partant de zéro, j'ai pu au bout de quatre mois à écrire un petit programme qui se connecte sur un site internet et qui récupère un fichier. [Le programme se trouve ici]({filename}/wget-en-python-3-avec-gestion-des-cookies-et-du-post.markdown).

Ensuite, comme j'ai pu le lire un peu partout, il faut sans doute 10 ans pour maîtriser un langage. Et c'est là encore un gros avantage de Python, il permet d'appendre à son rythme sans attendre 10 ans pour se faire plaisir. On peut commencer à écrire des programmes simples et puis, avec un peu plus d'expérience, on attaque les classes. Mais encore une fois, ce n'est pas une obligation. De la même manière, on peut appendre module par module : le module de traitement d'image, le module d'interface graphique, la connexion à une base de données ... A son rythme je vous dis... Et si un jour vous voulez l'utiliser de manière professionnelle, pas de soucis, il est aussi fait pour ça.

Si vous êtes convaincu par Python, quelques petites astuces pour démarrer :

- apprendre à utiliser la ligne de commande en parallèle (si vous êtes sur Linux ou Mac). C'est important pour lancer un programme python, mais également pour installer des modules complémentaires python (via la commande `pip`)
- lire, lire et lire
- faire des essais, se tromper, lire, refaire des essais, et miracle, ça fonctionne
- utiliser la ligne de commande python pour tester son script en direct
- bien comprendre le système d'encodage (aka c'est quoi UTF8 ?)

Des liens utiles :

- [le site officiel de python](https://www.python.org)
- [Openclassroom (ex site du Zéro)](http://fr.openclassrooms.com/informatique/python/cours)
