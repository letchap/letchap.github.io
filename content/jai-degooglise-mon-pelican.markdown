Title: J'ai dégooglisé mon Pelican
Date: 2014-12-29 21:41
Category: Pelican 
Tags: degooglisons, piwik, openshift, duckduckgo
Slug: jai-degooglise-mon-pelican


Mon blog Pelican est libre, mais il cache des solutions propriétaires :

- il est hébergé par Github
- il gère les commentaires avec Disqus
- le trafic est analysé par Google analytics
- il utilise google search pour les recherches sur le site

	
Je vais dans cet article me concentrer sur la dégooglisation, à savoir, remplacer Google analytics et Google search.

### J'ai remplacé Google analytics par Piwik

Pendant longtemps j'ai buté sur le fait que je ne suis pas auto-hébergé et donc, difficile de monter des solutions libres dans ce cas. Et puis j'ai découvert Openshift de Red Hat. Cela me permet d'avoir une infrastructure cloud sous licence libre (Apache licence 2.0) sur laquelle je peux installer jusqu'à trois applications gratuitement.

La plateforme va me permettre dans un premier temps d'héberger ma solution d'analyse de trafic, puis de commentaires, et finalement mon site.

Chaque chose en son temps, je commence par l'analyse de trafic et le remplacement de google analytics. La solution sera Piwik. Piwik est un outil d'analyse de trafic web opensource (licence GPL v3). Pour plus d'information sur Piwik, vous pouvez vous rendre sur leur site [à cette adresse](http://fr.piwik.org "Piwik"). La seule contrainte de Piwik est de posséder son propre serveur, ou d'en utiliser un. Pour moi, ce sera donc le Pass (Plateform as a service) d'Openshift.

#### Créer un compte Openshift et installer Piwik

Le tutoriel est [à cette adresse](https://github.com/openshift/piwik-openshift-quickstart "Piwik Openshift Quickstart"). Je ne peux pas mieux expliquer, donc, le plus simple, c'est de suivre le lien.

Quelques petits conseils néanmoins :

- Il faut vérifier que la bonne version de Ruby est bien installée
- L'installation se fait par le terminal, pas par le site openshift
- Il faut bien vérifier l'échange de clé ssh. Si vous avez déjà utilisé git, le concept ne doit pas poser de problème.
- Une fois Piwik installé, penser à configurer votre site


#### Remplacer Google analytics par Piwik dans Pelican

Pour installer piwik, il suffit d'installer ce script à la place du script de google analytics.
    
    <script type="text/javascript">
      var _paq = _paq || [];
      _paq.push(['trackPageView']);
      _paq.push(['enableLinkTracking']);
      (function() {
        var u="//piwik-letchap.rhcloud.com/";
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['setSiteId', 1]);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
        g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
      })();
    </script>
    <noscript><p><img src="//piwik-letchap.rhcloud.com/piwik.php?idsite=1" style="border:0;" alt="" /></p></noscript>


### Je suis complétement dégooglisé

Pour finir, j'avais un formulaire de recherche sur le site qui utilisait google :

    <form class="navbar-form navbar-right" action="http://google.com/search" method="get">
	<fieldset role="search">
	  <input type="hidden" name="q" value="site:letchap.github.io" />  
	  <input type="search" class="form-control col-lg-8" name="q" results="0" placeholder="Search" />  
	</fieldset>
    </form>  

J'ai remplacé google par Duckduckgo, ce qui se traduit dans le formulaire par :

    <form action="https://duckduckgo.com" method="get">
      <div class="row collapse">
        <div class="large-9 small-10 columns" >
          <input type="search" name="q" results="0" placeholder="Search">
          <input type="hidden" name="sites" value="letchap.github.io" />
        </div>
      </div>    
    </form>     
    

Au prochaine épisode, nous essaierons de nous passer de Disqus.


