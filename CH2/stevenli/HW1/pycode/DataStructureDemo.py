from collections import deque


# This is a py class for data structure demo

# Class for binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    # insert a node in the tree
    def insert(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current

    # recursive function to return an in-order listing of nodes
    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)


# Create a Hash table class
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1

        self.slots[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


# create a main function to call above method and class
def main():
    print("This is main function")
    # create a new list
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    print("Fruits are ", fruits)

    # ceate a new stack
    mystack = [3, 4, 5]
    print("stack is", mystack)
    # add element in stack
    mystack.append(6)
    mystack.append(7)
    print('stack is ', mystack, 'after I added two numbers in it')
    # Remove the second last element from stack which is 6
    mystack.pop(-2)
    print('Now stack is ', mystack)

    # Create a queue
    myqueue = deque(["Eric", "John", "Michael"])
    print("my queue is ", myqueue)
    # Append Terry and Graham in the queue
    myqueue.append("Terry")
    myqueue.append("Graham")
    print("my queue is", myqueue, "after I added Terry and Graham in it")
    # The first to arrive now leaves
    myqueue.popleft()
    print('my queue is', myqueue, 'after I removed the first element from queue')

    # Create a dictionary
    mydictionary = {'jack': 4098, 'sape': 4139}
    mydictionary['guido'] = 4127
    print('my dictionary is:', mydictionary)
    # Get the value of "jack"
    print(mydictionary["jack"])

    # loop through dictionary
    print("Loop through my dictionary")
    for k, v in mydictionary.items():
        print(k, v)

    # Create a set
    myset = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print("My set is: ", myset)

    # Create a Tuple
    mytuple = (12345, 45678, 'hello tuple')
    mytuple2 = ('physics', 'chemistry', 1997, 1998)
    thesumtuple = mytuple + mytuple2
    print('Therefore I got a new tuple: ', thesumtuple)
    # tuple can be nested

    # Create a binary tree
    n1 = Node("root node")
    n2 = Node("left child node")
    n3 = Node("right child node")
    n4 = Node("left grandchild node")

    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4

    n1.inorder(n1)

    # Create a new hash table
    ht = HashTable()
    # ht.put("good", "eggs")
    # ht.put("better", "ham")
    # ht.put("best", "spam")
    # ht.put("ad", "do not")
    # ht.put("ga", "collide")

    ht["good"] = "eggs"
    ht["better"] = "ham"
    ht["best"] = "spam"
    ht["ad"] = "do not"
    ht["ga"] = "collide"
    #
    for key in ("good", "better", "best", "worst", "ad", "ga"):
        v = ht.get(key)
        print(v)


if __name__ == '__main__':
    main()
