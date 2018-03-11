# -*-coding: utf-8 -*-
# Author: 
from graphs.Graph import Graph
from graphs.Vertex import Vertex
from myQueue import Queue

def bfs(g, start):
    start.setDisatance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDisatance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('balck')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertex('sage'))