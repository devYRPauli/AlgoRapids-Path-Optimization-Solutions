from typing import List


def min_cost_nk(ind: int, cost: List[int], dp: List[int], k: int) -> int:
    """
    Calculate minimum cost to reach index using top-down DP with memoization.
    
    Args:
        ind: Target index to reach
        cost: List of costs for each platform
        dp: Memoization array for storing computed results
        k: Maximum jump distance allowed
        
    Returns:
        Minimum cost to reach the index
    """
    # Base case: if at the start (index 0), the cost is 0
    if ind == 0:
        return 0

    # Check if we have already computed the cost for this index
    if dp[ind] != -1:
        return dp[ind]

    # Initialize minimum cost as infinity
    min_cost = float('inf')

    # Check up to k platforms back from the current platform
    for j in range(1, k + 1):
        if ind - j >= 0:
            # Recursively find the minimum cost to the previous platform
            temp = min_cost_nk(ind - j, cost, dp, k)
            # Total cost including the jump to the current platform
            jump = temp + cost[ind-j]
            # Update the minimum cost if this path is cheaper
            min_cost = min(jump, min_cost)

    # Store the computed minimum cost for this index
    dp[ind] = min_cost
    return dp[ind]


def main() -> None:
    """Main function to read input and solve the river crossing problem."""
    # Read the number of platforms and the maximum jump length
    n, k = map(int, input().split())
    
    # Validate input
    if n <= 0 or k <= 0:
        print("Error: n and k must be positive integers")
        return
    
    # Read the costs for each platform
    cost = list(map(int, input().split()))
    
    # Validate cost array length
    if len(cost) != n:
        print(f"Error: Expected {n} costs but got {len(cost)}")
        return
    
    # Append 0 to cost, as jumping to the end incurs no additional cost
    cost.append(0)
    # Update the number of platforms including the end point
    n = len(cost)
    # Initialize a DP array with -1 (uncomputed states)
    dp = [-1] * n

    # Compute the minimum cost to reach the end
    min_cost = min_cost_nk(n - 1, cost, dp, k)

    # Backtrack to find the path leading to the minimum cost
    n -= 1
    min_path = []
    for i in range(n, -1, -1):
        if min_cost == dp[i-1] + cost[i-1]:
            min_path.append(i-1)
            min_cost -= cost[i-1]
    # Append the start point to the path and reverse it for correct order
    min_path.append(0)
    min_path.reverse()

    # Print the path
    [print(i, end=" ") for i in min_path]
    print()

if __name__ == "__main__":
    main()