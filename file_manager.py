SCORE_FILE = "highscore.txt"
highscore = 0

def load_highscore():
    global highscore
    try:
        with open(SCORE_FILE, "r") as f:
            highscore = int(f.read())
    except:
        highscore = 0

def save_highscore():
    with open(SCORE_FILE, "w") as f:
        f.write(str(highscore))
