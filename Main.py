from tkinter import *
from functools import partial # to prevent unwanted windows
import random

title_num = random.randint(0,100)


class Converter:

    def __init__(self,parent):
        
        def background_colour(self):
            r = random.randint(16,256)
            g = random.randint(16,256)
            b = random.randint(16,256)
            
            global hexcode
            hexcode = "#"+hex(r).lstrip("0x")+hex(g).lstrip("0x")+hex(b).lstrip("0x")        
        
        instructions = "Yo WHATS UP GAMERS?! It's ya boi... uh"
        
        background_colour(self)
        
        # Formatting variables...
        
        background_colour = str(hexcode) # Grey colour
        
        # Converter Frame
        self.converter_frame = Frame(pady=100,width=4000, bg=background_colour)
        self.converter_frame.grid()
        
        
        # Temperature Converter Heading (row 0)
        self.converter_label = Label(self.converter_frame,bg=background_colour, 
                                     text="Temperature Converter",
                                     font=("Comic Sans MS","15","bold","underline","italic"),
                                     padx=10,pady=10)
        self.converter_label.grid(row=0)        
        
        
        # User instructions ( row 1)
        self.instructions_label = Label(self.converter_frame,bg=background_colour, 
                                     text=instructions,
                                     font=("Comic Sans MS","8","italic"),wrap=250,justify=LEFT,padx=10,pady=10)
        self.instructions_label.grid(row=1)
        
        # Temperature entry box (row 2)
        self.converter_entry = Entry(self.converter_frame, width=20, font=("Comic Sans MS","14","bold"))
        
        self.converter_entry.grid(row=2)
        
        # Conversion buttons frame (row 3)
        
        # Answer label (row 4)

        # History / Help button frame (row 5)


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