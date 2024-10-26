import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAAB", font=("helvetica",24))],
         [sg.Text("BANJARMASIN", font=("courier",18))]]
Window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   element_justification = "center",
                   size=(430,200))
Window.read()
Window.close()