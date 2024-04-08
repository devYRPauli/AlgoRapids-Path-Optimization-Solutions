# Algorithms-Optimization

## Project Overview
This project delves into solving two nuanced river crossing problems using advanced algorithmic techniques. It showcases the design, analysis, and implementation of eight distinct algorithms to optimize the cost and number of jumps required to cross a river, given a set of platforms with associated costs.

## Table of Contents
- [Installation](#installation)
- [Problem Definition](#problem-definition)
  - [Basic River Crossing Problem](#basic-river-crossing-problem)
  - [Advanced River Crossing Problem with Exact Jump](#advanced-river-crossing-problem-with-exact-jump)
- [Algorithms](#algorithms)
  - [Overview](#overview)
  - [Time and Space Complexity](#time-and-space-complexity)
- [Running the Code](#running-the-code)
- [Conclusions](#conclusions)

## Installation
Clone the repository to your local machine:
git clone https://github.com/YourUsername/RiverCrossingOptimization-Algorithms.git
Ensure you have Python 3.x installed, as the implementations use Python. No external libraries are required.

## Problem Definition

### Basic River Crossing Problem
Objective: Minimize the cost of crossing a river using platforms, with a given maximum jump length.

### Advanced River Crossing Problem with Exact Jump
Objective: Similar to the Basic problem, but with an added constraint of an exact number of jumps that must be taken.

## Algorithms

### Overview
- ALG1-ALG4: Focus on the Basic River Crossing Problem, utilizing brute force and dynamic programming strategies.
- ALG5-ALG8: Aimed at solving the Advanced Problem, employing similar algorithmic principles tailored to the additional constraint.

### Time and Space Complexity
- Algorithm 1 (ALG1)
  - Time Complexity: Θ(k^n) - Brute force approach without memoization, leading to exponential time complexity due to the recursive computation of each state an exponential number of times.
  - Space Complexity: O(k^n) - Recursive calls occupy the call stack, increasing the space complexity exponentially.
- Algorithm 2 (ALG2)
  - Time Complexity: Θ(n*k) - Utilizes memoization to store the results of subproblems, reducing redundant calculations. Each state is computed once with a linear search over 'k' previous states.
  - Space Complexity: O(n) - Linear space is used to store the results of subproblems in an array.
- Algorithm 3 (ALG3)
  - Time Complexity: Θ(n*log(n)) - Enhancements with a Min-Heap data structure allow for logarithmic time access to the minimum value among the 'k' previous platforms, optimizing the retrieval process.
  - Space Complexity: O(n) - Space is required for storing the states and the Min-Heap, which at most contains 'n' elements, contributing to linear space complexity.
- Algorithm 4 (ALG4)
  - Time Complexity: Θ(n) - Achieves linear time complexity through the use of a monotonic queue, optimizing state transitions and ensuring each platform is considered once.
  - Space Complexity: O(n) - Utilizes a queue and an array for storing computed values, both of which have sizes linear in terms of the number of platforms.
- Algorithm 5 (ALG5)
  - Time Complexity: Θ(k^n) - Similar to ALG1, this brute force approach for the advanced problem also leads to exponential time complexity due to the recursive computation of each state.
  - Space Complexity: O(k^n) - The recursive depth and the call stack size contribute to an exponential space complexity.
- Algorithm 6 (ALG6)
  - Time Complexity: O(m⋅n⋅k) - Nested loops iterate over the number of jumps 'm', the number of platforms 'n', and the possible next platforms 'k', leading to a cubic time complexity in the worst case.
  - Space Complexity: O(n⋅m) - Utilizes a 2D array for dynamic programming, where each cell represents a state defined by a platform and the remaining number of jumps.
- Algorithm 7 (ALG7)
  - Time Complexity: O(m * n * log n) - Incorporates dynamic programming with a Min-Heap for optimizing access times, leading to an improved time complexity that accounts for 'm' jumps and 'n' platforms with logarithmic access for minimum cost retrieval.
  - Space Complexity: O(n * m) - Similar to ALG6, space complexity is governed by the size of the 2D dynamic programming table and additional structures like Min-Heaps.
- Algorithm 8 (ALG8)
  - Time Complexity: Θ(n*m) - Further optimizes the dynamic programming approach by reducing the inner loop's complexity using a monotonic queue, achieving a linear time complexity relative to the number of platforms and jumps.
  - Space Complexity: O(n*m) - Maintains a dynamic programming table with 'n' platforms and 'm' jumps, alongside data structures for efficiently tracking the minimum costs.

## Running the Code
python alg1.py

## Conclusion
This project highlighted the effectiveness of dynamic programming in solving constrained optimization problems, showcasing significant improvements in both computational time and resource utilization across various algorithmic strategies.
