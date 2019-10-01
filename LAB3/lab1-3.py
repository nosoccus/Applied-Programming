n1 = int(input('n1='))
n2 = int(input('n2='))
def newfunc(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    lst = []
    for i in range(n1, n2 + 1):
        if i > 0:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                lst.append(i)
    if len(lst) == 0:
        raise Exception("NoSimpleDigits")
    else:
        return lst

print(newfunc(n1, n2))
