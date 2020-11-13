#!/usr/bin/python
import random

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk ,Image
import tkinter.font as font


top = tk.Tk()
top['bg'] ='#49A'
# Code to add widgets will go here...
def result_values():
    lbl_user = lbl_value["text"]
    lbl_computer = lbl_random["text"]

    if(lbl_user=="Rock" and lbl_computer=="Paper"):

        lbl_score_com["text"]=increase_com()
    elif(lbl_user=="Rock" and lbl_computer=="Scissor"):
        lbl_score_you["text"]=increase_you()
    elif(lbl_user=="Paper" and lbl_computer=="Rock"):
        lbl_score_you["text"]=increase_you()
    elif(lbl_user=="Paper" and lbl_computer=="Scissor"):
        lbl_score_com["text"]=increase_com()
    elif(lbl_user=="Scissor" and lbl_computer=="Rock"):
        lbl_score_com["text"]=increase_com()
    elif(lbl_user=="Scissor" and lbl_computer=="Paper"):
        lbl_score_you["text"]=increase_you()
    else:
        lbl_tie["text"]="You are in tie"



def increase_you():
    value = int(lbl_score_you["text"])
    lbl_score_you["text"] = f"{value + 1}"
def increase_com():
    value = int(lbl_score_com["text"])
    lbl_score_com["text"] = f"{value + 1}"
def random_values():
    val=random.choice(("Rock","Paper","Scissor"))
    lbl_random["text"]=val


def handlePress_rock():



        random_values()


        lbl_value["text"] = "Rock"
        result_values()




def handlePress_paper():

        random_values()


        lbl_value["text"] = "Paper"
        result_values()



def handlePress_scissor():

        random_values()


        lbl_value["text"] = "Scissor"
        result_values()

def decrese(event):
    value = int(lbl_decrese["text"])



    if(value==10):
        messagebox.showinfo("top","winner is {}".format(winner()))
    else:
        lbl_decrese["text"] = f"{value + 1}"
def winner():
    you=int(lbl_score_you["text"])
    com=int(lbl_score_com["text"])
    if(you > com):
        return "You"
    else:
        return "Computer"























greeting = tk.Label(text="Welcom To Rock Paper Scissor Game",foreground="yellow",background="blue")
greeting.pack()

# define font
myFont = font.Font(family='Helvetica', size=15, weight='bold')


img1=Image.open ("rock.jpg")
image1 = img1.resize((150, 150), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(image1)

button_rock = tk.Button(
    text="Rock",


    image=my_img1,
    command=handlePress_rock
)
button_rock.bind("<Button-1>", decrese)
lbl_value=tk.Label(top,text="You Choose  ")
lbl_value.place(x=400,y=300)
lbl_value['font']=myFont
lbl_value=tk.Label(top,text="Change the text you")
lbl_value.place(x=700,y=300)
lbl_random=tk.Label(top,text="Computer Choose ")
lbl_random.place(x=400,y=500)
lbl_random['font']=myFont
lbl_random=tk.Label(top,text="Change the text computer")
lbl_random.place(x=700,y=500)

lbl_score_text_you=tk.Label(top,text="Your score is : ")
lbl_score_text_you.place(x=50,y=100)
lbl_score_text_you['font']=myFont
lbl_score_text_com=tk.Label(top,text="Computer score is : ")
lbl_score_text_com.place(x=50,y=150)
lbl_score_text_com['font']=myFont

lbl_score_you=tk.Label(top,text="0")
lbl_score_you.place(x=200,y=100)
lbl_score_com=tk.Label(top,text="0")
lbl_score_com.place(x=200,y=150)




button_rock.place(x=400,y=100)
img2=Image.open ("paper.jpg")
image2 = img2.resize((150, 150), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(image2)

button_paper = tk.Button(
    text="Paper",
    image=my_img2,
    command=handlePress_paper
)
button_paper.place(x=700,y=100)
button_paper.bind("<Button-1>", decrese)
img3=Image.open ("scissor.jpg")
image3 = img3.resize((150, 150), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(image3)
button_scissor = tk.Button(
    text="Scissor",
    image=my_img3,
    command=handlePress_scissor
)
button_scissor.place(x=1000,y=100)
button_scissor.bind("<Button-1>", decrese)

lb_chance=tk.Label(text="Round")
lb_chance.place(x=450,y=50)
lb_chance['font']=myFont
lbl_decrese=tk.Label(text="0")
lbl_decrese.place(x=200,y=50)








top.mainloop()
