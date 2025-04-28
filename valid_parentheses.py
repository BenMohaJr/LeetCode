class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        closing = {'}', ']', ')'}
        couples = {'{': '}', '[': ']', '(': ')'}
        validator = []
        
        for bracket in s:
            if bracket not in closing:
                validator.append(bracket)
            else:
                if not validator:
                    return False
                open_bracket = validator.pop()
                expected_closing = couples.get(open_bracket)
                if bracket != expected_closing:
                    return False
                
        return not validator
