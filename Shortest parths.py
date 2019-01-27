from intersection import Intersection
from block import Block
from floormap1 import blocklst, intersectionlst
import queue as Queue
from collections import defaultdict


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

        # for inserting an element in the queue

    def insert(self, vertex,weight):
        self.queue.append([vertex,weight])

        # for popping an element based on Priority

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



def dijsktra(A,start):
    dist =[]
    prev =[]
    for i in range(len(A)):
        dist.append(1000000)
        prev.append("null")
    dist[start] = 0
    Q = PriorityQueue()
    for v in range(len(A)):
        Q.insert(v,dist[v])
    while not Q.isEmpty():
        w = Q.delete()
        for edge in A[w[0]]:
            if type(edge) != int:
                tmp = dist[w[0]] + edge[1]
                if tmp < dist[edge[0]]:
                    dist[edge[0]] = tmp
                    prev[edge[0]] = w[0]
    return dist , prev


Adjlst = []
n = (len(intersectionlst))
for k in range(n):
    Adjlst.append([k])
edgelst = []
intersectionnode = []
for inter in intersectionlst:
    intersectionnode.append([inter,inter.all_blocks])
for v in range(len(intersectionnode)):
    for block1 in intersectionnode[v][1]:
        for j in range(len(intersectionnode)):
            for block2 in intersectionnode[j][1]:
                if block1.A[0] == block2.A[0] and j != v and block1.A[1] == block2.A[1]:
                    if block1.A[1]-block1.B[1] != 0:
                        edgelst.append([j,v,abs(block1.A[1]-block1.B[1])])
                        edgelst.append([v,j,abs(block2.A[1]-block2.B[1])])
                    else:
                        edgelst.append([j, v, abs(block1.A[0] - block1.B[0])])
                        edgelst.append([v, j, abs(block2.A[0] - block2.B[0])])

for edge in edgelst:
    Adjlst[edge[0]].append([edge[1],edge[2]])


# exit in floor 1 is intercation beghimno
# the representative number is 2,5,7,8,9,13,14,15
# we need to do minus 1 because the list begins with 0
exitlst = [1,4,6,7,8,12,13,14]
dist2,prev2= dijsktra(Adjlst,1)
dist5,prev5= dijsktra(Adjlst,4)
dist7,prev7= dijsktra(Adjlst,6)
dist8,prev8= dijsktra(Adjlst,7)
dist9,prev9= dijsktra(Adjlst,8)
dist14,prev14= dijsktra(Adjlst,12)
dist15,prev15= dijsktra(Adjlst,13)
dist16,prev16= dijsktra(Adjlst,14)
distlst = [dist2,dist5,dist7,dist9,dist14,dist15,dist16]
prevlst = [prev2,prev5,prev7,prev9,prev14,prev15,prev16]

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
            finallst[k] = [mini,minipath]
total = [] # total is the path to the exit for each intersection
for num in range(n):
    lst = []
    path = finallst[num][1]
    start = num
    while start not in exitlst:
        start = path[start]
        lst.append(start)
    total.append(lst)
print(total)