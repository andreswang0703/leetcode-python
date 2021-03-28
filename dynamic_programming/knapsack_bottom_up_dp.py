

def solve_knapsack_bottom_up(weights, values, capacity):
    dp = [[-1 for x in range(0, capacity + 1)] for y in range(0, len(weights))]

    # first column: max profit with 0 capacity: so 0 (can't choose anything)
    for i in range(0, len(weights)):
        dp[i][0] = 0
    
    # first row: max profit choosing from first item
    # select the first item if has enough capacity
    for i in range(0, capacity + 1):
        dp[0][i] = 0 if i < weights[0] else values[0]

    for i in range(1, len(weights)):
        for j in range(1, capacity + 1):
            select_cur = 0
            if j >= weights[i]:
                select_cur = values[i] + dp[i - 1][j - weights[i]]
            ignore_cur = dp[i - 1][j]
            dp[i][j] = max(select_cur, ignore_cur)
    
    return dp[len(weights) - 1][capacity]

if __name__ == '__main__':
    capacity = 7
    values = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    print(solve_knapsack_bottom_up(weights, values, capacity))
