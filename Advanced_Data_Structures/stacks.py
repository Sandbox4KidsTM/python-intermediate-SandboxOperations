class My_Stack():

    def __init__(self):
        # Create an empty Stack, we will be using a private list
        pass

    def __repr__(self):
        # Return a string of the stack, top to bottom, seperated by comments
        return ", ".join(str(x) for x in reversed(self._stack)

    def push(self, element):
        # Adds an element to the top of the stack.
        pass

    def pop(self):
        # Removes and returns the element at the top of the stack
        pass

    def peek(self):
        # Take a look at the top of the stack (return that element but do not remove it)
        pass
