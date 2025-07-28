from collections import defaultdict

def is_valid_sudoku(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    boxes = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            if (board[i][j] in rows[i] or
                board[i][j] in cols[j] or
                board[i][j] in boxes[(i // 3, j // 3)]):
                return False
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            boxes[(i // 3, j // 3)].add(board[i][j])
    
    return True
# Example usage
board = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
print(f"Input: {board}")
print(f"Output: {is_valid_sudoku(board)} (represents {'valid' if is_valid_sudoku(board) else 'invalid'} Sudoku board)")