from collections import deque


from collections import deque

def min_cost_path(cost, k):
    """
    Finds the minimum cost path from the first to the last element of the given cost array, 
    where the cost of moving from element i to element j is cost[j] and i <= j <= i+k.
    
    Args:
    - cost (list): A list of integers representing the cost of moving from one element to another.
    - k (int): An integer representing the maximum distance between two elements.
    
    Returns:
    - None: The function only prints the minimum cost path.
    """
    n = len(cost)
    dp = [0] * n
    path = [-1] * n
    queue = deque([0])

    dp[0] = cost[0]

    for i in range(1, n):
        # Remove elements from the left of the queue that are out of range
        while queue and queue[0] < i - k:
            queue.popleft()
        
        # Calculate the minimum cost to reach the current element
        dp[i] = dp[queue[0]] + cost[i]
        path[i] = queue[0]

        # Remove elements from the right of the queue that have higher cost than the current element
        while queue and dp[i] < dp[queue[-1]]:
            queue.pop()
        queue.append(i)

    platform_path = []
    min_cost = dp[-1]
    n -= 2

    # Traverse the path backwards to find the minimum cost path
    for i in range(n, -1, -1):
        if min_cost == dp[i]:
            platform_path.append(i)
            min_cost -= cost[i]

    # Print the minimum cost path
    print(' '.join(map(str, reversed(platform_path))))


def main():
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))
    cost.append(0)
    min_cost_path(cost, k)


if __name__ == "__main__":
    main()