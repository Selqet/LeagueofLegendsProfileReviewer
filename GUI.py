import tkinter as tk
from PIL import ImageTk, Image

welcomewin = tk.Tk()
welcomewin.geometry()
wframe = tk.Frame(master = welcomewin, height = 150, width = 500)
wframe.pack()
wlabel = tk.Label(wframe, text = "Enter API")
wlabel.place(x=120,y=20)
wentry = tk.Entry(wframe, width = 43)
wentry.place(x=120, y=50)
welcomewin.mainloop()
r'''
root = tk.Tk()

canv = tk.Canvas(root, width=1215, height=717, bg='white')
canv.grid()

img = ImageTk.PhotoImage(Image.open(r".\Dragontail\img\champion\splash\Azir_4.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=tk.NW, image=img)
root.mainloop()
'''


