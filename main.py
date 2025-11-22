import os
import keyboard

from file_manager import load_highscore
from board import print_board
from game_logic import (
    add_tile, left, right, up, down, over
)
import game_logic
import file_manager

size = 4

def get_key():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "up":
                return "w"
            elif event.name == "down":
                return "s"
            elif event.name == "left":
                return "a"
            elif event.name == "right":
                return "d"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ---- GAME START ----
load_highscore()
game_logic.score = 0

board = [[0] * size for _ in range(size)]
add_tile(board, size)
add_tile(board, size)

print_board(board, size, game_logic.score)

while True:
    print("Use arrow keys ✨")
    move = get_key()

    old = [row[:] for row in board]

    if move == "a":
        board = left(board, size)
    elif move == "d":
        board = right(board, size)
    elif move == "w":
        board = up(board, size)
    elif move == "s":
        board = down(board, size)

    if old != board:
        add_tile(board, size)

    clear_screen()
    print_board(board, size, game_logic.score)

    if over(board, size):
        print("💀 Game Over!")
        break
