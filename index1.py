#!/usr/bin/python
import random

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk ,Image
import tkinter.font as font
from tkinter.simpledialog import askstring

















top = tk.Tk()
#top.geometry("300x300+120+120")
top['bg'] ='#49A'
myFont = font.Font(family='Helvetica', size=15, weight='bold')


# Code to add widgets will go here...
def result_values():
    lbl_score_com['fg']='blue'
    lbl_score_com['bg']='#49A'
    lbl_score_you['fg']='blue'
    lbl_score_you['bg']='#49A'
    lbl_user = lbl_value_r["text"]
    lbl_computer = lbl_random_r["text"]
    lbl_dec=int(lbl_decrese["text"])

    if(lbl_user=="Rock" and lbl_computer=="Paper"):

        lbl_score_com["text"]=increase_com()
        lbl_won['text']='Computer win'
    elif(lbl_user=="Rock" and lbl_computer=="Scissor"):
        lbl_score_you["text"]=increase_you()
        lbl_won['text']='You wins'
    elif(lbl_user=="Paper" and lbl_computer=="Rock"):
        lbl_score_you["text"]=increase_you()
        lbl_won['text']='You win'
    elif(lbl_user=="Paper" and lbl_computer=="Scissor"):
        lbl_score_com["text"]=increase_com()
        lbl_won['text']='Computer win'
    elif(lbl_user=="Scissor" and lbl_computer=="Rock"):
        lbl_score_com["text"]=increase_com()
        lbl_won['text']='Computer win'
    elif(lbl_user=="Scissor" and lbl_computer=="Paper"):
        lbl_score_you["text"]=increase_you()
        lbl_won['text']='You win'
    else:

        #messagebox.showinfo("top","You are in tie")
        lbl_won['text']='You are in Tie with Computer'

    #if(lbl_dec==10):
        #lbl_won['text']='winner is {}'.format(winner())







def increase_you():
    value = int(lbl_score_you["text"])
    lbl_score_you["text"] = f"{value + 1}"

def increase_com():
    value = int(lbl_score_com["text"])
    lbl_score_com["text"] = f"{value + 1}"


def random_values():
    val=random.choice(["Rock","Paper","Scissor"])
    #filename = ImageTk.PhotoImage(file = random.choice(val))


    #img2=Image.open (val)
    #image2 = img2.resize((50, 50), Image.ANTIALIAS)
    #val_random=random.choice(val)
    #img2=Image.open (val_random)
    #image2 = img2.resize((50, 50))
    #my_img2 = ImageTk.PhotoImage(img2)
    #filechoices = ["rock.jpg","paper.jpg","scissor.jpg"]

    #filename = ImageTk.PhotoImage(file = random.choice(val))




    #lbl_random_r.configure(image=filename,width=50,height=50)
    lbl_random_r['text']=val
    lbl_random_r['font']=myFont





def handlePress_rock():



        random_values()
        '''img2=Image.open ("rock.jpg")
        image2 = img2.resize((100, 100), Image.ANTIALIAS)
        my_img2 = ImageTk.PhotoImage(image2)


        lbl_value_r.configure(image=my_img2)'''
        lbl_value_r["text"]='Rock'


        #lbl_value_r["text"]=image=photo1
        result_values()





def handlePress_paper():

        random_values()
        '''img2=Image.open ("paper.jpg")
        image2 = img2.resize((100, 100), Image.ANTIALIAS)
        my_img2 = ImageTk.PhotoImage(image2)


        lbl_value_r.configure(image=my_img2)'''

        lbl_value_r["text"]='Paper'



        result_values()




def handlePress_scissor():

        random_values()
        '''img2=Image.open ("scissor.jpg")
        image2 = img2.resize((100, 100), Image.ANTIALIAS)
        my_img2 = ImageTk.PhotoImage(image2)


        lbl_value_r.configure(image=my_img2)'''

        lbl_value_r["text"]='Scissor'

        #lbl_value_r["text"]=my_img2



        result_values()


def decrese(event):
    value = int(lbl_decrese["text"])



    if(value==10):
        lbl_won['text']='winner is {}'.format(winner())

        messagebox.showinfo("top","winner is {}".format(winner()))
        msg=messagebox.askquestion('"Yes/No"','Do You want to Play again')
        print(msg)
        if(msg=='yes'):
            lbl_decrese['text']='0'
            lbl_score_you['text']='0'
            lbl_score_com['text']='0'
            lbl_won['text']=''
            lbl_value_r['text']=''
            lbl_random_r['text']=''
        if(msg=='no'):
            exit()


    else:
        lbl_decrese["text"] = f"{value + 1}"
def winner():
    you=int(lbl_score_you["text"])
    com=int(lbl_score_com["text"])
    if(you > com):
        return "You"
    elif(you==com):
        return "Both,Scores Are In Tie"
    else:
        return "Computer"







top.rowconfigure([1,2,3,4,5,6,7,8],minsize=50)
top.columnconfigure([2, 4, 6],minsize=50)

greeting = tk.Label(text="Welcome To Rock Paper Scissor Game",foreground="yellow",background="blue")
greeting.grid(row=1,column=4,padx=5,pady=25)
greeting['font']=myFont

lbl_won=tk.Label(text='',bg="#49A")
lbl_won.grid(row=2,column=4)
lbl_won['font']=myFont


lb_chance=tk.Label(text="Round")
lb_chance.grid(row=3,column=4,padx=10)
lb_chance['font']=myFont
lbl_decrese=tk.Label(text="0",bg='#49A')
lbl_decrese.grid(row=3,column=5)
lbl_decrese['font']=myFont



img2=Image.open ("paper.jpg")
image2 = img2.resize((150, 150), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(image2)

img3=Image.open ("scissor.jpg")
image3 = img3.resize((150, 150), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(image3)

img1=Image.open ("rock.jpg")
image1 = img1.resize((150, 150), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(image1)





button_rock = tk.Button(text="Rock", image=my_img1,
command=handlePress_rock)
button_paper = tk.Button(text="Paper", image=my_img2,
command=handlePress_paper)
button_scissor = tk.Button(text="Scissor",image=my_img3,
command=handlePress_scissor)

button_rock.grid(row=4, column=2,padx=150,pady=100)
button_rock.bind("<Button-1>", decrese)

button_paper.grid(row=4, column=4,padx=150,pady=100 )
button_paper.bind("<Button-1>", decrese)

button_scissor.grid(row=4, column=6,padx=150,pady=100)
button_scissor.bind("<Button-1>", decrese)


lbl_value=tk.Label(top,text="You Choose  ")
lbl_value.grid(row=5,column=2)
lbl_value['font']=myFont
lbl_value_r=tk.Label(top,text="",bg="#49A")
lbl_value_r.grid(row=5,column=4)
lbl_value_r['font']=myFont


lbl_random=tk.Label(top,text="Computer Choose")
lbl_random.grid(row=7,column=2)
lbl_random['font']=myFont
lbl_random_r=tk.Label(top,text="",bg="#49A")
lbl_random_r.grid(row=7,column=4)



lbl_score_you=tk.Label(top,text="0",bg='#49A',fg='#49A')
lbl_score_you.grid(row=5,column=6)
lbl_score_you['font']=myFont
lbl_score_com=tk.Label(top,text="0",bg='#49A',fg='#49A')
lbl_score_com.grid(row=7,column=6)
lbl_score_com['font']=myFont



lbl_tie=tk.Label(text='')
lbl_tie.grid(row=8,column=5)
lbl_tie['font']=myFont

































# define font













top.mainloop()
