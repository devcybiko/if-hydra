#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit()

winners = ["rs", "pr", "sp", "rl", "lx", "xs", "sl", "lp", "px", "xr"]
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1+player2 in winners: return 1
    else: return 2

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