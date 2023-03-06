Title: Utiliser Foundation et Sass avec Pelican
Date: 2014-08-29 21:38
Category: Foundation
Tags: Pelican, Foundation, Sass, Grunt
Slug: utiliser-foundation-et-sass-avec-pelican

Lorsque j'ai créé le site avec Pelican, j'ai cherché un framework responsive et le premier sur lequel je suis tombé sans trop chercher fut [Bootstrap](http://getbootstrap.com "Bootstrap"). En testant le CMS [Microbe](https://gitorious.org/get_microbe "Get Microbe"), j'ai découvert un nouveau framework : [Foundation](http://foundation.zurb.com "Foundation"). Voyant du Bootstrap partout, je me suis décidé à passer sur Foundation. En terme de fonctionnalités, il n'existe pas une énorme différence entre les deux, dans tous les cas un système de grille permet de gérer les différentes tailles d'écran en partant du principe que le site est d'abord créé pour des écrans mobiles,  un fichier style de base très complet est fourni en standard et quelques applets javascript agrémente le tout. Le passage de Bootstrap à Foundation n'était motivé que par l'esthétique pour ne pas avoir un site "qui a le même look que les autres".

Comme la logique entre Bootstrap et Fondation est la même, la migration de l'un vers l'autre se fait sans douleur.

Foundation apporte néanmoins deux fonctionnalités supplémentaires assez intéressantes : l'utilisation de [Sass](http://sass-lang.com "Sass") et de [Grunt](http://gruntjs.com "Grunt"). Sur le site de Foundation, [une page est dédiée à l'installation](http://foundation.zurb.com/docs/sass.html) de ces deux fonctionnalités qui sont liées. Ils existent pas mal de tutoriels en anglais qui expliquent comment créer un nouveau projet Fondation avec Sass. 

Ce que nous allons voir plus particulièrement ensemble est l'utilisation de ces deux outils avec Pelican. Mais tout d'abord ...


### Installation de Sass et automatisation des tâches avec Grunt

L'installation de Foundation dans sa version Sass est assez fastidieuse. Pas compliquée, mais fastidieuse. Cela m'a freiné pendant un petit moment. Pourquoi installer tout un bazar alors que le site fonctionne très bien avec css. Ce qui m'a finalement convaincu dans un premier temps, ce sont plus les possibilités d'automatisation apportées par Grunt que Sass lui-même.

Pourquoi fastidieux, parce qu'il faut installer un certain nombre de modules. Sass et Foundation sont des gems de Ruby. Donc, il faut avoir Ruby, donc rvm ou rbenv pour installer les gems. Ensuite, il faut installer Grunt, mais pour installer Grunt, il faut avoir npm. Plus compliqué que de simplement gérer une feuille de style.

Je vous renvoie à nouveau à la procédure complète sur [le site de Foundation](http://foundation.zurb.com/docs/sass.html "Getting start with Sass"). 

Par contre, une fois que tout est installé, c'est le bonheur.

#### Création d'un nouveau projet

Pour créer un nouveau projet, il suffit de se positionner dans le répertoire de son choix et de lancer la commande :

    foundation new project_name ‐‐libsass

Le projet contient alors :

- bower_components : ensemble des fichiers scss de Foundation ainsi que les javascripts
- css : le répertoire de sortie des fichiers scss après conversion en css
- js : nos propres javascripts
- node_modules : contient essentiellement grunt 
- scss : nos fichiers scss
- Gruntfile.js : j'y reviens juste après, le fichier permettant l'automatisation de nos tâches
- index.html : un fichier permettant de tester les modification de style


#### Mise à jour de Foundation

Si vous souhaitez bénéficier des dernières versions de Foundation, il suffit de lancer la commande suivante dans le répertoire projet :

    foundation update

Cela ne met à jour que le répertoire bower_components, avec les tous derniers fichiers scss ou javascript. C'est __TRES__ important pour la suite.


#### Utilisation de Sass et Grunt

Le véritable intérêt réside dans la mise à jour du style avec Sass et Grunt. Pour bien comprendre comment cela fonctionne, il faut faire un petit tour dans les fichiers gruntfile.js et scss/app.css.

Le contenu de gruntfile.js :

    module.exports = function(grunt) {
      grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
          options: {
            includePaths: ['bower_components/foundation/scss']
          },
          dist: {
            options: {
              outputStyle: 'compressed'
            },
            files: {
              'css/app.css': 'scss/app.scss'
            }        
          }
        },

        watch: {
          grunt: { files: ['Gruntfile.js'] },

          sass: {
            files: 'scss/**/*.scss',
            tasks: ['sass']
          }
        }
      });

      grunt.loadNpmTasks('grunt-sass');
      grunt.loadNpmTasks('grunt-contrib-watch');

      grunt.registerTask('build', ['sass']);
      grunt.registerTask('default', ['build','watch']);
    }

Dans ce fichier sont définies deux tâches : une tâche de transformation de fichier app.scss en app.css à travers la commande `sass` et une tâche de mise à jour de notre fichier css à chaque modification du fichier scss avec la commande `watch`.

Ce qui veut dire concrètement que, lorsque nous aurons créé notre projet, nous allons lancer dans le terminal la commande `grunt` qui va à la fois créer notre premier fichier app.css à partir du fichier app.scss et nous permettre de visualiser en temps réel sur notre page html toutes les modifications que nous pourrons apporter au fichier app.scss.

    grunt
    Running "sass:dist" (sass) task
    File "static/css/app.css" created.

    Running "watch" task
    Waiting...


Nous sommes maintenant prêt à apporter les modifications de style à notre site. Pour cela, regardons maintenant le contenu du fichier app.scss

    @import "settings";
    @import "foundation";

    // Or selectively include components
    // @import
    //   "foundation/components/accordion",
    //   "foundation/components/alert-boxes",
    //   "foundation/components/block-grid",
    //   "foundation/components/breadcrumbs",
    //   "foundation/components/button-groups",
    //   "foundation/components/buttons",
    //   "foundation/components/clearing",
    //   "foundation/components/dropdown",
    //   "foundation/components/dropdown-buttons",
    //   "foundation/components/flex-video",
    //   "foundation/components/forms",
    //   "foundation/components/grid",
    //   "foundation/components/inline-lists",
    //   "foundation/components/joyride",
    //   "foundation/components/keystrokes",
    //   "foundation/components/labels",
    //   "foundation/components/magellan",
    //   "foundation/components/orbit",
    //   "foundation/components/pagination",
    //   "foundation/components/panels",
    //   "foundation/components/pricing-tables",
    //   "foundation/components/progress-bars",
    //   "foundation/components/reveal",
    //   "foundation/components/side-nav",
    //   "foundation/components/split-buttons",
    //   "foundation/components/sub-nav",
    //   "foundation/components/switch",
    //   "foundation/components/tables",
    //   "foundation/components/tabs",
    //   "foundation/components/thumbs",
    //   "foundation/components/tooltips",
    //   "foundation/components/top-bar",
    //   "foundation/components/type",
    //   "foundation/components/offcanvas",
    //   "foundation/components/visibility";


Notre fichier app.scss (et par construction app.css) et construit à partir de l'ensemble des fonctions par défaut de Foundation qui se trouvent dans le répertoire bower_components (si si regardez bien le includePaths du fichier gruntfile.js) et des modifications que nous pourrions apporter à ces fonctions par défaut à partir du fichier _settings.scss.

Dit autrement, si on ne touche à rien, le fichier app.css est identique au fichier foundation.min.css classique.

Les modifications de style vont donc se faire en enlevant simplement des commentaires sur certaines lignes de _settings.scss.
    

### L'utilisation de Fondation avec Pelican

Un projet Pelican est structuré de la manière suivante :

    Mon-site
        |__ content
        |__ mon-theme-zf-css
        |   |__ static
        |   |   |__ css
        |   |   |__ js
        |   |__ template
        |__ output
        |__ pelicanconf.py

Lorsque que je crée un projet Foundation, je crée mon-theme-zf-sass, qui va avoir une structure différente de celle attendue par Pelican :

    mon-theme-zf-sass
        |__ bower_components
        |__ css
        |__ js
        |__ node_modules
        |__ scss
        

Après la création de mon-theme-zf-sass, je vais commencer par modifier le répertoire pour le rendre compatible avec la structure Pelican comme ceci :
    
    mon-theme-zf-sass
        |__ bower_components
        |__ static
        |  |__ css
        |  |__ js
        |__ node_modules
        |__ scss
        

Je dois alors modifier le fichier gruntfile.js pour qu'il prenne en compte la modification de destination du fichier css en remplaçant la ligne `'css/app.css': 'scss/app.scss'` par `'static/css/app.css': 'scss/app.scss'`.
        
        
J'ai déjà un thème Foundation css personnalisé. Il est composé de deux fichiers css, un fichier foundation.min.css qui contient les valeurs par défaut de fondation et un fichier style.css qui contient ma personnalisation. Je vais commencer par mettre exactement à l'identique mon thème Foundation css et mon thème Foundation Sass. Pour cela, il faut simplement :

- copier le fichier style.css dans le répertoire scss et le renommer _style.scss sans en modifier le contenu. Je transforme mon fichier style.css en "partial" scss pour qu'il puisse être intégré lors du traitement sass. Le preprocesseur sass sait très bien lire du contenu css.
- ajouter `@import "style"`dans le fichier app.scss. Je paramètre l'import de mon "partial"
- ne pas toucher au fichier _settings.scss

Le fichier app.css en sortie du traitement sass sera à l'identique de la somme de mes fichiers foundation.min.css et style.css. Cela est possible grâce à la possibilité offerte par sass de constituer un fichier css à partir de plusieurs fichiers scss, et parce qu'un fichier style.css est un fichier style.scss qui s'ignore.

Petit bonus, il est possible aussi d'ajouter le fichier normalize.scss, ce qui nous donne (en respectant bien cet ordre) :

    @import "normalize";
    @import "settings";
    @import "fondation";
    @import "style";


Si je souhaite bénéficier de nouvelles fonctionnalités Foundation, je n'ai qu'à faire un `foundation update` qui mettra à jour le répertoire bower_components, sans toucher aux autres répertoires ou fichiers de mon-theme-zf-sass. Pratique.

Dernier point, il ne faut pas oublier dans le fichier base.html de modifier l'appel aux feuilles de style en remplaçant normalize.css, foundation.min.css et style.css par app.css.

Voilà, tout est prêt pour utiliser Pelican avec Foundation et Sass. Pour faire les modifciations et voir le résultat en direct, il suffit de faire :

    cd mon-blog
    make devserver
    cd mon-theme-zf-sass
    grunt

Puis lancer le navigateur sur localhost:8000. Et à chaque modification de n'importe quel fichier Pelican, les modifcations apparaîtrons immédiatement sur le site. C'est magique !

Maintenant, il ne me reste plus qu'à essayer de "tuer" mon fichier style.css pour exploiter tout le potentiel de Sass. Ce sera pour de prochains épisodes.

### Un dernier point avec git

A la création d'un nouveau projet Foundation, un dépôt git est automatiquement créé (pour grunt je crois). Comme il se crée à l'intérieur de mon dépôt git existant (celui qui contient mon site pelican), ça met un peu le bazar quand je veux committer mes modifications. La solution la plus simple que j'ai trouvée jusqu'à présent est de supprimer le répertoire .git de mon projet Foundation, ce qui n'empêche pas les mises à jour futures avec grunt.

