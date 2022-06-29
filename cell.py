import ctypes
from tkinter import Button, Label
import random
import settings
import sys


class Cell:
    score_label_object = None
    all = []  # stores all instances of cell

    cell_count = float('inf')  #settings.CELL_COUNT
    cell_count_label_object = None

    mine_count = float('inf') # settings.MINES_COUNT
    mine_count_label_object = None

    score = 0
    score_label = None

    def __init__(self, x, y, is_mine=False, is_clicked=False):
        """
            initialize the class
        """
        self.is_mine = is_mine
        self.isClicked = is_clicked
        self.x = x  # for cell identification
        self.y = y  # for cell identification

        self.cell_btn_object = None
        Cell.all.append(self)

        self.bg_color = '#dc6b3f'
        self.border = 3
        self.btn_state = 'normal'
        self.wide = settings.CELL_WIDTH
        self.high = settings.CELL_HEIGHT

    def create_btn_object(self, location):
        """create button object"""
        btn = Button(
            location,
            width=self.wide,
            height=self.high,
            bg=self.bg_color,
            fg='white',
            bd=self.border
        )

        btn.bind('<Button-1>', self.left_click_actions)  # adding events to the button
        # <Button-1> represents left click
        btn.bind('<Button-3>', self.right_click_actions)
        # 1st argument in the above functions represents the event that generates some stimuli
        # 2nd argument is reference to the function that is to be executed on some event

        self.cell_btn_object = btn  # accomplishing relationship between cell and button class instance

    @staticmethod
    def create_cell_count_label(location):
        """static method to create cell count label"""
        lbl = Label(
            location,
            bg="#e8dab3",
            fg="#48616a",
            width=10, height=3,
            font=("", 11),  # font property accepts tuple
            text=f"Cells Left: {Cell.cell_count}",
            padx=4, pady=4
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_mine_count_label(location):
        """static method to create mine count label"""
        lbl = Label(
            location,
            bg="#e8dab3",
            fg="#48616a",
            width=10, height=3,
            font=("", 11),  # font property accepts tuple
            text=f"Mines Left: {Cell.mine_count}",
            padx=4, pady=4
        )
        Cell.mine_count_label_object = lbl

    @staticmethod
    def create_score_label(location):
        """static method to create score label"""
        lbl = Label(
            location,
            bg="#e8dab3",
            fg="#48616a",
            width=10, height=3,
            font=("", 11),  # font property accepts tuple
            text=f"Score: {Cell.score}",
            padx=4, pady=4
        )
        Cell.score_label_object = lbl

    def left_click_actions(self, event):
        """action on left click"""
        if (
                self.is_mine and
                self.cell_btn_object.cget('text') != "FLAG"
        ):
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if (
                    Cell.cell_count == 0
            ):
                # generating dialog box
                ctypes.windll.user32.MessageBoxW(  # for windows
                    0,
                    'You Won the Game',
                    'Congratulations',
                    0
                )
        if (
                Cell.cell_count == 0
        ):
            # generating dialog box
            ctypes.windll.user32.MessageBoxW(  # for windows
                0,
                'You Won the Game',
                'Congratulations',
                0
            )
            sys.exit()

    @property  # can use it just like a property
    def surrounded_cells(self):
        """fetching surrounding cells of self instance"""
        cells = [
            self.get_cell_by_axes(self.x - 1, self.y - 1),
            self.get_cell_by_axes(self.x - 1, self.y),
            self.get_cell_by_axes(self.x - 1, self.y + 1),
            self.get_cell_by_axes(self.x, self.y - 1),
            self.get_cell_by_axes(self.x + 1, self.y - 1),
            self.get_cell_by_axes(self.x + 1, self.y),
            self.get_cell_by_axes(self.x + 1, self.y + 1),
            self.get_cell_by_axes(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property  # can use it just like a property
    def surrounded_cells_mines_length(self):
        """fetching number of surrounding cells that contain mines of self"""
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def get_cell_by_axes(self, x, y):
        """fetching cell object using x and y attributes"""
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        # self.cell_btn_object.configure(
        #     bg="red", text = "BOMB"
        # )
        """clicked on mine; display: game lost"""
        if not self.isClicked:
            ctypes.windll.user32.MessageBoxW(
                None,
                'You clicked on a mine',
                'GAME OVER!!!',
                0,
                "Capture.png"
            )
            sys.exit()

    def show_cell(self):
        """show cell clicked and not a mine"""
        if self.isClicked is False:
            Cell.cell_count -= 1
            Cell.score += 10
            if self.surrounded_cells_mines_length == 0:
                self.cell_btn_object.configure(bg="black", borderwidth=3, relief="sunken")
            else:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="black",
                    borderwidth=3, relief="sunken"
                )
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
        self.isClicked = True

    def right_click_actions(self, event):
        """action on right click"""
        # print(event) #prints the metadat of the event
        if self.cell_btn_object.cget('text') == "FLAG":
            self.cell_btn_object.configure(
                bg=self.bg_color,
                text="",
                state='normal'
            )
            Cell.cell_count += 1
            Cell.mine_count += 1
            self.isClicked = False
        else:
            self.cell_btn_object.configure(
                bg="green",
                text="FLAG"
            )
            Cell.cell_count -= 1
            Cell.mine_count -= 1
            Cell.score += 10
            self.isClicked = True
        Cell.cell_count_label_object.configure(
            text=f"Cells Left: {Cell.cell_count}"
        )
        if Cell.mine_count_label_object:
            Cell.mine_count_label_object.configure(
                text=f"Cells Left: {Cell.mine_count}"
            )

    @staticmethod
    def randomize_mines():
        """placing mines in random manner"""
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
