from typing import List


def threeSum(nums: List[int]) -> List[int]:
    nums.sort()
    result = []
    for i, elm in enumerate(nums):
        if (i > 0 and elm == nums[i - 1]):
            continue
        middle, end = i + 1, len(nums) - 1
        while(middle < end):
            three = elm + nums[middle] + nums[end]
            if (three > 0):
                end -= 1
            elif(three < 0):
                middle += 1
            else:
                p = [elm, nums[middle], nums[end]]
                result.append(p)
                while nums[middle] == p[1] and middle < end:
                    middle += 1
                while nums[end] == p[2] and middle < end:
                    end -= 1
    return result


nums = [0, 1, 1]  # [-1,0,1,2,-1,-4]

print(threeSum(nums))
