import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
Window = sg.Window(title="Contoh Button",
                   layout=[[sg.Text("Contoh Button")],
                           [sg.Button("Button Simpan")],
                           [sg.Button("Button Keluar")]
                           ],
                    size=(400,200),
                    font=("Times", 18))
kejadian,nilai = Window.read()
print(kejadian, "=>", nilai)
Window.close()