class My_Queue():
    def __init__(self):
        self._queue = []

    def __repr__(self):
        return ", ".join(str(x) for x in self._queue)

    def push(self, value):
        self._queue.insert(0, value)

    def pop(self):
        return self._queue.pop()

    def peek(self):
        return self._queue[-1]

q = My_Queue()
q.push("Mike")
q.push("Bob")
q.push("Dan")
q.push("Hannah")

next_person = q.peek()
print("Next person in line is", next_person)
print("I am going to help the next person in line")
q.pop()
print(q)