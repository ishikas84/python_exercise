def uniques_only(input):

    output = dict.fromkeys(input, None)
    return list(output.keys())


if __name__ == '__main__':

    nums = iter([1, 2, 3])
    output = uniques_only(nums)
    print(iter(output), iter(output))
    print(next(output), 1)
    print(next(nums), 2)
