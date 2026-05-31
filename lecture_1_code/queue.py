class Queue:
    def __init__(self):
        self.rear = -1
        self.data = []

    def enqueue(self, value):
        self.data.append(value) # extend size and add value to end of queue
        self.rear += 1 # move rear pointer to the new rear of the queue

    def dequeue(self):
        value = self.data[0] # read value at front of queue
        del self.data[0] # remove front value
        self.rear -= 1 # move rear pointer down
        return value # return the dequeued value
    
    def peek(self):
        return self.data[0]
    
    def isEmpty(self):
        return self.rear == -1

    def print(self):
        print(self.rear)
        print(self.data)
