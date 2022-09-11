#!/usr/bin/env node
const process = require("process");

function die(msg) {
    console.log("\n", msg, "\n")
    process.exit();
}

winners = ["rs", "pr", "sp"]
function winner(player1, player2) {
    if (player1 === player2) return 0; // tie "guard"
    if (winners.includes(player1+player2)) return 1;
    else  return 2;
}

function testWinner(player1, player2, expected) {
    actual = winner(player1, player2)
    if (actual === expected) console.log(`correct: ${player1} v. ${player2} should give ${expected} and it does.`);
    else  die(`wrong: ${player1} v. ${player2} should give ${expected} but it gave ${actual} - your function is broken`);
}

function main() {
    testWinner("r", "r", 0)
    testWinner("r", "p", 2)
    testWinner("r", "s", 1)
    testWinner("p", "r", 1)
    testWinner("p", "p", 0)
    testWinner("p", "s", 2)
    testWinner("s", "r", 2)
    testWinner("s", "p", 1)
    testWinner("s", "s", 0)
}

main()