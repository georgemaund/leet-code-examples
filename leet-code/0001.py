class Solution:

    def twoSumBinary(self, nums: list[int], target: int) -> list[int]:

        def binarySort(sNums: list[int], target: int) -> tuple[int]:
            for x in sNums:
                low = 0
                high = len(sNums)
                y = target - x
                while len(sNums[low:high]) > 1:
                    n = low + (len(sNums[low:high]) // 2)
                    if sNums[n-1] == y:
                        return (x, y)
                    elif sNums[n-1] < y:
                        low = n
                    elif sNums[n-1] > y:
                        high = n - 1
                if sNums[n] == y:
                    return(x, y)

        sNums = sorted(nums)
        numsAns = binarySort(sNums, target)
        i = nums.index(numsAns[0])
        for j, y in enumerate(nums):
            if y == numsAns[1] and j != i:
                return[i, j]