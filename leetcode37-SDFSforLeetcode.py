import time


class Solution:

    def solveSudoku(self, board) -> None:
        pass


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
