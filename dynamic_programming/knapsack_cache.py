
def solve_knapsack_with_dp(weights, values, capacity):
    '''
    Improved implementation for 0/1 knapsack problem.
    
    Cache calculation in 2d array, because recursion call only has capacity and index changing.

    time: O(n * capacity)
    space: O(n * capacity)
    
    '''
    dp = [[-1 for x in range(0, capacity + 1)] for y in range(0, len(weights))]
    return recursion(dp, weights, values, capacity, 0)

def recursion(dp, weights, values, capacity, index):
    if index >= len(weights):
        return 0
    
    if dp[index][capacity] != -1:
        return dp[index][capacity]
    
    select_cur = 0
    if capacity >= weights[index]:
        select_cur = recursion(dp, weights, values, capacity - weights[index], index + 1) + values[index]
    
    ignore_cur = recursion(dp, weights, values, capacity, index + 1)

    max_value = max(select_cur, ignore_cur)
    dp[index][capacity] = max_value

    return max_value

if __name__ == '__main__':
    capacity = 7
    values = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    print(solve_knapsack_with_dp(weights, values, capacity))