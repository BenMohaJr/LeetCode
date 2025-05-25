from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        counter = {}
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > threshold:
                return num
