

class FaceduckError(ValueError):
    def __init__(self, id):
        self.id = id
