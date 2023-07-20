class Solution:
    def convertStrBoard2Int(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    board[r][c] = int(board[r][c])
                else:
                    board[r][c] = 0
        return board

    def getRow(self, row):
        return self.board[row]

    def isValidRow(self, row):
        row = self.getRow(row)
        for i in range(1, 10):
            if row.count(i) > 1:
                return False

    def getCol(self, col):
        column = []
        for i in range(9):
            column.append(self.board[i][col])
        return column

    def isValidColumn(self, col):
        column = self.getCol(col)
        for i in range(1, 10):
            if column.count(i) > 1:
                return False

    def getBox(self, row, col):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[row*3 + i][col*3 + j])
        return box

    def isValidBox(self, row, col):
        box = self.getBox(row, col)
        for i in range(1, 10):
            if box.count(i) > 1:
                return False

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

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.board = self.convertStrBoard2Int(board)
        # r = self.getRow(0)
        # m = self.findMissing(r)
        b = self.getBox(0, 0)
        m = self.findMissing(b)
        # print(m)

        lists = list(self.permutations(m))
        print("lists", lists)

        r0_missing = self.findMissing(self.getRow(0))
        r1_missing = self.findMissing(self.getRow(1))
        r2_missing = self.findMissing(self.getRow(2))

        lists_r0_ok = []
        lists_r1_ok = []
        lists_r2_ok = []

        for l in lists:
            if l[0] in r0_missing:
                lists_r0_ok.append(l)
        print("lists_r0_ok", lists_r0_ok)

        for l in lists_r0_ok:
            if l[0] in r1_missing:
                lists_r1_ok.append(l)
        print("lists_r1_ok", lists_r1_ok)


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


print(s.solveSudoku(board))
