#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit()

def get_name(s):
    if s == 'r': return "Rock"
    elif s == 'p': return "Paper"
    elif s == 's': return "Scissors"
    elif s == 'l': return "Lizard"
    elif s == 'x': return "Spock"
    else: return "ERROR"

def get_reason(s):
    if s == "sp": return "Scissors cuts Paper"
    elif s =="pr": return "Paper covers Rock"
    elif s == "rl": return "Rock crushes Lizard"
    elif s == "lx": return "Lizard poisons Spock"
    elif s == "xs": return "Spock smashes Scissors"
    elif s == "sl": return "Scissors decapitates Lizard"
    elif s == "lp": return "Lizard eats Paper"
    elif s == "px": return "Paper disproves Spock"
    elif s == "xr": return "Spock vaporizes Rock"
    elif s == "rs": return "As it always has, Rock crushes Scissors."
    elif s == 'rr': return "It's a tie."
    elif s == 'pp': return "It's a tie."
    elif s == 'ss': return "It's a tie."
    elif s == 'll': return "It's a tie."
    elif s == 'xx': return "It's a tie."
    else: return "ERROR"

winners = ["rs", "pr", "sp", "rl", "lx", "xs", "sl", "lp", "px", "xr"]
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1+player2 in winners: return 1
    else: return 2

def testWinner(player1, player2, expected):
    ### Here we're getting the names of the player's choices
    ### and the reason for the win or loss
    actual = winner(player1, player2)
    name1 = get_name(player1)
    name2 = get_name(player2)
    reason = get_reason(player1 + player2)
    if reason == "ERROR": reason = get_reason(player2 + player1) ### reverse this if player1 loses
    if actual == expected: 
        print(f"correct: {name1} v. {name2} should give '{reason}' and it does.")
    else: 
        die(f"wrong: {name1} v. {name2} should give '{reason}' but didn't - your function is broken")

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