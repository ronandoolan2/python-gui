#import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image

path = '/home/ronan/Downloads/python/elance/april2/neptune.png'

root = Tk()
img = ImageTk.PhotoImage(Image.open(path))
#img.zoom(5, 5)
root.grid()
#img2 = img.thumbnail((50, 50))
#img3=ImageTk.PhotoImage(img2)
panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(column=0,row=1)

root.mainloop()
