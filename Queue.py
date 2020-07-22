from collections import deque


class Queuuuu:
    def __init__(self):
        self.buffer = deque()

    def enqeueu(self, value):
        self.buffer.insert(0, value)
        print(self.buffer)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


q = Queuuuu()
q.enqeueu({'Name': 'Ketan Kulkarni',
           'Age': 29})
q.enqeueu({'Name': 'Aasawari Kulkarni',
           'Age': 29})
q.enqeueu({'Name': 'Rachit Kulkarni',
           'Age': 1.2})
