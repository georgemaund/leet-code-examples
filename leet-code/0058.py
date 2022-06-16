class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        word = (s.rsplit(maxsplit=1))[-1]
        return len(word)