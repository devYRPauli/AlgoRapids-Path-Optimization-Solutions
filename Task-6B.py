def find_minimum_cost_bottom_up(n, cost, k, m):
    """
    Finds the minimum cost to reach the last platform from the first platform
    by jumping from one platform to another. Each jump has a cost associated with it.

    Args:
    - n (int): the total number of platforms
    - cost (List[int]): a list of integers representing the cost of jumping from one platform to another
    - k (int): the maximum number of platforms that can be jumped over in a single jump
    - m (int): the total number of jumps allowed

    Returns:
    - minimum_cost (int): the minimum cost to reach the last platform from the first platform
    - jump_path (List[int]): a list of integers representing the path of jumps taken to reach the last platform
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


def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))
    minimum_cost, jump_path = find_minimum_cost_bottom_up(n, cost, k, m)
    print(' '.join(map(str, jump_path)))


if __name__ == "__main__":
    main()