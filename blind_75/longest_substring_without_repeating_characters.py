# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
#                 r
#              l
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a 
# subsequence and not a substring.


"""
Start Time: 8:35 9/10/23
End Time: 9:03 
window = {}
res = 0
Psueudocode:

go through each char
add right to window
while the window is invalid
  move the left forward
compare result with current window size

Algo
- Correct inuition. On line 37 I just said "while the window is valid". I should
have really dug into this to make sure I understood what that meant

Impl
- Used a set instead of a counter. I made the assumption I could use a set 
without considering other data types. We acutally needed counts
"""
from collections import defaultdict

def longest_substring_without_repeating_chars(chars):
    window = defaultdict(int)
    result, left = 0, 0
    for right in range(len(chars)):
        window[chars[right]] += 1
        while window[chars[right]] > 1:
            window[chars[left]] -= 1
            left += 1
        result = max(right - left + 1, result)
    return result
"""
abca
   r
"""

assert longest_substring_without_repeating_chars("a") == 1
assert longest_substring_without_repeating_chars("abca") == 3
assert longest_substring_without_repeating_chars("aaaaaa") == 1
assert longest_substring_without_repeating_chars("abcdefa") == 6