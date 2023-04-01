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

        # colors for the application
        self.primary = '#081F4D'
        self.secondary = '#0083FF'
        self.white = '#FFFFFF'


        # the Standard request url
        self.url = f'https://v6.exchangerate-api.com/v6/d0c0d5e10cfe3d746be6fdde/latest/USD'

        # making the Standard request to the API and converting the request to json
        self.response = requests.get(f'{self.url}').json()

        # converting the currencies to dictionaries
        self.currencies = dict(self.response['conversion_rates'])



        # label for the text Currency Converter
        self.top_frame = Frame(self.window, bg = self.primary, width = 300, height = 80)
        self.top_frame.grid(row = 0, column = 0)

        self.name_label = Label(self.top_frame, text = 'Currency Converter', bg = self.primary,
                                 fg = self.white, padx = 24, pady = 30, justify = CENTER, 
                                 font = ('Poppins 20 bold') )
        self.name_label.grid(row = 0, column = 0)

        # bottom frame
        self.bottom_frame = Frame(self.window, width = 300, height = 250)
        self.bottom_frame.grid(row = 1, column = 0)

        # widgets inside the bottom frame
        self.from_currency_label = Label(self.bottom_frame, text = 'FROM: ',
                                          font = ('Poppins 10 bold'), justify = LEFT)
        self.from_currency_label.place(x = 5, y = 10)

        self.to_currency_label = Label(self.bottom_frame, text = 'TO: ',
                                   font = ('Poppins 10 bold'), justify = RIGHT)
        self.to_currency_label.place(x = 160, y = 10)

        self.amount_label = Label(self.bottom_frame, text = 'AMOUNT: ',
                              font = ('Poppins 10 bold'), justify = LEFT)
        self.amount_label.place(x = 5, y = 55)

        #combobox for holding from_currencies
        self.from_currency_combo = ttk.Combobox(self.bottom_frame,
                                            values = list(self.currencies.keys()), width = 14,
                                              font = ('Poppins 10 bold'))
        self.from_currency_combo.place(x = 5, y = 30)

        self.to_currency_combo = ttk.Combobox(self.bottom_frame,
                                          values = list(self.currencies.keys()), width = 14,
                                            font = ('Poppins 10 bold'))
        self.to_currency_combo.place(x = 160, y = 30)

        # entry for amount
        self.amount_entry = Entry(self.bottom_frame, width = 25, font = ('Poppins 15 bold'))
        self.amount_entry.place(x = 5, y = 80)

        # an empty label for displaing the result
        self.result_label = Label(self.bottom_frame, text = '', font = ('Poppins 10 bold'))
        self.result_label.place(x = 5, y = 115)
        

        # an empty label for displaying the time
        self.time_label = Label(self.bottom_frame, text = '', font = ('Poppins 10 bold'))
        self.time_label.place(x = 5, y = 135)


        



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    c = Converter()
    c.run()