class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        j = len(nums) - 1
        k = 0

        while i < j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                i += 1

        for x in nums:
            if x != val:
                k += 1
            else:
                return k