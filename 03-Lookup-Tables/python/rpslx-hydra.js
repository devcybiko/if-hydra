#!/usr/bin/env node
const process = require("process");

function die(msg) {
    console.log("\n", msg, "\n")
    process.exit();
}

function winner(player1, player2) {
    // returns 1 if player one wins
    // returns 2 if player two wins
    // returns 0 if it's a tie
    if (player1 === player2) return 0 // tie "guard";
    if (player1 === "r" && player2 === "s") return 1;
    else if (player1 === "r" && player2 === "l") return 1;
    else if (player1 === "p" && player2 === "r") return 1;
    else if (player1 === "p" && player2 === "x") return 1;
    else if (player1 === "s" && player2 === "p") return 1;
    else if (player1 === "s" && player2 === "l") return 1;
    else if (player1 === "l" && player2 === "x") return 1;
    else if (player1 === "l" && player2 === "p") return 1;
    else if (player1 === "x" && player2 === "s") return 1;
    else if (player1 === "x" && player2 === "r") return 1;
    else  return 2;
}

function winner_naive(player1, player2) {
    // returns 1 if player one wins
    // returns 2 if player two wins
    // returns 0 if it's a tie
    if (player1 === "r") {
        if (player2 === "r") return 0;
        else if (player2 === "p") return 2;
        else if (player2 === "s") return 1;
        else if (player2 === "l") return 1;
        else if (player2 === "x") return 2;
        else  die("invalid value for player 2: " + player2);
    } else if (player1 === "p") {
        if (player2 === "r") return 1;
        else if (player2 === "p") return 0;
        else if (player2 === "s") return 2;
        else if (player2 === "l") return 2;
        else if (player2 === "x") return 1;
        else  die("invalid value for player 2: " + player2);
    } else if (player1 === "s") {
        if (player2 === "r") return 2;
        else if (player2 === "p") return 1;
        else if (player2 === "s") return 0;
        else if (player2 === "l") return 1;
        else if (player2 === "x") return 2;
        else  die("invalid value for player 2: " + player2);
    } else if (player1 === "l") {
        if (player2 === "r") return 2;
        else if (player2 === "p") return 1;
        else if (player2 === "s") return 2;
        else if (player2 === "l") return 0;
        else if (player2 === "x") return 1;
        else  die("invalid value for player 2: " + player2);
    } else if (player1 === "x") {
        if (player2 === "r") return 1;
        else if (player2 === "p") return 2;
        else if (player2 === "s") return 1;
        else if (player2 === "l") return 2;
        else if (player2 === "x") return 0;
        else  die("invalid value for player 2: " + player2);
    } else  die("invalid value for player 2: " + player2);

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

main();
