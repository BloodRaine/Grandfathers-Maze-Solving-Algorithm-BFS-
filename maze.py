#!/usr/local/bin/python3

from collections import deque

# Container Object, each edge is stored in a hash map as as (start,end):(color, type, [Adjacency List])
Maze = {}

#Read in first line from file, that first line is not used in this program so nothing is done with it
text_file = open("input.txt", "r")
text_file.readline()

# For each subsequent line, create one forward traveling and one backwards traveling "node" representing each edge in the Maze
for line in text_file:
    start, end, color, typ = line.split()
    Maze[(start,end)] = (color, typ, [])
    Maze[(end,start)] = (color, typ, [])

# Check start and end nodes and link together adjacent nodes
for key, value in Maze.items():
    for k, v in Maze.items():
       if ((key[1] == k[0]) and (key[0] != k[1]) and (value[0] == v[0] or value[1] == v[1])):
           value[2].append(k)

#Bredth First Search
S = set()
Q = deque([]) # to be used as a queue

root = ('A','B')
goal = ('i','j')

#add root to set and queue
S.add(root)
Q.append(root)

#Backtrace dictionary stored as (child):(parent)
Backtrace = {}
Backtrace[root] = None

while Q:
    current = Q.popleft()
    if current == goal:
        break
    val = Maze[current]
    for n in val[2]:
        if n not in S:
            S.add(n)
            Backtrace[n] = current
            Q.append(n)

#Backtrace to build path
path = []
path.append(goal)
node = goal
while current != root:
    current = Backtrace[node]
    path.append(current)
    node = current

print("The path through the maze takes", len(path), "steps and follows the path :", path[::-1])

