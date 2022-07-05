class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        stack = []
        xStr = str(x)
        pali = ""
        for n in xStr:
            stack.append(n)
        while len(stack) > 0:
            pali += stack.pop()
        if xStr == pali:
            return True
        return False