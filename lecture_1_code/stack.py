class Stack:
    def __init__(self):
        self.top = -1
        self.data = []

    def push(self, value):
        self.data.append(0) # increase size of stack
        self.top += 1 # move top pointer to the new top of the stack
        self.data[self.top] = value # assign the value to the new top of the stack

    def pop(self):
        if self.isEmpty():
            print("Stack is empty, cannot pop.")
            return None
        value = self.data[self.top] # read value at top
        del self.data[self.top] # remove top value
        self.top -= 1 # move top pointer down
        return value # return the popped value
    
    def isEmpty(self):
        return self.top == -1
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty, cannot peek.")
            return None
        return self.data[self.top]

    def print(self):
        print(self.top)
        print(self.data)

    # since stack is LIFO, popping elements and pushing them to another stack will reverse the order of the elements
    def invert(self):
        temp1 = Stack()
        temp2 = Stack()

        while not self.isEmpty():
            temp1.push(self.pop())

        while not temp1.isEmpty():
            temp2.push(temp1.pop())

        while not temp2.isEmpty():
            self.push(temp2.pop())