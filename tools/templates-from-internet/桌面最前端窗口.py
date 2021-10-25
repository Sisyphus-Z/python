import PySimpleGUIQt as sg
layout = [[sg.Text("Demo Test")]]
window = sg.Window('', layout=layout, keep_on_top=True, no_titlebar=True, alpha_channel=0.3)
while True:
    event, value = window.Read()