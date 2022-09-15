def add(*nargs) -> list:
    matrix = []
    if not check_length(nargs):
        raise ValueError("Given matrices are not the same size")
    for rows in zip(*nargs):
        if check_length(rows):
            row = [sum(r) for r in zip(*rows)]
            matrix.append(row)
        else:
            raise ValueError("Given matrices are not the same size.")
    return matrix


def check_length(*nargs) -> bool:
    r = {len(r[0]) for r in zip(*nargs)}
    return len(r) == 1


m1 = [[6, 6], [3, 1]]
m2 = [[1, 2], [3, 4], [5, 6]]
m3 = [[6, 6], [3, 1, 2]]

add(m1, m2)
add(m1, m3)
add(m1, m1, m1, m3, m1, m1)
add(m1, m1, m1, m2, m1, m1)
