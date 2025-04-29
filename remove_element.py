from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = len(nums) - 1
        tail = 0
        k = 0
        while head >= tail:
            if nums[tail] != val:
                tail += 1
                k += 1
                continue

            while head > tail:
                if nums[head] == val:
                    head -= 1
                    continue
                # Swap in a valid value
                nums[tail] = nums[head]
                nums[head] = val
                head -= 1
                tail += 1
                k += 1
                break
        
        return k
