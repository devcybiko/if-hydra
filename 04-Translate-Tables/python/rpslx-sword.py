#!/usr/bin/env python

def die(msg):
    print("\n", msg, "\n")
    exit()

name_keys = ["r", "p", "s", "l", "x"]
name_values = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
reason_keys = ["sp", "pr", "rl", "lx", "xs", "sl", "lp","px", "xr", "rr", "pp", "ss", "ll", "xx"]
reason_values = [
    "Scissors cuts Paper",
    "Paper covers Rock",
    "Rock crushes Lizard",
    "Lizard poisons Spock",
    "Spock smashes Scissors",
    "Scissors decapitates Lizard",
    "Lizard eats Paper",
    "Paper disproves Spock",
    "Spock vaporizes Rock",
    "As it always has, Rock crushes Scissors.",
    "It's a tie",
    "It's a tie",
    "It's a tie",
    "It's a tie",
    "It's a tie"    
]

def lookup_range(key, keys, values):
    # this is the 'hard' way. iterate over all the keys until you find the one you want
    for i in range(0, len(keys)):
        if keys[i] == key: break ### get out when we find the key
    value = values[i] ### return the corresponding value
    return value

def lookup(key, keys, values):
    if key in keys:
        i = keys.index(key) ### find the position of the key in the keys
        value = values[i] ### return the corresponding value
    else:
        value = "ERROR"
    return value

winners = ["rs", "pr", "sp", "rl", "lx", "xs", "sl", "lp", "px", "xr"]
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1+player2 in winners: return 1
    else: return 2

def testWinner(player1, player2, expected):
    ### Here we're getting the names of the player's choices
    ### and the reason for the win or loss
    actual = winner(player1, player2)
    name1 = lookup(player1, name_keys, name_values)
    name2 = lookup(player2, name_keys, name_values)
    reason = lookup(player1 + player2, reason_keys, reason_values)
    if reason == "ERROR": 
        reason = lookup(player2 + player1, reason_keys, reason_values) ### reverse this if player1 loses
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