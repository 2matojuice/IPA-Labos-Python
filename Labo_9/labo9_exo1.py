#Ex 1.1
texte = ""
def sans_espace(texte):
    texte_2 = ""
    m=len(texte)
    for i in range(m):
        if texte[i] != " ":
            texte_2 += texte[i]
    return texte_2

print(sans_espace(texte))

#Ex 1.2
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = len(alphabet)
valeur = {}

for i in range(n):
    valeur[alphabet[i]]=10+i

def lettres_en_chiffres(texte):
    res = ""
    m=len(texte)
    for i in range(m):
        if texte[i] == " " or texte[i].isdigit():
            res+=texte[i]
        else:
            res += str(valeur[texte[i]])
    return res

#Ex 1.3
iban = ""

def iban_valide(iban):
    iban = iban[4: ] + iban[:4]
    iban = lettres_en_chiffres(iban)
    iban = sans_espace(iban)

    if int(iban)%97 == 1: 
        return True
    else: 
        return False

#Ex 1.4:

def chiffres_de_controle():
