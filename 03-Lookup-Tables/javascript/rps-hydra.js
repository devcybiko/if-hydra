#!/usr/bin/env node
const process = require("process");

function die(msg) {
    console.log("\n", msg, "\n")
    process.exit(1)
}

function winner(player1, player2) {
    // returns 1 if player one wins
    // returns 2 if player two wins
    // returns 0 if it's a tie
    if (player1 === player2) return 0 // tie "guard";
    if (player1 === "r" && player2 === "s") return 1;
    else if (player1 === "p" && player2 === "r") return 1;
    else if (player1 === "s" && player2 === "p") return 1;
    else return 2;
}

function winner_naive(player1, player2) {
    if (player1 === "r") {
        if (player2 === "r") return 0;
        else if (player2 === "p") return 2;
        else if (player2 === "s") return 1;
        else die("invalid value for player 2: " + player2);
    } else if (player1 === "p") {
        if (player2 === "r") return 1;
        else if (player2 === "p") return 0;
        else if (player2 === "s") return 2;
        else die("invalid value for player 2: " + player2);
    } else if (player1 === "s") {
        if (player2 === "r") return 2;
        else if (player2 === "p") return 1;
        else if (player2 === "s") return 0;
        else die("invalid value for player 2: " + player2);
    } else die("invalid value for player 2: " + player2);
}

function testWinner(player1, player2, expected) {
    actual = winner(player1, player2)
    if (actual === expected) console.log(`correct: ${player1} v. ${player2} should give ${expected} and it does.`);
    else die(`wrong: ${player1} v. ${player2} should give ${expected} but it gave ${actual} - your function is broken`);
}

function main() {
    testWinner("r", "r", 0);
    testWinner("r", "p", 2);
    testWinner("r", "s", 1);
    testWinner("p", "r", 1);
    testWinner("p", "p", 0);
    testWinner("p", "s", 2);
    testWinner("s", "r", 2);
    testWinner("s", "p", 1);
    testWinner("s", "s", 0);
}

main();