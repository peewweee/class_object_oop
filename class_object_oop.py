# Class and Object - OOP
# Phoebe Rhone L. Gangoso | BSCPE 1-4

import PySimpleGUI as sg

# pseudocode
# create class tv
class TV:
    # channel, volume, on/off
    def __init__(self):
        self.Channel = 1
        self.VolumeLevel = 1
        self.on = False
    # turn on method
    def TurnOn(self):
        self.on = True
    # turn off method
    def TurnOff(self):
        self.on = False
    # return channel method
    def GetChannel(self):
        return self.Channel
    # set new channel
    def SetChannel(self, Channel):
        if 1 <= Channel <= 120:
            self.Channel = Channel
    # return volume
    def GetVolume(self):
        return self.VolumeLevel
    # set volume
    def SetVolume(self, VolumeLevel):
        if self.on and 1 <= VolumeLevel <= 7:
            self.VolumeLevel = VolumeLevel
    # increase channel
    def ChannelUp(self):
        if self.on and self.Channel < 120:
            self.Channel += 1
    # decrease channel
    def ChannelDown(self):
        if self.on and self.Channel > 1:
            self.Channel -= 1
    # increase volume
    def VolumeUp(self):
        if self.on and self.VolumeLevel < 7:
            self.VolumeLevel += 1
    # decrease volume
    def VolumeDown(self):
        if self.on and self.VolumeLevel > 1:
            self.VolumeLevel -= 1

# test driver program
    # create two objects
def TestTV():
    first_tv = TV()
    first_tv.TurnOn()
    first_tv.SetChannel(30)
    first_tv.SetVolume(3)

    second_tv = TV()
    second_tv.TurnOn()
    second_tv.ChannelUp()
    second_tv.ChannelUp()
    second_tv.SetVolume(2)

    layout = [[sg.Text(f"TV 1's channel is {first_tv.GetChannel()} and volume level is {first_tv.GetVolume()}",
                       font='helvetica')],
              [sg.Text(f"TV 2's channel is {second_tv.GetChannel()} and volume level is {second_tv.GetVolume()}",
                       font='helvetica')],
              [sg.Button('Exit')]]

    window = sg.Window('TV Class', layout, margins=(75,30), element_justification='c')

    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()

# call test driver program method
TestTV()