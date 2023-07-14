#!/usr/bin/env node

function fizzbuzz(n) {
    let fizz = n % 3 === 0 ? "Fizz" : "";
    let buzz = n % 5 === 0 ? "Buzz" : "";
    return fizz+buzz || n; // takes advantage of the 'falsey' nature of the empty string
}

function fizzbuzz_rules(n) {
    if (n % 15 === 0) return "FizzBuzz";
    if (n % 3 === 0) return "Fizz";
    if (n % 5 === 0) return "Buzz";
    return n;
}

function die(msg) {
    const process = require('process');
    console.log("\n", msg, "\n");
    process.exit(1);
}

function testFizzBuzz(n, expected) {
    let actual = ""+ fizzbuzz(n); // idiomatic expression that converts a number to a string
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