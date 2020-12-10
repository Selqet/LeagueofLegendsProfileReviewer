import tkinter as tk
from PIL import ImageTk, Image

welcomewin = tk.Tk()
welcomewin.geometry('500x150')

wlabel = tk.Label(welcomewin, text = "Enter API")
wlabel.place(y = 5)

wentry = tk.Entry(welcomewin, width = 43)
wentry.place(anchor = tk.SE)

welcomewin.mainloop()
r'''
root = tk.Tk()

canv = tk.Canvas(root, width=1215, height=717, bg='white')
canv.grid()

img = ImageTk.PhotoImage(Image.open(r".\Dragontail\img\champion\splash\Azir_4.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=tk.NW, image=img)
root.mainloop()
'''


