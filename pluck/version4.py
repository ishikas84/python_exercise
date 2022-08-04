DEFAULT = object()


def _pluck(Data, key, sep='.', default=DEFAULT):
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


def pluck(Data, *keys, sep='.', default=DEFAULT):
    items = tuple(_pluck(Data, key, sep, default) for key in keys)
    return items[0] if len(keys) == 1 else items




data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck(data, 'amount'))
print(pluck(data, 'category.group'))
print(pluck(data, 'category.created', default='N/A'))
print(pluck(data, 'category/name', sep='/'))