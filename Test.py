import tkinter as tk
from PIL import ImageTk, Image

def WelcomeWindow():
    def ReadAPI():
        global apikey
        apikey = wentry.get()
        welcomewin.destroy()

    welcomewin = tk.Tk()
    welcomewin.geometry('400x120')

    wframe = tk.Frame(welcomewin, width = 400, height = 120)
    wframe.pack()

    wlabel = tk.Label(wframe, text = "Enter API key")
    wlabel.place(x = 200, y = 10, anchor = tk.N)

    wentry = tk.Entry(wframe, name = 'wentry', show = '*', width = 43)
    wentry.place(x = 200, y = 40, anchor = tk.N)

    wbutton = tk.Button(wframe, text = "Confirm", command = ReadAPI)
    wbutton.place(x=200, y=70, anchor = tk.N)

    welcomewin.mainloop()

WelcomeWindow()
print(apikey)


r'''
root = tk.Tk()

canv = tk.Canvas(root, width=1215, height=717, bg='white')
canv.grid()

img = ImageTk.PhotoImage(Image.open(r".\Dragontail\img\champion\splash\Azir_4.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=tk.NW, image=img)
root.mainloop()
'''


