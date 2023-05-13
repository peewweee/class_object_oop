# Class and Object - OOP
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# pseudocode
# create class tv
class TV:
    def __init__(self, TvNumber, TurnOn, TurnOff, GetChannel, SetVolume, GetVolume):
        self.TvNumber = TvNumber
        self.TurnOn = TurnOn
        self.TurnOff = TurnOff
        self.GetChannel = GetChannel
        self.SetVolume = SetVolume
        self.GetVolume = GetVolume
    # method to display objects
    def show(self):
        print(self.TvNumber, self.GetChannel, self.GetVolume)

# Test driver program
def TestTV():
    # create two objects
    first_tv = TV('TV 1','None', 'None', 30, 'None', 3)
    first_tv.show()

# call test driver method
TestTV()