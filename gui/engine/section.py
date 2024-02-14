import tkinter


class AppSection:

    def __init__(self, name, content=[]):
        self.name = name
        self.elements = content

    def append(self, elements):
        for e in elements:
            self.elements.append(e)

    def remove(self, elements):
        for e in elements:
            self.elements.remove(e)
