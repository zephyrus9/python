# -*-coding: utf-8 -*-
# Author: 


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.isEmpty())
    q.enqueue(4.9)
    print([s for s in q])
    print(q.dequeue())
