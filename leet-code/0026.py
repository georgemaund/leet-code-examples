class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        x = None
        k = 0
        for n in nums:
            if n != x:
                x = n
                nums[k] = x
                k += 1
        return k