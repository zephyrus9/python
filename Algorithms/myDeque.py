# -*-coding: utf-8 -*-
# Author: 

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':

    # 判断是否为回文
    def palchecker(aString):
        chardeuqe = Deque()
        for ch in aString:
            chardeuqe.addRear(ch)
        stillEqual = True

        while chardeuqe.size() > 1 and stillEqual:
            first = chardeuqe.removeFront()
            last = chardeuqe.removeRear()
            if first != last:
                stillEqual = False

        return stillEqual

print(palchecker('TOPPOT'))

