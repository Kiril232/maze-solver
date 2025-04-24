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

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        m1.create_cells()
        m1.break_entrance_and_exit()
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False
        )

        self.assertEqual(
            m1.cells[-1][-1].has_bottom_wall,
            False
        )

    def test_visited_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        m1.create_cells()
        m1.break_entrance_and_exit()
        m1.break_walls_r(0, 0)
        m1.reset_cells_visited()
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m1.cells[i][j].visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()
