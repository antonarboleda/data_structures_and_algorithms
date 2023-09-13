# Input: dictionary[] = {"GEEKS", "GEEFS", "GE", "GEMS", "FOR", "QUIZ", "GO"};
#        boggle[][]   = {{'G', 'I', 'Z'},
#                        {'U', 'E', 'K'},
#                        {'Q', 'S', 'E'}};
#       isWord(str): returns true if str is present in dictionary
#                    else false.

# Output:  Following words of dictionary are present
#          GEEKS
#          QUIZ
"""
Pre Calculation of insertion into a Trie

The time complexity is O(NM) where N is the length of the dictionary 
and M is the length of the longest word

Space complexity is O(26^N) where N is the number of characters we allow in 
the dictionary. I.e. if we only allow alphabetical chars, it's 26! size nodes

Searching using a Trie and the Boggle Board
Time Complexity is 4^(N^2) because there are 4 directions and N is the length 
of the N by N board
Space Complexity is N^2 because of the recursive calls
"""

class TrieNode:
    def __init__(self, char, is_word=False):
        self.dictionary = {}
        self.is_word = is_word
        self.char = char

    def add_word(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.dictionary:
                cur.dictionary[char] = TrieNode(char)
            cur = cur.dictionary[char]
        cur.is_word = True
        
def get_neighbors(row,col, boggle, visited):
    neighbors = []
    for i,j in [(0,1),(1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
        if 0 <= row+i < len(boggle) and 0 <= col+j < len(boggle[0]) and (row+i,col+j) not in visited:
            neighbors.append((row+i,col+j))
    return neighbors

def find_words(row, col, boggle, result, root, path, visited):
    if root.is_word:
        result.append("".join(path))
        return

    
    for nei in get_neighbors(row, col, boggle, visited):
        x,y = nei
        if boggle[x][y] in root.dictionary:
            visited.add((x,y))
            path.append(boggle[x][y])            
            new_root = root.dictionary[boggle[x][y]]
            
            find_words(x,y,boggle, result, new_root, path, visited)
    
            path.pop()
            visited.remove((row,col))

def boggle(dictionary, boggle):
    root = TrieNode("")
    n, m = len(boggle), len(boggle[0])
    for word in dictionary:
        root.add_word(word)
    result = []

    for row in range(n):
        for col in range(m):
            char = boggle[row][col]
            if char in root.dictionary:
                find_words(
                    row,
                    col,
                    boggle, 
                    result, 
                    root.dictionary[char], 
                    [char], 
                    set([(row,col)])
                )
    print(result)
    return result

board = [
    ["G", "I", "Z"],
    ["U", "E", "K"],
    ["Q", "S", "E"]
]
assert boggle(["GEEKS", "FOR", "GO", "QUIZ"], board) == sorted(["GEEKS", "QUIZ"])
sorted(["GEEKS", "QUIZ"])