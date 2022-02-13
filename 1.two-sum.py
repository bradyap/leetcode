#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        
        for i, n in enumerate(nums):
            if n in temp:
                return [i, temp[n]]
            temp[target - n] = i

# @lc code=end

