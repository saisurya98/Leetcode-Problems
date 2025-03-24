class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # The idea is to change the 0 to 2 intermediately before changing 2 back to 1 if condition is present
        # Same apply change 1 to 3 interm before changing 3 back to 0 if codition is true.
        # TC-O(m*n)
        # SC-O(1)
        m = len(board)
        n = len(board[0])
        if board is None or len(board) == 0:
            return None

        # 0-1->2
        # 1-0->3
        for i in range(m):
            for j in range(n):
                liveneighbours = self.countliveneighbours(board, i, j)
                if board[i][j] == 1:
                    if liveneighbours < 2:
                        board[i][j] = 3
                    if liveneighbours > 3:
                        board[i][j] = 3
                else:
                    if liveneighbours == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def countliveneighbours(self, board: list[list[int]], row: int, col: int) -> int:
        count = 0
        m = len(board)
        n = len(board[0])
        # U D L R UL UR DL DR
        # 1,1
        # 0,1 -2,1- 1,0- 1,2 - 0,0- 0,2- 2,0- 2,2

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for neigh in dirs:
            new_row = row + neigh[0]
            new_col = col + neigh[1]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and (
                    board[new_row][new_col] == 1 or board[new_row][new_col] == 3):
                count += 1
        return count

sol=Solution()
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))



