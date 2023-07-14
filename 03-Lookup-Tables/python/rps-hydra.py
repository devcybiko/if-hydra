#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit(1)

def winner(player1, player2):
    """ 
    returns 1 if player one wins
    returns 2 if player two wins
    returns 0 if it's a tie
    """
    if player1 == player2: return 0 ### tie "guard"
    if player1 == "r" and player2 == "s": return 1
    elif player1 == "p" and player2 == "r": return 1
    elif player1 == "s" and player2 == "p": return 1
    else: return 2

def winner_naive(player1, player2):
    if player1 == "r":
        if player2 == "r": return 0
        elif player2 == "p": return 2
        elif player2 == "s": return 1
        else: die("invalid value for player 2: " + player2)
    elif player1 == "p": 
        if player2 == "r": return 1
        elif player2 == "p": return 0
        elif player2 == "s": return 2
        else: die("invalid value for player 2: " + player2)
    elif player1 == "s":
        if player2 == "r": return 2
        elif player2 == "p": return 1
        elif player2 == "s": return 0
        else: die("invalid value for player 2: " + player2)
    else: die("invalid value for player 2: " + player2)

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