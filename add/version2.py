def add(*nargs) -> list:
    matrix = []
    for rows in zip(*nargs):
        row = [sum(r) for r in zip(*rows)]
        matrix.append(row)
    return matrix


matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
print(add(matrix1, matrix2, matrix3))
