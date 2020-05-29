from tkinter import *

root = Tk()
root.geometry('1000x600')

#container frames
in_output_nodes = Frame(root,bg='cyan',width=200,height=150)
in_hidden_nodes = Frame(root, bg='lavender',width=200,height=150)
in_input_nodes = Frame(root, bg='gray',width=200,height=150)
clear_button_frame = Frame(root,bg='black',width=200,height=150)
out_output_nodes = Frame(root,bg='blue',width=800,height=200)
out_hidden_nodes = Frame(root,bg='purple',width=800,height=200)
out_input_nodes = Frame(root, bg='white',width=800,height=200)

#place frames in gui
in_output_nodes.grid(row=0,column=0)
in_hidden_nodes.grid(row=1,column=0)
in_hidden_nodes.grid(row=2,column=0)
clear_button_frame.grid(row=3,column=0)
out_output_nodes.grid(row=0,column=1)
out_hidden_nodes.grid(row=1,column=1)
out_input_nodes.grid(row=3,column=1)

# # Number of Input Nodes input
# e = Entry(root, width=50)
# e.grid(row=0,column=0)
# e.insert(0, "Number of input Nodes")

# def myClick():
#     for i in range(0,int(e.get())):
#         Button(root,text="1").grid(row=2,column=i)

# myButton=Button(root, text="Confirm",command=myClick)
# myButton.grid(row=1,column=0)

# #Clear every button is row 2
# def clear():
#     list = root.grid_slaves(row=2)
#     for l in list:
#         l.destroy()

# Button(root,text='Clear',command=clear).grid(row=0,column=3)




root.mainloop()