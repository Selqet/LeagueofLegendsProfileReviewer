import tkinter as tk
import Main
from tkinter import ttk
from PIL import ImageTk, Image

def WelcomeWindow():

    def ReadAPI():
        global apikey
        apikey = wentry.get()
        welcomewin.destroy()

    welcomewin = tk.Tk()
    welcomewin.geometry('400x120')
    welcomewin.title('Welcome, Summoner')

    wframe = tk.Frame(welcomewin, width = 400, height = 120)
    wframe.pack()

    wlabel = tk.Label(wframe, text = 'Enter your API key')
    wlabel.place(x = 200, y = 10, anchor = tk.N)

    wentry = tk.Entry(wframe, show = '*', width = 43)
    wentry.place(x = 200, y = 40, anchor = tk.N)

    wbutton = tk.Button(wframe, text = 'Confirm', command = ReadAPI)
    wbutton.place(x=200, y=70, anchor = tk.N)

    welcomewin.mainloop()

def MainWindow():

    def Search():
        summoner = srchsument.get()
        server = srchsrvr.get()
        Main.GetSummonerData(summoner, server)        

    def SwitchSummoner():
        pass

    root = tk.Tk()
    root.title('LeagueofLegendsProfileReviewer')

    background = tk.Canvas(root, width=1215, height=717, bg='white')
    background.grid()
    img = ImageTk.PhotoImage(Image.open(r'.\Resources\DefaultBackground.jpg'))
    background.create_image(0, 0, anchor=tk.NW, image=img)

    searchframe = tk.Frame(root, width = 200, height = 120, bg = 'white')
    searchframe.place(x=0, y=0)
    srchsumlbl = tk.Label(searchframe, text = "Summoner's name", bg = 'white')
    srchsumlbl.place(x=100, y=20, anchor = tk.N)
    srchsument = tk.Entry(searchframe, width = 20)
    srchsument.place(x=100, y=45, anchor = tk.N)
    srchsrvr = ttk.Combobox(searchframe, values=['BR1','EUN','EUW','JP1','KR','LA1','LA2','NA1','OC1','TR1','RU'], width = 5)
    srchsrvr.place(x=38, y=80)
    srchbtn = tk.Button(searchframe, text = 'Search', command = Search)
    srchbtn.place(x=110, y=76)

    root.mainloop()



