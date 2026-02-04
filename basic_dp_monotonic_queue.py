from collections import deque
from typing import List


def min_cost_path(cost: List[int], k: int) -> None:
    """
    Finds the minimum cost path using DP with monotonic queue optimization.
    
    Args:
        cost: A list of integers representing the cost of each platform
        k: Maximum jump distance allowed
    
    Returns:
        None: The function prints the minimum cost path
    """
    n = len(cost)
    dp = [0] * n
    path = [-1] * n
    queue = deque([0])

    dp[0] = cost[0]

    for i in range(1, n):
        # Remove elements from the left of the queue that are out of range
        while queue and queue[0] < i - k:
            queue.popleft()
        
        # Calculate the minimum cost to reach the current element
        dp[i] = dp[queue[0]] + cost[i]
        path[i] = queue[0]

        # Remove elements from the right of the queue that have higher cost than the current element
        while queue and dp[i] < dp[queue[-1]]:
            queue.pop()
        queue.append(i)

    # Reconstruct the path using the path array
    platform_path = []
    current = n - 1
    
    while current != -1:
        platform_path.append(current)
        current = path[current]
    
    # Print the minimum cost path (excluding the destination)
    print(' '.join(map(str, reversed(platform_path[1:]))))


def main() -> None:
    """Main function to read input and solve the river crossing problem."""
    n, k = map(int, input().split())
    
    # Validate input
    if n <= 0 or k <= 0:
        print("Error: n and k must be positive integers")
        return
    
    cost = list(map(int, input().split()))
    
    # Validate cost array length
    if len(cost) != n:
        print(f"Error: Expected {n} costs but got {len(cost)}")
        return
    
    cost.append(0)
    min_cost_path(cost, k)


if __name__ == "__main__":
    main()