
"""
A child is running up a staircase with n steps and can hop either 1, 2, or 3 steps.
Count how many possible ways the child can run up the stairs.
"""
def count_possible_ways(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2
    return count_helper(n, arr)

def count_helper(n, arr):
    if n < 3:
        return arr[n]
    
    if arr[n] == 0:
        arr[n] = count_helper(n - 1, arr) + count_helper(n - 2, arr) + count_helper(n - 3, arr)
    return arr[n]


if __name__ == "__main__":
    a = count_possible_ways(6)
    print(a)
