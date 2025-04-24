import time
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "root"
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, p1, p2, top=True, bottom=True, left=True, right=True, window=None):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.win = window
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        if self.has_top_wall:
            self.win.draw_line(Line(self.p1, Point(self.p2.x, self.p1.y)))

        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.p1.x, self.p2.y), self.p2))

        if self.has_left_wall:
            self.win.draw_line(Line(self.p1, Point(self.p1.x, self.p2.y)))

        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.p2.x, self.p1.y), self.p2))

    def center_point(self):
        return Point(self.p1.x + ((self.p2.x - self.p1.x) / 2), self.p1.y + ((self.p2.y - self.p1.y) / 2))

    def draw_move(self, to_cell, undo=False):
        self_center = self.center_point()
        to_center = to_cell.center_point()
        color = "gray" if undo else "red"
        self.win.draw_line(Line(self_center, to_center), color)


class Maze:
    def __init__(self, p, n_rows, n_cols, cell_size_x, cell_size_y, win=None):
        self.start_point = p
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.self_size_x = cell_size_x
        self.self_size_y = cell_size_y
        self.window = win
        self.cells = []

    def create_cells(self):
        for i in range(0, self.n_cols):
            tmp = []
            for j in range(0, self.n_rows):
                tmp.append(Cell(Point(i * self.self_size_x, j * self.self_size_y),
                                Point(i * self.self_size_x + self.self_size_x,
                                      j * self.self_size_y + self.self_size_y)
                                , window=self.window))
            self.cells.append(tmp)

        if self.window is None:
            return

        for col in self.cells:
            for cell in col:
                cell.draw()
                self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(0.01)
