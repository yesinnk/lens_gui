import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Frame_examples_program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1000x600')
        self.window.title("Lens Unit Viewer GUI")
        self.create_widgets()

    def create_buttons(self, parent, a, b, c):
        button1 = ttk.Button(parent, text="do task " + a)
        button1.grid(row=1, column=1)
        button2 = ttk.Button(parent, text="do task " + b)
        button2.grid(row=2, column=1)
        button3 = ttk.Button(parent, text="do task " + c)
        button3.grid(row=3, column=1)

        return (button1, button2, button3)

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # - - - - - - - - - - - - - - - - - - - - -
        # LabelFrame
        labeled_frame_label = ttk.Label(self.window, text="")
        labeled_frame_label.grid(row=3, column=1, sticky=tk.W, pady=3)

        frame2 = ttk.LabelFrame(self.window, text="Example label", relief=tk.RIDGE)
        frame2.grid(row=4, column=1, sticky=tk.E + tk.W + tk.N + tk.S, padx=30, pady=4)
        self.create_buttons(frame2, "D", "E", "F")


        # - - - - - - - - - - - - - - - - - - - - -
        # Quit button in the lower right corner
        quit_button = ttk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=1, column=3)

# Create the entire GUI program
program = Frame_examples_program()

# Start the GUI event loop
program.window.mainloop()
