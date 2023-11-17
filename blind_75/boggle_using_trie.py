# Given a dictionary, a method to do a lookup in 
# the dictionary and a M x N board where every cell has one character. 
# Find all possible words that can be formed by a sequence of adjacent characters. 
# Note that we can move to any of 8 adjacent characters, but a word should not have 
# multiple instances of the same cell.
# Example: 

# Output: Following words of the dictionary are present
#          GEEKS
#          QUIZ

# Explanation:

"""
n = len(dictionary)

time O(d * mn^2)
space 

trie
w = longest word in the dictionary
time = O(mn * w)
space = (26 + 26) ^ w
For each word
    go through the boggle board
        if character == first character of word if exists()     

Build Trie

for word in words:
    trie.addWord(word)
----
Search board for word existence
def search_and_update_result(parent, board, result, row, col):
  get current which inside parents children
  if the current node is end word:
    add it to the result
    mark end node as not an end word anymore
    

  Find the current cell valid neighbors:
    if they exist in current nodes children:
        save original val
        mark the original boggle board with #
        search_and_update_result(current, board, result, row, col)
        unmark with original val
    

def search_for_words():
    for row in board
        for col in board[0]
            if the character is in the roots children and search_and_update_result(root, board, result):
                add the word to result
"""
class TrieNode:
    def __init__(self):
        self.raw_word = None
        self.end_word = False
        self.children = {}
    
    def __repr__(self) -> str:
        return f"{self.children} {self.raw_word} {self.end_word}"
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def __repr__(self) -> str:
        return f"{self.root}"
    
    def addWord(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_word = True
        current.raw_word = word

def get_valid_neighbors(row, col, board):
    n, m = len(board), len(board[0])
    result = []
    for x, y in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,1), (-1,-1), (1,-1)]:
        nei_row, nei_col = row + x, col + y
        if 0 <= nei_row < n and 0 <= nei_col < n:
            result.append((nei_row, nei_col))
    return result

def search_and_update_result(parent_node, row, col, result, board):
    char = board[row][col]
    current_node = parent_node.children[char]
    if current_node.end_word:
        result.append(current_node.raw_word)
        current_node.end_word = False
    board[row][col] = "#"
    for nei_row, nei_col in get_valid_neighbors(row, col, board):
        if board[nei_row][nei_col] in current_node.children:
            search_and_update_result(current_node, nei_row, nei_col, result, board)
    board[row][col] = char
    if parent_node.children[char].children == {}:
        parent_node.children.pop(char)

def boggle_board(dictionary, board):
    trie = Trie()
    for word in dictionary:
        trie.addWord(word)
    print(trie)
    n, m = len(board), len(board[0])
    result = []
    for row in range(n):
        for col in range(m):
            if board[row][col] in trie.root.children:
                search_and_update_result(trie.root, row, col, result, board)
    print(result)
    return result
# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#        boggle[][]   = {{'G', 'I', 'Z'},
#                        {'U', 'E', 'K'},
#                        {'Q', 'S', 'E'}};    
dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
board = [
    ["G", "O", "Z"],
    ["U", "E", "E"],
    ["Q", "S", "K"]
]
boggle_board(dictionary, board)
