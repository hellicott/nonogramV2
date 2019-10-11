from grid import Grid
from nonogram_reader import NonogramReader


class NonogramSolver(object):

    def __init__(self, grid: Grid):
        self.grid = grid

    def solve(self):
        num_iterations = 0
        while not self.grid.is_solved() and num_iterations < 1000000:
            num_iterations += 1
            self.grid.setup_grid()
            self.grid.attempt_to_solve()
            self.print_info(num_iterations)
        if self.grid.is_solved():
            self.grid.fill_completed_lines()
            self.print_info(num_iterations)
        else:
            print("*" * 30)
            print("*** COULD NOT BE SOLVED :( ***")
            print("*" * 30)

    def print_info(self, num):
        print("Iteration num: {}".format(num))
        print(self.grid)
        print("SOLVED? {}".format(self.grid.is_solved()))
        print("-" * 40)


def main():
    path = r"C:\Users\HEllicott\Documents\FlamingGoats\Challenges\nonogramV2\nonogram_inputs\tv.json"
    reader = NonogramReader(path)
    row_hints, column_hints = reader.get_row_and_column_hints()
    grid = Grid(row_hints, column_hints)
    print(grid)
    solver = NonogramSolver(grid)
    solver.solve()


main()
