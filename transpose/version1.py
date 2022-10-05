from typing import Any, List, Optional


def transpose(matrix: List[List[Any]]) -> Optional[List[List[Any]]]:
    trans_matrix = None
    for row in matrix:
        trans_to_column = [[elem] for elem in row]
        if trans_matrix is None:
            trans_matrix = trans_to_column
        else:
            temp = [prev_row + next_row for prev_row, next_row in zip(trans_matrix, trans_to_column)]
            trans_matrix = temp
    return trans_matrix


matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(transpose(matrix))

csv_data = [
    ["Mary's Coffee", "3.50", "Dining"],
    ["Spirit", "187.00", "Travel"],
    ["Joe's Eats", "24.28", "Dining"],
    ["Metro", "12.00", "Travel"],
    ["Lyft", "23.45", "Travel"],
    ["Lyft", "4.00", "Travel"],
    ["Mary's Coffee", "6.75", "Dining"],
]
merchants, costs, categories = transpose(csv_data)
total_cost = sum(float(c) for c in costs)
print(total_cost)
