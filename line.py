class Line(object):

    unknown = "."
    filled = "X"
    empty = "_"

    def __init__(self, length, hints, index):
        self.line_list = [self.unknown] * length
        self.hints = hints
        self.length = length
        self.index = index

    def is_solved(self):
        return self.as_hints() == self.hints

    def update_string(self, position, value):
        self.line_list[position] = value

    def find_definite_squares(self):
        definite_positions = []
        if sum(self.hints) > self.length/2:
            forwards_list = self.get_hints_as_bool_list(self.hints)
            backwards_list = self.get_hints_as_bool_list(self.hints[::-1])[::-1]
            for i in range(self.length):
                if backwards_list[i] and forwards_list[i]:
                    definite_positions.append(i)
        return definite_positions

    def get_unknown_square_positions(self):
        positions = []
        for i in range(self.length):
            if self.line_list[i] == self.unknown:
                positions.append(i)
        return positions

    def get_hints_as_bool_list(self, hints):
        bool_list = []
        for num in hints:
            bool_list.extend([True]*num)
            bool_list.append(False)
        diff = self.length - len(bool_list)
        if diff > 0:
            bool_list.extend([False]*diff)
        else:
            bool_list = bool_list[0:self.length]
        return bool_list

    def get_ratio(self):
        num_expected_to_be_filled = sum(self.hints)
        num_currently_filled = self.line_list.count(self.filled)

        num_left_to_be_filled = num_expected_to_be_filled - num_currently_filled
        num_currently_unknown = self.line_list.count(self.unknown)

        ratio = num_left_to_be_filled / num_currently_unknown
        return ratio

    def as_hints(self):
        hints = []
        num = 0
        for square in self.line_list:
            if square == "X":
                num += 1
            elif num > 0:
                hints.append(num)
                num = 0
        if num > 0:
            hints.append(num)
        return hints

    def __str__(self):
        return "".join(self.line_list)
