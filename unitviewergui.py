import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Frame_examples_program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tk Grouping Examples")
        self.window.geometry("700x400")

        self.create_widgets()

    def create_buttons(self, parent, a, b, c):
        button1 = ttk.Button(parent, text="do task " + a)
        button1.grid(row=1, column=1)
        button2 = ttk.Button(parent, text="do task " + b)
        button2.grid(row=2, column=1)
        button3 = ttk.Button(parent, text="do task " + c)
        button3.grid(row=3, column=1)
        return (button1, button2, button3)

    def create_labels(self, parent):
        button1 = ttk.Label(parent, text="Example " )
        button1.grid(row=1, column=1)
        button2 = ttk.Label(parent, text="Example " )
        button2.grid(row=1, column=2, pady=10)
        button3 = ttk.Label(parent, text="Example " )
        button3.grid(row=1, column=3)

    def create_nodes(self,parent):
        buttonborder = tk.Frame(parent, highlightbackground="#37d3ff",
                             highlightcolor="#37d3ff",
                             highlightthickness=4,
                             bd=0)

        photoshop = tk.Button(buttonborder, 
                            text='Output',
                            fg='#37d3ff',
                            bg='#001d26')

        photoshop.grid(row=0,column=0)
        buttonborder.grid(row=0,column=0,padx=10,pady=10)

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5
        # LabelFrame

        self.window.grid_columnconfigure(0,weight=1)
        self.window.grid_columnconfigure(1,weight=4)
        self.window.grid_rowconfigure(1,weight=1)

        eventTimeFrame = ttk.LabelFrame(self.window, text="Event Example Time Label", relief=tk.RIDGE)
        eventTimeFrame.grid(row=0,column=0, columnspan=2, sticky=tk.N + tk.E + tk.S+ tk.W)      
        self.create_labels(eventTimeFrame)

        frame2 = ttk.LabelFrame(self.window, text="Example label", relief=tk.RIDGE)
        frame2.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S+ tk.W)
        self.create_buttons(frame2, "1", "2", "3")

        frame3 = ttk.LabelFrame(self.window, text="Example label", relief=tk.RIDGE)
        frame3.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S+ tk.W)
        self.create_nodes(frame3)
        

# Create the entire GUI program
program = Frame_examples_program()
# Start the GUI event loop
program.window.mainloop()
