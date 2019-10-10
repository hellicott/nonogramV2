from grid import Grid


class Solver(object):

    def __init__(self, grid: Grid):
        self.grid = grid

    def fill_definite_squares(self):
        for i in range(len(self.grid.rows)):
            definite_positions = self.grid.rows[i].find_definite_squares()
            for position in definite_positions:
                self.grid.fill_square(i, position)
        for i in range(len(self.grid.columns)):
            definite_positions = self.grid.columns[i].find_definite_squares()
            for position in definite_positions:
                self.grid.fill_square(position, i)

    def solve(self):
        self.fill_definite_squares()
        while not self.grid.is_solved():
            break
