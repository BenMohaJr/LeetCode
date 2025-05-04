from typing import List
from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter()
        pairs = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            pairs += counts[key]
            counts[key] += 1

        return pairs
