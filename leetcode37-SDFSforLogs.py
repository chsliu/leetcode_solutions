import os
import platform
from datetime import datetime
import sys
import time


class Solution:
    solved = False
    nodes = 0

    def initStat(self):
        self.solved = False
        self.nodes = 0
        self.cnt = []
        self.br = []
        for i in range(9):
            self.cnt.append([0]*9)
            self.br.append([0]*9)

    def display(self):
        # print(self.board)
        # self.printLeetCodeAndswer(self.board)
        # exit()
        print("=== solution ===")
        self.printBoard(self.board)
        print("=== nodes ===")
        print("self.nodes", self.nodes)
        print("=== cnt ===")
        self.printBoard(self.cnt)
        print("=== br ===")
        self.printBoard(self.br)

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
        print()

    def ok(self, i, j):
        v = self.board[i][j]
        self.board[i][j] = '.'

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

    def solve(self, i, j):
        if j == 9:
            j = 0
            i += 1

        if i == 9 and j == 0:
            self.solved = True
            # self.display()
            # self.display4LeetCode()
            return

        self.nodes += 1
        self.cnt[i][j] += 1

        if self.nodes % 100000 == 0:
            print("nodes", self.nodes)

        if self.board[i][j] != '.':
            self.br[i][j] += 1
            self.solve(i, j+1)
            return

        for v in range(1, 10):
            self.board[i][j] = str(v)
            if self.ok(i, j):
                self.br[i][j] += 1
                self.solve(i, j+1)
            if self.solved:
                return
            self.board[i][j] = '.'

    def solveSudoku(self, board) -> None:
        self.board = board
        self.initStat()
        self.solve(0, 0)
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


def stop_timing(start):
    end = time.process_time()
    print("執行時間：%f 秒" % (end - start))


def main():
    try:
        start = time.process_time()
        s.solveSudoku(board)

    finally:
        stop_timing(start)


def line2sudokuboard(line):
    # board = []
    # for i in range(9):
    #     s = line[i*9:i*9+9]
    #     board.append([*s])
    # return board
    board = []
    for i in range(9):
        board.append([0]*9)
    for i in range(9):
        for j in range(9):
            board[i][j] = line[i*9+j]
    return board


def getSolution(board):
    line = ""
    for i in range(9):
        for j in range(9):
            # line.append(board[i][j])
            line += board[i][j]
    return line


def main2():

    # print("sys.argv", sys.argv)

    if len(sys.argv) < 2:
        print("Usage: python3 leetcode37.py <filename>")
        exit()

    # print(platform.node())
    questionfilename = sys.argv[1].split("\\")[1]
    # print("questionfilename", questionfilename)

    data = open(sys.argv[1], "r")
    # data = open("sudoku_puzzles\puzzles6_forum_hardest_1106", "r")

    print("Solving sudoku from file:", sys.argv[1])

    path = "logs"
    if not os.path.exists(path):
        os.makedirs(path)

    log_filename = datetime.strftime(
        datetime.now(), '%Y%m%d_%H%M%S')
    log_filename += "_"+platform.node()+"_" + questionfilename+".csv"
    log = open("logs/"+log_filename, "w")

    print("Writing log file:", "logs/"+log_filename)

    path = "solutions"
    if not os.path.exists(path):
        os.makedirs(path)

    solution_filename = questionfilename+"_solutions"+".txt"
    solutions = open("solutions/"+solution_filename, "w")

    print("Writing solution file:", "solutions/"+solution_filename)

    print()

    log.write("lineno,runtime,nodes,solution\n")

    lineno = 0
    start0 = time.process_time()
    for line in data:
        lineno += 1
        # print("line", line)
        if line[0] == "#":
            continue
        board = line2sudokuboard(line)
        # print("board", board)
        # print("board", board[0][0])
        print("Solving question on line", lineno, "...")
        # start = time.process_time()
        start = time.time()
        s.solveSudoku(board)
        end = time.time()
        # s.display()
        # logline = str(lineno)+","+str(end - start)+","+s.board+"\n"
        logline = str(lineno)+","+str(end - start)+","+str(s.nodes)+","+"\n"
        log.write(logline)

        solutions.write(str(lineno)+","+getSolution(s.board)+"\n")
        # log.close()
        # exit()

    end0 = time.process_time()
    logline = "-1"+","+str(end0 - start0)+","+"0"+","+"\n"
    # log.write(logline)


if __name__ == "__main__":
    # main()
    main2()
