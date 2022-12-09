def window(item, sep:int):
    output = []
    item = list(item)
    for i in range(0, len(item)):
        elements = tuple(item[i:i+sep])
        if len(elements) != sep or sep == 0:
            break
        output.append(elements)
    return output


numbers = [1, 2, 3, 4, 5, 6]
squares = (n**2 for n in numbers)
print(window(numbers, 2))
print(window(numbers, 3))
print(window(squares, 4))
print(window(numbers, 0))