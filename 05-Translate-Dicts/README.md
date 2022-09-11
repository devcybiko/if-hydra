# Translate Dictionary Swords: RPSLX, re-redux

As in the last chapter, we have a need to translate our `names` and `reasons` into strings. We learned how to use translate tables (arrays) to create a set of `keys` and `values`. But there's an even easier way to translate keys into values: Dictionaries.

## Dictionaries

Dictionaries (also called `Associative Arrays` or `Hash Tables` or simply `Hashes`) have the key-value mechanism built-in. This "mapping" is so powerful an useful that dictionaries have become the `swiss army knife` of the computer programmer.

Unlike our array-based solution, there is no need to iterate over the list of keys. We can simply `dereference` or `index` the dictionary the same way we do with an array - with a string inside square brackets:

* `name = names['r']`

It's that simple. Let's look at an example.

## The Sword: Translate Tables: Part II - Dictionaries

Dictionaries are defined by establishing a list of `{"key": "value"}` pairs inside a set of curly-braces.

```python
names = {
    "r": "Rock", 
    "p": "Paper", 
    "s": "Scissors", 
    "l": "Lizard", 
    "x": "Spock"
}
reasons = { 
    "sp": "Scissors cuts Paper",
    "pr": "Paper covers Rock", 
    "rl": "Rock crushes Lizard", 
    "lx": "Lizard poisons Spock", 
    "xs": "Spock smashes Scissors", 
    "sl": "Scissors decapitates Lizard",
    "lp": "Lizard eats Paper", 
    "px": "Paper disproves Spock",
    "xr": "Spock vaporizes Rock",
    "rs": "As it always has, Rock crushes Scissors.",
    "ps": "Scissors cuts Paper",
    "rp": "Paper covers Rock", 
    "lr": "Rock crushes Lizard", 
    "xl": "Lizard poisons Spock", 
    "sx": "Spock smashes Scissors", 
    "ls": "Scissors decapitates Lizard",
    "pl": "Lizard eats Paper", 
    "xp": "Paper disproves Spock",
    "rx": "Spock vaporizes Rock",
    "sr": "As it always has, Rock crushes Scissors.",
    "rr": "It's a tie",
    "ss": "It's a tie",
    "pp": "It's a tie",
    "ll": "It's a tie",
    "xx": "It's a tie"
}

def main():
    name = names['r'] ### returns 'Rock'
    reason = reasons['rs'] ### returns 'As it always has, Rock crushes Scissors'
```

Compare this to the code from the last chapter. I've added all the possible combinations to the `reasons` dictionary - including the ties. This makes the lookup even simpler.

We've done three very powerful things in this chapter:

1. We've made a strong link - or `association` between our keys and values by putting them both in dictionaries
1. We've eliminated the lookup function, reducing our lines-of-code count
1. And our lookup is very "natural" - we just address the dictionary the same as we do an array - but instead of numbers indexing the array, we can use strings to pull values out of the dictionary.

## The Moral

When you have a list of 'keys' that directly relate to 'values', the best solution is a `dictionary`. This idea of `key/value` pairs is used throughout computing. You'll encounter is in databases, memory caching, and internet protocols. The `key/value` lookup capability of `dictionaries` is so simple and powerful that `dictionaries` are considered the `Swiss Army Knife` of programming. 