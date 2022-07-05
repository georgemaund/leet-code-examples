class Solution:

    def plusOne(self, digits: list[int]) -> list[int]:
        largeInt = ""
        newDigits = []
        for i in digits:
            largeInt += str(i)
        largerInt = int(largeInt) + 1
        for i in str(largerInt):
            newDigits.append(int(i))
        return newDigits