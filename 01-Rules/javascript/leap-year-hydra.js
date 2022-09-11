#!/usr/bin/env node
const process = require('process');

function isLeapyear(year) {
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                return true;
            } else {
                return false;
            }
        } else {
            return true;
        }
    } else {
        return false;
    }
}

function testIsLeapyear(year, expected) {
    result = expected ? "should be a leap year" : "should not be a leap year";
    if (isLeapyear(year) === expected) {
        console.log(`correct: ${year} ${result}, as expected`);
    }else {
        console.log(`\nwrong: ${year} ${result} - your function reported otherwise\n`);
        process.exit()
    }
}

function main() {
    // the turn of the 20th century
    testIsLeapyear(1896, true)
    testIsLeapyear(1897, false)
    testIsLeapyear(1898, false)
    testIsLeapyear(1899, false)
    testIsLeapyear(1900, false)
    testIsLeapyear(1901, false)
    testIsLeapyear(1902, false)
    testIsLeapyear(1903, false)
    testIsLeapyear(1904, true)

    // the turn of the 21st century
    testIsLeapyear(1996, true)
    testIsLeapyear(1997, false)
    testIsLeapyear(1998, false)
    testIsLeapyear(1999, false)
    testIsLeapyear(2000, true)
    testIsLeapyear(2001, false)
    testIsLeapyear(2002, false)
    testIsLeapyear(2003, false)
    testIsLeapyear(2004, true)
}

main()