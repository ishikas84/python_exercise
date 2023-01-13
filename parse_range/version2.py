def parse_ranges(num_range: str):
    range_list = num_range.split(',')
    for n in range_list:
        if "->" in n:
            x = int(n.split("-")[0])
            yield x
        else:
            m = n.split('-')
            for x in range(int(m[0]), int(m[-1])+1):
                yield x


print(parse_ranges('1-2,4-4,8-13'))
print(parse_ranges('0-0, 4-8, 20-20, 43-45'))