<!-- LTeX: language=fr -->
# Avancée / Planning du cours de MIF08 (Compilation)
_Année 2024-2025_

* Matthieu Moy, Université Lyon 1, LIP https://matthieu-moy.fr/

## Communication et nouvelles du cours

* [NEWS.md](NEWS.md) contient les nouvelles du cours (envoyées par email également).

* Cette année, nous ~~utiliserons~~ détournerons le système d'issues de GitLab
  comme forum minimaliste. Vous pouvez poser vos questions en ajoutant une issue
  sur le dépôt : https://forge.univ-lyon1.fr/matthieu.moy/mif08-2025/-/issues .
  Activez les notifications sur le projet GitLab pour avoir un mail à chaque
  nouveau post.

## Intervenants

**CM**

Matthieu Moy

**TD**
- A: Matthieu Moy
- B: Alec Sadler
- C: Mathieu Lefort
- D: Nicolas Louvet
- E: Solène Richard

**TP**
- A: Matthieu Moy, Thomas Stavis
- B: Alec Sadler
- C: Mathieu Lefort
- D: Nicolas Louvet
- E: Thibaut Modrzyk, Solène Richard

## Vidéos des CM

Les vidéos réalisées pendant le COVID sont encore disponibles. Elles ne sont plus très à jour, mais peuvent vous aider si besoin (elles ne remplacent pas le présentiel !) :

[La playlist Youtube MIF08](https://www.youtube.com/playlist?list=PLtjm-n_Ts-J9HSZ9ahpbsC_kTQMzUZQPx)

## Infrastructure technique, logiciels à installer

Les TP utilisent la chaîne d'outils RiscV, un peu lourde à installer. Voir [INSTALL.md](INSTALL.md) pour les consignes. À faire avant les TPs si vous voulez travailler sur vos machines personnelles.

Si vous n'arrivez pas à installer les outils sur vos machines, vous pourrez travailler sur les ordinateurs de la fac, et en dernier recours nous fournissons aussi des machines virtuelles pré-installées : [VM.md](VM.md).

## Planning

## Jeudi 13/02/2025

- :book: 9h45 : Cours 1, Introduction, Lexing & Parsing
    - [transparents lexing et parsing](https://matthieu-moy.fr/cours/mif08/capmif_cours01_intro_lexing_parsing.pdf)
    - [Vidéo "teaser"](https://youtu.be/ny7HlqyuM9E)
    - [vidéo d'introduction au cours](https://www.youtube.com/watch?v=zGifE8MfPWA)
    - [vidéo lexing](https://www.youtube.com/watch?v=UlUTSsOA9Qc)
    - [vidéo parsing](https://www.youtube.com/watch?v=y9MrfDzrAmA)
    - :negative_squared_cross_mark: QCM sur TOMUSS, à faire avant mardi 18/2/2025, 23:59

- :pencil2: 11h30 : TD1, Lexing, Parsing, AST
    - [Énoncé du TD1](https://matthieu-moy.fr/cours/mif08/mif08-td1.pdf)
    - [Éléments de corrigés](https://matthieu-moy.fr/cours/mif08/mif08-td1-solutions.pdf)
    <!-- Solène Richard pas là -->

## Jeudi 20/2/2025

- :hammer: 9h45 : TP1, Introduction à Python, Lexing et Parsing avec ANTLR
    - Règles communes aux TP notés : [REGLES-TPs.md](REGLES-TPs.md)
    - Énoncé : [tp1.pdf](https://matthieu-moy.fr/cours/mif08/tp1.pdf)
    - Fichiers du TP1 : [TP01/](TP01/).
    - **Date limite pour le rendu (noté) : lundi 10 mars 2025, 23h59. (deadline stricte, aucun rendu accepté après cette date, prévoyez la marge de votre côté)**

<!-- période entreprise alternants -->

## Jeudi 13/3/2025

- :book: 8h : Cours 2: interprétation, typage
    - [transparents interprétation](https://matthieu-moy.fr/cours/mif08/capmif_cours02_interpretation.pdf)
    - [transparents typage](https://matthieu-moy.fr/cours/mif08/capmif_cours03_typing.pdf)
    - [vidéo typage](https://youtu.be/2A-hQy_6YlE)
    - [vidéo sémantique et interprète](https://youtu.be/8PYhBsgRO6g)
- :negative_squared_cross_mark: QCM sur TOMUSS, à faire avant mardi 18 mars 2025, 23:59.

- :hammer: 9h45-13h : TP2, Interprétation et Typage (début)
    <!-- Solène Richard pas là -->
    <!-- - Transparents de présentation : [capmif_labs.pdf](https://matthieu-moy.fr/cours/mif08/capmif_labs.pdf) -->
    - :100: TP noté sur ANTLR (24 minutes). Sujet pour s'entraîner : [CC1/cc1-sujet-exemple.pdf](CC1/cc1-sujet-exemple.pdf) (squelette et corrigé dans [CC1/](CC1/)).
    - Si besoin : des VM pour vous dépanner en cas de problème sur machine perso : [VM.md](VM.md)
    - Énoncé : [TP2 Interpreters and Types](https://matthieu-moy.fr/cours/mif08/tp2.pdf)
    - Fichiers du TP2 : [TP02/](TP02/) puis [MiniC/](MiniC/).
    - **Date limite pour le rendu (noté) :** Il est fortement recommandé de terminer le TP avant le TP3 la semaine suivante pour ne pas prendre de retard, mais vous pouvez rendre jusqu'à **dimanche 6 avril 2025, 23h59. (deadline stricte)**

## Jeudi 20/3/2025

- :book: 8h-9h30 : Cours 3, Typage (fin), machine cible (RISCV)
    - [transparents RiscV](https://matthieu-moy.fr/cours/mif08/capmif_cours04_riscv.pdf)
    - [vidéo sur RISCV](https://youtu.be/ZdElX9e_tAI)
    - Extrait de la documentation RISCV: [riscv_isa.pdf](https://matthieu-moy.fr/cours/mif08/riscv_isa.pdf)
- :negative_squared_cross_mark: QCM sur TOMUSS, à faire avant lundi 7 avril 2025, 23:59.

- :pencil2: 9h45 : TD2: Typing, Architecture RiscV
    - Rappel, extrait de la documentation RISCV : [riscv_isa.pdf](https://matthieu-moy.fr/cours/mif08/riscv_isa.pdf)
    - [TD2 Typing, RiscV](https://matthieu-moy.fr/cours/mif08/mif08-td2.pdf)

- :hammer: 11h30 : TP3, l'architecture RiscV
    - Énoncé : [TP3 architecture RiscV](https://matthieu-moy.fr/cours/mif08/tp3.pdf)
    - Fichiers du TP3 : [TP03/](TP03/).
    - Pas de rendu noté pour ce TP

<!-- période entreprise alternants -->

## Jeudi 10/4/2025

- :book: 8h-9h30 : Cours 4, génération de code
    - génération de code 3 adresses + allocation naïve, [transparents](https://matthieu-moy.fr/cours/mif08/capmif_cours05_3ad_codegen.pdf), [vidéo](https://youtu.be/m2x7leFnCN4)
    - Représentations intermédiaires, [transparents](https://matthieu-moy.fr/cours/mif08/capmif_cours06_irs.pdf), [vidéo 6a](https://youtu.be/dD9bRhLfykM), [vidéo 6b](https://youtu.be/Xico_JTK3XQ).
- :negative_squared_cross_mark: QCM sur TOMUSS, à faire avant mardi 15 avril 2025, 23:59.

- :pencil2: 9h45-11h15 : TD 3, génération de code
    <!-- Solène Richard pas là, remplacée par Théo ? -->
    - :100: Contrôle court (ANTLR et RiscV), voir instructions : [QCM.md](QCM.md).
    - Sujet : [TD3 génération de code](https://matthieu-moy.fr/cours/mif08/mif08-td3.pdf)
    <!-- - [Éléments de corrigé, partiel](https://matthieu-moy.fr/cours/mif08/mif08-td3-corrige-partiel.pdf) -->

- :hammer: 11h30-13h : TP 4, génération de code
    <!-- Solène Richard pas là, remplacée par Théo ? -->
    <!-- - Transparents de présentation : [capmif_labs.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_labs.pdf) -->
    - Rappel : des VM pour vous dépanner en cas de problème sur machine perso : [VM.md](VM.md)
    - Énoncé : [TP4 génération de code](https://matthieu-moy.fr/cours/mif08/tp4.pdf)
    - Fichiers du TP4 : [MiniC/CodeGen/](MiniC/CodeGen/).
    - [Documentation de la bibliothèque fournie](http://matthieu.moy.pages.univ-lyon1.fr/mif08-2025/)
    - **Date limite pour le rendu (noté) : mardi 6 mai 2025, 23h59 (malus 2 points par jour de retard, aucun rendu accepté après le dimanche soir).**

## Jeudi 17/4/2025

- :hammer: 9h45-13h : TP 4 (suite), cf. ci-dessus pour les supports.

<!-- période entreprise alternants + ponts de mai-->

## Jeudi 15/5/2025

- :book: 8h-9h30 : Cours 5, allocation de registres
    - Register allocation + data-flow analyses : [transparents](https://matthieu-moy.fr/cours/mif08/capmif_cours07_regalloc.pdf), [vidéo première partie](https://youtu.be/9902mMgDIK8), [vidéo deuxième partie](https://youtu.be/LknSDccweFw).
    - :negative_squared_cross_mark: QCM sur TOMUSS, à faire avant lundi 2 juin 2025, 23:59.


- :hammer: 9h45-13h : TP5, nouvelles fonctionnalités de langage
    - Énoncé : [TP5 (extension de langage)](https://matthieu-moy.fr/cours/mif08/tp5for.pdf)
    - Fichiers du TP5 : les mêmes qu'aux TP précédents.
     - **Date limite pour le rendu (noté) : vendredi 6 juin 2025, 23h59 (malus 2 points par jour de retard, aucun rendu accepté après le dimanche soir).**

## Jeudi 5/6/2025

- :pencil2: 9h45-11h15 : TD4, analyse de vivacité
    - Énoncé : [TD4 liveness](https://matthieu-moy.fr/cours/mif08/mif08-td4.pdf)


- :pencil2: 11h30-13h : TD5, allocation de registres intelligente
    - :100: Contrôle court (Typage), voir instructions : [QCM.md](QCM.md).
    - Énoncé : [TD5 regalloc](https://matthieu-moy.fr/cours/mif08/mif08-td5.pdf)

## Jeudi 12/06/2025

- :100: Examen.

## Pondération des notes (indicative pour l'instant sauf l'examen final qui sera forcément 40%)
  - QCM : non pris en compte dans la moyenne d'UE
  - 2 ou 3 interrogations écrites : 20% au total
  - TP1 parsing et évaluation d'expression : 6%
  - TP2 interprète : 10%
  - TP4 génération de code : 12%
  - TP5 extension de langage : 12%
  - Contrôle terminal (CT) : 40 %

Pour les interrogations écrites, la note prise en compte sera le maximum entre la note obtenue et la note de contrôle terminal. En cas d'absence (justifiée ou non), la note de CT remplace la note d'interrogation.

La session 2 remplace la note de contrôle terminal.

## Annales et consignes pour l'examen

* Aide-mémoire fourni avec le sujet en 2021 (un document similaire sera fourni cette année) : [mif08_companion.pdf](https://matthieu-moy.fr/cours/mif08/mif08_companion.pdf)

* L'examen session 1 2023-2024 : [exam_mif08_2024.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2024.pdf) et éléments de corrigé : [exam_mif08_2024_corr.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2024_corr.pdf) 

* L'examen session 1 2022-2023 : [exam_mif08_2023.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2023.pdf) et éléments de corrigé : [exam_mif08_2023_corr.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2023_corr.pdf) 

* L'examen session 1 2021-2022 : [exam_mif08_2022.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2022.pdf) et éléments de corrigé : [exam_mif08_2022_corr.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2022_corr.pdf)

* L'examen Session 1 2020-2021 : [exam_mif08_2020.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2020.pdf) et les éléments de corrigé : [exam_mif08_2020_corr.pdf](https://matthieu-moy.fr/cours/mif08/exam_mif08_2020_corr.pdf)

* [Consignes pour l'examen](https://matthieu-moy.fr/cours/mif08/exam_mif08-page1.pdf)
