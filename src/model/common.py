class UnsupportedOpException(Exception):
    def __init__(self, name: str):
        self.name = name

class BadRequestException(Exception):
    def __init__(self, name: str):
        self.name = name