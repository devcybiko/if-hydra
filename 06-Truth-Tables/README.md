# Truth Table Swords - Logic Gates

Logic gates are used in computer and electronics circuits. There are four basic types:

1. And
2. Or
3. Not
4. Xor

With the exception of the "Not" gate, all these gates take two or more binary inputs (zero/one, true/false) and generate a single output. One way to represent logic gates is using a truth table showing the inputs and the output. The inputs can be labeled "A" and "B" and the output is labeled "C".

## Truth Tables

### And Gate

The And gate takes two input "bits" which have a value of "0" or "1". The output is "0" if either input is "0" and "1" if and only if both "A" `and` "B" are "1".

|   | AND |   |
|---|---|---|
| A | B | C |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Or Gate

The Or gate takes two input "bits" which have a value of "0" or "1". The output is "1" if either input "A" `or` "B" is "1", and "0" otherwise.

|   | OR |   |
|---|---|---|
| A | B | C |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### Not Gate

The Not gate takes one input "bit" which hase a value of "0" or "1" and inverts it to "1" or "0".

|   | NOT |
|---|---|
| A | C |
|---|---|
| 0 | 1 |
| 1 | 0 |

### Xor Gate

Arguably, the XOR (exclusive or) is a combination of the three other gates. The output is "1" one or the other inputs, but not both, are "1". Otherwise the output is "0".

|   | XOR |   |
|---|---|---|
| A | B | C |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0|

## The Hydra

For this example, we'll implement an XOR gate. Admittedly there are simpler methods to implement this logic. We're establishing a pattern that we'll repeat in the next example.

```python
def xor(a, b):
    if a == 0:
        if b == 0:
            return 0
        else:
            return 1
    else:
        if b === 0:
            return 1
        else:
            return 0
```

## The Sword - Truth Tables

```python
xor = [ [0, 1], [1, 0]]
result = xor[a][b]
```
