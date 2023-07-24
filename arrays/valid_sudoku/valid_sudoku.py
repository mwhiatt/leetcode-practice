import collections

class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                curr = board[row][col]
                if curr == '.':
                    continue
                if curr in rows[row]:
                    return False
                if curr in cols[col]:
                    return False
                if curr in grid[(row // 3, col // 3)]:
                    return False
                rows[row].add(curr)
                cols[col].add(curr)
                grid[(row // 3, col // 3)].add(curr)
        return True