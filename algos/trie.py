class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.is_end_of_word = False
        self.char = char
    
    def __repr__(self) -> str:
        return f"{self.char} {str(self.is_end_of_word)} {self.children}"

class Trie:
    def __init__(self, subs):
        self.root = TrieNode("")
        self.subs = subs
    
    def add_word(self, word):
        cur = self.root
        for index, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = TrieNode(char)

            cur = cur.children[char]
            if index == len(word) - 1:
                cur.is_end_of_word = True            

    def add_word_with_subs(self, word):
        self.add_word_with_sub_recur(0, word, self.root)
    
    def add_word_with_sub_recur(self, index, word, parent):
        if index == len(word):
            parent.is_end_word = True
            print(parent)
            return
    

        characters = [word[index]] + self.subs.get(word[index], [])
        for char in characters:
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            self.add_word_with_sub_recur(index + 1, word, parent.children[char])
            
        cur = parent.children[word[index]]        
        if len(word) - 1 == index:
            cur.is_end_of_word = True
    
    def contains_bad_word(self, word) -> bool:
        for i, char in enumerate(word):
            if char in self.root.children and self.search(i, word):
                return True
        return False

    def search(self, start_index, word) -> bool:
        cur = self.root
        for i in range(start_index, len(word)):
            char = word[i]
            if char not in cur.children:
                return False
            
            cur = cur.children[char]
            if cur.is_end_of_word:
                return True
        return cur.is_end_of_word
                
    

t = Trie({"o": ["0"], "e": ["3", "X"]})
print(t)
t.add_word_with_subs("food")
t.add_word_with_subs("fool")
# t.add_word("f")

# assert t.search("f")
assert t.contains_bad_word("f00l")
assert t.contains_bad_word("usernamef00lsss")
assert t.contains_bad_word("f0ol")
# assert not t.search("flu")
# assert t.search("bar")
print(t.root)

            

 