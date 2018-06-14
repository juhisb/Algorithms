import heapq
from collections import defaultdict


def encode(weight):
    heap = [[w, [symbol, '']] for symbol, w in weight.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


#data = "The frog at the bottom of the well drifts off into the great ocean"
f=open('huffman.txt','r')
x=f.readlines()
l=[]
n=int(x[0])
for line in x[1:] :
    l.append(int(line))
#print(l)
weight = defaultdict(int)
for i in range(n):
    weight[i] =l[i]

huff = encode(weight)
length=[]
#print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    length.append(len(p[1]))
print(max(length))
print(min(length))