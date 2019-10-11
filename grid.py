from line import Line
import random


class Grid(object):

    def __init__(self, row_hints, column_hints):
        self.row_hints = row_hints
        self.column_hints = column_hints
        self.rows = []
        self.columns = []
        self.unsolved_rows = []
        self.unsolved_columns = []
        self.unsolved_row_nums = {}
        self.setup_grid()

    def setup_grid(self):
        self.unsolved_rows.clear()
        self.unsolved_columns.clear()
        self.rows, self.columns = self._create_grid()
        self.fill_definite_squares()
        self.fill_completed_lines()
        for row in self.rows:
            if not row.is_solved():
                self.unsolved_rows.append(row)
        for column in self.columns:
            if not column.is_solved():
                self.unsolved_columns.append(column)


    def _create_grid(self):
        rows = self._create_lines(len(self.row_hints), len(self.column_hints), self.row_hints)
        columns = self._create_lines(len(self.column_hints), len(self.row_hints), self.column_hints)
        return rows, columns

    @staticmethod
    def _create_lines(num_of_lines, length, hints):
        line_list = []
        for i in range(num_of_lines):
            line = Line(length, hints[i], i)
            line_list.append(line)
        return line_list

    def fill_square(self, row_num, column_num):
        self._insert_value_to_grid(row_num, column_num, Line.filled)

    def empty_square(self, row_num, column_num):
        self._insert_value_to_grid(row_num, column_num, Line.empty)

    def _insert_value_to_grid(self, row_num, column_num, value):
        self.rows[row_num].update_string(column_num, value)
        self.columns[column_num].update_string(row_num, value)

    def all_lines(self):
        all_lines = self.rows + self.columns
        return all_lines

    def is_solved(self):
        for line in self.all_lines():
            if line.is_solved():
                continue
            else:
                return False
        return True

    def attempt_to_solve(self):
        for unsolved_row in self.unsolved_rows:
            row_ratio = unsolved_row.get_ratio()
            for unsolved_col_num in unsolved_row.get_unknown_square_positions():
                col_ratio = self.columns[unsolved_col_num].get_ratio()
                ratio = (col_ratio + row_ratio) / 2
                if self.random_bool(ratio):
                    self.fill_square(unsolved_row.index, unsolved_col_num)

    # def attempt_to_solve(self):
    #     for row_num in range(len(self.unsolved_rows)):
    #         row_ratio = self.unsolved_rows[row_num].get_ratio()
    #         for col_num in range(len(self.unsolved_columns)):
    #             column_ratio = self.unsolved_columns[col_num].get_ratio()
    #             ratio = (column_ratio + row_ratio) / 2
    #             if self.random_bool(ratio):
    #                 self.fill_square(self.unsolved_rows[row_num].index,
    #                                  self.unsolved_columns[col_num].index)

    @staticmethod
    def random_bool(ratio):
        return random.randint(0, 100) < (ratio * 100)

    def fill_definite_squares(self):
        for i in range(len(self.rows)):
            definite_positions = self.rows[i].find_definite_squares()
            for position in definite_positions:
                self.fill_square(i, position)
        for i in range(len(self.columns)):
            definite_positions = self.columns[i].find_definite_squares()
            for position in definite_positions:
                self.fill_square(position, i)

    def fill_completed_lines(self):
        for i in range(len(self.rows)):
            if self.rows[i].is_solved():
                positions = self.rows[i].get_unknown_square_positions()
                for position in positions:
                    self.empty_square(i, position)
        for i in range(len(self.columns)):
            if self.columns[i].is_solved():
                positions = self.columns[i].get_unknown_square_positions()
                for position in positions:
                    self.empty_square(position, i)
            
    def __str__(self):
        return "\n".join([str(row) for row in self.rows])
