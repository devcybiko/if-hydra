#!/usr/bin/env node

function fizzbuzz(n) {
    if (n % 3 === 0) {
        if (n % 5 === 0) {
            return "FizzBuzz";
        }
        else return "Fizz";
    } else {
        if (n % 5 === 0) {
            return "Buzz";
        }
    }
    return "" + n; // idiomatic expression that converts a number to a string
}

function die(msg) {
    const process = require('process');
    console.log("\n", msg, "\n");
    process.exit(1);
}

function testFizzBuzz(n, expected) {
    let actual = fizzbuzz(n);
    if (actual === expected) console.log(`correct: ${n} should say ${expected} and it does.`);
    else die(`wrong: ${n} should say ${expected} but it said ${actual} - your function is broken`)
}

function main() {
    testFizzBuzz(1, "1");
    testFizzBuzz(2, "2");
    testFizzBuzz(3, "Fizz");
    testFizzBuzz(4, "4");
    testFizzBuzz(5, "Buzz");
    testFizzBuzz(6, "Fizz");
    testFizzBuzz(7, "7");
    testFizzBuzz(8, "8");
    testFizzBuzz(9, "Fizz");
    testFizzBuzz(10, "Buzz");
    testFizzBuzz(11, "11");
    testFizzBuzz(12, "Fizz");
    testFizzBuzz(13, "13");
    testFizzBuzz(14, "14");
    testFizzBuzz(15, "FizzBuzz");
}

main();