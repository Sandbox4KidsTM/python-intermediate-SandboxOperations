class My_Stack():

    def __init__(self):
        # Create an empty Stack, we will be using a private list
        self._stack = []
        pass

    def __repr__(self):
        # Return a string of the stack, top to bottom, seperated by comments
        return ", ".join(str(x) for x in reversed(self._stack))

    def push(self, element):
        # Adds an element to the top of the stack.
        self._stack.append(element)

    def pop(self):
        # Removes and returns the element at the top of the stack
        return self._stack.pop(-1)

    def peek(self):
        # Take a look at the top of the stack (return that element but do not remove it)
        return self._stack[-1]
