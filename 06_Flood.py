#!/usr/local/bin/python3.5

input='''4 5 2
100000 4 5 1 2
5 2 5 4 1
4 4 5 4 1
1 3 3 2 100000'''

result = "NO"
layer=input.split("\n")
w, l = int(layer[0].split(" ")[1]), int(layer[0].split(" ")[0])
blocks = [[0 for x in range(w)] for y in range(l)]
flooded = [[0 for x in range(w)] for y in range(l)]
flood = int(layer[0].split(" ")[2])

for lar in range(0, int(layer[0].split(' ')[0])):
        for lon in range(0, int(layer[0].split(' ')[1])):
                blocks[lar][lon] = layer[lar+1].split(" ")[lon]
lar, lon = 0, 0
option = 2
while option != 0:
