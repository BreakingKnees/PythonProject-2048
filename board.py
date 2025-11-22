from file_manager import highscore

RESET = "\033[0m"
BOLD = "\033[1m"

COLORS = {
    2:    BOLD + "\033[38;5;222m",
    4:    BOLD + "\033[38;5;220m",
    8:    BOLD + "\033[38;5;214m",
    16:   BOLD + "\033[38;5;208m",
    32:   BOLD + "\033[38;5;202m",
    64:   BOLD + "\033[38;5;196m",
    128:  BOLD + "\033[38;5;226m",
    256:  BOLD + "\033[38;5;227m",
    512:  BOLD + "\033[38;5;228m",
    1024: BOLD + "\033[38;5;229m",
    2048: BOLD + "\033[38;5;230m",
}

BORDER_COLOR = "\033[37m"

def print_board(board, size, score):
    print(f"Score: {score} | High Score: {highscore}")
    line = BORDER_COLOR + ("+------" * size) + "+" + RESET
    print("\n" + line)
    for row in board:
        for num in row:
            if num != 0:
                color = COLORS.get(num, "\033[107m\033[30m")
                cell = f"{color}{str(num).center(6)}{RESET}"
            else:
                cell = " ".center(6)
            print(f"{BORDER_COLOR}|{RESET}{cell}", end="")
        print(f"{BORDER_COLOR}|{RESET}")
        print(line)
