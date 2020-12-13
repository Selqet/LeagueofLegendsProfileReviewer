import requests
import json
import Resources
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def ReadAPI():
    global api_key
    api_key = wentry.get()
    welcomewin.destroy()

def Search():
    summoner = srchsument.get()
    server = srchsrvr.get()
    GetSummonerData(summoner, server) 

def SwitchSummoner(champions, masteryscore):
    mainmasteryframe = tk.Frame(root)
    mainmasteryframe.place(x=1215, y=0, anchor = tk.NE)

    championlbl = tk.Label(mainmasteryframe, text = 'Champions')
    championlbl.grid(row=0,column=0)
    championlbl = tk.Label(mainmasteryframe, text = 'Champions')
    championlbl.grid(row=0,column=3)
    masterylbl = tk.Label(mainmasteryframe, text = 'Score')
    masterylbl.grid(row=0,column=1)
    masterylbl = tk.Label(mainmasteryframe, text = 'Score')
    masterylbl.grid(row=0,column=4)
    for i in range(10):
        championlbl = tk.Label(mainmasteryframe, text = champions[i])
        championlbl.grid(row=i+1,column=0)
        masterylbl = tk.Label(mainmasteryframe, text = masteryscore[i])
        masterylbl.grid(row=i+1,column=1)
        emptylbl = tk.Label(mainmasteryframe, text = '   ')
        emptylbl.grid(row=i+1,column=2)
        championlbl = tk.Label(mainmasteryframe, text = champions[i+10])
        championlbl.grid(row=i+1,column=3)
        masterylbl = tk.Label(mainmasteryframe, text = masteryscore[i+10])
        masterylbl.grid(row=i+1,column=4) 

            
def WelcomeWindow():
    global welcomewin
    global wentry

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
    global root
    global srchsument
    global srchsrvr
    global background

    root = tk.Tk()
    root.title('LeagueofLegendsProfileReviewer')

    background = tk.Canvas(root, width=1215, height=717, bg='white')
    background.grid()
    img = ImageTk.PhotoImage(Image.open('.\\Resources\\DefaultBackground.jpg'))
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



def GetSummonerData(summoner, server):
    sumbynameresp = requests.get(f'https://{Resources.servers[server]}/lol/summoner/v4/summoners/by-name/{summoner}?api_key={api_key}')
    summonerdata = json.loads(sumbynameresp.content)
    summ_id = summonerdata['id']
    masteryresp = requests.get(f'https://{Resources.servers[server]}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summ_id}?api_key={api_key}')
    mastery = json.loads(masteryresp.content)
    with open(r'.\Dragontail\10.24.1\data\en_US\championFull.json', 'r') as readf:
        championfulldata = json.load(readf)

    keys = championfulldata['keys']
    champions = []
    masteryscore = []
    for champion in mastery[:20]:
        masteryscore.append(champion['championPoints'])
        championkey = str(champion['championId'])
        champions.append(keys[championkey])

    SwitchSummoner(champions, masteryscore)



WelcomeWindow()
MainWindow()

