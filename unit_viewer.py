import PySimpleGUI as sg
BUTTONSIZE = (30,6)
BUTTONFONT = ("Helvetica", 20)
SMALLERFONT = ("Helvetica", 20)
SQUAREBOX = (2,10)
RECTANGULARBOX = (4,10)
ENABLEEVENTS = True
SUBMITCHAMGE = True
ALLTRAINING = ('0','1','2','3','4','5','6')

menu_def = [['&Viewer', ['&Update After',['Examples','Weight Updates','Progress Reports','Training and Testing','Never'],
                        '&Cell Size',['5','6','7','8','9','10','11','12','14','16','18','20','24','28','32','40'],
                        '&Cell Spacing',['0','1','2','3','4','6','8','10'],
                        '&Update','&Refresh','&Print...','&Close']],
            ['&Example Set',['Training Set', 'Testing Set']],
            ['&Procedure',['Test','Train']],
            ['&Value', ['Outputs and Targets', 'Outputs', 'Targets', 'Inputs', 'External Inputs', 'Output Derivatives',
                       'Input Derivatives', 'Gains', 'Link Weights', 'Link Derivs', 'Link Deltas']],
['&Palette',['Blue-Black-Red','Blue-Red-Yellow','Black-Gray-White','Hinton Diagram']]]




layout = [  [sg.Menu(menu_def, tearoff=True,font=BUTTONFONT,size=(40,100))],

             [sg.Text('Event   ',font=SMALLERFONT), sg.Text('Example Time   ',font=SMALLERFONT),
              sg.Text('Event Time',font=SMALLERFONT),sg.Input(' ',size = (8,10), font = 'Any 20')],


             [sg.Input(' ',size = SQUAREBOX, font = 'Any 20'),sg.Text('/',font = 'Any 20'),sg.Input(' ',size = SQUAREBOX, font = 'Any 20'),sg.T('', font='any 20'),
              sg.Input(' ',size = RECTANGULARBOX, font = 'Any 20'),sg.Text('/',font = 'Any 20'),sg.Input(' ',size = RECTANGULARBOX, font = 'Any 20'),sg.T('   ', font='any 20'),
              sg.Input(' ',size = RECTANGULARBOX, font = 'Any 20'),sg.Text('/',font = 'Any 20'),sg.Input(' ',size = RECTANGULARBOX, font = 'Any 20'),
              sg.Input(' ',size = (8,10), font = 'Any 20'), sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],

            [sg.Frame('Training Set', [[sg.Listbox(values=ALLTRAINING, size=(23, 7),font=("Helvetica", 20))]],font=("Helvetica", 20)),
            sg.Frame('Outputs and Targets',[[sg.Listbox(values=ALLTRAINING, size=(23, 7),font=("Helvetica", 20))]], font=("Helvetica", 20)),
            sg.Slider(range=(1, 100), orientation='v', size=(11, 20), default_value=50)]
        ]

window = sg.Window('unit viewer',
                   layout,
                   border_depth=0,
                   use_default_focus=False,
                   )

button, value = window.Read()

