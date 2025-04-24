import unittest

from graphics import Maze, Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        m1.create_cells()
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_null_maze_create_cells(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        m1.create_cells()
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )


if __name__ == "__main__":
    unittest.main()
