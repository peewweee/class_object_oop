# Class and Object - OOP
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# pseudocode
# create class tv
class TV:
    # channel, volume, on/off
    def __init__(self):
        self.Channel = 1
        self.VolumeLevel = 1
        self.on = False
    # turn on method
    # turn off method
    # return channel method
    def GetChannel(self):
        return self.Channel
    # set new channel
    def SetChannel(self, Channel):
        if 1 <= Channel <= 120:
            self.Channel = Channel
    # return volume
    # set volume
    # increase channel
    # decrease channel
    # increase volume
    # decrease volume

# test driver program
    # create two objects
def TestTV():
    first_tv = TV()
    first_tv.SetChannel(30)
    print(first_tv.GetChannel())

# call test driver program method
TestTV()