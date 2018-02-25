# description : https://leetcode.com/problems/move-zeroes/description/ # NOQA
# author : Hussam
# solution : two pointers
# o(n) time, o(1) space


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tail = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail += 1
