# Translate Table Swords: RPSLX, redux

There is a problem with our solution to the RPSLX problem from the last chapter: the names of the different things thrown were not used - just their abbreviation. Also, it would be nice to display the "reason" for the win (or loss).

## The Hydra

Translating a code to a string is a very common activity in software. In our case, we want to translate "r" to "Rock", "p" to "Paper", "s" to "Scissors", etc...

This can be accomplished with an `if-hydra` easily:

```python
def get_name(s):
    if s == 'r': return "Rock"
    elif s == 'p': return "Paper"
    elif s == 's': return "Scissors"
    elif s == 'l': return "Lizard"
    elif s == 'x': return "Spock"
    else: return "ERROR"
```

Likewise, it would be super-cool to translate the winning combination into a descriptive string:

```python
def get_reason(s):
    if s == "sp": return "Scissors cuts Paper"
    elif s =="pr": return "Paper covers Rock"
    elif s == "rl": return "Rock crushes Lizard"
    elif s == "lx": return "Lizard poisons Spock"
    elif s == "xs": return "Spock smashes Scissors"
    elif s == "sl": return "Scissors decapitates Lizard"
    elif s == "lp": return "Lizard eats Paper"
    elif s == "px": return "Paper disproves Spock"
    elif s == "xr": return "Spock vaporizes Rock"
    elif s == "rs": return "As it always has, Rock crushes Scissors."
    else return "ERROR"
```

## The Sword: Translate Tables: Part I - Arrays

We can create a "Translate Table" by putting the "keys" in one array and the corresponding "values" in a second array. Then, we can look up the position of the "key" in the "keys" array, and then get value from **the same position in the values array**.

```python
name_keys = ["r", "p", "s", "l", "x"]
name_values = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
reason_keys = ["sp", "pr", "rl", "lx", "xs", "sl", "lp","px", "xr"]
reason_values = [
    "Scissors cuts Paper",
    "Paper covers Rock",
    "Rock crushes Lizard",
    "Lizard poisons Spock",
    "Spock smashes Scissors",
    "Scissors decapitates Lizard",
    "Lizard eats Paper",
    "Paper disproves Spock",
    "Spock vaporizes Rock",
    "As it always has, Rock crushes Scissors."
]

def lookup_range(key, keys, values):
    # this is the 'hard' way. iterate over all the keys until you find the one you want
    for i in range(0, len(keys)):
        if keys[i] == key: break ### get out when we find the key
    value = values[i] ### return the corresponding value
    return value

def lookup(key, keys, values):
    i = keys.index(key) ### find the position of the key in the keys
    value = values[i] ### return the corresponding value
    return value

def main():
    name = lookup('r', name_keys, name_values) ### returns 'Rock'
    reason = lookup('rs', reason_keys, reason_values) ### returns 'As it always has, Rock crushes Scissors'
```

Hopefully you can see that we can use the `lookup()` function for looking up both the `names` and the `reasons`. This sort of generalization of your code will make your life easier. As much as possible, programmers want to solve a problem once, and then reuse that solution over and over again.

Here, I've included a `lookup_range()` function to compare to the `lookup()` function. They're very similar. The `lookup_range()` function does an iteration over the `keys` to find the index of the `key` value in the `keys` array. Since this is a very common operation, there is a method on arrays called `index()` which makes this very easy. I've used the `index()` method in the final `lookup()` function.


## The Moral

When you have a list of 'keys' that directly relate to 'values', it's possible to create a lookup table to translate the `key` to the `value`. In the next chapter we'll learn an even easier way to make this translation - using `dictionaries`.