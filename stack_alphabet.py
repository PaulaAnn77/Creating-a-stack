# Paula Farebrother
# Created: July 2024
# Last modified: Oct 2024
# _________________________________
#  Creating a reverse filled stack with an array using capital letters of the
#  alphabel and pop() and chr()
# __________________________________

def push(x):
    global top
    if top >= size -1:
        print("Stack Overflow")
    else:
        top = top + 1
        data[top] = x

def pop():
    global top
    if top == -1:
        print("Stack underflow")
    else:
        top = top - 1
        return data[top+1]

def peek():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print(data[top])

size = 26
data = [0]*(size)
list = list(range(65, 91))
top = -1

for i in list:
    push(i)

print(data[0 : top + 1])
peek()

for i in data:
    char = pop()
    print(chr(char))
