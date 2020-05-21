import PySimpleGUI as sg
TOPFONT = ("Helvetica", 15)
FRAMEFONT = ("Helvetica", 15)
LISTFONT = ("Helvetica", 20)
BLANKFONT = 'any 20'

LISTENTRYSIZE = (23, 7)
SQUAREBOX = (2,10)
RECTANGULARBOX = (4,10)
CANVASWIDTH = 250
CAMVASHEIGHT = 235
ENABLEEVENTS = True
SUBMITCHAMGE = True
SQUARESIZE = 25

# variables from network
ALLTRAINING = ('0','1','2','3','4','5','6')
bias_layer = ["red"]
input_layer = ["blue","red"]
hidden_layer = ["blue","brown"]
output_layer = ["black"]
output_frame = ["red"]



menu_def = [['&Viewer', ['&Update After',['Examples','Weight Updates','Progress Reports','Training and Testing','Never'],
                        '&Cell Size',['5','6','7','8','9','10','11','12','14','16','18','20','24','28','32','40'],
                        '&Cell Spacing',['0','1','2','3','4','6','8','10'],
                        '&Update','&Refresh','&Print...','&Close']],
            ['&Example Set',['Training Set', 'Testing Set']],
            ['&Procedure',['Test','Train']],
            ['&Value', ['Outputs and Targets', 'Outputs', 'Targets', 'Inputs', 'External Inputs', 'Output Derivatives',
                       'Input Derivatives', 'Gains', 'Link Weights', 'Link Derivs', 'Link Deltas']],
            ['&Palette',['Blue-Black-Red','Blue-Red-Yellow','Black-Gray-White','Hinton Diagram']]]


layout = [  [sg.Menu(menu_def, tearoff=True,font=TOPFONT)],

             [sg.Text('Event   ',font=TOPFONT), sg.Text('Example Time   ',font=TOPFONT),
              sg.Text('Event Time',font=TOPFONT),sg.Input(' ',size = (8,10), font = 'Any 20')],

             [sg.Input(' ',size = SQUAREBOX, font = BLANKFONT),sg.Text('/',font = BLANKFONT),sg.Input(' ',size = SQUAREBOX, font = BLANKFONT),sg.T('', font=BLANKFONT),
              sg.Input(' ',size = RECTANGULARBOX, font = BLANKFONT),sg.Text('/',font = BLANKFONT),sg.Input(' ',size = RECTANGULARBOX, font = BLANKFONT),sg.T('   ', font=BLANKFONT),
              sg.Input(' ',size = RECTANGULARBOX, font = BLANKFONT),sg.Text('/',font = BLANKFONT),sg.Input(' ',size = RECTANGULARBOX, font = BLANKFONT),
              sg.Input(' ',size = (8,10), font = 'Any 20'), sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],

            [sg.Frame('Training Set', [[sg.Listbox(values=ALLTRAINING, size=LISTENTRYSIZE,font=LISTFONT)]],font=FRAMEFONT),
            sg.Frame('Outputs and Targets',[[
                                                    sg.Graph(
                                                        canvas_size=(CANVASWIDTH, CAMVASHEIGHT),
                                                        graph_bottom_left=(0, 0),
                                                        graph_top_right=(CANVASWIDTH, CAMVASHEIGHT),
                                                        key="graph"
                                                        )]]),
            sg.Slider(range=(1, 100), orientation='v', size=(11, 20), default_value=50)]
        ]

window = sg.Window('unit viewer',
                   layout,
                   border_depth=0,
                   use_default_focus=False,
                   )

# for the graph
window.Finalize()
graph = window.Element("graph")
#
# BIASLAYER = ["red"]
# INPUTLAER = ["blue","red"]
# HIDDENLAYER = ["blue","brown"]
# OUTPUTLAYER = ["black"]
# OUTPUTFRAME = ["red"]
rec_height = CAMVASHEIGHT/9
bias_v_coord = rec_height
input_v_coord = rec_height*3
hidden_v_coord = rec_height*5
output_v_coord = rec_height*7
bias_h_coord = [CANVASWIDTH/2-SQUARESIZE]
input_h_coord = [CANVASWIDTH/2-SQUARESIZE,CANVASWIDTH/2]
hidden_h_coord = [CANVASWIDTH/2-SQUARESIZE,CANVASWIDTH/2]
output_h_coord = [CANVASWIDTH/2]

for i in range(len(bias_layer)):
    color = bias_layer[i]
    h_coord = bias_h_coord[i]
    graph.DrawRectangle((h_coord, bias_v_coord), (h_coord+SQUARESIZE, bias_v_coord+SQUARESIZE), fill_color=color)

for i in range(len(input_layer)):
    color = input_layer[i]
    h_coord = input_h_coord[i]
    graph.DrawRectangle((h_coord, input_v_coord), (h_coord+SQUARESIZE, input_v_coord+SQUARESIZE), fill_color=color)

for i in range(len(hidden_layer)):
    color = hidden_layer[i]
    h_coord = hidden_h_coord[i]
    graph.DrawRectangle((h_coord, hidden_v_coord), (h_coord+SQUARESIZE, hidden_v_coord+SQUARESIZE), fill_color=color)

for i in range(len(output_layer)):
    color = output_layer[i]
    h_coord = output_h_coord[i]
    graph.DrawRectangle((h_coord, output_v_coord), (h_coord+SQUARESIZE, output_v_coord+SQUARESIZE), fill_color=color)

button, value = window.Read()

