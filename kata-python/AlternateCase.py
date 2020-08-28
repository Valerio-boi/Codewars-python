def alternateCase(s):
    # your code here
    lista = []
    stringa = ''
    for i in range(len(s)):
        if s[i] == s[i].upper():
            lista.append(s[i].lower())
        else:
            lista.append(s[i].upper())
    for i in range(len(lista)):
        stringa += lista[i]
    print(stringa)   
    return stringa