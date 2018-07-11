<img src="LogoLeDevoir.png" alt="Logo du Devoir" width="500" height="105" style="display:block;margin-left:auto;margin-right:auto;">

# Un siècle de culture au *Devoir*
Méthodologie détaillée d'un article pour [*Les Cahiers du journalisme*](http://cahiersdujournalisme.org/) (revue évaluée par les pairs).

### Étape 1 - Trouver les samedis

<img src="http://numerique.banq.qc.ca/images/signature/logoBAnQ_EnteteMob.png" width="100">

Toutes les éditions du *Devoir* entre le 1er janvier 1910 et le 31 décembre 2011 sont disponibles [dans la collection numérique du site web de Bibliothèque et Archives nationales Québec](http://numerique.banq.qc.ca/patrimoine/details/52327/2786824).

Cela fait près de 32 000 éditions sur plus de 50 000 fichiers accessibles en ligne (chaque cahier du journal est un fichier distinct). C'est beaucoup trop pour un seul article. J'ai choisi de ne prendre que les samedis. La première étape consistait donc à identifier tous les samedis depuis le 10 janvier 1910.

On en a la liste dans le fichier [**devoir-samedis.csv**](devoir-samedis.csv).

### Étape 2 - Extraire les fichiers

Une fois qu'on a les bonnes dates, il faut maintenant extraire les fichiers correspondants dans le site de BAnQ. Mais c'est un défi, car il n'y a aucun rapport entre la date de publication d'une édition donnée et son URL dans le site.

Par exemple, l'URL de l'édition du 1er mars 1985 est http://numerique.banq.qc.ca/patrimoine/details/52327/2790180. L'identifiant unique de cette édition est **2790180**.

Si on augmente ce nombre de 1 à **2790181**, on pourrait s'attendre à accéder à l'édition du 2 mars 1985. Eh non, on aboutit à [celle du 1er avril 1931](http://numerique.banq.qc.ca/patrimoine/details/52327/2790181). Poisson d'avril? Nenni.

Il se trouve heureusement que BAnQ dispose d'un API pour ses collections. Cet outil (non documenté) permet de consulter les métadonnées d'un item de la collection de BAnQ. Par exemple, les métadonnées de l'édition du *Devoir* du 1er mars 1985 ressemblent [à ceci](http://collections.banq.qc.ca/api/service-notice?handle=52327/2790180) ([2790180.json](2790180.json)):

Pour trouver quelles dates correspondent à quels identifiants, il 
