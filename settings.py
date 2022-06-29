# this file is for storing variables to avoid hard coding the data
from tkinter import messagebox

WIDTH_STARTUP = 700
HEIGHT_SATARTUP = 500

topFrameHeightPrct_startup = 10
centerFrameHeightPrct_startup = 70
bottomFrameHeightPrct_startup = 20
LEVELS = 'BEGINNER', 'INTERMEDIATE', 'ADVANCED'
LEVEL = LEVELS[0]
WIDTH = 700 if LEVEL == 'BEGINNER' else (945 if LEVEL == 'INTERMEDIATE' else 1090)
HEIGHT = 490 if LEVEL == 'BEGINNER' else (575 if LEVEL == 'INTERMEDIATE' else 850)
GRID_SIZE = 9 if LEVEL == 'BEGINNER' else (16 if LEVEL == 'INTERMEDIATE' else 24)
MINES_COUNT = 10 if LEVEL == 'BEGINNER' else (40 if LEVEL == 'INTERMEDIATE' else 99)
CELL_WIDTH = 5 if LEVEL == 'BEGINNER' else (4 if LEVEL == 'INTERMEDIATE' else 3)
CELL_HEIGHT = 2 if LEVEL == 'BEGINNER' else 1
CELL_COUNT = GRID_SIZE ** 2

# below values in percent; for frames
topFrameHeightPrct = 10

leftFrameHeightPrct = 100 - topFrameHeightPrct
leftFrameWidthPrct = 17 if LEVEL == 'BEGINNER' else (12.5 if LEVEL == 'INTERMEDIATE' else 11)

centerFrameHeightPrct = 100 - topFrameHeightPrct
centerFrameWidthPrct = 100 - (2 * leftFrameWidthPrct)

rightFrameWidthPrct = leftFrameWidthPrct
rightFrameHeightPrct = 100 - topFrameHeightPrct


# noinspection SpellCheckingInspection
def setLevel(LEVEL):
    global WIDTH
    WIDTH = 700 if LEVEL == 'BEGINNER' else (945 if LEVEL == 'INTERMEDIATE' else 1090)
    global HEIGHT
    HEIGHT = 490 if LEVEL == 'BEGINNER' else (575 if LEVEL == 'INTERMEDIATE' else 850)
    global GRID_SIZE
    GRID_SIZE = 9 if LEVEL == 'BEGINNER' else (16 if LEVEL == 'INTERMEDIATE' else 24)
    global MINES_COUNT
    MINES_COUNT = 10 if LEVEL == 'BEGINNER' else (40 if LEVEL == 'INTERMEDIATE' else 99)
    global CELL_WIDTH
    CELL_WIDTH = 5 if LEVEL == 'BEGINNER' else (4 if LEVEL == 'INTERMEDIATE' else 3)
    global CELL_HEIGHT
    CELL_HEIGHT = 2 if LEVEL == 'BEGINNER' else 1
    global CELL_COUNT
    CELL_COUNT = GRID_SIZE ** 2
    global leftFrameWidthPrct
    leftFrameWidthPrct = 17 if LEVEL == 'BEGINNER' else (12.5 if LEVEL == 'INTERMEDIATE' else 11)
    global leftFrameHeightPrct

    # noinspection SpellCheckingInspection
    leftFrameHeightPrct = 100 - topFrameHeightPrct
    global centerFrameHeightPrct
    centerFrameHeightPrct = 100 - topFrameHeightPrct
    global centerFrameWidthPrct
    centerFrameWidthPrct = 100 - (2 * leftFrameWidthPrct)

    global rightFrameWidthPrct
    rightFrameWidthPrct = leftFrameWidthPrct
    global rightFrameHeightPrct
    rightFrameHeightPrct = 100 - topFrameHeightPrct


def askMe():
    # Level select function
    while True:
        res = messagebox.askquestion('Level select', 'Are you a beginner?')
        if res == 'yes':
            setLevel('BEGINNER')
            return
        elif res == 'no':
            res = messagebox.askquestion('Level select', 'Are you an intermediate player?')
            if res == 'yes':
                setLevel('INTERMEDIATE')
                return
            elif res == 'no':
                res = messagebox.askquestion('Level select', 'Are you an advanced player?')
                if res == 'yes':
                    setLevel('ADVANCED')
                    return

        else:
            res = messagebox.askquestion('Level select', 'Select appropriate level(Yes)\n else quit(No)')
            if res == 'yes':
                continue
            else:
                exit()
