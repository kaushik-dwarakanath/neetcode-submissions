class Solution:
    def string_to_dict(self, s: str) -> dict:
        d = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        return self.string_to_dict(s) == self.string_to_dict(t)