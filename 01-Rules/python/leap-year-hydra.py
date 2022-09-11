#!/usr/bin/env python

def is_leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def test_is_leapyear(year, expected):
    result = "should be a leap year" if expected else "should not be a leap year"
    if is_leapyear(year) == expected:
        print(f"correct: {year} {result}, as expected");
    else:
        print(f"\nwrong: {year} {result} - your function reported otherwise\n")
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