'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/
'''


class Solution:
    def check(self, nums: List[int]) -> bool:
        l=False
        t=nums.copy()
        t.sort()
        for i in range(len(nums)):
            nums.insert(0,nums[len(nums)-1])
            nums.pop()
            if(nums==t):
                l=True
        return l