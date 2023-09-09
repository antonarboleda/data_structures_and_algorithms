# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# You are not allowed to solve the problem using any serialize methods (such as eval).

# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# ["Hello world", "hi"]
# "Hello word#Hi"
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Input: dummy_input = [""]
# Output: [""]

"""
-------- High Level Idea/Algorithm 
Idea

Similar to TCP protocol, encode the string with info about the length of the 
word with a delimiter
Then decode it by reading the encoded length
alphanumeric? uppercase vs lowercase
"5#Hello5##World"

["Hello", "HelloHello", ""]
 ["5#Hello", "10#HelloHello", "0#"]

Pseudocode

def encode
for each character add it to another list 
   prefix each word with len(word) + delimeter + word
return the joined list

example encoded string5#Hello10#HelloHello

def decode
init two pointers at start of string
iterate through string
if we run into delimiter #
get substring from s[i:j]
cast to int, then move pointers to next length 
i,j
5#Hello10#HelloHello

---------- Info about the practice session 
Start Time: 6:30pm
6:43 psuedocoding
Finished: 7:04 (tests cases I created passing and passed all Leetcode tests)
Notes - I spent some time wondering why not just using "".join(strings) and 
"".split() with a delimiter like "#" an interview I think they would have told 
me pretty quickly. Then realized that it wouldn't work if the user typed in the 
delimiter. Overall it was pretty good. I had some typos in the code so I need to 
improve on reading the code thoroughly for typos and running through examples 
"""
from typing import List

class Encoder:
    # Time: O(NM) N = length of strings O(N), M = len(longest word)
    # Space: O(NM) we're taking up the size of the list
    def encode(self, strings: List[str]) -> str:
        encoded_words = []
        for s in strings:
            encoded_words.append(str(len(s)) + "#" + s)
        return "".join(encoded_words)
    # Time: O(N^2) because of the substring operations inside the loop are N. 
    # Space: O(N)
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        decoded_words = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            w_length = int(s[i:j])
            j += 1
            word = s[j: j + w_length]
            decoded_words.append(word)
            j += w_length
            i = j
        return decoded_words


if __name__ == "__main__":
    encoder = Encoder()
    words = [["Hello", "World"], [""], ["####"]]
    for word_list in words:
        assert encoder.decode(encoder.encode(word_list)) == word_list    
    print("passed!")
