from tkinter import *
from functools import partial # to prevent unwanted windows
import random

title_num = random.randint(0,100)


class Converter:

    def __init__(self,parent):
        
        # Generating random hexcode for backgrund colour
        def background_colour(self):
            r = random.randint(128,255) # generate RGB values
            g = random.randint(128,255)
            b = random.randint(128,255)
            
            print(r,g,b)
            global hexcode
            # convert to hexdecimal and put into 1 value to feed into background colour
            hexcode = "#"+hex(r).lstrip("0x")+hex(g).lstrip("0x")+hex(b).lstrip("0x")
            print(hexcode)
        
        
        
        background_colour(self)
        
        # Formatting variables...
        
        background_colour = str(hexcode) # Random Colour from definition
        
        # Converter Frame
        self.converter_frame = Frame(pady=100,padx=75, bg=background_colour)
        self.converter_frame.grid()
        
        
        # Temperature Converter Heading (row 0)
        self.converter_label = Label(self.converter_frame,bg=background_colour, 
                                     text="Temperature Converter",
                                     font=("Comic Sans MS","15","bold","underline","italic"),
                                     padx=10,pady=10)
        self.converter_label.grid(row=0)        
        
        
        # User instructions ( row 1)
        instructions = "Markiplier... E... Lord Farquaad, Mark Zuckerburg, E, E, E"
        
        self.instructions_label = Label(self.converter_frame,bg=background_colour, 
                                     text=instructions,
                                     font=("Comic Sans MS","8","italic"),wrap=250,
                                     justify=LEFT,padx=10,pady=10)
        self.instructions_label.grid(row=1)
        
        # Conversion buttons frame (row 2), celsius button blue, fahrenheit button yellow 
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=2,pady=10)
        
        self.to_c_button = Button(self.conversion_buttons_frame,text="To Celsius",
                                  font="Helvetica 12 bold",bg="light blue",width=12,pady=10)
        self.to_c_button.grid(row=0)
        
        self.to_f_button = Button(self.conversion_buttons_frame,text="To Fahrenheit",
                                  font="Helvetica 12 bold",bg="yellow",width=12,pady=10)
        self.to_f_button.grid(row=0,column=1)
        
        # Temperature entry box (row 3)
        self.converter_entry = Entry(self.converter_frame, width=20, font=("Comic Sans MS","14","bold"))
        
        self.converter_entry.grid(row=3)
        
        # Answer label (row 4)
        self.converted_temp_label = Label(self.converter_frame, font= "Arial 16 italic",
                                          text="Bruh moment, can we get 5 likes on this video",
                                          bg=hexcode)
        self.converted_temp_label.grid(row=4)
        

        # History / Help button frame (row 5)
        self.help_history_frame = Frame(self.converter_frame)
        self.help_history_frame.grid(row=5)

        self.history_button = Button(self.help_history_frame,text="History",
                                  font="Helvetica 10 bold",bg="light gray",width=10,pady=10)
        self.history_button.grid(row=0,column=0)        
        
        self.help_button = Button(self.help_history_frame,text="Help",
                                  font="Helvetica 10 bold",bg="light gray",width=10,pady=10)
        self.help_button.grid(row=0,column=1)
        

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
