class Solution:
    def isValid(self, s: str) -> bool:
        char_closes_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }


        stack = []

        for char in s:
            if char not in char_closes_dict.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if item != char_closes_dict[char]:
                    return False

        return len(stack) == 0