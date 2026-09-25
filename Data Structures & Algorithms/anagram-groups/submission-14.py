from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # This is something where every single item will need to be compared
        # with all the other items to achieve a solution. That will be O(n2).

        # If we sort it instead, 

        anagram_groups = defaultdict(list)
        for word in strs:
            anagram_groups[''.join(sorted(word))].append(word)

        return list(anagram_groups.values())