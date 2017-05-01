#import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage
import csv



#def addToList(self, str_to_add):
#    if str_to_add not in self.list_of_strings:
#        self.list_of_strings.append(str_to_add)
list_imgs = []
print type(list_imgs)
with open('question-database.csv', 'rb') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
       for row in spamreader:
          for i in range(1, 5):
             if row[i] not in list_imgs:
                list_imgs.append(row[i]) 

for img in list_imgs:
   print img

#with open('coors.csv', mode='r') as infile:
#    reader = csv.reader(infile)
#    with open('coors_new.csv', mode='w') as outfile:
#        writer = csv.writer(outfile)
#        mydict = {rows[0]:rows[1] for rows in reader}
#print mydict
#DataCaptured = csv.reader("questions-database.csv", delimiter=',') 

#Category, Year = [], []
#for row in DataCaptured:
#   print row
#    if row[0] not in Year:
#        Year.append(row[0])
#    if row[1] not in Category:
#        Category.append(row[1])    

#print Category, Year        
# ['Category1', 'Category2', 'Category3'] ['1994', '1995', '1996', '1998']
#path = '/home/ronan/Downloads/python/elance/april2/neptune.png'

#root = Tk()
#img = ImageTk.PhotoImage(Image.open(path))
#img = PhotoImage(Image.open(path))
#img = Image.open(path)
#img2 = img.resize((50, 50), Image.BILINEAR)
#img3 = ImageTk.PhotoImage(img2)
#root.grid()
#img2 = img.thumbnail((50, 50))
#img2 = img.subsample(2, 2)
#img3=ImageTk.PhotoImage(img2)
#cover = resizeimage.resize_cover(img, [100, 100])
#panel = Label(root, image = img3)
##panel.pack(side = "bottom", fill = "both", expand = "yes")
#panel.grid(column=0,row=1)

