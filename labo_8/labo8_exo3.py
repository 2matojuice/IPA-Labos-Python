x =[3, 1, 3, 2, 3]
n = len(x)
i = 0

#Ex 3.1
def nb_doublons():
    compteur = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i]==x[j]:
                compteur += 1
    return compteur

print(nb_doublons())

#nb de calculs : T = (n-1)+(n-2)+...+2+1
# =(n-1)+(n-1)+...
# (n*(n-1))/2 
#=Coeff. binôme entre n et 2
#=> = O(n**2)
# => Si n double, T quadruple

#Ex 3.2

#nb de valeurs possibles = 100
#Valeur totale apparaît Cv fois => coeff. bin. (Cv 2) paires possibles
#Totale doublons = somme (Ck * (Ck-1))/2 cas possibles
#Temps totale = O(n+K) t.q n := taille de la liste et k:= nb de valeurs possibles