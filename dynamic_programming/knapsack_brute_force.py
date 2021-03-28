

def solve_knapsack_brute_force(weights, values, capacity):
    '''
    0/1 knapsack problem solved by brute force.
    Each recursion call represents a choice made on item[index] (select or not).
    
    time: O(2^n)
    space: O(n) - recursion call stack
    '''
    return recursion(weights, values, capacity, 0)

def recursion(weights, values, capacity, index):
    if index >= len(weights):
        return 0
    
    select_cur = 0
    if capacity >= weights[index]:
        select_cur = recursion(weights, values, capacity - weights[index], index + 1) + values[index]
    ignore_cur = recursion(weights, values, capacity, index + 1)
    return max(select_cur, ignore_cur)

if __name__ == '__main__':
    capacity = 7
    values = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    print(solve_knapsack_brute_force(weights, values, capacity))