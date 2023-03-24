def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    if len(nums) % 2 == 0:
        before = len(nums) // 2 - 1
        after = len(nums) // 2
        return (nums[before] + nums[after]) / 2
    else:
        return nums[len(nums)//2]

a = [1, 2]
b = [3]
print(findMedianSortedArrays(a, b))
a = [1, 2]
b = [3, 4]
print(findMedianSortedArrays(a, b))
