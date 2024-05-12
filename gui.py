import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box =sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window("My TO-DO App", layout=[[label, add_button], [input_box]])
window.read()
window.close()
