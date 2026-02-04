# Contributing to AlgoRapids

Thank you for your interest in contributing to AlgoRapids: Path Optimization Solutions! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Guidelines](#development-guidelines)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. Please be considerate and respectful in all interactions.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AlgoRapids-Path-Optimization-Solutions.git
   cd AlgoRapids-Path-Optimization-Solutions
   ```
3. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Types of Contributions

- **Bug fixes**: Fix issues in existing algorithms
- **New algorithms**: Implement new optimization approaches
- **Documentation**: Improve README, docstrings, or add tutorials
- **Testing**: Add test cases or improve test coverage
- **Performance improvements**: Optimize existing algorithms
- **Examples**: Add more example input files

## Development Guidelines

### Code Style

1. **Python Version**: Use Python 3.7 or higher
2. **Type Hints**: All functions should include type hints
3. **Docstrings**: Use clear, descriptive docstrings following Google style:

   ```python
   def function_name(param1: int, param2: str) -> bool:
       """
       Brief description of function.

       Args:
           param1: Description of param1
           param2: Description of param2

       Returns:
           Description of return value
       """
   ```

4. **Variable Naming**:
   - Use descriptive names: `min_cost` instead of `mc`
   - Use snake_case for functions and variables
   - Use UPPER_CASE for constants

5. **Input Validation**: All algorithms should validate input parameters

6. **Comments**: Add comments for complex logic, but prefer self-documenting code

### Algorithm Implementation Standards

When implementing a new algorithm:

1. **File Naming**: Use descriptive names following the pattern:
   - Basic problem: `basic_<strategy>.py`
   - Exact jumps problem: `exact_jumps_<strategy>.py`

2. **Required Functions**:

   ```python
   from typing import List, Tuple

   def algorithm_function(...) -> ...:
       """Clear docstring with complexity analysis."""
       pass

   def main() -> None:
       """Main function with input validation."""
       pass

   if __name__ == "__main__":
       main()
   ```

3. **Complexity Analysis**: Document time and space complexity in docstrings

4. **Error Handling**: Validate inputs and handle edge cases

### Testing

Before submitting:

1. Test your algorithm with the example files:

   ```bash
   python your_algorithm.py < examples/example1_basic.txt
   ```

2. Test edge cases:
   - Minimum inputs (n=1, k=1)
   - Large inputs
   - Invalid inputs (should show error messages)

3. Compare output with existing algorithms to verify correctness

## Submitting Changes

1. **Commit Messages**: Write clear, descriptive commit messages:

   ```
   Add monotonic deque optimization for basic problem

   - Implement O(n) time complexity algorithm
   - Add comprehensive docstrings
   - Include input validation
   ```

2. **Push to Your Fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**:
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear title and description
   - Reference any related issues

4. **PR Description Should Include**:
   - What changes were made
   - Why these changes are needed
   - How to test the changes
   - Any breaking changes or dependencies

## Reporting Bugs

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Minimal steps to reproduce the issue
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Environment**: Python version, OS, etc.
6. **Sample Input**: Input that triggers the bug (if applicable)

Example bug report:

```
Title: basic_dp_heap.py crashes with k > n

Description: The algorithm crashes when maximum jump distance exceeds number of platforms

Steps to Reproduce:
1. Run: echo "3 5\n1 2 3" | python basic_dp_heap.py
2. Observe crash

Expected: Should handle gracefully or show error message
Actual: IndexError: list index out of range

Environment: Python 3.9.5, macOS 12.0
```

## Suggesting Enhancements

When suggesting enhancements:

1. **Use Case**: Explain the use case for the enhancement
2. **Current Behavior**: Describe current behavior
3. **Proposed Behavior**: Describe proposed enhancement
4. **Benefits**: Explain benefits of the enhancement
5. **Alternatives**: Mention any alternative approaches considered

## Review Process

All submissions require review. We may ask for changes before merging. Please be patient and responsive to feedback.

## Recognition

Contributors will be acknowledged in the project. Significant contributions may result in being added as a project collaborator.

## Questions?

Feel free to open an issue with the "question" label if you have any questions about contributing.

Thank you for contributing to AlgoRapids!
