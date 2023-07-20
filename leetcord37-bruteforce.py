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

    def isValidRow(self, board, row):
        for i in range(1, 10):
            if board[row].count(i) > 1:
                return False

    def isValidColumn(self, board, col):
        column = []
        for i in range(9):
            column.append(board[i][col])
        for i in range(1, 10):
            if column.count(i) > 1:
                return False

    def isValidBox(self, board, row, col):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(board[row*3 + i][col*3 + j])
        for i in range(1, 10):
            if box.count(i) > 1:
                return False

    count = 0

    def printCount(self):
        print("count:", self.count)
        self.count = self.count + 1

    validcount = 0

    def isValidSudoku(self, board) -> bool:
        print("isValid", self.validcount)
        self.validcount = self.validcount + 1
        # print("count:", self.count)
        # self.count = self.count + 1
        self.printBoard(board)
        for r in range(9):
            if self.isValidRow(board, r) == False:
                # print("Row", r, "not valid")
                return False
        for c in range(9):
            if self.isValidColumn(board, c) == False:
                # print("Column", c, "not valid")
                return False
        for r in range(3):
            for c in range(3):
                if self.isValidBox(board, r, c) == False:
                    # print("Box", r, c, "not valid")
                    return False
        return True

    def findMissing(self, l):
        m = []
        for i in range(1, 10):
            if i not in l:
                m.append(i)
        return m

    def permutations(self, str):
        if len(str) <= 1:
            yield str
        else:
            for perm in self.permutations(str[1:]):
                for i in range(len(perm)+1):
                    # nb str[0:1] works in both string and list contexts
                    yield perm[:i] + str[0:1] + perm[i:]

    def printBoard(self, board):
        for r in range(9):
            print(board[r])
        print("")

    def copyBoard(self, board):
        newBoard = []
        for i in range(9):
            newBoard.append(board[i][:])
        return newBoard

    def checkPartialCol(self, board, row, col):
        nums = set()
        for r in range(row+1):
            if board[r][col] not in nums:
                nums.add(board[r][col])
        if len(nums) < row+1:
            return False
        return True

    def fillRow(self, board, row):
        # boards = []
        r = self.board[row]
        m = self.findMissing(r)

        lists = list(self.permutations(m))
        # print("lists", lists)
        for l in lists:
            # b = board.copy()
            b = self.copyBoard(board)
            # self.printBoard(b)
            # print("row", row, "list", l)
            for i in range(9):
                if b[row][i] == 0:
                    b[row][i] = l.pop(0)
            ###
            # checking if column has duplicate numbers
            ###
            toAdd = True
            for c in range(9):
                if not self.checkPartialCol(b, row, c):
                    toAdd = False
            ###
            # only Add When no duplicate numbers in column
            ###
            if toAdd:
                # boards.append(b)
                yield b
            # self.printBoard(b)
            # exit()
        # return boards
        # return None

    def solveRow(self, board, row):
        if row == 9:
            ans = self.isValidSudoku(board)
            if ans == True:
                # print(board)
                self.printBoard(board)
                exit()
        else:
            # boards = self.fillRow(board, row)
            # for b in boards:
            print("Row", row)
            for b in self.fillRow(board, row):
                # print("Row", row)
                # self.printCount()
                ans = self.solveRow(b, row + 1)
                if ans == False:
                    continue
            print("End Row", row)
            # self.printBoard(board)

    def solveSudoku(self, board) -> None:
        self.board = self.convertStrBoard2Int(board)
        self.solveRow(self.board, 0)


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

start = time.process_time()


def stop_timing():
    end = time.process_time()
    print("執行時間：%f 秒" % (end - start))


try:
    print(s.solveSudoku(board))

finally:
    stop_timing()
