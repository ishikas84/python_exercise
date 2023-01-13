def parse_ranges(num_range: str):
    range_list = num_range.split(',')
    nums = []
    for n in range_list:
        m = n.split('-')
        for x in range(int(m[0]), int(m[-1])+1):
            nums.append(x)
    return nums


print(parse_ranges('1-2,4-4,8-13'))
print(parse_ranges('0-0, 4-8, 20-20, 43-45'))