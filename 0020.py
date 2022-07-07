class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            elif len(stack) > 0:
                x = stack.pop()
                if not ((x == "(" and i == ")") or (x == "[" and i == "]") or (x == "{" and i == "}")):
                    return False
            else:
                return False
        return len(stack) == 0