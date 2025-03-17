import csv
import string
import requests
import random
from random import randint
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def Create():
  def username_generator ():
   adj = 'https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-adjectives.txt'
   noun = 'https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt'
   r = requests.get(adj)
   d = requests.get(noun)
   text1 = r.text
   text2 = d.text
   word1 = text1.split()
   word2 = text2.split()
   random_number = randint(0,99)
   random_number1 = randint(0,len(word1))
   random_number2 = randint(0,len(word2))
   x = word1[random_number1] + word2[random_number2] + str(random_number)
   return''.join(x)
  def pass_generator(size = 8, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):
   y = (random.choice(chars) for _ in range(size))
   return ''.join(y)

  input_file = INPUT.get()

  with open(input_file, 'r') as csvinput:
    with open('UsernameAndPassword.csv', 'w') as csvoutput:
        header = ["First Name","Last Name","Username","Password"]
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []

        for row in reader:
            row.append(username_generator())
            row.append(pass_generator())
            all.append(row)

        writer.writerow(header)
        writer.writerows(all)

  with open('UsernameAndPassword.csv') as f:
     reader = csv.DictReader(f, delimiter=',')
     for row in reader:
         user = row['Username']
         passw = row['Password']
         output.insert("", 0, values=(user, passw))

window = Tk()
window.geometry('1150x700')
window.title('Lietotājvārdu un paroles generators')
window.configure(bg = 'chartreuse1')

BACK = Label(window, bg = 'white')
BACK.place(x=58, y=56, width=1032,height=580)

T = Label(BACK, text = "Lietotājvārdu un paroles generators", bg = 'white', font = ('Comic Sans MC', 25, 'bold'))
T.place(x = 4, y = 56, width=1032,height=50)

#Saraksta nosaukuma input
INPUT_NAME = Label(BACK, text = 'Saraksta nosaukums', bg = 'white', font = ('Comic Sans MC', 10, 'italic'), fg = 'black')
INPUT_NAME.place(x=50, y=100, width=150,height=60)

INPUT = Entry(BACK, bg = 'white', relief = SOLID, font = ('Comic Sans MC', 15, 'italic'), bd=1)
INPUT.place(x=50, y = 180, height = 60, width = 260, anchor = "w")

#Instrukcija
I = Label(BACK, text = '''1. Ievadiet saraksta nosaukumu. 
2. Pēc tam klikšķiniet ”Izveidot”, lai veidot paroles 
un lietotājvārdus. 
3. Nospiediet izveidot linku, lai saņemt linku faila 
saglabāšanai.''', bg = 'white', font = ('Comic Sans MC', 13, 'italic'), anchor = 'nw', justify = LEFT)
I.place(x = 50, y = 240, width=480,height=250)

#Pogas Izveidot un Izveidot saiti
CREATE = Button(BACK, text = 'Izveidot',  font = ('Comic Sans MC', 17, 'italic'), bg = 'chartreuse1', fg = 'black', bd = 0)
CREATE.place(x=50, y=400, width=150,height=60)
CREATE.config(command=Create) 

CREATE_LINK = Button(BACK, text = 'Izveidot saiti',  font = ('Comic Sans MC', 17, 'italic'), bg = 'chartreuse1', fg = 'black', bd = 0)
CREATE_LINK.place(x=260, y=400, width=200,height=60)

# Saite
LINK_BOX = Label(BACK, bg = 'white', font = ('Comic Sans MC', 10, 'italic'), relief = SOLID, fg = 'black', bd=1)
LINK_BOX.place(x=100, y=480, height=60, width = 300)

#Paroļu un lietotājvārdu radīšana
SCROLL = LabelFrame(BACK, bd=2, bg = 'white', width = 50)
SCROLL.place(x=550, y=130, width=420, height= 390)

s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading', background="white")
s.configure("Treeview.Heading", borderwidth=0)

scrollbary = Scrollbar(SCROLL, orient=VERTICAL)

output = ttk.Treeview(SCROLL, columns=("Usernames", "Passwords"), height=400, selectmode="extended", yscrollcommand=scrollbary.set)  
scrollbary.config(command=output.yview)
scrollbary.pack(side=RIGHT, fill=Y)
output.heading('Usernames', text="Usernames", anchor=W)
output.heading('Passwords', text="Passwords", anchor=W)
output.column('#0', stretch=NO, minwidth=0, width=0)
output.column('#1', stretch=NO, minwidth=0, width=200)
output.column('#2', stretch=NO, minwidth=0, width=200)
output.pack()  

window.mainloop()