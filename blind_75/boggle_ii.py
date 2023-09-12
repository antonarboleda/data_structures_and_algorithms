
"""
Input: dictionary[] = {"GEEKS", "GEEFS", "GE", "GEMS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ

Optimization Idea
Idea 1
- For each word, insert each word into the trie
   Time: O(NM) M is longest word in the trie
   Space: O(NM) M is longest word in the trie

Idea 2
For each cell in boggle, get all paths DFS or BFS
    Once you have a word insert that into the Trie.
Time: O(N^2!) for all paths
Space: O(N^2!) for all paths oin the Trie

For each word in the dictionary
    Search in the trie 
"""
class Trie:
    def __init__(self):
        self.root = {}
    def add_word(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}            
            cur = cur[char]
    def has_word(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return True

def completed_searching(row,col,visited,boggle):
    n, m = len(boggle), len(boggle[0])    
    for nei in [
        (row+1, col), 
        (row-1,col), 
        (row,col+1), 
        (row,col-1),
        (row+1,col+1),
        (row+1,col-1),
        (row-1,col+1),
        (row-1,col-1),
    ]:
        next_row, next_col = nei
        if nei not in visited and next_row >= 0 and next_row < n and next_col >= 0 and next_col < m:
            return True
    return False
        
def get_all_words(row, col, boggle, path, all_words, visited):
    n, m = len(boggle), len(boggle[0])
    if n * m == len(visited):
        all_words.append("".join(path))
        return
    
    for nei in [(row+1, col), (row-1,col), (row,col+1), (row,col-1),(row+1,col+1),
        (row+1,col-1),
        (row-1,col+1),
        (row-1,col-1),]:
        next_row, next_col = nei
        if nei not in visited and next_row >= 0 and next_row < n and next_col >= 0 and next_col < m:
            path.append(boggle[next_row][next_col])
            visited.add((next_row,next_col))
            
            get_all_words(next_row, next_col, boggle, path, all_words, visited)

            path.pop()
            visited.remove((next_row,next_col))


    

def boggle(dictionary, boggle):
    root = Trie()
    result = []
    for row in range(len(boggle)):
        for col in range(len(boggle[0])):
            path = []
            all_words = []
            visited = set()
            get_all_words(row, col, boggle, [boggle[row][col]], all_words, set([(row,col)]))
            # print(all_words, "are the words")
            for word in all_words:
                root.add_word(word)
            
    for word in dictionary:
        if root.has_word(word):
            result.append(word)

    return result

board = [
    ["G", "I", "Z"],
    ["U", "E", "K"],
    ["Q", "S", "E"]
]
assert boggle(["GEEKS", "FOR", "GO", "QUIZ"], board) == sorted(["GEEKS", "QUIZ"])
sorted(["GEEKS", "QUIZ"])