DEFAULT = object()


def pluck(Data, key, sep='.', default=DEFAULT):
    if sep in key:
        keys = key.split(sep)
        d = Data
        for k in keys:
            try:
                d = d[k]
            except KeyError:
                if default is not DEFAULT:
                    return default
                raise
        return d
    else:
        return Data[key]









data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck(data, 'amount'))
print(pluck(data, 'category.group'))
print(pluck(data, 'category.created', default='N/A'))
print(pluck(data, 'category/name', sep='/'))