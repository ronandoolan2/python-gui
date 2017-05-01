#import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage

path = '/home/ronan/Downloads/python/elance/april2/neptune.png'

root = Tk()
#img = ImageTk.PhotoImage(Image.open(path))
#img = PhotoImage(Image.open(path))
img = Image.open(path)
img2 = img.resize((50, 50), Image.BILINEAR)
img3 = ImageTk.PhotoImage(img2)
root.grid()
#img2 = img.thumbnail((50, 50))
#img2 = img.subsample(2, 2)
#img3=ImageTk.PhotoImage(img2)
#cover = resizeimage.resize_cover(img, [100, 100])
panel = Label(root, image = img3)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(column=0,row=1)

root.mainloop()
