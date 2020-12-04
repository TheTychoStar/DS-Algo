# create a new stack
class stack:
    # create a new stack
    def __init__(self):
        self.stack = []
        #print("my stack is ", self.stack)

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
