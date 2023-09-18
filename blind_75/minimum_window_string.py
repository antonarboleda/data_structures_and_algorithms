# Given two strings s and t of lengths m and n respectively, return the minimum 
# window substring of s such that every character in t (including duplicates) 
# is included in the window. If there is no such substring, return the empty 
# string "".

# The testcases will be generated such that the answer is unique.
# s: "airbnb", t: "ib" -> min window "irb" 3
# s: "abcaa", t: "aa" -> 5 because entire string

"""
abaa
l   
   r
window = {a: 2, b: 1}
substring_occ = {a: 2}

gather occurences from substring
init window
result = len(chars) + 1
for every char
add it to window
while the window is valid -> all occurrences in window >= substring occurrences
  take minimum of result and window size
  remove left char from window
  increment left pointer

substr_occ = {i: 1, b: 1}
window = {a: 1, i: 1, r: 1, b: 1}
# s: "airbnb", t: "ib" -> min window "irb" 3
# s: "aaaa", t: "aa" -> 2 last two

Start Time: 9:35am 9/10/23
End Time: 10:00am 
Grade: A

"""
from collections import defaultdict

def equal_occ(window, substring_occ):
    for c, count in substring_occ.items():
        if window.get(c, 0) < count:
            return False
    return True

def minimum_window_string(string: str, substring: str) -> str:
    substring_occ = defaultdict(int)
    window = defaultdict(int)
    result = string
    found = False
    for c in substring:
        substring_occ[c] += 1
    left = 0
    for right in range(len(string)):
        window[string[right]] += 1
        while equal_occ(window, substring_occ):
            if len(string[left:right+1]) < len(result) or (len(string[left:right+1]) < len(result) and string[left:right+1] < result):
                result = string[left:right+1]
                found = True
            window[string[left]] -= 1
            left += 1
    return result if found else ""

assert minimum_window_string("airbnb", "ib") == "irb"
assert minimum_window_string("aaa", "aa") == "aa"
assert minimum_window_string("aaa", "a") == "a"
print("passed!")


    
