import tkinter as tk
from src.gui.elements.element import Element

class InteractiveButton(Element):

    def __init__(self, text, id, func):
        super().__init__(id)
        self.visual_element = tk.Button(text=text, command=func)

    def refresh(self, text, func):
        self.visual_element = tk.Button(text=text, command=func)
        self.pack()
