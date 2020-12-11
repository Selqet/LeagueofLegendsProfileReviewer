import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

background = tk.Canvas(root, width=1215, height=717, bg='white')
background.grid()

searchframe = tk.Frame(root, width = 200, height = 200, bg = 'white')
searchframe.place(x=0, y=0)
srchsumlbl = tk.Label(searchframe, text = "Summoner's name", bg = 'white')
srchsumlbl.place(x=100, y=20, anchor = tk.N)

img = ImageTk.PhotoImage(Image.open(r'.\Resources\DefaultBackground.jpg'))
background.create_image(0, 0, anchor=tk.NW, image=img)

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


