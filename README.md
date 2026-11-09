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
