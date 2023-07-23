"""
    Practicing Stacks
"""


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, new_val):
        if new_val not in self.stack:
            self.stack.append(new_val)
            return True

        return False

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            #No elements at the top of stack
            return None

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

        print("No elements in the stack")


stack = Stack()

stack.push("Monday")
stack.push("Tuesday")
print(f"Last element at the top of stack is {stack.peek()} ")
stack.push("Wednesday")
stack.push("Thursday")

print(f"Last element out from Stack is {stack.pop()}")

print("Lets go to pop all the elements in the stack")


while stack.peek():
    print(f"Poping element = {stack.pop()}")

print(f"Now the stack has {stack.peek()}")