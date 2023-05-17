# Main Program
# Phoebe Rhone L. Gangoso | BSCPE 1-4

from TV import TV
import PySimpleGUI as sg
sg.theme('dark green')

# test driver program
def TestTV():
    # create two objects
    first_tv = TV()
    first_tv.TurnOn()
    first_tv.SetChannel(30)
    first_tv.SetVolume(3)

    second_tv = TV()
    second_tv.TurnOn()
    second_tv.ChannelUp()
    second_tv.ChannelUp()
    second_tv.SetVolume(2)

    layout_text = [[sg.Text(f"TV 1's channel is {first_tv.GetChannel()} and volume level is {first_tv.GetVolume()}", font="Arial")],
              [sg.Text(f"TV 2's channel is {second_tv.GetChannel()} and volume level is {second_tv.GetVolume()}", font='Arial')],
              [sg.Text(f"\N{television}", font=100)],
              [sg.Button('Exit')]]

    window_layout = sg.Window('TV Class', layout_text, margins=(75,30), element_justification='c')

    while True:
        event, values = window_layout.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window_layout.close()
# call test driver program method
TestTV()