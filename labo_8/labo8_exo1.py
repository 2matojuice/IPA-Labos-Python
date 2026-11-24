x = [-5, -12, -3]

#Exo 1.1
#Considérer les cas liste vide et nombres négatifs (retourner un message)
plus_grand = x[0]
i = 0

while i < len(x):
    if x[i]>=plus_grand:
        plus_grand = x[i]
    i+=1

print(f"Maximum :{plus_grand}")

#Exo 1.2
def max(x):
    plus_grand = x[0]

    for i in range(len(x)):
            if x[i]>=plus_grand:
                plus_grand = x[i]
    return plus_grand

print(f"Max : {max(x)}")

#Exo 1.3 fait
