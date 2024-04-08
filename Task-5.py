def find_minimum_cost(n, cost, k, m):
    """
    Finds the minimum cost and path to reach the last platform from the first platform
    given the number of platforms, cost to jump on each platform, maximum number of jumps
    allowed and maximum distance that can be covered in a single jump.

    Args:
        n (int): Number of platforms
        cost (List[int]): Cost to jump on each platform
        k (int): Maximum distance that can be covered in a single jump
        m (int): Maximum number of jumps allowed

    Returns:
        Tuple[int, List[int]]: Minimum cost to reach the last platform and the path to reach there
    """
    def find_min_cost_from(platform, remaining_jumps):
        """
        Recursive function to find the minimum cost and path to reach the last platform
        from the given platform with the given number of remaining jumps.

        Args:
            platform (int): Current platform
            remaining_jumps (int): Number of remaining jumps

        Returns:
            Tuple[int, List[int]]: Minimum cost to reach the last platform and the path to reach there
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


def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))
    minimum_cost, jump_path = find_minimum_cost(n, cost, k, m)
    print(' '.join(map(str, jump_path)))


if __name__ == "__main__":
    main()