import json


class NonogramReader:
    def __init__(self, path_to_json_file):
        self.path = path_to_json_file

    def _read_json_puzzle_file(self):
        with open(self.path) as puzzle_file:
            hints = json.load(puzzle_file)
            return hints

    def get_row_and_column_hints(self):
        hints = self._read_json_puzzle_file()
        row_hints = hints["rows"]
        column_hints = hints["columns"]
        return row_hints, column_hints
