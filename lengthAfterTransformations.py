class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        from functools import lru_cache

        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(c: str, t: int) -> int:
            if t == 0:
                return 1
            if c == 'z':
                return (dp('a', t - 1) + dp('b', t - 1)) % MOD
            else:
                next_char = chr(ord(c) + 1)
                return dp(next_char, t - 1)

        total = 0
        for c in s:
            total = (total + dp(c, t)) % MOD

        return total
