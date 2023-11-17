"""
design/understand: 
pseudo
impl
debug
"""
# You are given two strings s and sub. You are also given a 2D 
# character array mappings where mappings[i] = [oldi, newi] 
# indicates that you may perform the following operation any number of times:

# Replace a character oldi of sub with newi.
# Each character in sub cannot be replaced more than once.

# Return true if it is possible to make sub a substring of s by replacing zero 
# or more characters according to mappings. Otherwise, return false.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "fool3e7bar", sub = "leet", 
# s = "foole3bar", sub = leet
# l3e7
#  mappings = [["e","3"],["t","7"],["t","8"]]
# Output: true
# Explanation: Replace the first 'e' in sub with '3' and 't' in sub with '7'.
# Now sub = "l3e7" is a substring of s, so we return true.
# Example 2:

# Input: s = "fooleetbar", sub = "f00l", mappings = [["o","0"]]
# Output: false
# Explanation: The string "f00l" is not a substring of s and no 
# replacements can be made.
# Note that we cannot replace '0' with 'o'.
# Example 3:

# Input: s = "Fool33tbaR", sub = "leetd", 
# l3etb
# mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
# Output: true
# Explanation: 
#   Replace the first and second 'e' in sub with '3' and 'd' in sub with 'b'.
# Now sub = "l33tb" is a substring of s, so we return true.
"""      for every mapping
        leetd
 replace /  \leetd don't replace
  l3etd        leetd
l3etd    l33td           
    

def replacement_is_possible(mapping, substring_str_builder):
    char, occurrences = mapping
    return char in substring_str_builder and str(occurrences) >= 0:

def match_replacement()

current_string = joined stringbuilder
result = False
if current_string in s:
    return True
for char_index, character in substring:
    for i, mapping in enumerate(mappings):
        mapping_character, str_occ = []
        if occ >= 0:
            mapping[i] = [char_map, occ - 1]
            tmp = string_builder[character_index]
            string_builder[character_index] = mapping_character

            map_replacement_recurse(mapping)
            string_builder[character_index] = tmp
            mapping[i] = [char_map, occ]

return result                
m = mapping
time: 2^m
space: 2^m
"""
def match_replacement_recur(index, substring_char_arr, mappings, s):
    if "".join(substring_char_arr) in s:
        print(substring_char_arr)
        return True
    
    if index == len(substring_char_arr):
        return False
    
    for mapping_idx, mapping in enumerate(mappings):
        char, occ = mapping
        if occ > 0:
            tmp = substring_char_arr[index]
            substring_char_arr[index] = char
            mappings[mapping_idx] = [char, occ - 1]
            
            if match_replacement_recur(index + 1, substring_char_arr, mappings, s):
                return True
    
            substring_char_arr[index] = tmp
            mappings[mapping_idx] = mapping
    return False

def match_replacement(s, substring, mappings):
    char_arr = substring.split()
    print(char_arr)
    result = match_replacement_recur(0, char_arr, mappings, s)
    print(result)
    return result
# Constraints:

# 1 <= sub.length <= s.length <= 5000
# 0 <= mappings.length <= 1000
# mappings[i].length == 2
# oldi != newi
# s and sub consist of uppercase and lowercase English letters and digits.
# oldi and newi are either uppercase or lowercase English letters or digits.
# Input: s = "fool3e7bar", sub = "leet", 
# s = "foole3bar", sub = leet
# l3e7
#  mappings = [["e","3"],["t","7"],["t","8"]]
# Output: true
mappings = [["e",3],["t",7],["t", 8]]
s = "fool3e7bar"
sub = "leet"
match_replacement(s, sub, mappings)


s = "fooleetbar"
sub = "f00l"
mappings = [["o", 0]]
assert not match_replacement(s, sub, mappings) 