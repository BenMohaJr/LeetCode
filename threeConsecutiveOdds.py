class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if not arr:
            return False
        
        counter = 0
        for value in arr:
            if value % 2 == 1:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                return True
        
        return False
