class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums = nums1 + nums2
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        # nums.remove(0)
        numss = [ele for ele in nums if ele != 0]
        return nums


s = Solution()

print(s.merge([1, 2, 3, 0, 0, 0], 5, [2, 5, 6], 3))
# print(s.reverse(-123))
# print(s.reverse(120))
