import time


class Solution:
    def convertStrBoard2Int(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    board[r][c] = int(board[r][c])
                else:
                    board[r][c] = 0
        return board

    def initStat(self):
        # self.cnt = [[0]*9]*9
        # self.br = [[0]*9]*9
        self.cnt = []
        self.br = []
        for i in range(9):
            self.cnt.append([0]*9)
            self.br.append([0]*9)

    def printBoard(self, board):
        for r in range(9):
            print(board[r])
        print("")

    def printLeetCodeAndswer(self, board):
        print('[["{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}"],'.format(board[0][0], board[0]
              [1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7], board[0][8]), end="")
        for r in range(1, 8):
            print('["{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}"],'.format(board[r][0], board[r][1],
                  board[r][2], board[r][3], board[r][4], board[r][5], board[r][6], board[r][7], board[r][8]), end="")
        print('["{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}"]]'.format(board[8][0], board[8]
              [1], board[8][2], board[8][3], board[8][4], board[8][5], board[8][6], board[8][7], board[8][8]), end="")

        for r in range(9):
            for c in range(9):
                self.leetcodeBoard[r][c] = str(board[r][c])

    nodes = 0

    def ok(self, i, j):
        v = self.board[i][j]
        self.board[i][j] = 0

        # isValidRow
        for r in range(9):
            if self.board[r][j] == v:
                return False

        # isValidColumn
        for c in range(9):
            if self.board[i][c] == v:
                return False

        # isValidBox
        row = int((i-(i % 3))/3)
        col = int((j-(j % 3))/3)
        for r in range(3):
            for c in range(3):
                if self.board[row*3 + r][col*3 + c] == v:
                    return False

        self.board[i][j] = v
        return True

    def display(self):
        print("=== solution ===")
        self.printBoard(self.board)
        print("=== nodes ===")
        print("self.nodes", self.nodes)
        print("=== cnt ===")
        self.printBoard(self.cnt)
        print("=== br ===")
        self.printBoard(self.br)

    def display4LeetCode(self):
        self.printLeetCodeAndswer(self.board)
        self.printBoard(self.leetcodeBoard)
        exit()

    def solve(self, i, j):
        if j == 9:
            j = 0
            i += 1

        if i == 9 and j == 0:
            self.display()
            # self.display4LeetCode()
            return

        self.nodes += 1
        self.cnt[i][j] += 1

        if self.board[i][j] != 0:
            self.br[i][j] += 1
            self.solve(i, j+1)
            return

        for v in range(1, 10):
            self.board[i][j] = v
            if self.ok(i, j):
                self.br[i][j] += 1
                self.solve(i, j+1)
            self.board[i][j] = 0

    def solveSudoku(self, board) -> None:
        self.board = self.convertStrBoard2Int(board)
        self.leetcodeBoard = board
        self.initStat()
        self.solve(0, 0)


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


def stop_timing(start):
    end = time.process_time()
    print("執行時間：%f 秒" % (end - start))


try:
    start = time.process_time()
    s.solveSudoku(board)

finally:
    stop_timing(start)
