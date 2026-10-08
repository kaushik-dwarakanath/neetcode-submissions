class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Use Boyer-Moore Voting Algorithm
        # Linear time complexity
        # Constant space complexity

        # majority HAS to be GREATER THAN floor(len(nums)/2) for this algorithm to work

        candidate = None
        count = 0

        for i in nums:
            if count == 0:
                candidate = i
            
            if i == candidate:
                count += 1  # Add vote if candidate number
            
            else:
                count -= 1  # Cancel vote if not candidate number
        
        return candidate