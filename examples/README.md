# Example Input Files

This directory contains sample input files to test the river crossing algorithms.

## Basic River Crossing Problem Examples

These examples are for algorithms that solve the basic problem (without exact jump constraint):

- `basic_brute_force.py`
- `basic_dp_memoization.py`
- `basic_dp_iterative.py`
- `basic_dp_heap.py`
- `basic_dp_monotonic_queue.py`

### example1_basic.txt

```
5 2
3 2 4 1 6
```

- 5 platforms with costs [3, 2, 4, 1, 6]
- Maximum jump distance: 2 platforms

### example2_basic.txt

```
7 3
1 5 3 2 4 6 2
```

- 7 platforms with costs [1, 5, 3, 2, 4, 6, 2]
- Maximum jump distance: 3 platforms

## Exact Jumps Problem Examples

These examples are for algorithms that solve the advanced problem (with exact jump constraint):

- `exact_jumps_brute_force.py`
- `exact_jumps_dp_memoization.py`
- `exact_jumps_dp_iterative.py`
- `exact_jumps_dp_heap.py`
- `exact_jumps_dp_monotonic_queue.py`

### example1_exact.txt

```
6 2 3
2 3 1 4 2 5
```

- 6 platforms with costs [2, 3, 1, 4, 2, 5]
- Maximum jump distance: 2 platforms
- Must make exactly 3 jumps

### example2_exact.txt

```
8 3 4
1 4 2 5 3 6 2 4
```

- 8 platforms with costs [1, 4, 2, 5, 3, 6, 2, 4]
- Maximum jump distance: 3 platforms
- Must make exactly 4 jumps

## Usage

To run an algorithm with an example:

```bash
# For basic problem
python basic_brute_force.py < examples/example1_basic.txt

# For exact jumps problem
python exact_jumps_brute_force.py < examples/example1_exact.txt
```
