# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
import csv
import random
import smtplib
from PIL import ImageTk, Image
from datetime import datetime

class Problem(object):
  def __init__(self, question = "", a = "", b = "", c = "", d = "", correct = ""):
    object.__init__(self)
    self.question = question
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.correct = correct

class act():
    print "you entered"
    
class App(Tk):
  def __init__(self):
    Tk.__init__(self)
#    default_font = tkFont.nametofont("Niagra Solid")
#    default_font.configure(size=20)
    self.problems = []
    self.counter = 0
    self.marks = 0
    self.login()
    self.planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","Laika","Moon","Sputnik","Soyuz","Titan","SpaceShuttle"]
    #self.addComponents()
    #self.loadProblems()
    self.msg = []   
    #self.showProblem(0)
    
    self.mainloop()

  def login(self):
    self.title("Quiz")
    self.svalue = StringVar() 
    self.Avalue = StringVar() 
    self.Bvalue = StringVar()
    self.Cvalue = StringVar()
    self.Dvalue = StringVar()
    self.grid()
    t = Label(self, text="Please login")
    t.grid(column=0,row=0)
    w = Entry(self,textvariable=self.svalue)
    w.grid(column=0,row=1)
    foo = Button(self,text="Login",command=self.intro)
    foo.grid(column=0,row=2)
#    img=PhotoImage(file="neptune.png")
#    img.zoom(5, 5)
    self.path = 'imgs/blank.png'
    self.img = Image.open(self.path)
    self.img2 = self.img.resize((50, 50), Image.BILINEAR)
    self.img3 = ImageTk.PhotoImage(self.img2)
#    Aimage = Label(self, image = self.img3) 
#    Aimage.grid(column=1, row=3)

  def close_window(self):
     self.destroy()    

  def intro(self):
    print "clear grid"
    for widget in self.winfo_children():
       widget.destroy()
    self.grid()
    print "populate grid"
    t = Label(self, text="Welcome to the space quiz, you will now have to answer 10 quesions")
    t.grid(column=0,row=0)
    foo = Button(self,text="Start test",command=self.addComponents)
    foo.grid(column=0,row=1)
    foo2 = Button(self,text="Exit",command=self.close_window)
    foo2.grid(column=1,row=1)
    self.msg.append("Hi " + self.svalue.get()) 
    self.msg.append("You started the quiz at" + str(datetime.now()))
    self.msg.append("Here are your questions and answers and your results")   
    print str(datetime.now())
 
  def showMarks(self):
    print "clear grid"
    for widget in self.winfo_children():
       widget.destroy()
    self.grid()
    print "populate grid"
    t = Label(self, text="You have completed the quiz here are your marks")
    t.grid(column=0,row=0)
    t2 = Label(self, text=self.marks)
    t2.grid(column=0,row=1)
    if(self.marks <= 30):
       t3 = Label(self, text=":(")
       t3.grid(column=0,row=2)
    elif(self.marks <= 60):
       t3 = Label(self, text=":/")
       t3.grid(column=0,row=2)
    else:
       t3 = Label(self, text=":)")
       t3.grid(column=0,row=2)
    self.msg.append("Your total score is " + str(self.marks))
    foo = Button(self,text="retake test",command=self.addComponents)
    foo.grid(column=0,row=3)
    foo2 = Button(self,text="Exit",command=self.close_window)
    foo2.grid(column=1,row=3)
    foo3 = Button(self,text="Email results",command=self.email)
    foo3.grid(column=2,row=3)

  def email(self):
    print "place holder for email"
    toplevel = Toplevel()
    toplevel.grid()
    t3 = Label(toplevel, text="username")
    t3.grid(column=0,row=0)
    t4 = Label(toplevel, text="date")
    t4.grid(column=0,row=1)
    t5 = Label(toplevel, text="time")
    t5.grid(column=0,row=2)
    t5 = Label(toplevel, text="mark")
    t5.grid(column=0,row=3)
    t6 = Label(toplevel, text="questions and answers")
    t6.grid(column=0,row=4)
    fromaddr=""
    toaddrs = ""
    msg='\n'.join(self.msg) 
    username=""
    password=''
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    exit()



  
  def addComponents(self):
    """ add components to the GUI """
    self.counter = 0
    self.marks = 0
    for widget in self.winfo_children():
       widget.destroy()
    self.title("Quiz")
    self.grid()
    self.columnconfigure(0, minsize = 100)
    self.columnconfigure(1, minsize = 200)
    self.columnconfigure(2, minsize = 100)
    self.Name = Label(self, text=self.svalue.get())
    self.Name.grid(column=3,row=0)
    self.lblQuestion = Label(self, text = "Question")
    self.lblQuestion.grid(columnspan = 3, sticky = "we")
    #mi=PhotoImage(file="neptune.png")
    #mi.zoom(5, 5)
    self.btnA = Button(self, text = "A", command = self.checkA, fg='black')
    self.btnA.grid(columnspan = 3, sticky = "we")
    self.astatus = Label(self, text=self.Avalue.get())
    self.astatus.grid(column=3, row=2)
    self.Aimage = Label(self, image = self.img3)
    self.Aimage.grid(column=0, row=2)

    self.btnB = Button(self, text = "B", command = self.checkB, fg='black')
    self.btnB.grid(columnspan = 3, sticky = "we")
    self.bstatus = Label(self, text=self.Bvalue.get())
    self.bstatus.grid(column=3, row=3) 
    self.Bimage = Label(self, image = self.img3)
    self.Bimage.grid(column=0, row=2)
    
    self.btnC = Button(self, text = "C", command = self.checkC, fg='black')
    self.btnC.grid(columnspan = 3, sticky = "we")
    self.cstatus = Label(self, text=self.Cvalue.get())
    self.cstatus.grid(column=3, row=4) 
    self.Cimage = Label(self, image = self.img3)
    self.Cimage.grid(column=0, row=2)
    
    self.btnD = Button(self, text = "D", command = self.checkD, fg='black')
    self.btnD.grid(columnspan = 3, sticky = "we")
    self.dstatus = Label(self, text=self.Dvalue.get())
    self.dstatus.grid(column=3, row=5) 
    self.Dimage = Label(self, image = self.img3)
    self.Dimage.grid(column=0, row=2)
    
    self.btnPrev = Button(self, text = "prev", command = self.prev)
    self.btnPrev.grid(row = 6, column = 0)
    
    self.lblCounter = Label(self, text = "0")
    self.lblCounter.grid(row = 6, column = 1)
    
    self.btnNext = Button(self, text = "next", command = self.next)
    self.btnNext.grid(row = 6, column = 2)
    self.loadProblems()
    self.showProblem(0)
    
  def checkA(self):
    self.check("A")

  def checkB(self):
    self.check("B")

  def checkC(self):
    self.check("C")

  def checkD(self):
    self.check("D")
    
  def check(self, guess):
    #compares the guess to the correct answer
    print "guess " + guess
    correct = self.problems[self.counter].correct
    print "correct " + correct
    self.msg.append("Your answer was " + guess)
    if guess == correct:
      #update ans
      if guess == "A":
         self.astatus["text"] = "✓"
      elif guess == "B":
         self.bstatus["text"] = "✓"
      elif guess == "C":
         self.cstatus["text"] = "✓" 
      else:
         self.dstatus["text"] = "✓"
      
      self.marks+=10
    else:
      if guess == "A":
         self.astatus["text"] = "x"
      elif guess == "B":
         self.bstatus["text"] = "x"
      elif guess == "C": 
         self.cstatus["text"] = "x"
      else:
         self.dstatus["text"] = "x"
      
      if correct == "A":
         self.btnA["fg"] = 'green'
      elif correct == "B":
         self.btnB["fg"] = 'green'
      elif correct == "C": 
         self.btnC["fg"] = 'green'
      else:
         self.btnD["fg"] = 'green'
      
  def prev(self):
    self.counter -= 1
    if self.counter < 0:
      self.counter = 0
    self.showProblem(self.counter)
    
  def next(self):
    self.counter += 1
    print self.marks
    if self.counter >= len(self.problems):
      print "if"
      self.counter = len(self.problems) - 1
      self.showMarks()
    else:
      self.showProblem(self.counter)
    print "count" + str(self.counter)
    if self.counter == 10:
      print "should finish"
      self.counter = len(self.problems) - 1
      self.showProblem(self.counter)
      self.showMarks()
    print "show " + str(self.counter)
    #self.showProblem(self.counter)

  def showProblem(self, counter):
    self.lblQuestion["text"] = self.problems[counter].question
    self.msg.append(self.problems[counter].question)
    self.btnA["text"] = self.problems[counter].a
    if(self.problems[counter].a.replace(" ", "") in self.planets):
       self.pathA = 'imgs/' + self.problems[counter].a.replace(" ", "") + '.png'
       self.imgA = Image.open(self.pathA)
       self.img2A = self.imgA.resize((50, 50), Image.BILINEAR)
       self.img3A = ImageTk.PhotoImage(self.img2A)
       Aimage = Label(self, image = self.img3A) 
       Aimage.grid(column=0, row=2)
    
    else:
    #image blank
       self.pathA = 'imgs/blank.png'
       self.imgA = Image.open(self.pathA)
       self.img2A = self.imgA.resize((50, 50), Image.BILINEAR)
       self.img3A = ImageTk.PhotoImage(self.img2A)
       Aimage = Label(self, image = self.img3A) 
       Aimage.grid(column=0, row=2)

    self.btnA["fg"] = 'black'
    self.astatus["text"] = ""
    self.btnB["text"] = self.problems[counter].b
    self.btnB["fg"] = 'black'
    if(self.problems[counter].b.replace(" ", "") in self.planets):
       self.pathB = 'imgs/' + self.problems[counter].b.replace(" ", "") + '.png'
       self.imgB = Image.open(self.pathB)
       self.img2B = self.imgB.resize((50, 50), Image.BILINEAR)
       self.img3B = ImageTk.PhotoImage(self.img2B)
       Bimage = Label(self, image = self.img3B) 
       Bimage.grid(column=0, row=3)
    
    else:
    #image blank
       self.pathB = 'imgs/blank.png'
       self.imgB = Image.open(self.path)
       self.img2B = self.imgB.resize((50, 50), Image.BILINEAR)
       self.img3B = ImageTk.PhotoImage(self.img2B)
       Bimage = Label(self, image = self.img3B) 
       Bimage.grid(column=0, row=3)

    self.bstatus["text"] = ""
    self.btnC["text"] = self.problems[counter].c
    self.btnC["fg"] = 'black'
    self.cstatus["text"] = ""
    if(self.problems[counter].c.replace(" ", "") in self.planets):
       self.pathC = 'imgs/' + self.problems[counter].c.replace(" ", "") + '.png'
       self.imgC = Image.open(self.pathC)
       self.img2C = self.imgC.resize((50, 50), Image.BILINEAR)
       self.img3C = ImageTk.PhotoImage(self.img2C)
       Cimage = Label(self, image = self.img3C) 
       Cimage.grid(column=0, row=4)
    
    else:
    #image blank
       self.pathC = 'imgs/blank.png'
       self.imgC = Image.open(self.pathC)
       self.img2C = self.imgC.resize((50, 50), Image.BILINEAR)
       self.img3C = ImageTk.PhotoImage(self.img2C)
       Cimage = Label(self, image = self.img3C) 
       Cimage.grid(column=0, row=4)
    
    self.btnD["text"] = self.problems[counter].d
    self.btnD["fg"] = 'black'
    self.dstatus["text"] = ""
    if(self.problems[counter].d.replace(" ", "") in self.planets):
       self.pathD = 'imgs/' + self.problems[counter].d.replace(" ", "") + '.png'
       self.imgD = Image.open(self.pathD)
       self.img2D = self.imgD.resize((50, 50), Image.BILINEAR)
       self.img3D = ImageTk.PhotoImage(self.img2D)
       Dimage = Label(self, image = self.img3D) 
       Dimage.grid(column=0, row=5)
    
    else:
    #image blank
       self.pathD = 'imgs/blank.png'
       self.imgD = Image.open(self.pathD)
       self.img2D = self.imgD.resize((50, 50), Image.BILINEAR)
       self.img3D = ImageTk.PhotoImage(self.img2D)
       Dimage = Label(self, image = self.img3D) 
       Dimage.grid(column=0, row=5)

    self.lblCounter["text"] = self.counter

  def loadProblems(self):
    question_list = random.sample(range(1, 20), 10)
    print question_list.sort()
    with open('question-database.csv', 'rb') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
       for i, row in enumerate(spamreader):
          if i in question_list:
             print i
             print row
             print row[5]
             self.problems.append(Problem(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]))
  
    
def main():
  a = App()
  
if __name__ == "__main__":
  main()
  
