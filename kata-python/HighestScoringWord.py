def high(x):
    lista = x.split(" ")
    grandezza ={}
    parola =''
    for i in range(len(lista)):
        p =0
        for e in lista[i]:
            p += ord(e) - 96
            if p in grandezza:
                continue
            else:
                grandezza[p]= lista[i]
        a = sorted(grandezza.keys())
    return grandezza.get(a[len(a) -1])