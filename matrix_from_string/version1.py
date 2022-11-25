def matrix_from_string(in_str: str) -> list:
    matrix = []
    in_str_rows = in_str.split("\n")
    for in_str_row in in_str_rows:
        in_str_row_list = in_str_row.split(" ")
        in_str_row_list = [x for x in in_str_row_list if x != ""]
        if len(in_str_row_list) == 0:
            continue
        in_str_row_list_float = [float(x) for x in in_str_row_list]
        matrix.append(in_str_row_list_float)
    return matrix


print(matrix_from_string("3 4 5"))
print(matrix_from_string("3 4 5\n6 7 8"))
print(matrix_from_string("1 2 3\n4 5 6\n7 8 9\n "))