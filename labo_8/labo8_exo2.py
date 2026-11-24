#Ex 2.1

#En C, pas de type de base pour entiers >= 2*64 => dépassement de capacité => résultat incorrecte
#Solution : implémenter nv type ou utiliser une librairie (gmp)
#Problème non existant en Python

def puissance(nombre, exposant):
    resultat = 1
    for i in range(exposant):
        resultat *= nombre
    return resultat

print(f"{puissance(2, 100)}")

#Ex 2.2
#Le nb de multiplication évolue de manière linéaire

#réponse : 10, 1000, 10000

#si n est l'exposant => nb de mult. =< n => = O(n)

#Ex 2.3

#2**16 = 2**8 x 2**8
#2**8 = 2**4 x 2**4
#2**4 = 2**2 x 2**2
#2**2 = 2 x 2

def puissance_rapide(nombre, exposant):
    if exposant == 0:
        return 1
    
    if exposant == 1:
        return nombre
    
    else:
        e2 = exposant / 2
        i = puissance_rapide(nombre, e2)
        if exposant%2 == 0:
            return i*i #une multi.
        else:
            return i*i*nombre #deux multiplication
        
#Obs : à chaque itération, on fait max 2 multiplication
#Nb d'itération = log2(n)
#Nb mult. =< 2 (car au plus deux) log2(n) = O(logn)