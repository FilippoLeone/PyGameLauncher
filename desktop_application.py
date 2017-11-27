from tkinter import *
import os.path,platform
from PIL import ImageTk, Image
from os.path import expanduser
from simplecrypt import encrypt, decrypt
import game

VERSION = " v0.1a" # Launcher version.

class Application(Frame):

    #### Encryption Start ######

    ## UserID / PrivKey Reading start ##
    def read_key(self):
        with open("UserID.battle","r") as self.key_file:
            self.key = self.key_file.read()
            return self.key
    ## UserID / PrivKey Reading End ##

    def decrypt_coin_string(self):
        self.password = self.read_key()
        with open("coins","rb") as self.keyfile:
            self.key = self.keyfile.read()
            self.key = decrypt(self.password, self.key)
            return self.key

    def encrypt_coin_string(self):
        self.password = self.read_key()
        self.coins = self.coins_managment()
        self.key = encrypt(self.password ,self.coins)
        self.keyfile = open("coins","w")
        self.keyfile.write(self.key)
        self.keyfile.close()

    #### Encryption End #########

    ### Coins Managment Start #######
    def coins_managment(self):
        if (self.firstuse):
            self.coins = self.decrypt_coin_string()
            self.firstuse = FALSE
            return self.coins
        else:
            self.aggiorna_coins()


    def aggiorna_coins(self, addcoins):
        self.coins = self.coins + self.addcoins
        return self.coins

    ### Coins Managment End #####

    def primo_avvio_coins(self):
        # todo check if file exists and create it if it doesn`t.
        self.curr_os = str(platform.system())
        if (self.curr_os == "Windows"):
            self.filedirectory = (expanduser("~") + "\\PyLauncher\\coins")
            return str(self.filedirectory)
        elif (self.curr_os == "Linux"):
            self.filedirectory = expanduser("~" + "/PyLauncher/coins")
            return str(self.filedirectory)
        else:
            print("Os not detected.")
            #todo do something here, like assign a static path and add MacOSX support
            return

    def file_check(self):
        if os.path.exists(self.primo_avvio_coins()):
            pass
        else:
            self.password = self.read_key()
            self.coins = "0"
            self.key = encrypt(self.password ,self.coins)
            self.keyfile = open("coins","w")
            self.keyfile.write(self.key)
            self.keyfile.close()

   ## def coin_exists(self):
     ##   if (os.path.isfile("coins")):
       ##     self.coins_managment()
       ## else:
       ##     pass


    def print_info(self):
        print("Info here")

### Graphical Interface Start ####

    def createCanvas(self):
        self.canvas = Canvas(root)
        self.canvas.pack()


    def createWidgets(self):
        ## temp func calling for alpha purposes ##
        #self.encrypt_coin_string()

        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        self.panel = Label(root, image=self.img)
        self.panel.pack(side="top", fill="both", expand="yes")

        self.coins = self.coins_managment()
        self.coins = str(self.coins)
        self.textbox = Text(root, height=1, width=35)

        self.textbox.insert(END,'{0}: {1} {2}'.format("Your Current Balance is", self.coins[2:-1],"Coins."))
        #self.textbox["state"] = DISABLED
        self.textbox.pack(pady=15, padx=10)


        self.coin_button = Button(root, height=1, width=20, command=self.print_info)
        self.coin_button["text"] = "(?) Information About the game"
        self.coin_button.pack(fill=X, pady=5, padx=30)

        self.QUEST = Button(root, height=1, width=20, command=self.OpenGame)
        self.QUEST["text"] = "(!) I want to play!"
        self.QUEST.pack(fill=X, pady=5, padx=30)

        self.REWARD = Button(root, height=1, width=20)
        self.REWARD["text"] = "(@_@) Rewards"
        self.REWARD.pack(fill=X, pady=5,padx=30)

        self.QUIT = Button(root, height=1, width=5)
        self.QUIT["text"] = "Exit"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack(fill=X,padx=55,pady=15)
        #self.createCanvas()

### Graphical Interface End #####

    def OpenGame(self):
        root.destroy()
        game.Init()

    def __init__(self, master=None):
        self.firstuse = TRUE
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        #self.createCanvas()
#__Start
    def __destroy__(self):
        self.root.destroy()

root = Tk()
root.title("PyGame Launcher" + VERSION)
app = Application(master=root)
app.mainloop()
root.destroy()
