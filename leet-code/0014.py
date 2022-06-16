class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:

        def lenSort(value: str) -> int:
            return len(value)

        strs.sort(key=lenSort)
        frstElem = strs[0]
        cmnPrefix = ""
        i = 0
        if (frstElem == "") or (len(strs) == 1):
            return frstElem
        while i < len(frstElem):
            for x in strs[1:]:
                if x[i] != frstElem[i]:
                    return cmnPrefix
            cmnPrefix += x[i]
            i += 1
        return cmnPrefix