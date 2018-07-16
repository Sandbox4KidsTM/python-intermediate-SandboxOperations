# -*- coding: utf-8 -*-

## Stacks - Stacks are a LIFO data structure. (Last In, First Out)
# Lets impletment a Stack using a list

class My_Stack():
    def __init__(self):
        self._stack = []
        
    def __repr__(self):
        return ", ".join(str(x) for x in reversed(self._stack))
        
    def push(self, item):
        self._stack.append(item)
    
    def pop(self):
        return self._stack.pop()
    
    def peek(self):
        return self._stack[-1]
    
stack = My_Stack()
stack.push(145)
stack.push("Red")
stack.push("Green")
stack.push("Blue")
print(stack)

print(stack.peek() == "Blue")
print(stack.pop() == "Blue")
print(stack)