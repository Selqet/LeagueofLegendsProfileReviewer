import lolapi
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self,api :lolapi.LOL,master=None):
        super().__init__(master)
        self.pack()
        self.api = api
        self.master = master
        self.init_window()
        self.mainmasteryframe = tk.Frame(self)

        self.background = tk.Canvas(self, width=1215, height=717)
        self.background.pack()
        img = Image.open('./Resources/DefaultBackground.jpg')
        self.canvas_img = ImageTk.PhotoImage(image=img)
        self.background.create_image(0, 0,anchor=tk.NW,image=self.canvas_img)
        self.searchframe = tk.Frame(self, width = 200, height = 120, bg = 'white')
        self.searchframe.place(x=0, y=0)
        self.srchsumlbl = tk.Label(self.searchframe, text = "Summoner's name", bg = 'white')
        self.srchsumlbl.place(x=100, y=20, anchor = tk.N)
        self.srchsument = tk.Entry(self.searchframe, width = 20)
        self.srchsument.place(x=100, y=45, anchor = tk.N)
        self.srchsrvr = ttk.Combobox(self.searchframe, values=['BR1','EUN1','EUW1','JP1','KR','LA1','LA2','NA1','OC1','TR1','RU'], width = 5)
        self.srchsrvr.current(10)
        self.srchsrvr.place(x=38, y=80)
        self.srchbtn = tk.Button(self.searchframe, text = 'Search', command = self.Search)
        self.srchbtn.place(x=110, y=76)

    def init_window(self):
        self.master.maxsize(1215,717)
        self.master.minsize(1215,717)
        self.master.geometry("1215x717")
        self.master.title('League of Legends Profile Reviewer')

    def ChangeBackground(self, champion):
        self.canvas_img = self.api.get_champion_image(champion)
        self.background.create_image(0, 0,anchor=tk.NW,image=self.canvas_img)
    
    def Search(self):
        self.mainmasteryframe.destroy()
        self.img = Image.open('./Resources/DefaultBackground.jpg')
        self.canvas_img = ImageTk.PhotoImage(image=self.img)
        self.background.create_image(0, 0,anchor=tk.NW,image=self.canvas_img)
        summoner = self.srchsument.get()
        region = self.srchsrvr.get()
        champions = self.api.get_champion_data(summoner, region, 20)
        if champions == -1 or len(champions) == 0:
            return
        leaguedata = self.api.get_summoner_league(region)
        self.CreateMasteryTable(champions)
        self.ChangeBackground(list(champions.keys())[0])
        self.CreateRankInfo(leaguedata)

    def CreateMasteryTable(self, champions):
            self.mainmasteryframe = tk.Frame(self)
            self.mainmasteryframe.place(x=1215, y=0, anchor = tk.NE)
            i = 0
            self.championlbl = tk.Label(self.mainmasteryframe, text = 'Champion')
            self.championlbl.grid(column = 0, row = i)
            self.championlbl = tk.Label(self.mainmasteryframe, text = '   ')
            self.championlbl.grid(column = 1, row = i)
            self.championlbl = tk.Label(self.mainmasteryframe, text = 'Score')
            self.championlbl.grid(column = 2, row = i)
            for key in champions:
                i += 1
                self.championlbl = tk.Label(self.mainmasteryframe, text = key)
                self.championlbl.grid(column = 0, row = i)
                self.championlbl = tk.Label(self.mainmasteryframe, text = '   ')
                self.championlbl.grid(column = 1, row = i)
                self.championlbl = tk.Label(self.mainmasteryframe, text = champions[key])
                self.championlbl.grid(column = 2, row = i)
    
    #940 165
    def CreateRankInfo(self, leaguedata):
        for item in leaguedata:
            if item['queueType'] == 'RANKED_SOLO_5x5':
                self.rankimg = self.api.get_rank_image(item["tier"])
                self.background.create_image(150, 540, image=self.rankimg)
                return
        

        
class WelcomeWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.master.geometry("400x120")
        self.master.maxsize(400,120)
        self.master.title('Welcome, Summoner')
        self.wlabel = tk.Label(self,text = 'Enter your API key')
        self.wlabel.grid(pady = 5)
        self.wentry = tk.Entry(self,show = '*', width = 43)
        self.wentry.grid(pady = 5)
        self.wbutton = tk.Button(self,text = 'Confirm', command = self.EnterApiKey)
        self.wbutton.grid(pady = 5)
        
    def EnterApiKey(self):
        api_key = self.wentry.get()
        api = lolapi.LOL(api_key)
        Application(api,self.master)
        self.destroy()