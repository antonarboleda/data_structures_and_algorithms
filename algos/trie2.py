class Trie:
    def __init__(self):
        self.root = {}
 
    def __repr__(self):
        return f"{self.root}"

    def add_word(self, word):
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur["is_end"] = True

    def add_phrase(self, phrase):
        words = phrase.split()
        cur = self.root
        for word in words:
            if word not in cur:
                cur[word] = {}
            cur = cur[word]
        cur["is_end_word"] = True

t = Trie()
t.add_word("what")
t.add_word("blah")
t.add_word("test")
t.add_phrase("my dog is the best")
print(t)