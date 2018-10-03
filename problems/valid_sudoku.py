# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku
import unittest


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for k in range(0, 3):
            for i in range(0, 9):
                check_list = [False] * 9
                for j in range(0, 9):
                    # vertical
                    if k == 0:
                        ch = board[i][j]
                    # horizontal
                    elif k == 1:
                        ch = board[j][i]
                    # sub grid
                    else:
                        ch = board[(j // 3) + (i // 3) * 3][(j % 3) + ((i * 3) % 9)]
                        print(ch)
                    if ch == '.':
                        continue
                    val = int(ch) - 1

                    if check_list[val]:
                        return False
                    check_list[val] = True
        return True


class TestValidSudoku(unittest.TestCase):
    def test(self):
        sol = Solution()
        board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], 
                 ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
                 ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
                 ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
                 ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
                 ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
                 ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
                 ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
                 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
        self.assertEqual(
            sol.isValidSudoku(board),
            True
        )


if __name__ == '__main__':
    unittest.TestCase()
