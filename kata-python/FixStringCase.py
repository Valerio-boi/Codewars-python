def solve(s):
    pass
    lista = []
    conteggioUpper = 0
    conteggioLower = 0
    for i in range(len(s)):
        lista.append(s[i])
    print(s)
    for e in lista:
        if e == e.upper():
            conteggioUpper+=1
        else:
            conteggioLower+=1
    if conteggioUpper > conteggioLower:
        print(s.upper())
        return s.upper()
    if conteggioLower > conteggioUpper:
        print(s.lower())
        return s.lower()
    if conteggioUpper == conteggioLower:
        print(s.lower())
        return s.lower()