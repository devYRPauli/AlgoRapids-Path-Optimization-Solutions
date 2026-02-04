from typing import List


def min_cost_nk(ind: int, cost: List[int], dp: List[int], k: int) -> int:
    """
    Calculate minimum cost to reach index using bottom-up DP.
    
    Args:
        ind: Target index to reach (unused in bottom-up approach)
        cost: List of costs for each platform
        dp: DP array for storing computed results
        k: Maximum jump distance allowed
        
    Returns:
        Minimum cost to reach the last index
    """
    n = len(cost)
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(1, min(k + 1, i + 1)):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + cost[i - j])
    
    return dp[n - 1]


def main() -> None:
    """
    Main function to read input, calculate minimum cost path, and print the path.
    """
    # Taking input from the user
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

    # Adding a dummy element to the end of the cost list
    cost.append(0)

    # Initializing variables
    n = len(cost)
    dp = [float('inf')] * n

    # Calculating the minimum cost path from the last element to the first element
    min_cost = min_cost_nk(n - 1, cost, dp, k)

    # Removing the dummy element from the cost list
    n -= 1

    # Calculating the indices of the minimum cost path in reverse order
    min_path = []
    for i in range(n, -1, -1):
        if min_cost == dp[i-1] + cost[i-1]:
            min_path.append(i-1)
            min_cost -= cost[i-1]
    min_path.append(0)
    min_path.reverse()

    # Printing the indices of the minimum cost path in reverse order
    [print(i, end=" ") for i in min_path]
    print()


if __name__ == "__main__":
    main()

