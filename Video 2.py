from tkinter import *
from functools import partial # to prevent unwanted windows
import random

title_num = random.randint(0,10)

class Converter:
    def __init__(self,parent):
        
        
        # Formatting variables...
        background_colour = "light blue"
        
        # Converter Main Screen GUI...
        self.converter_frame = Frame(padx=120,pady=80, bg= background_colour)
        self.converter_frame.grid()
        
        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", 
                                          font=("Arial","16","bold"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.temp_converter_label.grid(row=0)
        
        
        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help me I've fallen and I cant get up", 
                                  font=("Arial","14"),padx=10,pady=10, command=self.help)
        
        self.help_button.grid(row=1)
    
    def help(self):
        print("Ha shame")
        get_help = Help(self)
        get_help.help_text.cnfigure(text="Help text goes here")

#main routine
if __name__ == "__main__":
    root = Tk()
    if title_num == 1:
        root.title("It's Celcius not Centigrade")
    else:
        root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()