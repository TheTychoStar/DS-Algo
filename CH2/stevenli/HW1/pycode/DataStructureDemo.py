from collections import deque

# This is a py class for data structure demo

# Class for binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



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

    # Create a binary tree









if __name__=='__main__':
    main()




