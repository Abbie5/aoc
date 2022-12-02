#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.read().replace("A","X").replace("B","Y").replace("C","Z").splitlines()

moves = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


total = 0
for line in lines:
    me = line[2]
    you = line[0]
    total += moves[me]
    if me == you: #draw
        total += 3
    elif (me == "X" and you == "Z") or (me == "Y" and you == "X") or (me == "Z" and you == "Y"): #i win
        total += 6

print(total)
