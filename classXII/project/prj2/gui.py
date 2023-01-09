import PySimpleGUI as sg
import os
icon = os.getcwd() + r"\classXII\project\prj2\download.ico"
sg.theme("Light Blue 3")
layout = [
    [sg.Text("This is project")],
    [sg.Text("Enter Snide Comments:"),sg.Input(key="comm",enable_events=True)],
    [sg.Button("Start Project"),sg.Exit()]
]

window = sg.Window("window1",layout,size=(640,280),resizable=True,icon=icon)

while True:
    event , values = window.Read()
    if event in (sg.WINDOW_CLOSED, "Exit"): break
    if event == "Start Project": sg.popup_error("Project Does not Exist \nWhat do you expect from Ujjwal")
    print(event,values)
window.close()
