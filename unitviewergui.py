import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Frame_examples_program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tk Grouping Examples")
        self.window.geometry("700x400")
        self.create_widgets()


    def create_labels(self, parent):
        button1 = ttk.Label(parent, text="Example " )
        button1.grid(row=1, column=1)
        button2 = ttk.Label(parent, text="Example " )
        button2.grid(row=1, column=2, pady=10)
        button3 = ttk.Label(parent, text="Example " )
        button3.grid(row=1, column=3)

    def create_output_nodes(self,parent,row,col):
        buttonborder = tk.Frame(parent, highlightbackground="#05476E",
                             highlightcolor="#05476E",
                             highlightthickness=6,
                             bd=0)

        photoshop = tk.Button(buttonborder, 
                            text='    ',
                            fg='#05476E',
                            bg='#F4370F')

        photoshop.grid(row=row,column=col,sticky=tk.N)
        buttonborder.grid(row=row,column=col,padx=20,pady=20,sticky=tk.N)

    def create_input_nodes(self,parent,row,col):

        buttonborder = tk.Frame(parent, highlightbackground="#F4370F",
                             highlightcolor="#F4370F",
                             highlightthickness=3,
                             bd=0)

        photoshop = tk.Button(buttonborder, 
                            text='    ',
                            fg='#F4370F',
                            bg='#F4370F')

        photoshop.grid(row=row,column=col,sticky=tk.N)
        buttonborder.grid(row=row,column=col,padx=20,pady=20,sticky=tk.N)

    def create_hidden_nodes(self,parent,row,col):
        buttonborder = tk.Frame(parent, highlightbackground="#05476E",
                             highlightcolor="#05476E",
                             highlightthickness=3,
                             bd=0)

        photoshop = tk.Button(buttonborder, 
                            text='    ',
                            fg='#05476E',
                            bg='#05476E')

        photoshop.grid(row=row,column=col,sticky=tk.N)
        buttonborder.grid(row=row,column=col,padx=20,pady=20,sticky=tk.N)

    
    def example1(self,frame):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()

        self.create_output_nodes(frame,row=0,col=2)
        self.create_output_nodes(frame,row=0,col=3)

        for i in range(1,5):
            self.create_hidden_nodes(frame,row=1,col=i)

        for i in range(0,6):
            self.create_hidden_nodes(frame,row=2,col=i)

        self.create_input_nodes(frame,row=3,col=2)
        self.create_input_nodes(frame,row=3,col=3)

    def example2(self,frame):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()

        self.create_output_nodes(frame,row=0,col=3)

        for i in range(1,7):
            self.create_hidden_nodes(frame,row=1,col=i)

        for i in range(0,6):
            self.create_hidden_nodes(frame,row=2,col=i)

        self.create_input_nodes(frame,row=3,col=2)
        self.create_input_nodes(frame,row=3,col=3)

    def example3(self,frame):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()

        self.create_output_nodes(frame,row=0,col=3)

        row=1
        for i in range(1,100):
            if i%5==0:
                row+=1
                self.create_hidden_nodes(frame,row=row,col=i)
            else:
                self.create_hidden_nodes(frame,row=row,col=i)

        # for i in range(0,6):
        #     self.create_hidden_nodes(frame,row=2,col=i)

        # self.create_input_nodes(frame,row=3,col=2)
        # self.create_input_nodes(frame,row=3,col=3)



    def create_buttons(self, parent, a, b, c, frame):
        button1 = ttk.Button(parent, text="do task " + a, command=lambda: self.example1(frame))
        button1.grid(row=1, column=1)
        button2 = ttk.Button(parent, text="do task " + b,  command=lambda: self.example2(frame))
        button2.grid(row=2, column=1)
        button3 = ttk.Button(parent, text="do task " + c, command=lambda: self.example3(frame))
        button3.grid(row=3, column=1)
        return (button1, button2, button3)

    def create_listbox(self,parent,frame):

        listbox = tk.Listbox(parent)
        listbox.pack(side=tk.LEFT,fill="both",expand=True)

        for item in ["example1","example2"]:
            listbox.insert(tk.END, item)

        x=listbox.get(tk.ACTIVE)
        btn = tk.Button(parent,text="select",command=lambda: self.example1(frame) )
        btn.pack()

    def create_scrollbar(self,parent):
        sbr=tk.Scrollbar(parent)
        sbr.grid(column=5,sticky=tk.E)
        

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        self.window.grid_columnconfigure(0,weight=1)
        self.window.grid_columnconfigure(1,weight=4)
        self.window.grid_rowconfigure(1,weight=1)

        eventTimeFrame = ttk.LabelFrame(self.window, text="Event Example Time Label", relief=tk.RIDGE)
        eventTimeFrame.grid(row=0,column=0, columnspan=2, sticky=tk.N + tk.E + tk.S+ tk.W)      
        self.create_labels(eventTimeFrame)


        frame3 = ttk.LabelFrame(self.window, text="Example label", relief=tk.RIDGE)
        frame3.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S+ tk.W)

        frame2 = ttk.LabelFrame(self.window, text="Example label", relief=tk.RIDGE)
        frame2.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S+ tk.W)

        #self.create_listbox(frame2, frame=frame3)
        self.create_buttons(frame2, "1", "2", "3", frame=frame3)
        #self.create_scrollbar(frame3)
        

# Create the entire GUI program
program = Frame_examples_program()
# Start the GUI event loop
program.window.mainloop()
