import ui
import tkinter
import lolapi

root = tkinter.Tk()
app = ui.Application(lolapi.LOL(""),root)
app.mainloop()