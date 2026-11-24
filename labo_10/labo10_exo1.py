#Ex 1.1

n = 13
res = 0

def en_binaire(n):
    if n == 0:
        return 0
    else:
        n_binaire = []
        res = n
        while res > 0:
            n_binaire.append(res % 2)
            res = res //2
            n_binaire = n_binaire[::-1]
        s = ""
        for b in n_binaire:
            s += str(b)

        return int(s)

print(en_binaire(n))

#Ex 1.2

def en_base(n, base):
    if n == 0:
        return 0
    else:
        n_bis =[]
        res = n
        while res > 0:
            n_bis.append(n%base)
            res = res // base
        n_bis= n_bis[::-1]
        s=""
        for el in n_bis:
            s += str(el)
        return int(el)