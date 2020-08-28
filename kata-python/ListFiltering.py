def filter_list(l):
    lista=[]
    for i in l:
        if type(i) != type(""):
            lista.append(i)
    return lista