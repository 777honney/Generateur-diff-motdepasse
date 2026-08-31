import itertools

with open("ro.txt", "w") as fichier:
    
    long = int(input("La longueur du mot de passe : "))
    
    cl = "abcdefghijklmnopqrstuvwxyz0123456789"

    for combinaison in itertools.product(cl, repeat=long):
        motdepasse = "".join(combinaison)
        fichier.write(motdepasse + "\n")

print("Document créé")
