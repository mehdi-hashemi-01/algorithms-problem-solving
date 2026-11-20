<div align="center">

# Algorithms & Problem Solving

**A pattern-first collection of Python exercises for learning and teaching algorithms.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Arrays](https://img.shields.io/badge/Arrays-49_scripts-157A75)
![Hashing](https://img.shields.io/badge/Hashing-20_scripts-6554A3)

[Pattern index](#pattern-index) · [Frequency counting](#frequency-counting-in-practice) · [Run an example](#run-an-example) · [Roadmap](#roadmap)

</div>

Start with **Running Sum** to see how one saved value changes the next step of an array scan. Then try **Valid Anagram** to see what changes when each character needs its own counter. The collection groups LeetCode exercises and short classroom examples by the idea they practice.

## Pattern index

### Arrays

| Pattern | What to look for | Start with |
|:--|:--|:--|
| [One pass](01-arrays/01.One%20Pass) | Can the next answer be built from the previous one? | [Running Sum of 1d Array](01-arrays/01.One%20Pass/1480.Running%20Sum%20of%201d%20Array.py) |
| [Running aggregates](01-arrays/02.Running%20Aggreate) | Can a running total and the overall total describe both sides of an index? | [Find Pivot Index](01-arrays/02.Running%20Aggreate/724.Find%20Pivot%20Index.py) |
| [Prefix sums](01-arrays/03.Prefix%20Sum) | Will several queries ask for sums over the same array? | [Range Sum Query – Immutable](01-arrays/03.Prefix%20Sum/303.Range%20Sum%20Query%20-%20Immutable.py) |
| [Prefix and suffix](01-arrays/04.Prefix%20Suffix) | What contribution comes from each side of the current element? | [Product of Array Except Self](01-arrays/04.Prefix%20Suffix/238.Product%20of%20Array%20Except%20Self.py) |
| [In-place modification](01-arrays/05.In-Place%20Modification) | Where should the next retained element be written? | [Move Zeroes](01-arrays/05.In-Place%20Modification/283.Move%20Zeroes.py) |
| [Index placement](01-arrays/06.Index%20Placement) | Does each value have a natural position in the array? | [Find All Numbers Disappeared in an Array](01-arrays/06.Index%20Placement/448.Find%20All%20Numbers%20Disappeared%20in%20an%20Array.py) |
| [Kadane’s algorithm](01-arrays/07.Kadane) | Is it better to extend the current subarray or start again here? | [Maximum Subarray](01-arrays/07.Kadane/53.Maximum%20Subarray.py) |
| [Matrix traversal](01-arrays/08.Matrix) | How do row and column indices change along a spiral? | [Spiral Traversal](01-arrays/08.Matrix/06.SpiralTraversal.py) |

### Hashing

| Pattern | What to look for | Start with |
|:--|:--|:--|
| [Membership](02-hashing/01.Membership%20or%20Existence) | Have we seen this value before? | [Contains Duplicate](02-hashing/01.Membership%20or%20Existence/217.Contains%20Duplicate.py) |
| [Value-to-index lookup](02-hashing/02.Value%20Index%20-%20Complement) | Which earlier index holds the complement of this value? | [Two Sum](02-hashing/02.Value%20Index%20-%20Complement/1.%20Two%20Sum.py) |
| [Frequency counting](02-hashing/03.Frequency%20Counting) | How many copies of each value are available? | [Valid Anagram](02-hashing/03.Frequency%20Counting/242.Valid%20Anagram.py) |
| [Set operations](02-hashing/05.Set%20Operations) | Which words use letters from a single keyboard row? | [Keyboard Row](02-hashing/05.Set%20Operations/500.Keyboard%20Row.py) |

## Frequency counting in practice

A set can tell you that a letter exists. A frequency table can also tell you whether there are enough copies left. Try these five variations in order.

| Exercise | What the counts represent |
|:--|:--|
| [Valid Anagram](02-hashing/03.Frequency%20Counting/242.Valid%20Anagram.py) | Both strings must have the same count for every letter. |
| [Ransom Note](02-hashing/03.Frequency%20Counting/383.Ransom%20Note.py) | Each letter in the note consumes one copy from the magazine. |
| [Intersection of Two Arrays II](02-hashing/03.Frequency%20Counting/350.Intersection%20of%20Two%20Arrays%20II.py) | Each shared value appears as many times as the smaller of its two counts. |
| [Sort Characters by Frequency](02-hashing/03.Frequency%20Counting/451.Sort%20Characters%20By%20Frequency.py) | The counts determine the order of the character groups. |
| [Unique Number of Occurrences](02-hashing/03.Frequency%20Counting/1707.Unique%20Number%20of%20Occurrences.py) | A second pass checks whether two values share the same count. |

**Trace the intersection** of `[4, 4, 9]` and `[4, 9, 4, 4]`. Count the first array, then spend one copy for each match in the second.

| Next value | Copies left (4, 9) after this step | Output so far |
|:--|:--|:--|
| Start | 2, 1 | `[]` |
| 4 | 1, 1 | `[4]` |
| 9 | 1, 0 | `[4, 9]` |
| 4 | 0, 0 | `[4, 9, 4]` |
| 4 | 0, 0 | `[4, 9, 4]` |

The fourth lookup finds that both copies of 4 have already been used.

## Run an example

From the repository root, run the following script with Python 3.

```bash
python "01-arrays/01.One Pass/1480.Running Sum of 1d Array.py"
```

The script starts with `[1, 1, 1, 1]` and prints `[1, 2, 3, 4]`. Change the input to `[2, -1, 3]` and predict the output before running it again.

## Roadmap

The current exercises cover arrays and hashing. The remaining topic folders outline the planned progression.

| Folders | Topics |
|:--|:--|
| 03–06 | Two pointers, sliding window, stacks and queues, binary search |
| 07–11 | Linked lists, backtracking, trees, heaps, graphs |
| 12–15 | Greedy algorithms, intervals, dynamic programming, advanced topics |
