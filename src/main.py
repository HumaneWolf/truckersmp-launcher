import tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox
import os
from subprocess import call
from truckersmplauncher.settings import Settings
from truckersmplauncher.update import Update
import platform

class Launcher:
    def __init__(self):

        #vars
        appdir = os.getcwd()
        self.settingsChanged = False

        #Settings
        self.settings = Settings(appdir)

        #Create Window
        self.main = tkinter.Tk()
        self.main.geometry("800x400")
        self.main.wm_title("TruckersMP Launcher")

        #fonts
        self.font_head = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.font_bitwarning = font.Font(family = "Times", size = 12, slant = "italic")

        #Logos
        self.image = tkinter.Canvas(self.main, height = 400, width = 250)
        logos = appdir + "\\logos.png"
        logosimg = PhotoImage(master = self.image, width = 250, height = 400, file = logos) 
        self.image.create_image(125, 200, image = logosimg)
        self.image.pack(side = "left")

        #Launch
        self.launch = tkinter.Label(self.main, text = "Play...", font = self.font_head)
        self.launch.pack()

        #Quitting
        self.quitButton = tkinter.Button(self.main, command = self.quit, text = "Quit Launcher")
        self.quitButton.pack(side = "bottom")

        #Settings
        self.settingsButton = tkinter.Button(self.main, command = self.openSettings, text = "Settings")
        self.settingsButton.pack(side = "bottom")

        #ETS2
        self.ets2Menu = tkinter.Frame(self.main, width = 400, borderwidth = 5)
        self.ets2Menu.pack()
        ets2 = appdir + "\\ets2.gif"
        ets2img = PhotoImage(master = self.main, width = 33, height = 18, file = ets2) 
        self.ets2mpButton = tkinter.Button(self.ets2Menu, command = self.launchETS2MP, text = "Launch Euro Truck Simulator 2 Multiplayer", image = ets2img, compound = "left", width = 330)
        self.ets2mpButton.pack(side = "left")
        self.ets2Button = tkinter.Button(self.ets2Menu, command = self.launchETS2, text = "Singleplayer")
        self.ets2Button.pack(side = "right")

        #ATS
        self.atsMenu = tkinter.Frame(self.main, width = 400, borderwidth = 5)
        self.atsMenu.pack()
        ats = appdir + "\\ats.gif"
        atsimg = PhotoImage(master = self.atsMenu, width = 42, height = 18, file = ats) 
        self.atsmpButton = tkinter.Button(self.atsMenu, command = self.launchATSMP, text = "Launch American Truck Simulator 2 Multiplayer", image = atsimg, compound = "left", width = 330)
        self.atsmpButton.pack(side = "left")
        self.atsButton = tkinter.Button(self.atsMenu, command = self.launchATS, text = "Singleplayer")
        self.atsButton.pack(side = "right")

        if (self.is64bitWin() == False):
            self.bitWarning = tkinter.Label(self.main, text = "WARNING: You seem to be running a 32 bit operating system. This is not supported for Multiplayer nor American Truck Simulator.", font = self.font_bitwarning, foreground = "#ff0000", wraplength = 500)
            self.bitWarning.pack()

        print("UI Opened")
        tkinter.mainloop()
        print("UI Closed")

    #Other UI stuff
    def quit(self):
        print("Quit command issued")
        self.main.destroy()

    def openSettings(self):
        print("Opening settings")
        tkinter.messagebox.showinfo("Settings", "This section has not been finished yet.")
        #self.settingsChanged = True

    #Games
    def launchETS2MP(self):
        call([self.settings.tmpdir + "\launcher_ets2mp.exe"])
        print("Launching Euro Truck Simulator 2 MP")
        self.quit()

    def launchETS2(self):
        if (self.is64bitWin() == True):
            call([self.settings.ets2dir + "\\bin\win_x64\eurotrucks2.exe"])
            print("Launching Euro Truck Simulator 2 SP 64bit")
            self.quit()
        else:
            call([self.settings.ets2dir + "\\bin\win_x86\eurotrucks2.exe"])
            print("Launching Euro Truck Simulator 2 SP 32bit")
            self.quit()

    def launchATSMP(self):
        call([self.settings.tmpdir + "\launcher_ets2mp.exe"])
        print("Launching American Truck Simulator MP")
        self.quit()

    def launchATS(self):
        call([self.settings.atsdir + "\\bin\win_x64\\amtrucks.exe"])
        print("Launching American Truck Simulator 2 SP")
        self.quit()

    #Bits
    def os_platform(self):
        true_platform = os.environ['PROCESSOR_ARCHITECTURE']
        try:
            true_platform = os.environ["PROCESSOR_ARCHITEW6432"]
        except KeyError:
            pass
        return true_platform

    def is64bitWin(self):
        if (self.os_platform() == "AMD64" or self.os_platform() == "I64"):
            return True
        else:
            return False

l = Launcher()
while (l.settingsChanged == True):
    l = Launcher()

print("Goodbye")
