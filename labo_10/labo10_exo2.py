#Ex 2.1

alphabet = "abcdefghijklmnopqrstuvwxyz"
valeur = {}

for i in range(len(alphabet)):
    valeur[alphabet[i]]= i

def decaler(letter, decalage):
    if letter not in alphabet:
        return letter
    else: i = valeur[letter]
    
    return alphabet[(i+decalage)%len(alphabet)]