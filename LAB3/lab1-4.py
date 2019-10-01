arr = ['a',  ['c', 1, 3], ['f', 7, [4, '4']],  [{'lalala': 111}]]

lst = []

def func(arr):
    for i in arr:
        if type(i) == list:
            func(i)
        else:
            lst.append(i)
    return lst

print(func(arr))
