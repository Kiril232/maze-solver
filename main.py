from graphics import Window, Point, Line, Cell, Maze

if __name__ == "__main__":
    win = Window(800, 600)
    m1 = Maze(Point(0, 0), 10, 12, 10, 10, win)
    m1.create_cells()
    win.wait_for_close()
