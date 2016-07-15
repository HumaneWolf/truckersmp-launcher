class Settings:
    def __init__(self, appdir):
        self.tmpdir = "D:\Games\TruckersMP" #TruckersMP Directory
        self.ets2dir = "D:\Steamapps\SteamApps\common\Euro Truck Simulator 2" #ETS2 Directory
        self.atsdir = "D:\Steamapps\SteamApps\common\American Truck Simulator" #ATS Directory
        self.lastversion = "0.2.1.0.1" #The latest version last time the software was opened.
        self.nointro = False #Skip game intro?
        self.otherCmd = "" #Other commandline flags, most people won't use this.

        self.appdir = appdir

        self.loadSettings()

    def loadSettings(self):
        print("Loading Settings..")

        #Todo: Settings file, settings loading, settings saving, file generator.
        #Format: JSON