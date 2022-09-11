# Lookup Tabel Swords: Rock, Paper, Scissors, Lizard, Spock

## Rock, Paper, Scissors: (From [Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors))

> Rock paper scissors is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). 

> It has three possible outcomes: a draw, a win or a loss. A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or "breaks scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie.

## Rock, Paper, Scissors, Lizard, Spock: (from "[The Big Bang Theory](https://the-big-bang-theory.com/rock-paper-scissors-lizard-spock/)")

> Rock Paper Scissors Lizard Spock is an extension of the classic game of chance, Rock Paper Scissors, created by Sam Kass and Karen Bryla.

> Sam Kass explains he created the expanded game because it seemed like most games of Rock Paper Scissors with people you know would end in a tie.

> Rock Paper Scissors Lizard Spock was first mentioned in the Season 2 episode, The Lizard-Spock Expansion, the title of which references the game. It was last mentioned in The Rothman Disintegration.

> As Sheldon explains, "Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors."


## The Hydra

For Rock, Paper, Scissors (RPS) there is a "naive" solution which compares every "throw" that player1 can make against every throw that player2 can make. This results in an "order n-squared" `if-hydra`. In other words, there'd be nine comparisons to determine a winner. And if we extend to Lizard, Spock (RPSLX), then it would take `5*5` or 25 comparisons.

However, RPS can be written using a simpler `if-hydra` that assumes anything that isn't a win for player1 is a win for player2 (excluding ties, of course - which can trivially be checked as a "guard"). There are a total of 3 winning combinations. However, when the rules of the game extend to RPSLX the number of winning combinations increases to 10 - hence 10 comparisons in the `if-hydra`.

The number of winning combinations is expressed mathematically as:

```
p(n) = n * (n - 1) / 2

or...

p(n) = (n^2 - n) / 2
```

Notice that this is still a "quadratic" relationship. Here is a table of the number of combinations as the number of possible "throws" increases:

![Table of n v. p(n)](table.png "Table of n v. p(n)")

And here is the corresponding graph:

![Graph of n v. p(n)](graph.png "Graph of n v. p(n)")

Notice that the graph indicates that the number of comparisons increases as the square of the number of "throws." This is what makes generalizing such problems nearly impossible when using the `if-hydra`.

Here is the `if-hydra` for RPS with 3 comparisons (aside from the "guard"):

```python
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1 == "r" and player2 == "s": return 1
    elif player1 == "p" and player2 == "r": return 1
    elif player1 == "s" and player2 == "p": return 1
    else: return 2
```

And here is the `if-hydra` for RPSLX with 10 comparisons (aside from the "guard"):

```python
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1 == "r" and player2 == "s": return 1
    elif player1 == "r" and player2 == "l": return 1
    elif player1 == "p" and player2 == "r": return 1
    elif player1 == "p" and player2 == "x": return 1
    elif player1 == "s" and player2 == "p": return 1
    elif player1 == "s" and player2 == "l": return 1
    elif player1 == "l" and player2 == "x": return 1
    elif player1 == "l" and player2 == "p": return 1
    elif player1 == "x" and player2 == "s": return 1
    elif player1 == "x" and player2 == "r": return 1
    else: return 2
```

## The Sword: Lookup Tables

As an alternative, we could put all the possible combinations in a "lookup table" (aka "array" or "list"). Then, "look up" the `player1 + player2` choice in the table. If that combination is in the table, then `player1` wins, else `player2` wins. (Notice that combining the `player1` and `player2` choices hearkens back to the `Concatenation Sword` from the last chapter.)

Here is the code for RPS using an array to validate all the possible winning combinations:

```python
winners = ["rs", "pr", "sp"]
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1+player2 in winners: return 1
    else: return 2
```
And here is the code for RPSLX:

```python
winners = ["rs", "pr", "sp", "rl", "lx", "xs", "sl", "lp", "px", "xr"]
def winner(player1, player2):
    if player1 == player2: return 0 ### tie "guard"
    if player1+player2 in winners: return 1
    else: return 2
```

Hopefully, you've recognized that there is no difference in the `winner()` function in both the RPS and RPSLX solutions. The only difference is the `winners` array.

## The Moral

This demonstrates the power of using an array as a look-up table for valid values. 

The presence of a valid value can be determined with the `in` Python operator (or `includes` method in JavaScript) with very fast performance, and very clear and concise code.

Using data as a replacement for an `if-hydra` is very often the most performant and generic (or generalizable) solution.
