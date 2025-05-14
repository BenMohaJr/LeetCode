from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for row in range(numRows):
            current_row = [1] * (row + 1)
            for col in range(1, row):
                current_row[col] = pascal[row - 1][col - 1] + pascal[row - 1][col]
            pascal.append(current_row)
        return pascal
