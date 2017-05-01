from Tkinter import *
root = Tk()
svalue = StringVar() # defines the widget state as string
w = Entry(root,textvariable=svalue) # adds a textarea widget
w.textbox.grid(column=0,row=0)
def act():
    print("you entered")
    print('%s' % svalue.get())
foo = Button(root,text="Press Me", command=act)
foo.textbox.grid(column=0,row=1)
root.mainloop()
