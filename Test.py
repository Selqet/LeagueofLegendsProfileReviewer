import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def Search():
    summmoner = srchsument.get()
    server = srchsrvr.get()
    print(summmoner)
    print(server)

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
r'''
img = ImageTk.PhotoImage(Image.open(r".\Dragontail\img\champion\splash\Azir_4.jpg"))  # PIL solution
background.create_image(0, 0, anchor=tk.NW, image=img)

root = tk.Tk()

canv = tk.Canvas(root, width=1215, height=717, bg='white')
canv.grid()

img = ImageTk.PhotoImage(Image.open(r".\Dragontail\img\champion\splash\Azir_4.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=tk.NW, image=img)
root.mainloop()
'''


