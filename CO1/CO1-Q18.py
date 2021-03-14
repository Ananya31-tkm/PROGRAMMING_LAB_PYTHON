def Merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a': 100, 'b': 48, 'e': 55}
dict2 = {'d': 62, 'c': 14}
print(Merge(dict1, dict2))
print(dict2)
