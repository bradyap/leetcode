#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        max = 0
        
        for c in s:
            if c in temp:
                if (len(temp) > max):
                    max = len(temp)
                temp = temp[temp.index(c) + 1:] + c
            else: 
                temp += c

        if len(temp) > max:
            max = len(temp)
        
        return max
            
# @lc code=end

