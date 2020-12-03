from tkinter import *
from PIL import ImageTk, Image
root = Tk()

canv = Canvas(root, width=2000, height=2000, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open(r"F:\Python\Project\Dragontail\img\champion\splash\Azir_4.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=NW, image=img)

mainloop()
input()

