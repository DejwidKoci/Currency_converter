from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import requests
import json

class Converter:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('310x340+500+200')
        self.window.title('Currency Converter')
        self.window.resizable(height = FALSE, width= FALSE)
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    c = Converter()
    c.run()