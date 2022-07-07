def uniques_only(iterable):
    seen = []
    for item in iterable:
        if item not in seen:
            yield item
            seen.append(item)