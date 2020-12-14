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

        self.background = tk.Canvas(self, width=1215, height=717, bg='white')
        self.background.pack()
        img = Image.open('./Resources/DefaultBackground.jpg')
        self.canvas_img = ImageTk.PhotoImage(image=img)
        self.background.create_image(0, 0,anchor=tk.NW,image=self.canvas_img)
        self.button = tk.Button(self,text='Search', command=self.Splash)
        self.button.place(x=10,y=10)
    
    def init_window(self):
        self.master.maxsize(1215,717)
        self.master.minsize(1215,717)
        self.master.geometry("1215x717")
        self.master.title('League of Legends Profile Reviewer')

    def Splash(self):
        self.canvas_img = self.api.get_champion_image("Aatrox")
        self.background.create_image(0, 0,anchor=tk.NW,image=self.canvas_img)

class WelcomeWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.master.geometry("400x120")
        self.master.maxsize(400,120)
        self.master.title('Welcome, Summoner')
        self.wlabel = tk.Label(self,text = 'Enter your API key')
        self.wlabel.place(x = 200, y = 10, anchor = tk.N)
        self.wlabel.pack()
        self.wentry = tk.Entry(self,show = '*', width = 43)
        self.wentry.place(x = 200, y = 40, anchor = tk.N)
        self.wentry.pack()
        self.wbutton = tk.Button(self,text = 'Confirm', command = self.EnterApiKey)
        self.wbutton.place(x=200, y=70, anchor = tk.N)
        self.wbutton.pack()
        
    def EnterApiKey(self):
        api_key = self.wentry.get()
        api = lolapi.LOL(api_key)
        Application(api,self.master)
        self.destroy()