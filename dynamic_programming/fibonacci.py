
def fibonacci_brute_force(n):
    """
    Brute force: O(2^n) time
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_brute_force(n - 1) + fibonacci_brute_force(n - 2)



def fibonacci_top_down(n):
    """
    Optimize to O(n) using cache
    """
    arr = [0] * (n + 1)
    return fibonacci_top_down_helper(n, arr)

def fibonacci_top_down_helper(n, arr):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if arr[n] == 0:
        # use array to cache result
        arr[n] = fibonacci_top_down_helper(n - 1, arr) + fibonacci_top_down_helper(n - 2, arr)

    return arr[n]



def fibonacci_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]


def fibonacci_bottom_up_constant_space(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    c = 1

    idx = 2
    while idx < n + 1:ß
        c = a + b
        a = b
        b = c
        idx += 1
    return c


if __name__ == "__main__":
    a = fibonacci_brute_force(10)
    b = fibonacci_top_down(10)
    c = fibonacci_bottom_up(10) 
    d = fibonacci_bottom_up_constant_space(10)

    print(a)
    print(b)
    print(c)
    print(d)