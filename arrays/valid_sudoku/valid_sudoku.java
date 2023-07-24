package valid_sudoku;
import java.util.*;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> rowChars = null;
        Set<Character> colChars = null;
        Set<Character> blockChars = null;

        // check rows and columns
        for (int i = 0; i < board.length; i++) {
            rowChars = new HashSet<>();
            colChars = new HashSet<>();
            for (int j = 0; j < board[i].length; j++) {
                char leftRight = board[i][j];
                char upDown = board[j][i];
                if (leftRight != '.') {
                    if (rowChars.contains(leftRight)) {
                        return false;
                    }
                    rowChars.add(leftRight);
                }
                if (upDown != '.') {
                    if (colChars.contains(upDown)) {
                        return false;
                    }
                    colChars.add(upDown);
                }
            }
        }

        // check inner squares
        for (int i = 0; i < board.length; i+=3) {
            for (int j = 0; j < board[i].length; j+=3) {
                blockChars = new HashSet<>();
                for (int k = i; k < i+3; k++) {
                    for (int l = j; l < j+3; l++) {
                        if (board[k][l] == '.') {
                           continue;
                        }
                        if (blockChars.contains(board[k][l])) {
                            return false;
                        }
                        blockChars.add(board[k][l]);
                    }
                }
            }
        }
        return true;
    }
}
