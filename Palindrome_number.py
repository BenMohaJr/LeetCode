class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Handle negative numbers (they are not palindromes due to '-')
        if x < 0:
            return False
        
        x_str = str(x)
        
        # 2. Initialize pointers the loop
        start = 0
        end = len(x_str) - 1

        # 3. Loop while start pointer is less than end pointer
        while start < end:
            # 4. Check characters
            if x_str[start] != x_str[end]:
                return False # Not a palindrome
            
            # 5. Move pointers inward
            start += 1
            end -= 1
            
        # 6. If the loop finishes without finding mismatches, it is a palindrome
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        x_str = str(x)
        # Compare the string with its reverse using slicing [::-1]
        return x_str == x_str[::-1]
