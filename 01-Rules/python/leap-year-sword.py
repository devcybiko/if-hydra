#!/usr/bin/env python

def is_leapyear(year):
    return (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0)

def is_leapyear_rule_based(year):
    rule1 = year % 4 == 0
    rule2 = year % 100 == 0
    rule3 = year % 400 == 0
    return rule1 and not rule2 or rule3

def test_is_leapyear(year, expected):
    result = "is a leap year" if expected else "is not a leap year"
    if is_leapyear(year) == expected:
        print(f"correct: {year} {result}, as expected");
    else:
        print(f"\nwrong: {year} {result} - your function is broken\n")
        exit()

def main():
    #the turn of the 20th century
    test_is_leapyear(1896, True)
    test_is_leapyear(1897, False)
    test_is_leapyear(1898, False)
    test_is_leapyear(1899, False)
    test_is_leapyear(1900, False)
    test_is_leapyear(1901, False)
    test_is_leapyear(1902, False)
    test_is_leapyear(1903, False)
    test_is_leapyear(1904, True)

    # the turn of the 21st century
    test_is_leapyear(1996, True)
    test_is_leapyear(1997, False)
    test_is_leapyear(1998, False)
    test_is_leapyear(1999, False)
    test_is_leapyear(2000, True)
    test_is_leapyear(2001, False)
    test_is_leapyear(2002, False)
    test_is_leapyear(2003, False)
    test_is_leapyear(2004, True)

main()