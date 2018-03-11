# -*-coding: utf-8 -*-
# Author:

from myGraphs import Vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(t)
        if t not in self.vertList:
            nv = self.addVertex(t)
            self.vertList[f].addNeighbor(self.vertList[t], cost)

        def getVertices(self):
            return self.vertList.keys()

        def __iter__(self):
            return iter(self.vertList.values())

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)