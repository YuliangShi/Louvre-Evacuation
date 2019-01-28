from intersection import Intersection
from block import Block
from floormap import blocklst, intersectionlst
import queue as Queue
from collections import defaultdict
import bintrees




class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

        # for inserting an element in the queue

    def insert(self, vertex, weight):
        self.queue.append([vertex, weight])

        # for popping an element based on Priority

    def update(self,vertex,prevweight,newweight):
        for var in range(len(self.queue)):
            if self.queue[var] == [vertex,prevweight]:
                del self.queue[var]
                self.queue.append([vertex,newweight])

    def delete(self):
        try:
            mini = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] < self.queue[mini][1]:
                    mini = i
            item = self.queue[mini]
            del self.queue[mini]
            return item
        except IndexError:
            print()
            exit()



def dijsktra(A, start, intersectionlist):
    dist = []
    prev = []
    for i in range(len(A)):
        dist.append(10000)
        prev.append("null")
    dist[start] = 0
    Q = PriorityQueue()
    for v in range(len(A)):
        Q.insert(v,dist[v])
    while not Q.isEmpty():
        w = Q.delete()
        for edge in A[w[0]]:
            #print(edge)
            if type(edge) == list:
                #print(edge)
                tmp = dist[w[0]] + edge[1] + intersectionlist[edge[0]].length * 1/2
                if tmp < dist[edge[0]]:
                    Q.update(edge[0],dist[edge[0]],tmp)
                    dist[edge[0]] = tmp
                    prev[edge[0]] = w[0]
    return dist, prev


def makeadjlst(intersectionlist):
    Adjlst = []
    n = len(intersectionlist)
    for k in range(n):
        Adjlst.append([k])
    edgelst = []
    intersectionnode = []
    for inter in intersectionlist:
        intersectionnode.append([inter, inter.all_blocks])


# This is where to calculate wedges for each edge
# normal edge length is the length of the block
# the stair's length will * 2 as stair is more dangerous for too many people
    for v in range(len(intersectionnode)):
        for block1 in intersectionnode[v][1]:
            for j in range(len(intersectionnode)):
                for block2 in intersectionnode[j][1]:
                    if block1.A[0] == block2.A[0] and j != v and block1.A[1] == block2.A[1] and block1.B[0] == block2.B[0] and block1.B[1] == block2.B[1] and block1.A[2] == block2.A[2] and block1.B[2] == block2.B[2]:
                        if block1.floor == 1 or block1.floor == 0 or block1.floor == -1:
                            if block1.A[1] - block1.B[1] != 0:
                                edgelst.append([j, v, abs(block1.A[1] - block1.B[1])])
                            else:
                                edgelst.append([j, v, abs(block1.A[0] - block1.B[0])])
                        else:
                            if block1.A[1] - block1.B[1] != 0:
                                edgelst.append([j, v, abs(block1.A[1] - block1.B[1]) * 2])
                            else:
                                edgelst.append([j, v, abs(block1.A[0] - block1.B[0]) * 2])

    for edge in edgelst:
        Adjlst[edge[0]].append([edge[1], edge[2]])
    return Adjlst


# exit is intersection 0,9 14,30,34
Adjlst = makeadjlst(intersectionlst)
exitlst = [0,9,14,30,34]
distlst = []
prevlst = []
for num in exitlst:
    dist, prev = dijsktra(Adjlst, num, intersectionlst)
    distlst.append(dist)
    prevlst.append(prev)
# print(prevlst[0])
# dist0,prev0= dijsktra(Adjlst,0)
# dist9,prev9= dijsktra(Adjlst,9)
# istlst = [dist0,dist9]
# prevlst = [prev0,prev9]
n = len(intersectionlst)
finallst = []
for s in range(n):
    finallst.append([])
for k in range(n):
    mini = distlst[0][k]
    minipath = prevlst[0]
    finallst[k] = [mini, minipath]
    for g in range(len(distlst)):
        if mini > distlst[g][k]:
            mini = distlst[g][k]
            minipath = prevlst[g]
            finallst[k] = [mini, minipath]
total = []  # total is the path to the exit for each intersection
for num in range(n):
    lst = []
    path = finallst[num][1]
    start = num
    while start not in exitlst:
        if start == "null":
            break
        else:
            lst.append(start)
            start = path[start]
    lst.append(start)
    total.append(lst)
print(total)
