from tkinter import *
from functools import partial # to prevent unwanted windows
import random

title_num = random.randint(0,100)

class Converter:
    def __init__(self,parent):
        
        
        # Formatting variables...
        background_colour = "light blue"
        
        # Converter Main Screen GUI...
        self.converter_frame = Frame(padx=120,pady=80, bg= background_colour)
        self.converter_frame.grid()
        
        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", 
                                          font=("Comic Sans MS","15","bold","italic"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.temp_converter_label.grid(row=0)
        
        
        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help me I've fallen and I cant get up", 
                                  font=("Comic Sans MS","14","underline"),padx=10,pady=10, command=self.help)
        
        self.help_button.grid(row=1)
    
    def help(self):
        # Text to show the Help button was pressed
        print("Ha shame")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")
        

class Help:
    def __init__(self,partner):
        background = "pink"
        
        partner.help_button.config(state=DISABLED)
        
        

#main routine
if __name__ == "__main__":
    root = Tk()
    if title_num < 11:
        if title_num == 1:
            root.title("Also try Terraria!")
        else:
            root.title("It's Celsius not Centigrade")
    else:
        root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()