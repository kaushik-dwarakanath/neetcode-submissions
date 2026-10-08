class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = dict()

        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 0
            dict_nums[i] += 1
        
        dec_freq = sorted(dict_nums.keys(), key = lambda x: dict_nums[x], reverse = True)
        return dec_freq[:k]