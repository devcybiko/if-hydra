#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit()

names = {
    "r": "Rock", 
    "p": "Paper", 
    "s": "Scissors", 
    "l": "Lizard", 
    "x": "Spock"
}
reasons = { 
    "sp": "Scissors cuts Paper",
    "pr": "Paper covers Rock", 
    "rl": "Rock crushes Lizard", 
    "lx": "Lizard poisons Spock", 
    "xs": "Spock smashes Scissors", 
    "sl": "Scissors decapitates Lizard",
    "lp": "Lizard eats Paper", 
    "px": "Paper disproves Spock",
    "xr": "Spock vaporizes Rock",
    "rs": "As it always has, Rock crushes Scissors.",
    "ps": "Scissors cuts Paper",
    "rp": "Paper covers Rock", 
    "lr": "Rock crushes Lizard", 
    "xl": "Lizard poisons Spock", 
    "sx": "Spock smashes Scissors", 
    "ls": "Scissors decapitates Lizard",
    "pl": "Lizard eats Paper", 
    "xp": "Paper disproves Spock",
    "rx": "Spock vaporizes Rock",
    "sr": "As it always has, Rock crushes Scissors.",
    "rr": "It's a tie",
    "ss": "It's a tie",
    "pp": "It's a tie",
    "ll": "It's a tie",
    "xx": "It's a tie"
}

winners = ["rs", "pr", "sp", "rl", "lx", "xs", "sl", "lp", "px", "xr"]
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1+player2 in winners: return 1
    else: return 2

def testWinner(player1, player2, expected):
    ### Here we're getting the names of the player's choices
    ### and the reason for the win or loss
    actual = winner(player1, player2)
    name1 = names[player1]
    name2 = names[player2]
    reason = reasons[player1 + player2]
    if actual == expected: 
        print(f"correct: {name1} v. {name2} should give '{reason}' and it does.")
    else: 
        die(f"wrong: {name1} v. {name2} should give '{expected}' but gave '{actual}' - your function is broken")

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