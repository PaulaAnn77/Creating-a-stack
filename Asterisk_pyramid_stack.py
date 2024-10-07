# Paula Farebrother
# Created: 9th July 2024
# Last modified: Oct 2024
# _________________________________
#  Creating an asterisk pyramid
# __________________________________

class Pyramid:
    def __init__(self, size):
        self.size = size + 1
        self.data = [0] * (self.size)
        self.top = -1

    def push(self, x):
        if self.top >= self.size - 1:
            print("Stack Overflow")
        else:
            self.top = self.top + 1
            self.data[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            self.top = self.top - 1
            return self.data[self.top+1]

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(self.data[self.top])

    def isEmpty(self):
        if self.top == -1:
            print("Stack is empty")

    def isFull(self):
        if self.top == self.size - 1:
            print("List is full")

    def show(self):
        print(pyramid.data[0: pyramid.top + 1])

    def getTriangle(self):
        """ creates a triangle made from asterisks """
        # need to adapt from range() to stack
        for i in range(1, self.size):
            # using formula (2n-1)
            row = (((" " * (self.size - i)) + ("*" * (2 * i - 1))))
            print(row)  # optional print function, remove to only show
            # reverse when called
            self.push(row)

    def iter(self):
        while self.top != -1:
            row = self.pop()
            print(row)


pyramid = Pyramid(12)


pyramid.getTriangle()
print()
print("This is the top of the stack now: ")
pyramid.peek()
print()

print()
print("Reverse pyramid using pop() and print: ")
pyramid.iter()
