class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valExists = True
        while valExists:
            try:
                nums.remove(val)
            except ValueError:
                valExists = False
        
        return len(nums)