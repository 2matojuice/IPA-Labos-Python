import random

#Ex 4.1 (version naïve) = O(n**2)
#On ne peut pas vendre avant d'avoir acheté

prix=[7, 6, 4, 3, 2, 1, 0]
#prix = [random.randint(0, 10) for _ in range(30)]

def meilleur_gain(prix):
    gain = 0
    compteur = 0
    for i in range(len(prix)):
        for j in range(i+1, len(prix)):
            compteur +=1
            res = prix[j]-prix[i]
            if res > gain:
                gain = res
    print(compteur)
    return gain

print(f"{meilleur_gain(prix)}")
print(prix)

#Ex 4.2
#moins_cher([0,i]) = min(prix[i, moins_cher([0, i-1])])
#Total meilleur gain itère sur tous les jours de vente et retourn le meilleur gain possible.

def meilleur_gain_opti(prix):
    gain = 0
    compteur = 0

    for i in range(len(prix)):
        if prix[i]>prix[i+1]: