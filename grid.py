from line import Line


class Grid(object):

    def __init__(self, num_of_rows, num_of_columns):
        self.rows = self.create_lines(num_of_rows, num_of_columns)
        self.columns = self.create_lines(num_of_columns, num_of_rows)

    @staticmethod
    def create_lines(num_of_lines, length):
        line_list = []
        for i in range(num_of_lines):
            line = Line(length)
            line_list.append(line)
        return line_list
