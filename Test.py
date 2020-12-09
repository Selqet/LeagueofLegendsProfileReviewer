import tkinter as tk

def Close():
    startwindow.destroy()

startwindow = tk.Tk()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command = Close
)
button.pack()
startwindow.mainloop()


