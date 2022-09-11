# Rule-based swords: Leap Year

The basic rules for leap year calculation are:

1. every year divisible by 4
1. but not century years
1. except those divisible by 400

## The Hydra

A classic way to write this is as a series of `if-else` statements that return a `true` or `false` result. 
This results in a complicated chain of rules that may not be obvious

```python
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
```

## The Sword: Rules and Boolean  Logic

An alternative is to use rules and Boolean logic . 

Each rule can be assigned to a single variable. This makes the rule logic much easier to understand.

```python
def is_leapyear(year):
    rule1 = year % 4 == 0
    rule2 = year % 100 == 0
    rule3 = year % 400 == 0
    return rule1 and not rule2 or rule3
```

Even easier is a single line that expresses all the rules in a single expression. (Note the use of parentheses to make the order of operations clear.)

```python
def is_leapyear(year):
    return (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0)
```

## The Moral

Collapsing an `if-hydra` into a series of rules expressed as a boolean expression can make the code much easier to understand and debug. Collapsing it further into a single expression makes for compact and expressive code. Be sure to use parentheses where necessary to ensure the terms are evaluated properly and to make the code easier to understand.
