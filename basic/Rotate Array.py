'''
https://leetcode.com/problems/rotate-array/submissions/
'''



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            k=nums.pop()
            nums.insert(0,k)
