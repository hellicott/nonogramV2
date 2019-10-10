class Line(object):

    unknown = "."
    filled = "X"
    empty = "_"

    def __init__(self, length, hints):
        self.line_string = self.unknown*length
        self.hints = hints

    def is_solved(self):
        return self.as_hints() == self.hints

    def update_string(self, position, value):
        self.line_string[position] = value

    def as_hints(self):
        hints = []
        num = 0
        for square in self.line_string:
            if square == "X":
                num += 1
            elif num > 0:
                hints.append(num)
                num = 0
        if num > 0:
            hints.append(num)
        return hints
