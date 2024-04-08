def min_cost_nk(ind, cost, dp, k):
    n = len(cost)
    for k in range(k+1):
        dp[k] = cost[0]
    for i in range(1, n):
        for plat in range(i+1, min(i+k+1, n)):
            if dp[plat] > cost[i]+dp[i]:
                dp[plat] = cost[i]+dp[i]
    return dp[len(dp)-1]


def main():
    """
    This function takes input from the user, calculates the minimum cost path from the last element to the first element
    of the given list of costs, and prints the indices of the path in reverse order.
    """
    # Taking input from the user
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))

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

