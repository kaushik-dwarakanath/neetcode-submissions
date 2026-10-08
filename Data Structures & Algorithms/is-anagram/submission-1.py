class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            if s[i] not in dict_s.keys():
                dict_s[s[i]] = 1
            elif s[i] in dict_s.keys():
                dict_s[s[i]] += 1
            
            if t[i] not in dict_t.keys():
                dict_t[t[i]] = 1
            elif t[i] in dict_t.keys():
                dict_t[t[i]] += 1
        
        return dict_s == dict_t