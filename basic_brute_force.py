from typing import Tuple, List


def min_cost_nk(ind: int, cost: List[int], k: int) -> Tuple[int, List[int]]:
    """
    Calculate minimum cost to reach index using brute force recursion.
    
    Args:
        ind: Target index to reach
        cost: List of costs for each platform
        k: Maximum jump distance allowed
        
    Returns:
        Tuple of (minimum cost, path to reach the index)
    """
    # Base case: if we are at the first platform, the cost is 0 and the path is [0]
    if ind == 0:
        return 0, [0]

    # Initialize minimum cost as infinity and an empty path
    min_cost = float('inf')
    min_path = []

    # Check up to k steps back from the current platform
    for j in range(1, k + 1):
        # Ensure the previous platform index is valid
        if ind - j >= 0:
            # Recursively calculate the cost and path for the previous platform
            next_cost, path = min_cost_nk(ind - j, cost, k)
            # If the total cost to reach the current platform is less than the current minimum, update it
            if next_cost + cost[ind-j] < min_cost:
                min_cost = next_cost + cost[ind-j]
                min_path = [ind] + path

    # Return the minimum cost and the corresponding path to reach the current platform
    return min_cost, min_path


def main() -> None:
    """Main function to read input and solve the river crossing problem."""
    # Read the number of platforms and the maximum jump length
    n, k = map(int, input().split())
    
    # Validate input
    if n <= 0 or k <= 0:
        print("Error: n and k must be positive integers")
        return
    
    # Read the cost for each platform
    cost = list(map(int, input().split()))
    
    # Validate cost array length
    if len(cost) != n:
        print(f"Error: Expected {n} costs but got {len(cost)}")
        return
    
    # Append 0 to cost, as jumping to the end incurs no additional cost
    cost.append(0)
    n = len(cost)
    # Compute the minimum cost and path to reach the end
    min_cost, min_path = min_cost_nk(n - 1, cost, k)
    # Print the path, excluding the dummy start platform, in reverse order
    print(' '.join(map(str, reversed(min_path[1:]))))


if __name__ == "__main__":
    main()
