#!/usr/bin/env python

def fizzbuzz(n):
    if n % 3 == 0:
        if n % 5 == 0:
            return "FizzBuzz"
        else: return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n

def die(msg):
    print("\n", msg, "\n")
    exit(1)

def testFizzBuzz(n, expected):
    actual = str(fizzbuzz(n)) # convert it to a string
    if (actual == expected): print(f"correct: {n} should say {expected} and it does.")
    else: die(f"wrong: {n} should say {expected} but it said {actual} - your def is broken")

def main():
    testFizzBuzz(1, "1")
    testFizzBuzz(2, "2")
    testFizzBuzz(3, "Fizz")
    testFizzBuzz(4, "4")
    testFizzBuzz(5, "Buzz")
    testFizzBuzz(6, "Fizz")
    testFizzBuzz(7, "7")
    testFizzBuzz(8, "8")
    testFizzBuzz(9, "Fizz")
    testFizzBuzz(10, "Buzz")
    testFizzBuzz(11, "11")
    testFizzBuzz(12, "Fizz")
    testFizzBuzz(13, "13")
    testFizzBuzz(14, "14")
    testFizzBuzz(15, "FizzBuzz")

main()