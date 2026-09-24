class Solution:

    def encode(self, strs: List[str]) -> str:
        # The idea is to essentially provide the decoder with information
        # about the string upfront so that it can use it to decode.
        # Now, the number is not a single value but can be double digit so
        # We need to capture that as well.
        strs_with_lengths = [f"{len(string)}#{string}" for string in strs]

        return "".join(strs_with_lengths)

    def decode(self, s: str) -> List[str]:

        # List to hold the solution.
        solution = []

        # Index to keep moving in the string.
        i = 0

        # Loop until we finish the sequence.
        while i < len(s):

            # Pulling the size. The size is essentially from i until
            # we find the first #.
            size = []
            while s[i] != '#':
                size.append(s[i])
                i += 1

            size = int(''.join(size))

            word = s[i + 1: i + 1 + size]
            print(word)
            i += size + 1

            solution.append(word)
        return solution
