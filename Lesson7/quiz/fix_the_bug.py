# Fix the Bug

def count(number, row):
    return reduce(lambda acc, this: (1 + acc) if this == number else acc, row, 0)

def horiz_checker(board):
    size = len(board) - 1
    for row in range(size):
        if not (all(map(lambda x : count(x, board[row]) <= 1, board[row]))): return False
    return True

board_good = [[1,2,3],
              [4,5,6],
              [7,8,9]]

board_bad = [[1,1,1],
             [4,5,6],
             [7,8,9]]

board_bug = [[1,2,3],
             [4,4,4],
             [7,8,9]]

print(horiz_checker(board_good))
print(horiz_checker(board_bad))
print(horiz_checker(board_bug))