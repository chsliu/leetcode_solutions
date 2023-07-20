nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

i, j = 0, 0
nums = []
# while i < m:
#     while j < n:
#         if nums1[i] < nums2[j]:
#             nums.append(nums1[i])
#             i = i+1
#         else:
#             nums.append(nums2[j])
#             j = j+1
#         j = j+1
#     i = i+1

while i < m and j < n:
    if nums1[i] <= nums2[j]:
        nums.append(nums1[i])
        i = i+1
    else:
        nums.append(nums2[j])
        j = j+1

while i < m:
    nums.append(nums1[i])
    i = i+1

while j < n:
    nums.append(nums2[j])
    j = j+1

nums1 = nums
print(nums1)
