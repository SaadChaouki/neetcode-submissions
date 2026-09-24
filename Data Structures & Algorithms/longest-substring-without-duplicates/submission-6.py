class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Setting a variable to keep track of the longest sequence size. 
        # This can also be the actual sequence.
        longest_string_size = 0

        # The problem that we have is that we need to reset because it's possible 
        # that the item that was found is the first one and has to be dropped from
        # the left and then we need to continue essentially. 

        # What we'll be implementing is essentially a sliding window. We're 
        # moving the right part, fixing the left part. If the right part finds
        # a character which already exists, move the left part to the last index

        character_index = {}


        # Here, we'll be moving through the string. However, we need to reset the start
        # when we find a duplicate. We'll implement a sliding window. 
        # We have the left and the right. The left will be fixed. The right
        # will keep moving. If right is inside the substring, we set the left to
        # that index in that list.
        left_idx = 0

        # The right index is essentially what will be moving. The left index will
        # just keep following it. Can it be a for loop?
        for right_idx, char in enumerate(s):
            if char in character_index and character_index[char] >= left_idx:
                left_idx = character_index[char] + 1
            character_index[char] = right_idx
            longest_string_size = max(longest_string_size, right_idx - left_idx + 1)

        return longest_string_size


