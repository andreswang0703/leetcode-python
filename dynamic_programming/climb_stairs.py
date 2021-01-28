
"""
No.70 Climb stairs. (easy)

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Date: 01/27/2021
"""
def count_ways(n):
    if n < 3:  # need this check, or n = 1 will fail
        return n

    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2

    return count_helper(n, arr)

def count_helper(n, arr):
    if n < 3:
        return arr[n]
    
    if arr[n] == 0:
        arr[n] = count_helper(n - 1, arr) + count_helper(n - 2, arr)
    return arr[n]


def count_ways_constant_space(n):
    if n < 3:
        return n
    
    a = 1
    b = 2
    c = 0
    for i in range(2, n): # n - 2 iterations
        c = a + b
        a = b
        b = c
    return c


