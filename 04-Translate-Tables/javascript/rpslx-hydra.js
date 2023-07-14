#!/usr/bin/env node
const process = require("process");

function die(msg) {
    console.log("\n", msg, "\n")
    process.exit(1);
}

function get_name(s) {
    if (s === 'r') return "Rock";
    else if (s === 'p') return "Paper";
    else if (s === 's') return "Scissors";
    else if (s === 'l') return "Lizard";
    else if (s === 'x') return "Spock";
    else  return "ERROR";
}

function get_reason(s) {
    if (s === "sp") return "Scissors cuts Paper";
    else if (s ==="pr") return "Paper covers Rock";
    else if (s === "rl") return "Rock crushes Lizard";
    else if (s === "lx") return "Lizard poisons Spock";
    else if (s === "xs") return "Spock smashes Scissors";
    else if (s === "sl") return "Scissors decapitates Lizard";
    else if (s === "lp") return "Lizard eats Paper";
    else if (s === "px") return "Paper disproves Spock";
    else if (s === "xr") return "Spock vaporizes Rock";
    else if (s === "rs") return "As it always has, Rock crushes Scissors.";
    else if (s === 'rr') return "It's a tie.";
    else if (s === 'pp') return "It's a tie.";
    else if (s === 'ss') return "It's a tie.";
    else if (s === 'll') return "It's a tie.";
    else if (s === 'xx') return "It's a tie.";
    else  return "ERROR";
}

let winners = ["rs", "pr", "sp", "rl", "lx", "xs", "sl", "lp", "px", "xr"]
function winner(player1, player2) {
    if (player1 === player2) return 0 // tie "guard";
    if (winners.includes(player1+player2)) return 1;
    else  return 2;
}

function testWinner(player1, player2, expected) {
    // Here we're getting the names of the player's choices
    // && the reason for the win || loss
    let actual = winner(player1, player2)
    let name1 = get_name(player1)
    let name2 = get_name(player2)
    let reason = get_reason(player1 + player2)
    if (reason === "ERROR") reason = get_reason(player2 + player1) // reverse this if player1 loses;
    if (actual === expected) {
        console.log(`correct: ${name1} v. ${name2} should give '${reason}' and it does.`)
    } else {
        die(`wrong: ${name1} v. ${name2} should give '${expected}' but gave '${actual}' - your function is broken`)
    }
}

function main() {
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
}

main()
