class Trinode:
    def __init__(self):
        self.child = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.node = Trinode()

    def insert(self,string):
        n = len(string)

        if n == 0:                  #base case
            self.node.isEnd = True
            return

        if string[0] in self.node.child:
            self.node.child[string[0]].insert(string[1:])
        else:
            self.node.child[string[0]] = Trie()
            self.node.child[string[0]].insert(string[1:])

    def search(self,word):
        temp = self.node
        for i in range(len(word)):
            if word[i] not in temp.child:
                return False
            else:
                temp = temp.child[word[i]].node

        if temp.isEnd is True:
            return True
        else:
            return False


string1 = 'nimit'
string2 = 'nitin'
obj = Trie()
obj.insert(string1)
obj.insert(string2)
print(obj.search('nimit')
      )
