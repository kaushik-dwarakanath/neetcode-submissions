class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) Solution using enumerate and complement
        seen = {}   # To store the index of all the traversed elements

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i