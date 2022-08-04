
def pluck(Data, key, sep='.'):
    if sep in key:
        keys = key.split(sep)
        d = Data
        for k in keys:
            d = d[k]
        return d
    else:
        return Data[key]









data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck(data, 'amount'))
print(pluck(data, 'category.group'))
# print(pluck(data, 'category.created'))
print(pluck(data, 'category/name', sep='/'))