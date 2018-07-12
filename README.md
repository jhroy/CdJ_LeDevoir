<img src="LogoLeDevoir.png" alt="Logo du Devoir" width="500" height="105" style="display:block;margin-left:auto;margin-right:auto;">

# Un siècle de culture au *Devoir*
Méthodologie détaillée d'un article pour [*Les Cahiers du journalisme*](http://cahiersdujournalisme.org/) (revue évaluée par les pairs).

:pencil2: :pencil2: :pencil2:

### Étape 1 - Trouver les samedis

<img src="http://numerique.banq.qc.ca/images/signature/logoBAnQ_EnteteMob.png" width="100">

Toutes les éditions du *Devoir* entre le 1er janvier 1910 et le 31 décembre 2011 sont disponibles [dans la collection numérique du site web de Bibliothèque et Archives nationales Québec](http://numerique.banq.qc.ca/patrimoine/details/52327/2786824).

Cela fait près de 32 000 éditions sur plus de 50 000 fichiers accessibles en ligne (chaque cahier du journal est un fichier distinct). C'est beaucoup trop pour un seul article. J'ai choisi de ne prendre que les samedis. La première étape consistait donc à identifier tous les samedis depuis le 10 janvier 1910.

On en a la liste dans le fichier suivant&nbsp;:
* [**devoir-samedis.csv**](devoir-samedis.csv).

### Étape 2 - Recourir à un API caché de BAnQ

Une fois qu'on a les bonnes dates, il faut maintenant extraire les fichiers correspondants dans le site de BAnQ. Mais c'est un défi, car il n'y a aucun rapport entre la date de publication d'une édition donnée et son URL dans le site.

Par exemple, l'URL de l'édition du 1er mars 1985 est http://numerique.banq.qc.ca/patrimoine/details/52327/2790180. L'identifiant unique de cette édition est la dernière partie de son URL, soit **2790180**. Rien, dans ce nombre, ne permet de reconnaître le 1er mars 1985.

En outre, si on augmente ce nombre de 1 à **2790181**, on pourrait s'attendre à accéder à l'édition du 2 mars 1985. Eh non, on aboutit à [celle du 1er avril 1931](http://numerique.banq.qc.ca/patrimoine/details/52327/2790181). Problème.

Il se trouve heureusement que BAnQ dispose d'un API pour ses collections. Cet outil (non documenté) permet de consulter les métadonnées d'un item de la collection de BAnQ. Par exemple, les métadonnées de l'édition du *Devoir* du 1er mars 1985 ressemblent [à ceci](http://collections.banq.qc.ca/api/service-notice?handle=52327/2790180)&nbsp;:
* [**2790180.json**](2790180.json)

Pour trouver quelles dates correspondent à quels identifiants, il faut aller à la pêche en essayant tous les identifiants possibles. C'est ce que fait l'un des premiers scripts programmés pour ce projet&nbsp;: 
* [**devoir-api.py**](devoir-api.py)

Il vérifie tous les identifiants dans une fourchette donnée et si l'API nous dit que cet identifiant mène à une édition du devoir, on l'inscrit dans un fichier CSV&nbsp; (le fichier ci-dessous peut être utile à toute personne qui souhaiterait trouver rapidement les adresses web des 49&nbsp;672 fichiers compris dans les archives complètes du *Devoir*:
* [**devoir-api.csv**](devoir-api.csv)

Une fois qu'on a trié uniquement les éditions du samedi, on se retrouve avec ce fichier qui va nous servir à l'étape suivante&nbsp;:
* [**devoir-source-des-pdf.csv**](devoir-source-des-pdf.csv)

### Étape 3 - Extraire les fichiers

Le script ci-dessous puise dans le fichier **devoir-source-des-pdf.csv** pour télécharger les 10&nbsp;753 fichiers PDF des éditions du samedi auxquelles on s'intéresse. Une fois chaque fichier téléchargé, il fait trois chosesnbsp;:
* il extrait le texte du PDF à l'aide de la bibliothèque [textract](https://github.com/deanmalmgren/textract);
* il sépare ce texte en [entités lexicales](https://fr.wikipedia.org/wiki/Analyse_lexicale), ou *tokens*, à l'aide de la bibliothèque [NLTK (Natural Language Toolkit)](https://www.nltk.org/) et les sauvegarde dans un fichier texte (le script en produit 10&nbsp;753 alors ils ne sont pas tous recopiés ici, mais en voici un exemple: [**ledevoir-brut-19660219.txt**](ledevoir-brut-19660219.txt));
* il effectue ensuite un tri dans ces *tokens* afin d'exclure les [**mots vides**](https://fr.wikipedia.org/wiki/Mot_vide) et de ne conserver que les mots de deux caractères ou plus, puis il sauvegarde ces mots dans un fichier CSV (il y en a tout autant; en voici un exemple: [**ledevoir-token2-19921212_D.csv**](ledevoir-token2-19921212_D.csv)).

* [**devoir-extraction.py**](devoir-extraction.py)

Voici la liste des mots-vides utilisés&nbsp;:
* [**stopwords.py**](stopwords.py) -> il s'agit en fait d'un fichier python ne définissant qu'une liste appelée `stop` contenant ces mots vides; le fichier est invoqué au début du script ci-dessus par la mention `from stopwords import stop`. Elle est inspirée de [cette collection](https://github.com/stopwords-iso/stopwords-fr).

### Étape 4 - Lemmatisation

