class Solution:
    
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)
        while len(nums[low:high]) > 1:
            n = low + (len(nums[low:high]) // 2) - 1
            if nums[n] == target:
                return n
            elif nums[n] < target:
                low = n + 1
            elif nums[n] > target:
                high = n
        if nums[low] < target:
            return low + 1
        else:
            return low