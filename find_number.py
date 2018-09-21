def find_number(x):
    missing=[]
    if not isinstance(x,list):
                raise TypeError('Invalid Input')
    for  i in range(1,10):
        if i not in x:
           missing.append(i)
           return(missing)
find_number([1,2,3,5,6,7,9])