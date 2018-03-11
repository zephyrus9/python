# -*-coding: utf-8 -*-
# Author:


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # 创建空字典

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.getConnectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connetedTo[nbr]
