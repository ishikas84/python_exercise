def add(matrix1: list, matrix2: list) -> list:
    matrix = []
    for row1, row2 in zip(matrix1, matrix2):
        row = [e1 + e2 for e1, e2 in zip(row1, row2)]
        matrix.append(row)
    return matrix
