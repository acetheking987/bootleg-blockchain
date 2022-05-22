import json

class file_handler():
    def __init__(self, file) -> None:
        self.file = file

    def read_file(self) -> list:
        with open(self.file, 'r') as f:
            return json.load(f)

    def write_file(self, data: dict) -> None:
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)