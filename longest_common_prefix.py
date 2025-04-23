class Solution:
    """
    Provides a solution for finding the longest common prefix among a list of strings.
    """
    def longestCommonPrefix(self, string_list: List[str]) -> str:

        if not string_list:
            return ""

        common_prefix = ""

        sorted_list = sorted(string_list) # Use a new variable if you want to keep the original order

        # Get the first string (lexicographically smallest after sorting)
        first_string = sorted_list[0]
      
        # Get the last string (lexicographically largest after sorting)
        last_string = sorted_list[-1]

        # Determine the maximum possible length for the common prefix,
        # which is the length of the shorter of the first and last strings.
        # We only need to compare characters up to this length.
        comparison_length = min(len(first_string), len(last_string))

        # Iterate through the character indices up to the comparison length
        for char_index in range(comparison_length):
            # Compare the characters at the current index in the first and last strings
            if first_string[char_index] != last_string[char_index]:
                # If characters don't match, the common prefix ends before this index.
                # Return the prefix found so far.
                return common_prefix
            # If characters match, append the character to our result string
            common_prefix += first_string[char_index]

        # If the loop completes without finding any mismatches,
        # the entire accumulated string `common_prefix` is the longest common prefix.
        return common_prefix
