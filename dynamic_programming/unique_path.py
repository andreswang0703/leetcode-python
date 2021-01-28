
"""
No.62 and No.63 unique path I and II.

Date: 01/27/2021
"""

def unique_path(m, n):
    """
    No.62 Unique Path. (medium)

    time: O(m * n)
    space: O(m * n)
    """
    dp = [[1] * n for i in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]



def unique_path_with_obstacles(grid):
    """
    No.63 Unique path II. (medium)

    time: O(m * n)
    space: O(m * n)
    """

    # check top-left corner 
    if grid[0][0] == 1:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    
    dp = [[0] * n for i in range(m)]
    dp[0][0] = 1
    
    # populate first row
    for i in range(1, n):
        accessible = grid[0][i] == 0 and dp[0][i - 1] == 1
        dp[0][i] = 1 if accessible else 0
    
    # first column
    for i in range(1, m):
        accessible = grid[i][0] == 0 and dp[i - 1][0] == 1
        dp[i][0] = 1 if accessible else 0
    
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]



if __name__ == "__main__":
    paths = unique_path(3, 7)
    print(paths)

    input_grid = [[0,0,0],[0,1,0],[0,0,0]]
    paths2 = unique_path_with_obstacles(input_grid)
    print(paths2)
