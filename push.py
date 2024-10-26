import PySimpleGUI as sg
susunan=[[sg.Push(),
          sg.Text("UNISKA MAAB",font=("helvetica",24)),
          sg.Push()],
          [sg.Push(),
           sg.Text("BANJARMASIN", font=("Courier",18)),
           sg.Push()]
           ]
Window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   size=(400,200))
Window()
Window.close()