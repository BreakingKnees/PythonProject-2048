import random
import file_manager
from file_manager import highscore, save_highscore

score = 0

def add_tile(board, size):
    empty = [(i, j) for i in range(size) for j in range(size) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.9 else 4

def compress(row, size):
    r = [x for x in row if x != 0]
    r += [0] * (size - len(r))
    return r

def merge(row, size):
    global score

    for i in range(size - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0

            # FIX: use real shared highscore
            if score > file_manager.highscore:
                file_manager.highscore = score
                file_manager.save_highscore()
    return row


def left(board, size):
    new = []
    for row in board:
        row = compress(row, size)
        row = merge(row, size)
        row = compress(row, size)
        new.append(row)
    return new

def right(board, size):
    new = [row[::-1] for row in board]
    new = left(new, size)
    new = [row[::-1] for row in new]
    return new

def transpose(board):
    return [list(r) for r in zip(*board)]

def up(board, size):
    t = transpose(board)
    t = left(t, size)
    return transpose(t)

def down(board, size):
    t = transpose(board)
    t = right(t, size)
    return transpose(t)

def over(board, size):
    for row in board:
        if 0 in row:
            return False
    for i in range(size):
        for j in range(size - 1):
            if board[i][j] == board[i][j + 1]:
                return False
    for i in range(size - 1):
        for j in range(size):
            if board[i][j] == board[i + 1][j]:
                return False
    return True
