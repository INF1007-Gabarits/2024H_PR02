<h1 style="text-align: center;">[INF1007] | Projet 2 - Sudoku</h1>

![PR02](./assets/images/cover.webp)

<p align="left"> <i>Crédits: <a href="https://openai.com/blog/dall-e/">DALLE 3</a></i></p>

## Table des matières

- [Introduction](#introduction)
- [Objectifs](#objectifs)
- [Partie 1. La logique du jeu](#partie-1-la-logique-du-jeu)
- [Partie 2. Tests unitaires](#partie-2-tests-unitaires)
- [Partie 3. L'interface graphique](#partie-3-l'interface-graphique)
- [Partie 4. Journalisation](#partie-4-journalisation)
- [Partie 5. Métriques de journalisation](#partie-5-métriques-de-journalisation)
- [Remise](#remise)
- [Barème](#barème)

## ⏰ Date de remise : le dimanche 14 avril 23h59.

## Introduction

- Le [**Sudoku**](https://fr.wikipedia.org/wiki/Sudoku) est un puzzle logique basé sur une grille de 9x9, avec l'objectif de remplir chaque ligne, colonne et sous-grille 3x3 avec les chiffres de 1 à 9 sans répétitions. 

- La création de votre jeu Sudoku impliquera l'utilisation de la programmation orientée objet pour structurer le jeu, l'interface graphique via [**pygame**](https://www.pygame.org/docs/) pour l'interaction utilisateur et le module [**logging**](https://docs.python.org/3/library/logging.html) pour la journalisation des événements et des erreurs. 

- Enfin, l'analyse des métriques de journalisation (plus particulièrement de la sévérité à travers le temps) avec [**seaborn**](https://seaborn.pydata.org) permet de visualiser des métriques telles que la sévérité des événements au fil du temps, offrant une approche intégrée pour le développement, le suivi et l'optimisation du jeu.

## Objectifs

- Intégrer les concepts de programmation orientée objet en vue de l'avènement d'une partie Sudoku complète.

- Apprendre à s'auto-documenter; à développer son autonomie en cherchant à travers la documentation pour mener à bien son projet.

- Apprendre à critiquer son propre code, à l'aide de tests unitaires qui valident la logique du jeu.

- Intégrer les concepts de journalisation au niveau de l'exécution de l'application entière, et ce, à travers le temps et selon divers niveaux de sévérité.

- Apprendre à produire une visualisation des métriques de journalisation récoltées (des sévérités) à travers le temps.

- Livrer un produit clef en main.

## Partie 1. La logique du jeu

- Au sein du skelette, nous vous fournissons d'emblée certaines classes pour faire office de présentation et pour orienter essentiellement votre programmation. Toutefois, **ces classes ne sont pas exhaustives**.

- Ne vous privez donc pas d'ajouter des classes, des interfaces, des méthodes, des constantes, des attributs et des variables pour augmenter la lisibilité et la maintenabilité de votre code. Un rappel préemptif : vous allez devoir tester votre logique ; quoi de mieux qu'un code modulaire !

### 1.1. Génération du jeu (`sudoku.py`)

#### Vous devez :

1. Générer un plateau de jeu Sudoku vide (méthode `generate_empty_board`).
- 1.1. **Il n'y a pas de restriction au niveau des constantes initiales injectées au sein du tableau dit *vide* de contenu.**

- 1.2. **Une seule instance devrait être référée en tout temps (Singleton).**

2. Implémenter un algorithme de complétion automatique dudit plateau, en partant d'un tableau vide ou prérempli (méthode `compute_complete_board`). Untel algorithme devrait être développé en programmation dynamique (*backtracking*). Vous pouvez vous référer aux tutoriels suivants (n'oubliez pas de citer vos références au sein de votre code !) :

- [Algorithm to Solve Sudoku | Sudoku Solver](https://www.geeksforgeeks.org/sudoku-backtracking-7/)
- [Sudoku-Backtracking algorithm and visualization](https://medium.com/analytics-vidhya/sudoku-backtracking-algorithm-and-visualization-75adec8e860c)
- [Use Backtracking Algorithm to Solve Sudoku](https://dev.to/christinamcmahon/use-backtracking-algorithm-to-solve-sudoku-270)
- [How to solve sudoku puzzles using backtracking algorithms and TypeScript](https://medium.com/@sulistef/how-to-solve-sudoku-puzzles-using-backtracking-algorithms-and-typescript-a3d7516c48ca)
- [Sudoku Solving algorithms](https://www.tutorialspoint.com/data_structures_algorithms/sudoku_solving_algorithms.htm)
- [Cracking Sudoku — How to Explore Backtracking Algorithms With Python](https://itnext.io/cracking-sudoku-how-to-explore-backtracking-algorithms-with-python-63a67067045d)
- [Solving Sudoku Puzzle using Backtracking in Python | Daily Python #29](https://medium.com/daily-python/solving-sudoku-puzzle-using-backtracking-in-python-daily-python-29-99a825042e)
- [Sudoku Solver-Python using Backtracking](https://levelup.gitconnected.com/sudoku-solver-python-using-backtracking-1aff17a3340)
- [Sudoku Solver with Python : a methodical approach for algorithm optimization [part 1]](https://medium.com/@ev.zafeiratos/sudoku-solver-with-python-a-methodical-approach-for-algorithm-optimization-part-1-b2c99887167f)
- [Solve a Sudoku Puzzle Using Backtracking in Python](https://python.plainenglish.io/solve-a-sudoku-puzzle-using-backtracking-in-python-8e9eb58e57e6)

- 2.1. **L'algorithme doit être développé en programmation dynamique**.

- 2.2. **L'algorithme développé doit être référencé adéquatement. Essayez de ne pas réinventer la roue en suivant l'un des tutoriels mentionnés ci-haut**.

- 2.3. **La complexité algorithmique n'est pas restreinte au niveau spatial ni temporel. Néanmoins, le temps et la complexité de votre approche ne devraient pas impacter l'expérience utilisateur**.

3. Générer un plateau de jeu Sudoku de départ pour l'utilisateur (méthode `generate_user_board`). 

- 3.1. **Le niveau de difficulté doit être intégré lors de la génération.**

- 3.2. **Le niveau de difficulté doit contenir trois modes : `Facile`, `Intermédiare` et `Avancé`.**

- 3.3. **Le niveau de difficulté par défaut doit être `Facile`**.

- 3.4. **Le changement du niveau de difficulté à travers l'interface utilisateur doit réinitialiser le jeu au complet et appliquer le niveau de difficulté sélectionné.**

- 3.5. **Les niveaux de difficulté dictent le nombre de cases déjà remplies au moment de l'affichage du plateau Sudoku de départ au joueur. Pour le mode `Avancé`, seul le nombre minimal de cases préremplies sont affichées comme point de départ au joueur (il ne devrait exister qu'une seule case à découvrir qui contient un seul `Indice`). Pour le mode `Intermédiaire`, quelques cases supplémentaires (d'une (1) à cinq (5) excédentaires) sont ajoutées en haut du mode `Avancé` pour aider le joueur à débuter la partie. Pour le mode `Facile`, six (6) à dix (10) cases supplémentaires sont remplies d'emblée.**

- 3.6. **Pour une case donnée, implémentez un algorithme de recherche d'`Indices`. Un `Indice` représente tout simplement une possibilité parmi les valeurs que peut posséder une case du plateau de jeu, selon l'état actuel dudit plateau. Lorsque l'utilisateur sélectionne une case vide du plateau au sein de la vue du jeu, et clique ensuite sur le bouton `Hints`, toutes les indices sont affichées élégamment dans le terminal au niveau de la case sélectionnée sur le plateau du jeu. Fonctionnalité bonie : vous pouvez afficher tous les indices à même une case sélectionnée du plateau du jeu à la suite d'un clic sur le bouton `Hints`.**

### Partie 2. Tests unitaires

- **Toute fonctionnalité développée qui a trait à la logique de génération et de déroulement de partie doit être testée.**

- **Aucune méthode reliée à la vue de [pygame](https://www.pygame.org/docs/) ne doit être testée.**

- **La librairie à utiliser est [unittest](https://docs.python.org/3/library/unittest.html)**.

- **Deux tests doivent être effectués par méthode cible : un premier test de cas d'utilisation *normal* et un second test de cas d'utilisation *limite***.

### Partie 3. L'interface graphique

#### Vous devez :

- **Implémenter le déroulement de partie à travers la visualisation graphique. Une `Partie` devrait être scindée en `Tour`. Au premier `Tour`, le plateau de jeu doit s'initialiser automatiquement avec une difficulté `Facile` lorsque le joueur quitte le menu principal vers la vue du jeu (à la suite du clic sur `Play`). Un `Tour` n'a pas de limite de temps. Lors d'un `Tour`, le joueur doit être capable de sélectionner une case vide du plateau de jeu. La sélection se fait avec une souris ou par pavé tactile, à la fois pour le déplacement et le clic vers la case d'intérêt. Une case déjà remplie ne doit pas pouvoir être sélectionnée. Une fois une case vide sélectionnée, ladite case doit arborer un style visuel qui permet de la différencier des autres cases vides. Lorsqu'une case devient sélectionnée, il est possible d'entrer**

- **N'importe quel bouton de l'interface doit être accessible en tout temps, en étant réactif aux événements.**









#### Question bonie (1 point)

- Écrivez une description précise de l'exécution du programme utilisé par les pirates lors de l'attaque, selon le code transpilé à l'exercice 1. Cette description devrait figurer au sein du fichier **`boni.txt`**.

##### **Attention !** Ne convertissez en aucun cas ce programme (.txt) en fichier exécutable (.py) !

### Partie 2. Obfuscation

- La firme **Skynet** en a assez de se faire larguer des virus par des cybercriminels ! Elle décide ainsi de contre-attaquer ! Quoi de mieux que de combattre le feu par le feu !
- Vous devez développer une fonction qui permet d'obfusquer n'importe quel programme de la firme dans le but de combattre les malfaiteurs. Laissez-vous guider par les instructions includes au sein du fichier **`exercice1.py`** pour arriver à vos fins.
- Dans le cadre de cet exercice, vous devrez obfusquer le **`programme-a-obfusquer.txt`** au sein du fichier **`programme-obfusque.txt`**.

## Exécution des tests unitaires

- Pour tester votre programme, une suite de tests est mise à votre disposition au sein de **`test-exercice.py`**.

- Pour vous aider à tester individuellement les fonctions, nous vous fournissons des **[constantes de tests](./assets/constants/tests.py)**, permettant d'activer ou de désactiver un ou plusieurs tests en particulier.

- Deux tests d'intégration globale sont aussi inclus pour valider votre approche, à même les tests unitaires.

## Remise

- Pour soumettre votre travail, créez un fichier zip nommé `LXX-YY-TP2.zip`, où `XX` est le numéro de votre section de laboratoire et `YY` le numéro de votre équipe (par exemple, `L02-04-TP2.zip` pour la section 02, équipe 04).

- Incluez uniquement, dans ce zip, votre script **`exercice.py`** et votre fichier répondu **`boni.txt`** si vous souhaitez courir la chance de remporter un point boni.

- Cela dit, assurez-vous que chaque script fonctionne correctement et déposez le fichier zip dans la boîte Moodle du TP correspondant à votre section. Aussi, assurez-vous d'exécuter le fichier `test-exercice.py` pour valider vos solutions avant de soumettre le fichier zip.

## Barème

| Fonctions                            | Points |
| ------------------------------------ | ------ |
| ajouter_caracteres_dico              | 2      |
| ajouter_codes_morts_dico             | 2      |
| ajouter_fonctions_asm_dico           | 2      |
| ajouter_autres_symboles_dico         | 2      |
| creer_dictionnaire                   | 1      |
| calculer_longueur_clefs_dictionnaire | 2      |
| transpiler                           | 3      |
| transpilation                        | 1      |
| obfusquer_contenu                    | 3      |
| inverser_dictionnaire                | 1      |
| obfuscation                          | 1      |
| Bonus                                | 1      |
| **Total**                            | **20** |