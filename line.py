class Line(object):

    unknown = "."
    filled = "X"
    empty = "_"

    def __init__(self, length):
        self.line_string = self.unknown*length
