
def ctoi(c):
    return ord(c) - 97


class Trie:

    def __init__(self):
        self.nodes = [None for _ in range(26)]
        self.end = False

    def insert(self, word: str) -> None:
        temp = self
        for c in word:
            i = ctoi(c)
            if not temp.nodes[i]:
                temp.nodes[i] = Trie()
            temp = temp.nodes[i]
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self
        for c in word:
            i = ctoi(c)
            if not temp.nodes[i]:
                return False
            temp = temp.nodes[i]
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self
        for c in prefix:
            i = ctoi(c)
            if not temp.nodes[i]:
                return False
            temp = temp.nodes[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
