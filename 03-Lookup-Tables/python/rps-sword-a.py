#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit(1)

winners = [
    [ 0, 2, 1], #r
    [ 1, 0, 2], #p
    [ 2, 1, 0] #s
]

convert = {"r": 0, "p": 1, "s": 2}
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
    testWinner("p", "r", 1)
    testWinner("p", "p", 0)
    testWinner("p", "s", 2)
    testWinner("s", "r", 2)
    testWinner("s", "p", 1)
    testWinner("s", "s", 0)

main()