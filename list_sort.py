def list_sort(lista):
    evens = []
    odds = []
    chars = []
    if isinstance(lista, int):
        return ('Invalid Input')
    if isinstance(lista,str):
        return('Invalid Input')
    for x in lista:
        if isinstance(x, int):
            if (x % 2 == 0):
                evens.append(x)
            else:
                 odds.append(x)
            if isinstance(x,str):
                chars.append(x)
   
    return dict(evens=sorted(evens),odds=sorted(odds),chars=sorted(chars))
list_sort([10,2,8,'c','f'])

                        
