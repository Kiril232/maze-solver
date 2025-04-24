from graphics import Window, Point, Line, Cell, Maze

if __name__ == "__main__":
    win = Window(800, 600)
    m1 = Maze(Point(0, 0), 5, 5, 50, 50, win)
    m1.create_cells()
    m1.break_entrance_and_exit()
    m1.break_walls_r(0, 0)
    m1.draw_cells()
    win.wait_for_close()
