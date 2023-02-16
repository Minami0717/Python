from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry("640x480")

frame = Frame(window)
frame.pack(fill="both", expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

txt = Text(frame, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

window.mainloop()
