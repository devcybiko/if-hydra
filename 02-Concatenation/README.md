# Concatenation Swords: Fizz Buzz

From [Wikipedia](https://en.wikipedia.org/wiki/Fizz_buzz):

> Fizz buzz is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", and any number divisible by five with the word "buzz".

> Fizz buzz has been used as an interview screening device for computer programmers. Writing a program to output the first 100 FizzBuzz numbers is a relatively trivial problem requiring little more than a loop and conditional statements. However, its value in coding interviews is to analyze fundamental coding habits that may be indicative of overall coding ingenuity.

> However, if the number is divisible by both three and five, then the program should print "FizzBuzz".

## The Hydra

A simple implementation of this program uses an `if-hydra` with division by 3 checked for no remainder first, then division by 5. Besides raising the specter of the Hydra, it also checks the division by 5 in two places - which defies the "[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)" rule.

```python
def fizzbuzz(n):
    if n % 3 == 0:
        if n % 5 == 0:
            return "FizzBuzz"
        else: return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n
```

## The Sword: Concatenation

One solution is the rule-based solution we saw in the leap year example: 

```python
def fizzbuzz_rules(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0: return "Fizz"
    if n % 5 == 0: return "Buzz"
    return n
```

This has the advantage of checking the division by both 3 and 5 by checking for a division by 15 - which is the product of 3 and 5. If this doesn't return a result, then the next rule - division by 3 - is checked, then division by 5, and finally if none pass, then the number is returned.

However, this overlooks the fact that if both the division by 3 and division by 5 rules pass, "FizzBuzz" is the mere concatenation of these two rules. If neither rule "fires" then the number is returned instead.

```python
def fizzbuzz(n):
    fizz = "Fizz" if n % 3 == 0 else ""
    buzz = "Buzz" if n % 5 == 0 else ""
    return fizz+buzz or n # takes advantage of the 'falsey' nature of the empty string
```

## The Moral

You can slay the `if-hydra` by looking for mathematical solutions and combining conditions into one. Rule-based solutions are a good first step, but there are often clever and concise solutions lurking in the middle of the problem definition.

Also, in the rule-based solution, you might think of `if (n % 15 === 0)` as a 'guard' against a special case of the program. Guards are a well-respected way to simplify algorithms.
