class Solution:
    def isValidRow(self, row):
        # print(self.board)
        # print(self.board[row])
        for i in range(1, 10):
            if self.board[row].count(i) > 1:
                return False

    def isValidColumn(self, col):
        column = []
        for i in range(9):
            column.append(self.board[i][col])
        # print(column)
        for i in range(1, 10):
            if column.count(i) > 1:
                return False

    def isValidBox(self, row, col):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[row*3 + i][col*3 + j])
        # print(box)
        for i in range(1, 10):
            if box.count(i) > 1:
                return False

    def convertStrBoard2Int(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    board[r][c] = int(board[r][c])
                else:
                    board[r][c] = 0
        return board

    def isValidSudoku(self, board) -> bool:
        self.board = self.convertStrBoard2Int(board)
        # self.isValidRow(0)
        # self.isValidColumn(0)
        # self.isValidColumn(8)
        # self.isValidBox(0, 0)
        # self.isValidBox(2, 2)
        for r in range(9):
            if self.isValidRow(r) == False:
                return False
        for c in range(9):
            if self.isValidColumn(c) == False:
                return False
        for r in range(3):
            for c in range(3):
                if self.isValidBox(r, c) == False:
                    return False
        return True


s = Solution()

board = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


print(s.isValidSudoku(board))
