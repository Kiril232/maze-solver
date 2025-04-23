from graphics import Window, Point, Line, Cell, Maze

if __name__ == "__main__":
    win = Window(800, 600)
    maze = Maze(Point(0,0), 3, 3, 100, 100, win)
    maze.create_cells()
    win.wait_for_close()
