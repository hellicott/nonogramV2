from line import Line
from grid import Grid


class Solver(object):

    def __init__(self, grid: Grid):
        self.grid = grid

    def solve(self):
        while not self.grid.is_solved():
            break
