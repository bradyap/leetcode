#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0
        
        while i < len(nums1) or j < len(nums2):
            a, b = float("inf"), float("inf")
            if i < len(nums1):
                a = nums1[i]
            if j < len(nums2):
                b = nums2[j]
            
            if a > b:
                nums.append(b)
                j += 1
            else:
                nums.append(a)
                i += 1
                
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]
        

# @lc code=end

