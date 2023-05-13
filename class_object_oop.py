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
    def GetVolume(self):
        return self.VolumeLevel
    # set volume
    def SetVolume(self, VolumeLevel):
        if 1 <= VolumeLevel <= 7:
            self.VolumeLevel = VolumeLevel
    # increase channel
    # decrease channel
    # increase volume
    # decrease volume

# test driver program
    # create two objects
def TestTV():
    first_tv = TV()
    first_tv.SetChannel(30)
    first_tv.SetVolume(3)
    print(first_tv.GetVolume())

# call test driver program method
TestTV()