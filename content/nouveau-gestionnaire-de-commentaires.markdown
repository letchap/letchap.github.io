Title: Nouveau gestionnaire de commentaires
Date: 2023-02-05 15:31
Category: Pelican
Tags: Pelican, cusdis, disqus
Slug: nouveau-gestionnaire-de-commentaires

Avec la remise en vie du site, je voulais réinstaller un service de commentaires. Je ne veux pas utiliser Disqus (et encore moins depuis qu'ils ont introduit de la publicité) et j'ai la flemme de réinstaller Isso.

j'ai trouvé un petit utilitaire de commentaires, [cusdis](https://cusdis.com/), qu'il est possible d'herbéger soi-même, mais moi j'ai pris l'option facile dans un premier temps et pour aller vite. Il suffit de cliquer sur l'option hosted service, de créer un compte et de coller le code suivant dans sa page html.

    <div id="cusdis_thread"
      data-host="https://cusdis.com"
      data-app-id="l'id fourni"
      data-page-id="{{ PAGE_ID }}"
      data-page-url="{{ PAGE_URL }}"
      data-page-title="{{ PAGE_TITLE }}"
    ></div>
    <script async defer src="https://cusdis.com/js/cusdis.es.js"></script>

Il y a un petit écran permettant de gérer les commentaires (approbation, rejet) et la possibilité de recevoir des alertes par mail.

Ca prend 2 minutes chrono.

C'est gratuit.

Je n'ai besoin de rien de plus.


