#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit(1)

winners = [
    [ 0, 2, 1, 1, 2], #r
    [ 1, 0, 2, 2, 1], #p
    [ 2, 1, 0, 1, 2], #s
    [ 2, 1, 2, 0, 1], #l
    [ 1, 2, 1, 2, 0], #x
]

convert = {"r": 0, "p": 1, "s": 2, "l": 3, "x": 4}
def winner(player1, player2):
    p1 = convert[player1]
    p2 = convert[player2]
    return winners[p1][p2]

def testWinner(player1, player2, expected):
    actual = winner(player1, player2)
    if actual == expected: print(f"correct: {player1} v. {player2} should give {expected} and it does.")
    else: die(f"wrong: {player1} v. {player2} should give {expected} but it gave {actual} - your function is broken")

def main():
    testWinner("r", "r", 0)
    testWinner("r", "p", 2)
    testWinner("r", "s", 1)
    testWinner("r", "l", 1)
    testWinner("r", "x", 2)
    testWinner("p", "r", 1)
    testWinner("p", "p", 0)
    testWinner("p", "s", 2)
    testWinner("p", "l", 2)
    testWinner("p", "x", 1)
    testWinner("s", "r", 2)
    testWinner("s", "p", 1)
    testWinner("s", "s", 0)
    testWinner("s", "l", 1)
    testWinner("s", "x", 2)
    testWinner("l", "r", 2)
    testWinner("l", "p", 1)
    testWinner("l", "s", 2)
    testWinner("l", "l", 0)
    testWinner("l", "x", 1)
    testWinner("x", "r", 1)
    testWinner("x", "p", 2)
    testWinner("x", "s", 1)
    testWinner("x", "l", 2)
    testWinner("x", "x", 0)

main()