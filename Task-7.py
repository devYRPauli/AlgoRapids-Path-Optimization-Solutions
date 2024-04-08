import heapq


import heapq

def find_minimum_cost(n, cost, k, m):
    """
    Finds the minimum cost and path to reach the last platform in a game where the player can jump
    at most k platforms at a time and can make a total of m jumps. Each platform has a cost associated
    with it that the player has to pay to land on it.

    Args:
        n (int): The total number of platforms.
        cost (List[int]): A list of length n containing the cost of landing on each platform.
        k (int): The maximum number of platforms the player can jump at a time.
        m (int): The total number of jumps the player can make.

    Returns:
        Tuple[int, List[int]]: A tuple containing the minimum cost and the path to reach the last platform.

    Example:
        >>> find_minimum_cost(5, [1, 2, 3, 4, 5], 2, 3)
        (7, [0, 2, 4])
    """
    # Initialize memoization table
    memo = [[(float('inf'), []) for _ in range(m + 1)] for _ in range(n)]
    memo[0][1] = (cost[0], [0])

    # Fill memoization table
    for remaining_jump in range(2, m + 1):
        heap = []
        for i in range(min(k, n)):
            heapq.heappush(heap, (memo[i][remaining_jump - 1][0], i))

        for platform in range(n):
            while heap and heap[0][1] < platform - k:
                heapq.heappop(heap)

            if heap:
                prev_cost, prev_platform = heap[0]
                min_cost = prev_cost + cost[platform]
                path = memo[prev_platform][remaining_jump - 1][1] + [platform]
                memo[platform][remaining_jump] = (min_cost, path)

            if platform < n - 1:
                heapq.heappush(heap, (memo[platform][remaining_jump - 1][0], platform))

    # Find minimum cost and path to reach the last platform
    min_cost, min_path = float('inf'), []
    for i in range(max(0, n - k), n):
        if memo[i][m][0] < min_cost:
            min_cost, min_path = memo[i][m]

    return min_cost, min_path


def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))
    minimum_cost, jump_path = find_minimum_cost(n, cost, k, m)
    print(' '.join(map(str, jump_path)))


if __name__ == "__main__":
    main()