<img src="LogoLeDevoir.png" alt="Logo du Devoir" width="500" height="105" style="display:block;margin-left:auto;margin-right:auto;">

# Un siècle de culture au *Devoir*
Méthodologie détaillée d'un article pour [*Les Cahiers du journalisme*](http://cahiersdujournalisme.org/) (revue évaluée par les pairs)

### Étape 1 - Extraction des fichiers

Toutes les éditions du *Devoir* entre le 1er janvier 1910 et le 31 décembre 2011 sont disponibles [dans la collection numérique du site web de Bibliothèque et Archives nationales Québec](http://numerique.banq.qc.ca/patrimoine/details/52327/2786824).

Mais les extraire de façon ordonnée est un défi, car il n'y a aucun rapport entre l'URL d'une édition donnée et sa date de publication. Par exemple, l'URL de l'édition du 1er mars 1985 est http://numerique.banq.qc.ca/patrimoine/details/52327/2790180. Le numéro de code de cette édition est **2790180**. Si on augmente ce nombre de 1 à **2790181**, on pourrait s'attendre à accéder à l'édition du 2 mars 1985. Eh non, on aboutit à [celle du 1er avril 1931](http://numerique.banq.qc.ca/patrimoine/details/52327/2790181). Poisson d'avril? Nenni.

Il se trouve heureusement que BAnQ dispose d'un API pour ses collections. Cet outil (non documenté) permet de consulter les métadonnées d'un item de la collection de BAnQ. Par exemple, les métadonnées de notre édition du *Devoir* du 1er mars 1985 [sont ici](http://collections.banq.qc.ca/api/service-notice?handle=52327/2790180).
