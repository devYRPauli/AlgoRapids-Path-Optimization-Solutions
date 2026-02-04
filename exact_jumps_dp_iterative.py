from typing import Tuple, List


def find_minimum_cost_bottom_up(n: int, cost: List[int], k: int, m: int) -> Tuple[float, List[int]]:
    """
    Finds minimum cost using bottom-up DP for exact jumps problem.

    Args:
        n: Total number of platforms
        cost: List of costs for jumping on each platform
        k: Maximum number of platforms that can be jumped over
        m: Exact number of jumps required

    Returns:
        Tuple of (minimum cost, path of jumps taken)
    """
    # initialize the dynamic programming table and path table
    dp = [[float('inf')] * (m + 1) for _ in range(n)]
    path = [[[] for _ in range(m + 1)] for _ in range(n)]

    # set the base case for the last platform
    for i in range(n):
        if i + k >= n:
            dp[i][1] = cost[i]
            path[i][1] = [i]

    # fill the dynamic programming table and path table using bottom-up approach
    for j in range(2, m + 1):
        for i in range(n - 2, -1, -1):
            for next_platform in range(i + 1, min(i + k + 1, n)):
                if dp[next_platform][j - 1] + cost[i] < dp[i][j]:
                    dp[i][j] = dp[next_platform][j - 1] + cost[i]
                    path[i][j] = [i] + path[next_platform][j - 1]

    # get the minimum cost and jump path
    jump_path = path[0][m]
    minimum_cost = dp[0][m] if jump_path else float('inf')

    # adjust the minimum cost if the first platform was not included in the jump path
    if jump_path and jump_path[0] != 0:
        minimum_cost -= cost[0]

    return minimum_cost, jump_path


def main() -> None:
    """Main function to read input and solve the exact jumps river crossing problem."""
    n, k, m = map(int, input().split())
    
    # Validate input
    if n <= 0 or k <= 0 or m <= 0:
        print("Error: n, k, and m must be positive integers")
        return
    
    cost = list(map(int, input().split()))
    
    # Validate cost array length
    if len(cost) != n:
        print(f"Error: Expected {n} costs but got {len(cost)}")
        return
    
    minimum_cost, jump_path = find_minimum_cost_bottom_up(n, cost, k, m)
    print(' '.join(map(str, jump_path)))


if __name__ == "__main__":
    main()