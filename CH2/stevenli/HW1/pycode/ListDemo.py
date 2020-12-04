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


# create a tree class
class tree:
    def __init__(self, key):
        self.left=None
        self.right = None
        self.val=key




# create a main function to call above method and class
def main():
    print("This is main function")




if __name__=='__main__':
    main()




