import PySimpleGUI as sg

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

layout = [
    [sg.Menu(menu_def, tearoff=True,font = ("Helvetica", 20))],
    [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)]
]


window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.read()