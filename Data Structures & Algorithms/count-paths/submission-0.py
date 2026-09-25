class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
        JOSEPH'S WORKSPACE:

        im given mxn grid
        i can only move to right or down

        edge case: m == 1 or n == 1, return 1

        example:

        Input: m = 3, n = 6

        Output: 21

        SOLUTION 1:
        1. Start from (0,0)
        2. recursively move right and down
        3. return 1 when i reach destination

        def pathfinder(row,col):
            if row == m - 1 and col == n - 1:
                return 1

            path = 0
        #moving down
            if row + 1 < m:
                path += pathfinder(row +1, col)

        #moving right
            if col + 1 < n:
                path += pathfinder(row, col +1)
            
            return path

        return pathfinder(0,0)

        OPTIMIZED SOLUTION

        use dynamic prgramming
        each cell stores the number of wyas to get to the cell
        ways[row][col] = ways[row-1][col] + ways[row][col-1]]

        pseudocode
        1. create an array of n number of ones
        2. for each remaining row, update from left to right
        3. return the last value
        """
        """
        def pathfinder(row,col):
            if row == m - 1 and col == n - 1:
                return 1

            path = 0

        #moving down
            if row + 1 < m:
                path += pathfinder(row +1, col)

        #moving right
            if col + 1 < n:
                path += pathfinder(row, col +1)
            
            return path

        return pathfinder(0,0)
        """

        dp = [1] * n

        for row in range(1,m):
            for col in range(1,n):
                dp[col] += dp[col-1]

        return dp[-1]
