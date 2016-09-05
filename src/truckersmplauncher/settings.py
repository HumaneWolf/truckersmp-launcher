import os.path
import json
import tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox

class Settings:
    def __init__(self, appdir):
        self.tmpdir = "D:\Games\TruckersMP" #TruckersMP Directory
        self.ets2dir = "D:\Steamapps\SteamApps\common\Euro Truck Simulator 2" #ETS2 Directory
        self.atsdir = "D:\Steamapps\SteamApps\common\American Truck Simulator" #ATS Directory
        #self.lastversion = "0.2.1.0.1" #The latest version last time the software was opened.
        self.nointro = False #Skip game intro?
        self.otherCmd = "" #Other commandline flags, most people won't use this.

        self.appdir = appdir

        self.loadSettings()

    def loadSettings(self):
        print("Loading Settings..")

        if (os.path.isfile(self.appdir + "\launchersettings.json")):
            file = open(self.appdir + "\launchersettings.json", "r")
            try:
                data = json.load(file)
                self.tmpdir = data["tmpdir"]
                self.ets2dir = data["ets2dir"]
                self.atsdir = data["atsdir"]
                self.nointro = data["nointro"]
                self.otherCmd = data["otherCmd"]
                print("Settings file loaded.")
            except json.decoder.JSONDecodeError:
                print("Settings file invalid")
                file.close()
                self.saveSettings()

        else:
            print("Making new settings file")
            self.saveSettings()

    def saveSettings(self):
        data = {}
        data["tmpdir"] = self.tmpdir
        data["ets2dir"] = self.ets2dir
        data["atsdir"] = self.atsdir
        data["nointro"] = self.nointro
        data["otherCmd"] = self.otherCmd

        file = open(self.appdir + "\launchersettings.json", "w")
        json.dump(data, file)
        file.close()
        print("New settings file generated")

    def openSettings(self):
        #Var
        self.settings = tkinter.Tk()

        #Setting some UI settings
        self.settings.geometry("800x400")
        self.settings.wm_title("TruckersMP Launcher Settings")

        #fonts
        self.font_head = font.Font(family = "Helvetica", size = 36, weight = "bold")

        #Logos
        self.image = tkinter.Canvas(self.settings, height = 400, width = 250)
        logos = self.appdir + "\\logos.png"
        logosimg = PhotoImage(master = self.image, width = 250, height = 400, file = logos) 
        self.image.create_image(125, 200, image = logosimg)
        self.image.pack(side = "left")

        #Settings...
        self.header = tkinter.Label(self.settings, text = "Settings...", font = self.font_head)
        self.header.pack()

        #Close button
        self.quitButton = tkinter.Button(self.settings, command = self.quitSettings, text = "Close Settings")
        self.quitButton.pack(side = "bottom")

        tkinter.mainloop()

    def quitSettings(self):
        self.settings.destroy()