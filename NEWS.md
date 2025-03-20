<!-- LTeX: language=fr -->
# Nouvelles du cours

Les nouvelles du cours apparaîtront ici au fur et à mesure.

## 20/03/2025 : à propos de couverture, QCM, deadlines

Vos TP notés seront évalués essentiellement sur deux critères :

* La correction du code (Python, ANTLR) que vous avez écrit, mesurée par le
  nombre d'échecs de votre compilateur dans la base de tests enseignant.

* La qualité de votre base de tests (i.e. les fichiers .c), mesurée par la
  couverture de votre base de tests sur le compilateur enseignant. Vous pouvez
  maximiser la couverture de votre base de tests sur votre compilateur. Pour
  chaque TP, vous devriez avoir 100% de couverture sur la partie du code Python
  concernée (MiniCInterpretVisitor.py pour le TP d'interprétation, etc.). Vous
  voyez le pourcentage de couverture à la fin de l'exécution de la base de
  tests, mais beaucoup d'entre vous n'ont pas lu jusqu'au bout, en particulier
  la phrase « Coverage HTML written to dir htmlcov » qui vous invite à regarder
  le rapport de couverture détaillé (en couleurs et tout !) dans le répertoire
  htmlcov/.

Certaines lignes sont volontairement ignorées dans le rapport de couverture, en
particulier les lignes contenant `MiniCInternalError` (cf. ), qui par définition ne
peuvent pas être couvertes. Il y avait un petit bug de mon squelette et une
ligne était forcément non-couverte mais pas ignorée, un « git pull » vous
apportera la correction.

J'en profite pour vous rappeler les prochaines deadlines :

* J'ai rouvert le QCM2, je laisse aux retardataires jusqu'à ce lundi soir pour y
  répondre.

* TP2 : dimanche 6 avril 2025, 23h59. (deadline stricte) (il était déjà fortement
  recommandé de l'avoir terminé pour aujourd'hui)

* QCM3 : lundi 7 avril 2025, 23:59.

## 13/03/2025 : nouvelles du cours

Plusieurs informations :

* Les notes de TP1 et CC1 sont en ligne. Dans les deux cas, passez votre souris
  sur la note pour voir le détail du barème. Je me permets d'insister sur
  quelques points :
  - La correction de ce CC ainsi que des autres TPs est automatisée. Une «
    petite » erreur comme une erreur de syntaxe dans votre code a pour
    conséquence que votre code ne fonctionne pas, ce qui a des conséquences
    dramatiques sur la note. Si vous trouvez cela sévère, imaginez que vous
    mettez votre code en production et demandez-vous si ce serait grave d'avoir
    une erreur de syntaxe dedans ... Ces erreurs sont triviales à éviter, soyez
    méthodiques pour ne pas perdre de points bêtement.
  - Je vous donne des consignes et des Makefile qui fonctionnent. Ne modifiez
    pas les Makefiles, si vous le faites vous avez de bonnes chances d'avoir du
    code qui ne fonctionne pas chez moi, avec la même conséquence dramatique.

* Je rappelle que j'applique la « règle du max » pour les CC (mais pas pour les
  TP à terminer en temps libre) : la note prise en compte est à chaque fois le
  max entre la note de CC et la note de contrôle terminal. Ce n'est pas une
  raison pour ne pas travailler les CC, mais ne vous démoralisez pas si vous
  avez eu une mauvaise note en CC, tout est rattrapable.

* La plateforme OpenStack qui héberge nos VM sera éteinte ce vendredi soir et
  probablement HS tout le week-end.

* Je vous rappelle que vous avez un QCM sur le CM1 à remplir pour la semaine
  prochaine.

## 10/03/2025 : corrigé du TD1 en ligne

Je ne distribue normalement pas les corrigés des TDs, mais le TD1 étant assez
dense, et pour vous permettre de vous préparer au mieux au CC de jeudi, je viens
de publier un corrigé ici :

  https://matthieu-moy.fr/cours/mif08/mif08-td1-solutions.pdf

Notez que pour beaucoup d'exercices les énoncés sont un peu vagues pour laisser
la place à la discussion en TD. Pour le CC noté ce jeudi, l'énoncé sera aussi
précis que possible et pourra avoir des définitions différentes de celles du TD.
Au risque d'enfoncer une porte ouverte : lisez en détails l'énoncé !

## 5/03/2025 : Contrôle continu le 13 mars

Nous ferons le premier contrôle continu ce jeudi 13 mars en début de TP (pour
rappel, tout est indiqué dans le fichier README.md à la racine du Git). Il
s'agit d'un TP noté en temps limité (24 minutes plus tiers-temps éventuel) sur
l'analyse lexicale et syntaxique avec ANTLR, sans document ni site web autre que
le Git étudiant autorisé.

Vous trouverez un sujet blanc pour vous entraîner dans le répertoire CC1 du
dépôt Git (faites un `git pull`). Le TP noté utilisera la même infrastructure de
tests et les mêmes commandes. Le TP sera relativement facile si vous avez bien
assimilé les notions vues jusqu'ici (CM1, TD1, TP1) et que vous avez fait le
sujet blanc. C'est à l'inverse très difficile de terminer le TP dans le temps
imparti dans le cas contraire.

Vous pourrez composer au choix sur vos machines personnelles ou sur les PC de la
fac (dans la limite des postes disponibles, donc si vous avez une machine
personnelle, apportez-la !). Assurez-vous que votre environnement est
opérationnel (ANTLR et pytest installés, si `make test` fonctionne sur le sujet
blanc, c'est bon).

Le sujet réel fera intervenir en particulier des mots clés, des identificateurs
et des nombres littéraux.

Autre information : j'ai ré-ouvert le QCM 1 pour les étudiants qui ne l'avaient
pas rempli (ce qui a pour effet de bord de cacher la correction pour les
autres).
