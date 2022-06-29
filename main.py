from tkinter import *
import cell
import settings as sett
import utils

root = Tk()
# initialising window element of tkinter
# taking root is the convention

Button(root, text='Click to Continue', padx=10, pady=5, command=sett.askMe()).pack(pady=20)

root.configure(bg='black')
root.geometry(f'{sett.WIDTH}x{sett.HEIGHT}')  # defines size; width x height
root.title('Minesweeper')

# by default window is resizable, this may prove disadvantageous
# root.resizable(False, False)  # false twice; once for width and height each

# the window is divided into multiple frames
top_frame = Frame(
    root,
    bg='#1f1b18',
    width=sett.WIDTH,
    height=utils.height_prct(sett.topFrameHeightPrct)
)  # initialising the frame
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='#1f1b18',
    height=utils.height_prct(sett.leftFrameHeightPrct),
    width=utils.width_prct(sett.leftFrameWidthPrct),
    highlightbackground="#de6d41",
    highlightthickness=2
)
left_frame.place(x=0, y=utils.height_prct(sett.topFrameHeightPrct))

right_frame = Frame(
    root,
    bg='#1f1b18',
    height=utils.height_prct(sett.rightFrameHeightPrct),
    width=utils.width_prct(sett.rightFrameWidthPrct),
    highlightbackground="#de6d41",
    highlightthickness=2
)
right_frame.place(
    x=utils.width_prct(sett.centerFrameWidthPrct + sett.leftFrameWidthPrct),
    y=utils.height_prct(sett.topFrameHeightPrct)
)

center_frame = Frame(
    root, bg='#1f1b18',
    width=utils.width_prct(sett.centerFrameWidthPrct),
    height=utils.height_prct(sett.centerFrameHeightPrct)
)
center_frame.place(
    x=utils.width_prct(sett.leftFrameWidthPrct),
    y=utils.height_prct(sett.topFrameHeightPrct)
)

center_frame.grid_propagate(False)  # to disable frame to change size when grid is used
left_frame.grid_propagate(False)
top_frame.grid_propagate(False)

# grid is used to align elements easily and dynamically ; used instead of place
for x in range(sett.GRID_SIZE):
    for y in range(sett.GRID_SIZE):
        c = cell.Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=y, row=x,
            padx=2, pady=2,
        )

cell.Cell.create_cell_count_label(left_frame)
cell.Cell.cell_count_label_object.grid(
    row=0, column=0, padx=5, pady=3
)

cell.Cell.create_mine_count_label(left_frame)
cell.Cell.mine_count_label_object.grid(
    row=2, column=0, padx=5, pady=3
)

cell.Cell.create_score_label(left_frame)
cell.Cell.score_label_object.grid(
    row=4, column=0, padx=5, pady=3
)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='MINESWEEPER GAME',
    font=('', 20)
)
game_title.place(
    x=utils.width_prct(25),
    y=utils.height_prct(1)
)
cell.Cell.randomize_mines()

root.mainloop()  # telling the root object to run until we close it
#
# c1=Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column=0,
#     row=0
# )
#
# btn1 = Button(
#     center_frame,
#     bg='blue',
#     text = 'FIRST Button'
# )
# btn1.place(x=0,y=0)
