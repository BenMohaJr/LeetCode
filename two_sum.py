class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return
        
        complements = {}

        for idx, value in enumerate(nums):
            complement = target - value
            if value in complements:
                return [idx, complements[value]]
            
            complements[complement] = idx
        return []
        
