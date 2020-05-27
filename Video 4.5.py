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
        get_help.help_text.configure(text="Situation 1: Google it idk lol \nSituation 2: Die \nSituation 3: Turn it off and on again")
        

class Help:
    def __init__(self,partner):
        background_c = "pink"
        
        # Disable help button after pressing to make sure it isn't spammed
        partner.help_button.config(state=DISABLED)
        
        # creates actual box
        self.help_box = Toplevel()
        
        # Re-enable help button when red cross is used
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))
        
        # Gui Frame
        self.help_box_frame = Frame(self.help_box,height=100,width=300,bg=background_c)
        self.help_box_frame.grid()
        
        # Help box Heading (row 0)
        self.help_box_label = Label(self.help_box_frame,text="H E L P",
                                   font=("Arial","20","italic"),
                                   bg=background_c,padx=10,pady=10)
        
        self.help_box_label.grid(row=0)
        
        # Help text (label, row 1)
        self.help_text = Label(self.help_box_frame, text="", justify=LEFT,
                               width=40, bg= background_c, wrap=250)
        self.help_text.grid(row=1)
        
        # Closing button (row 2)
        self.help_close_button = Button(self.help_box_frame, text="CLOSE",padx=10,pady=10,
                                        command=partial(self.close_help, partner))
        self.help_close_button.grid(row=2,pady=10)
    
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

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