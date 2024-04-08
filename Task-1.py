def min_cost_nk(ind, cost, k):
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


def main():
    # Read the number of platforms and the maximum jump length
    n, k = map(int, input().split())
    # Read the cost for each platform
    cost = list(map(int, input().split()))
    # Append 0 to cost, as jumping to the end incurs no additional cost
    cost.append(0)
    n = len(cost)
    # Compute the minimum cost and path to reach the end
    min_cost, min_path = min_cost_nk(n - 1, cost, k)
    # Print the path, excluding the dummy start platform, in reverse order
    print(' '.join(map(str, reversed(min_path[1:]))))


if __name__ == "__main__":
    main()
