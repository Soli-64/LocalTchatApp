import tkinter as tk
from src.gui.elements.element import Element

class InteractiveLabel(Element):

    def __init__(self, text, id):
        super().__init__(id)
        self.visual_element = tk.Label(text=text)

    def refresh(self, text):
        self.visual_element = tk.Label(text=text)
        self.pack()
