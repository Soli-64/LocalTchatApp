import tkinter


class App:

    def __init__(self, window, app_name, dimensions):
        self.window = window
        self.window.title(app_name)
        self.window.geometry(dimensions)
        self.sections = {}

    def target_section(self, name):

    def new_section(self, section):
        self.sections[f'{section.name}'] = section

    def remove_section(self, name):
        self.sections[f'{name}'] = {}

    def pack(self):
        for section in self.sections.values():
            for element in section.elements:
                element.pack()

    def mainloop(self):
        self.pack()
        self.window.mainloop()
