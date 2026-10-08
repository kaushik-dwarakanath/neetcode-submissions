class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums_freq = dict()

        for i in nums:
            if i not in nums_freq:
                nums_freq[i] = 0
            
            nums_freq[i] += 1

            if nums_freq[i] > n//2:
                return i