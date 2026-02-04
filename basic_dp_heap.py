import heapq
from collections import deque
from typing import List


def min_cost_nk(ind: int, cost: List[int], dp: List[int], k: int) -> int:
    """
    Calculates the minimum cost to reach the last index using DP with min-heap optimization.

    Args:
        ind: Current index (unused in this implementation)
        cost: Array of costs for each platform
        dp: Array to store the minimum cost to reach each index
        k: Maximum jump distance allowed

    Returns:
        Minimum cost to reach the last index of the array
    """
    n = len(cost)
    last_k_plats = []
    last_k_indexes = deque()
    dp[0] = cost[0]

    for i in range(1, min(k + 1, n)):
        dp[i] = cost[i] + cost[0]
        last_k_plats.append((dp[i], i))
        last_k_indexes.append(i)

    heapq.heapify(last_k_plats)

    for i in range(k + 1, n):
        while last_k_indexes and last_k_indexes[0] < i - k:
            last_k_indexes.popleft()
        while last_k_plats and last_k_plats[0][1] < i - k:
            heapq.heappop(last_k_plats)
        min_cost_last_k = last_k_plats[0][0]
        dp[i] = cost[i] + min_cost_last_k
        heapq.heappush(last_k_plats, (dp[i], i))
        last_k_indexes.append(i)

    return dp[n - 1]


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
    n = len(cost)
    dp = [float('inf')] * n
    min_cost = min_cost_nk(n - 1, cost, dp, k)
    
    # Backtrack to find the path
    min_path = []
    i = n - 1
    current_cost = min_cost
    
    while i > 0:
        min_path.append(i)
        for j in range(1, min(k + 1, i + 1)):
            if i - j >= 0 and dp[i] == dp[i - j] + cost[i - j]:
                current_cost -= cost[i - j]
                i = i - j
                break
    
    min_path.append(0)
    print(' '.join(map(str, reversed(min_path[1:]))))


if __name__ == "__main__":
    main()

