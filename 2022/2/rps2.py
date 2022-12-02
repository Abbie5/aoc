#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

moves = {
    "A": 1,
    "B": 2,
    "C": 3
}

outcomes = {
    "X": 0, #lose
    "Y": 3, #draw
    "Z": 6  #win
}

lose = {
    "A": "B", # paper wins against rock
    "B": "C", # scissors wins agains paper
    "C": "A"  # rock wins agains scissors
}

win = {
    "A": "C", # paper wins against rock
    "B": "A", # scissors wins agains paper
    "C": "B"  # rock wins agains scissors
}


total = 0
for line in lines:
    print(line)
    outcome = line[2]
    you = line[0]

    me = None
    if outcome == "Y": #draw
        me = you
    elif outcome == "X": #i win
        me = win[you]
    elif outcome == "Z": #i lose
        me = lose[you]

    print(me)
    total += moves[me]
    total += outcomes[outcome]

print(total)
