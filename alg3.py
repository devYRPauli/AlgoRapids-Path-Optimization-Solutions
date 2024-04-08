import heapq
from collections import deque


import heapq
from collections import deque

def min_cost_nk(ind, cost, dp, k):
    """
    Calculates the minimum cost to reach the last index of the given array of costs
    with the constraint that at most k consecutive indices can be visited at once.

    Args:
    - ind (int): current index
    - cost (List[int]): array of costs
    - dp (List[int]): array to store the minimum cost to reach each index
    - k (int): maximum number of consecutive indices that can be visited at once

    Returns:
    - int: minimum cost to reach the last index of the array
    """
    n = len(cost)
    last_k_plats = [] # heap to store the minimum cost of last k indices
    last_k_indexes = deque() # deque to store the indices of last k indices
    dp[0] = cost[0] # minimum cost to reach first index is the cost of first index

    # calculate minimum cost to reach first k indices
    for i in range(1, k + 1):
        dp[i] = cost[i] + cost[0] # minimum cost to reach i-th index is the sum of cost of i-th index and cost of first index
        last_k_plats.append((dp[i], i)) # add the minimum cost of i-th index to heap
        last_k_indexes.append(i) # add the index of i-th index to deque

    heapq.heapify(last_k_plats) # heapify the heap

    # calculate minimum cost to reach remaining indices
    for i in range(k + 1, n):
        while deque and last_k_indexes[0] < i - k:
            last_k_indexes.popleft() # remove the index of the first element of deque if it is outside the range of last k indices
        while last_k_plats and last_k_plats[0][1] < i - k:
            heapq.heappop(last_k_plats) # remove the first element of heap if it is outside the range of last k indices
        min_cost_last_k = last_k_plats[0][0] # minimum cost of last k indices is the first element of heap
        dp[i] = cost[i] + min_cost_last_k # minimum cost to reach i-th index is the sum of cost of i-th index and minimum cost of last k indices
        heapq.heappush(last_k_plats, (dp[i], i)) # add the minimum cost of i-th index to heap
        last_k_indexes.append(i) # add the index of i-th index to deque

    return dp[len(dp) - 1] # return the minimum cost to reach the last index of the array
def min_cost_nk(ind, cost, dp, k):
    n = len(cost)
    last_k_plats = []
    last_k_indexes = deque()
    dp[0] = cost[0]

    for k in range(1, k + 1):
        dp[k] = cost[k] + cost[0]
        last_k_plats.append((dp[k], k))
        last_k_indexes.append(k)

    heapq.heapify(last_k_plats)

    for i in range(k + 1, n):
        while deque and last_k_indexes[0] < i - k:
            last_k_indexes.popleft()
        while last_k_plats and last_k_plats[0][1] < i - k:
            heapq.heappop(last_k_plats)
        min_cost_last_k = last_k_plats[0][0]
        dp[i] = cost[i] + min_cost_last_k
        heapq.heappush(last_k_plats, (dp[i], i))
        last_k_indexes.append(i)
    return dp[len(dp) - 1]


def main():
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))
    cost.append(0)
    n = len(cost)
    dp = [float('inf')] * n
    min_cost = min_cost_nk(n - 1, cost, dp, k)
    n -= 2
    min_path = []
    for i in range(n, -1, -1):
        if min_cost == dp[i]:
            min_path.append(i)
            min_cost -= cost[i]
    print(' '.join(map(str, reversed(min_path))))


if __name__ == "__main__":
    main()

