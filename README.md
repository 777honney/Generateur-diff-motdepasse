#Password generator
# Générateur de mots de passe (Wordlist Generator)

## Description
Ce script Python génère un fichier contenant **toutes les combinaisons possibles** de caractères pour une longueur de mot de passe donnée. Il utilise le module `itertools` pour produire ces combinaisons de façon exhaustive.

## Fonctionnement
1. Le script demande à l'utilisateur la longueur du mot de passe souhaitée.
2. Il utilise un jeu de caractères composé des lettres minuscules (`a-z`) et des chiffres (`0-9`), soit 36 caractères possibles.
3. Grâce à `itertools.product`, il génère toutes les combinaisons possibles de cette longueur.
4. Chaque combinaison est écrite dans un fichier `ro.txt`, une par ligne (qui peux être changé).
5. Un message `"Document créé"` confirme la fin de l'exécution.

## Exemple d'utilisation
```bash
python script.py
La longueur du mot de passe : 3
Document créé
```

Cela générera dans `ro.txt` toutes les combinaisons de 3 caractères possibles, par exemple :

<img width="523" height="443" alt="image" src="https://github.com/user-attachments/assets/7a592068-2259-4bde-920e-1d290d6440a3" />


## ⚠️ Attention : croissance exponentielle
Le nombre de combinaisons suit la formule `36^longueur`. Cela monte très vite :

| Longueur | Nombre de combinaisons | Taille approximative |
|----------|------------------------|-----------------------|
| 3        | 46 656                 | quelques Ko            |
| 4        | 1 679 616               | quelques Mo            |
| 5        | ~60 millions            | plusieurs centaines de Mo |
| 6        | ~2,1 milliards          | plusieurs dizaines de Go |

Au-delà de 5-6 caractères, le script peut saturer la mémoire disque et prendre un temps très long à s'exécuter.

## Prérequis
- Python 3
- Aucune dépendance externe (uniquement la bibliothèque standard `itertools`)

## Usage prévu
Ce type de générateur est habituellement utilisé dans un cadre **pédagogique ou de test de robustesse de mots de passe** (par exemple pour mesurer le temps nécessaire à un brute-force sur un système que l'on possède ou qu'on est autorisé à tester). Il ne doit pas être utilisé pour accéder à des comptes ou systèmes sans autorisation.

## Améliorations possibles
- Optimiser la vitesse d'écriture sur disque.
- Limiter/avertir automatiquement si la longueur demandée dépasse un seuil raisonnable.
