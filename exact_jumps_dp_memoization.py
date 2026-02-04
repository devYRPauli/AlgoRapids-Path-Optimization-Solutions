from typing import Tuple, List, Optional


def find_minimum_cost(n: int, cost: List[int], k: int, m: int) -> Tuple[int, List[int]]:
    """
    Finds minimum cost and path using top-down DP with memoization for exact jumps.
    
    Args:
        n: Number of platforms
        cost: List of costs to jump on each platform
        k: Maximum number of platforms that can be jumped over
        m: Exact number of jumps required
        
    Returns:
        Tuple of (minimum cost, path to reach the last platform)
    """
    def find_min_cost_from(platform: int, remaining_jumps: int) -> Tuple[float, List[int]]:
        """
        Recursively finds the minimum cost and path to reach the last platform.
        
        Args:
            platform: Current platform
            remaining_jumps: Number of remaining jumps
            
        Returns:
            Tuple of (minimum cost, path to reach there)
        """
        # If only one jump is remaining
        if remaining_jumps == 1:
            # If the last platform can be reached from the current platform
            if platform + k >= n:
                return cost[platform], [platform]
            else:
                return float('inf'), []
        # If the minimum cost and path for the current platform and remaining jumps is already calculated
        if memo[platform][remaining_jumps] != (None, None):
            return memo[platform][remaining_jumps]
        # Initialize minimum cost and path
        min_cost = float('inf')
        path = []
        # Check the minimum cost and path for all the platforms that can be reached from the current platform
        for next_platform in range(platform + 1, min(platform + k + 1, n)):
            next_cost, next_path = find_min_cost_from(next_platform, remaining_jumps - 1)
            if next_cost + cost[platform] < min_cost:
                min_cost = next_cost + cost[platform]
                path = [platform] + next_path
        # Store the minimum cost and path for the current platform and remaining jumps
        memo[platform][remaining_jumps] = (min_cost, path)
        return min_cost, path

    # Initialize memoization table
    memo = [[(None, None) for _ in range(m + 1)] for _ in range(n)]
    # Find the minimum cost and path to reach the last platform from the first platform
    min_cost, min_path = find_min_cost_from(0, m)
    # If the path is not empty and the first platform is not included in the path
    if min_path and min_path[0] != 0:
        min_cost -= cost[0]
    return min_cost, min_path


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
    
    minimum_cost, jump_path = find_minimum_cost(n, cost, k, m)
    print(' '.join(map(str, jump_path)))


if __name__ == "__main__":
    main()
