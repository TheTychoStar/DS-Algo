# This is a py class for list demo
print('This is a first python demo file')

class listObj:
    # create a new list called my list
    mylist = ["apple", "banana", "cherry"]
    print ("My list is", mylist)

    # create a dictionary
    mydict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
            }

    print('My dictionary is', mydict)

# create a new stack
class stack:
    # create a new stack
    def __init__(self):
        self.stack=[]
        #print("my stack is ", self.stack)

    # use list append method to add element in stack
    def add_elemens(self, weekday):
        if weekday not in self.stack:
            self.stack.append(weekday)
            return True
        else:
            return False

    # Use peek to check the top element in stack
    def peek(self):
        return self.stack(-1)

# create a tree class
class tree:
    def __init__(self, key):
        self.left=None
        self.right = None
        self.val=key

    


# create a main function to call above method and class
def main():
    print("This is main function")
    mystack = stack()
    mystack.add_elemens('Mon')

    print(mystack.peek)

if __name__=='__main__':
    main()




