class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]

        for i in range(len(first)):
            count = 0
            for j in strs[1::]:
                if first[:i+1] == j[:i+1]:
                    count += 1
                else:
                    break

            if count == len(strs) - 1:
                res = first[:i+1]
        
        return res