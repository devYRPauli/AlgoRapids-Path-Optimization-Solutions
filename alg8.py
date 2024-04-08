from collections import deque


from typing import List, Tuple
from collections import deque

def find_minimum_cost(n, cost, k, m):
    """
    This function finds the minimum cost and path for a given set of costs and constraints.

    Args:
    - n (int): The number of elements in the cost list.
    - cost (List[int]): The list of costs.
    - k (int): The maximum distance between two elements in the path.
    - m (int): The number of elements in the path.

    Returns:
    - Tuple[int, List[int]]: A tuple containing the minimum cost and the path.

    Example:
    >>> find_minimum_cost(5, [1, 2, 3, 4, 5], 2, 3)
    (6, [0, 2, 4])
    """

    # Initialize memoization table and path table
    memo = [[float('inf')] * (m + 1) for _ in range(n)]
    memo[0][0] = cost[0]
    path = [[[] for _ in range(m + 1)] for _ in range(n)]
    path[0][0] = [0]

    # Iterate over the path
    for j in range(1, m + 1):
        deq = deque()

        # Iterate over the cost list
        for i in range(n):
            # Remove elements from the left end of the deque if they are out of range
            while deq and deq[0] < i - k:
                deq.popleft()

            # If the deque is not empty, update the memoization and path tables
            if deq:
                prev_index = deq[0]
                memo[i][j] = memo[prev_index][j - 1] + cost[i]
                path[i][j] = path[prev_index][j - 1] + [i]

            # Remove elements from the right end of the deque if they have a higher cost than the current element
            while deq and memo[deq[-1]][j - 1] >= memo[i][j - 1]:
                deq.pop()
            deq.append(i)

    # Find the minimum cost and path
    min_cost = float('inf')
    min_path = []
    for i in range(max(0, n - k), n):
        if memo[i][m - 1] < min_cost:
            min_cost = memo[i][m - 1]
            min_path = path[i][m - 1]

    return min_cost, min_path


def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))
    minimum_cost, jump_path = find_minimum_cost(n, cost, k, m)
    print(' '.join(map(str, jump_path)))


if __name__ == "__main__":
    main()