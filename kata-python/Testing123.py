def number(lines):
    #your code here
    print(lines)
    lista = []
    for i in range(len(lines)):
        lista.append(str(i + 1)+': '+str(lines[i]))
    return lista