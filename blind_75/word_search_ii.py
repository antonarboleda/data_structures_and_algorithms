# Given an m x n board of characters and a list of strings words, 
# return all words on the board.

# Each word must be constructed from letters of sequentially adjacent 
# cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.

"""
BOARD

oaan
etae
ihkr
ifvl

words: oath, pea, eat rain, vkx, ax, aa
output: eat oath
Notes:

Pseudocode:
DFS or BFS - going to go with BFS since it's similar to a problem "does a path
exist?" 

for every word check if the first char exists in the board
if the first char does
bfs if we can complete the word
   distance = 0
   while loop
     distance away from source is going to be the index in the target string
   if the distance away isn't equal to the (length of the word - 1) return False
   then we never reached the end of the word  
   get each edge (valid neighbors)

O(N) * Mn^2
add word if bfs is true
Start:  3:50pm 9/9/23
End: 4:43pm Finished tests passed locally
[
    ["a","b","c"],
    ["a","e","d"],
    ["a","f","g"]
]
["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]

-------------------- Post session notes
This seemed pretty straight forward where I boiled it down to a matrix search 
problem. Given a start node where the first letter of a word equals a cell
in the matrix, can we reach the end. I opted for BFS but my fatal flaw
was that I used a single visited set. This doesn't work because you need 
to explore all paths. In a backtracking solution after you explore all possibilities, 
you need to undo the state change. With BFS, I created copies of the 
visited set for each path.


"""
from typing import List
from collections import deque


def get_adj_nodes(r,c, board):
    directions = [(r+1, c), (r-1,c),(r,c+1),(r,c-1)]
    return [(i, j) for i, j in directions
            if 0<=i<len(board) and 0<=j<len(board[0])]

def bfs(row, col, word, board):
    visited = set((row,col))
    queue = deque([(row, col, 0, visited)])
    while queue:
        row, col, index, visited = queue.popleft()
        if index == len(word) - 1:
            return True
        for adj_node in get_adj_nodes(row,col, board):
            i,j = adj_node
            if adj_node not in visited and board[i][j] == word[index+1]:
                visited.add(adj_node)
                copy = visited.copy()
                queue.append((i, j, index + 1, copy))
    return False

def word_search_ii(board: List[List[str]], words: List[str]) -> List[str]:
    found_words = set()
    for word in words:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if word not in found_words and word and board[row][col] == word[0] and \
                    bfs(row, col, word, board):
                    found_words.add(word)
    return list(found_words)                

board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
] 
words = ["oath","pea","eat","rain"]

assert sorted(word_search_ii(board, words)) == sorted(["eat", "oath"])
board2 = [
    ["a","b","c"],
    ["a","e","d"],
    ["a","f","g"]
]
words2 = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]

assert sorted(word_search_ii(board2, words2)) == sorted(["abcdefg","befa","eaabcdgfa","gfedcbaaa"])
print("tests passed!")