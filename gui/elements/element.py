
class Element:

    def __init__(self, id: str):
        self.id = id
        self.visual_element = ""

    def pack(self):
        self.visual_element.pack()