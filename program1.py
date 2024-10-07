class Solution(object):
    def isValid(self, s):
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[ch] != top_element:
                    return False
            else:
                stack.append(ch)        
        return not stack

