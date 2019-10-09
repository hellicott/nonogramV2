from line import Line


class Grid(object):

    def __init__(self, num_of_rows, num_of_columns, row_hints, column_hints):
        self.rows = self.create_lines(num_of_rows, num_of_columns, row_hints)
        self.columns = self.create_lines(num_of_columns, num_of_rows, column_hints)
        self.row_hints = row_hints
        self.column_hints = column_hints

    @staticmethod
    def create_lines(num_of_lines, length, hints):
        line_list = []
        for i in range(num_of_lines):
            line = Line(length, hints[i])
            line_list.append(line)
        return line_list

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
