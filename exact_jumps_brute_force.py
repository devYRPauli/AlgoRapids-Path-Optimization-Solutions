from typing import Tuple, List


def find_minimum_cost(n: int, cost: List[int], k: int, m: int) -> Tuple[int, List[int]]:
    """
    Finds the minimum cost and path using brute force with exact number of jumps.

    Args:
        n: Number of platforms
        cost: Cost to jump on each platform
        k: Maximum distance that can be covered in a single jump
        m: Exact number of jumps required

    Returns:
        Tuple of (minimum cost, path to reach the last platform)
    """
    def find_min_cost_from(platform: int, remaining_jumps: int) -> Tuple[int, List[int]]:
        """
        Recursive function to find the minimum cost and path to reach the last platform.

        Args:
            platform: Current platform
            remaining_jumps: Number of remaining jumps

        Returns:
            Tuple of (minimum cost, path to reach the last platform)
        """
        if remaining_jumps == 1:
            if platform + k >= n:
                return cost[platform], [platform]
            else:
                return float('inf'), []
        min_cost = float('inf')
        path = []
        for next_platform in range(platform + 1, min(platform + k + 1, n)):
            next_cost, next_path = find_min_cost_from(next_platform, remaining_jumps - 1)
            if next_cost + cost[platform] < min_cost:
                min_cost = next_cost + cost[platform]
                path = [platform] + next_path
        return min_cost, path

    # Find the minimum cost and path to reach the last platform from the first platform
    min_cost, min_path = find_min_cost_from(0, m)

    # If the path starts from a platform other than the first platform, subtract the cost of the first platform
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