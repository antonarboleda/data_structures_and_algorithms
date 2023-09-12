# Boggle, but where the dictionary is all English words in the boggle board, 
# but you can do whatever precalculations you want with the English dictionary. 
# in other words, measure the time complexity of the precalculation and the 
# calculations after you see the boggle board separately, and optimize the time 
# complexity after seeing the boggle board


"""
input: dictionary and boggle
output: A set of words that are present in the dictionary that can be found
inside the boggle

[
    [a, a, a, a, a, a, a, a, a]
    [a, a, a, a, a, a, a, a, a]
    [a, a, a, a, a, a, a, a, a]
    [a, a, a, a, a, a, a, a, a]
]

High level - initial idea
for every word
    for every row
        for every col
            if it matches first character and we found it in the graph
                add it to the set of words
return the set of words

Time: N = length of dictionary
Time: Time O(N) * O(MK)^2
Space: O(N) * O(MK) assuming we use BFS

Pre processing optimization
For each cell in the board, add it's location into a hash map. When we go
through each word, instead of search the board, perform a bfs in each 
startpoint for the letters.

Reduces the time complexity from O(N) * O(MK)^2 to O(N) * O(MK)

start_points: {str: List[(int, int)]} - char to indices

"""
from typing import List
from collections import defaultdict, deque

def get_neighbors(r: int,c: int,board: List[List[str]], visited) -> List[int]:
    neighbors = []
    for x, y in [
            (r+1,c), 
            (r-1,c), 
            (r,c+1), 
            (r,c-1),
            (r-1,c+1),
            (r+1,c+1),
            (r+1,c-1),
            (r-1,c-1),
        ]:
        if  0 <= x < len(board) and 0 <= y < len(board[0]) and (x,y) not in visited:
            neighbors.append((x,y))
    return neighbors

def contains_word(row, col, word, boggle) -> bool:
    queue = deque([(row,col, 0)])
    visited = set()
    while queue:
        r,c, distance = queue.popleft()
        visited.add((r,c))
        for nei_row, nei_col in get_neighbors(r,c, board, visited):
            if distance+1 == len(word):
                return True
            elif distance+1 < len(word) and boggle[nei_row][nei_col] != word[distance+1]:
                continue

            queue.append((nei_row, nei_col, distance+1))
    return False

def contains_word_dfs(r, c, word, index, boggle) -> bool:
    if index == len(word):
        return True
    if word[index] != boggle[r][c]:
        return False
    
    tmp = boggle[r][c]
    boggle[r][c] = "#"
    ans = False
    for x, y in [
            (r+1,c), 
            (r-1,c), 
            (r,c+1), 
            (r,c-1),
            (r-1,c+1),
            (r+1,c+1),
            (r+1,c-1),
            (r-1,c-1),
        ]:
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            continue

        if board[x][y] == "#":
            continue

        if contains_word_dfs(x,y,word,index+1,boggle):
            ans = True
            break

    boggle[r][c] = tmp
    return ans

def boggle(words: List[str], boggle: List[List[str]]) -> List[str]:
    result = []
    start_points = defaultdict(list)
    for row in range(len(boggle)):
        for col in range(len(boggle[0])):
            start_points[boggle[row][col]].append((row,col))
    for word in words:
        if not word:
            continue
        
        for x, y in start_points[word[0]]:
            # if contains_word(x,y, word, boggle):
            if contains_word_dfs(x, y, word, 0, boggle):                
                result.append(word)
                break
    return result

board = [
    ["G", "I", "Z"],
    ["U", "E", "K"],
    ["Q", "S", "E"]
]
assert boggle(["GEEKS", "FOR", "GO", "QUIZ"], board) == sorted(["GEEKS", "QUIZ"])
sorted(["GEEKS", "QUIZ"])
print("passed!")
