from collections import deque

# This is a py class for data structure demo

# Class for binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    # recursive function to return an in-order listing of nodes
    def inorder (self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)





# create a main function to call above method and class
def main():
    print("This is main function")
    # create a new list
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    print("Fruits are ", fruits)

    #ceate a new stack
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
    print("my queue is", myqueue,"after I added Terry and Graham in it")
    # The first to arrive now leaves
    myqueue.popleft()
    print('my queue is', myqueue, 'after I removed the first element from queue')

    # Create a dictionary
    mydictionary = {'jack':4098, 'sape':4139}
    mydictionary['guido']=4127
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
    mytuple2= ('physics', 'chemistry', 1997, 1998)
    thesumtuple = mytuple+mytuple2
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








if __name__=='__main__':
    main()




