import tkinter as tk
import tkinter.font as font
from PIL import ImageTk ,Image
import random
from tkinter import messagebox,Canvas
from tkinter.simpledialog import askstring
import time
from itertools import count






def winner_yc():
    #from tkinter import *
    #import time
    #import os
    '''root = tk.Tk()

    frames = [ImageTk.PhotoImage(file='gif1.gif',format = 'gif -index %i' %(i)) for i in range(70)]

    def update(ind):

        frame = frames[ind]
        ind += 1

        label.configure(image=frame)
        root.after(70, update, ind)
    label = tk.Label(root)
    label.grid(row=0,column=0)
    root.after(0, update, 0)
    root.mainloop()'''

    class ImageLabel(tk.Label):
        """a label that displays images, and plays them if they are gifs"""
        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)

    root = tk.Toplevel()
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('winner.gif')

    root.after(5000, lambda: root.destroy()) # Destroy the widget after 30 seconds

    #root.after(5000,messagebox.askquestion(top,'Do you want to play again') ) # Destroy the widget after 30 seconds
# Destroy the widget after 30 seconds







    root.mainloop()










def win(lbl_won):
    top2=tk.Toplevel()
    top2['bg']="#4B0082"
    #top2.attributes('-fullscreen', True)




    top2.overrideredirect(1)



    w = top2.winfo_reqwidth()
    h = top2.winfo_reqheight()
    ws = top2.winfo_screenwidth()
    hs = top2.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top2.geometry('%dx%d+%d+%d' % (x,w+350,y+100,h)) ## this part allows you to only change the location






    img2=Image.open ("youwin.jpg")
    image2 = img2.resize((450, 350), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(image2)


    img3=Image.open ("youlose.jpg")
    image3 = img3.resize((450, 350), Image.ANTIALIAS)
    my_img3 = ImageTk.PhotoImage(image3)


    img4=Image.open ("noone.jpg")
    image4 = img4.resize((450, 350), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(image4)

    top2.columnconfigure([0], weight=1, minsize=75)
    top2.rowconfigure([0], weight=1, minsize=50)



    if(lbl_won['text']=='You wins'):
        frame=tk.Label(top2,image=my_img2)
        frame.grid(row=0,column=0)
        top2['bg']="#4B0082"

        top2.after(1000, lambda: top2.destroy()) # Destroy the widget after 30 seconds

    elif(lbl_won['text']=='Computer win'):
        frame=tk.Label(top2,image=my_img3)
        frame.grid(row=0,column=0)
        top2['bg']='#8B0000'

        top2.after(1000, lambda: top2.destroy()) # Destroy the widget after 30 seconds

    else:
        frame=tk.Label(top2,image=my_img4)
        frame.grid(row=0,column=0)
        top2['bg']='#FF4500'


        top2.after(1000, lambda: top2.destroy()) # Destroy the widget after 30 seconds






    top2.mainloop()



def btn_exit1():
    exit()
def on_click(event):

    event.widget.delete(0, tk.END)



def no_name():
    entry_na=entry_name.get()
    if(entry_na=="Please Type Your Name To Start The Game " or entry_na==''):
        messagebox.showinfo(top, "Please enter name to continue")
    else:
        top1=tk.Toplevel()
        top1.title("Home")
        #top1.geometry("600x600+320+320")
        top1.attributes('-fullscreen', True)
        top1['bg'] ='#9ACD32'
        top1.columnconfigure([0,1,2,3,4,5,6,7,8,9,10], weight=1, minsize=75)
        top1.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1, minsize=50)









        def entry_nam():

            entry_na=entry_name.get()
            lbl=tk.Label(master=top1,font=("Calibri 20"),text='',fg="#8B008B",bg="#ff8000")
            lbl.grid(row=0,column=4)
            lbl['text']="Welcome {} ".format(entry_na)
            print(entry_na)
        entry_nam()




        # Code to add widgets will go here...
        def result_values():
            lbl_score_com['fg']='#FF4500'
            lbl_score_com['bg']='#9ACD32'
            lbl_score_you['fg']='#FF4500'
            lbl_score_you['bg']='#9ACD32'
            lbl_decrese['fg']='#FF4500'
            lbl_user = lbl_value_r["text"]
            lbl_computer = lbl_random_r["text"]
            lbl_dec=int(lbl_decrese["text"])

            if(lbl_user=="Rock" and lbl_computer=="Paper"):

                lbl_score_com["text"]=increase_com()
                lbl_won['text']='Computer win'
                win(lbl_won)
            elif(lbl_user=="Rock" and lbl_computer=="Scissor"):
                lbl_score_you["text"]=increase_you()
                lbl_won['text']='You win'
                win(lbl_won)
            elif(lbl_user=="Paper" and lbl_computer=="Rock"):
                lbl_score_you["text"]=increase_you()
                lbl_won['text']='You win'
                win(lbl_won)
            elif(lbl_user=="Paper" and lbl_computer=="Scissor"):
                lbl_score_com["text"]=increase_com()
                lbl_won['text']='Computer win'
                win(lbl_won)
            elif(lbl_user=="Scissor" and lbl_computer=="Rock"):
                lbl_score_com["text"]=increase_com()
                lbl_won['text']='Computer win'
                win(lbl_won)
            elif(lbl_user=="Scissor" and lbl_computer=="Paper"):
                lbl_score_you["text"]=increase_you()
                lbl_won['text']='You win'
                win(lbl_won)

            else:

                #messagebox.showinfo("top","You are in tie")
                lbl_won['text']='No One Wins'
                win(lbl_won)

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



            if(value>=9):

                lbl_won['text']='winner is {}'.format(winner())



                if(lbl_won['text']=='winner is You' or lbl_won['text']=='winner is Computer'):
                    messagebox.showinfo(top1,"Winner is {}".format(winner()))






                    #messagebox.showinfo(top1,"winner is {}".format(winner()))
                else:

                    messagebox.showinfo(top1,"No one win {}".format(winner()))



                msg=messagebox.askquestion('Do you want to paly again')
                if(msg=='yes'):
                    no_name()
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

                return "Both, Are In Tie"
            else:
                return "Computer"


        def btn_exit():
            exit()








        myFont = font.Font(family='Helvetica', size=18, weight='bold')
        myFont1 = font.Font(family='Helvetica', size=25, weight='bold')
        myFont2 = font.Font(family='Helvetica', size=15, weight='bold')


        lbl_won=tk.Label(master=top1,text='',bg="#9ACD32",fg="#FF4500")
        lbl_won.grid(row=1,column=4)
        lbl_won['font']=myFont

        lb_chance=tk.Label(master=top1,text="Round",bg="#ff8000",fg="#8B008B")
        lb_chance.grid(row=2,column=4,padx=10)
        lb_chance['font']=myFont
        lbl_decrese=tk.Label(master=top1,text="0",bg='#9ACD32',fg="#9ACD32")
        lbl_decrese.grid(row=2,column=5)
        lbl_decrese['font']=myFont1


        img2=Image.open ("paper.jpg")
        image2 = img2.resize((150, 150), Image.ANTIALIAS)
        my_img2 = ImageTk.PhotoImage(image2)

        img3=Image.open ("scissor.jpg")
        image3 = img3.resize((150, 150), Image.ANTIALIAS)
        my_img3 = ImageTk.PhotoImage(image3)

        img1=Image.open ("rock.jpg")
        image1 = img1.resize((150, 150), Image.ANTIALIAS)
        my_img1 = ImageTk.PhotoImage(image1)





        button_rock = tk.Button(master=top1,text="Rock", image=my_img1,command=handlePress_rock)
        button_paper = tk.Button(master=top1,text="Paper", image=my_img2,command=handlePress_paper)

        button_scissor = tk.Button(master=top1,text="Scissor",image=my_img3,command=handlePress_scissor)


        button_rock.grid(row=3, column=3)
        button_rock.bind("<Button-1>", decrese)

        button_paper.grid(row=3, column=4)
        button_paper.bind("<Button-1>", decrese)

        button_scissor.grid(row=3, column=5)
        button_scissor.bind("<Button-1>", decrese)



        lbl_value=tk.Label(top1,text="You Choose  ",bg="#ff8000",fg="#8B008B")
        lbl_value.grid(row=5,column=2)
        lbl_value['font']=myFont
        lbl_value_r=tk.Label(top1,text="",bg="#9ACD32",fg="#FF4500")
        lbl_value_r.grid(row=5,column=4)
        lbl_value_r['font']=myFont


        lbl_random=tk.Label(top1,text="Computer Choose",bg="#ff8000",fg="#8B008B")
        lbl_random.grid(row=7,column=2)
        lbl_random['font']=myFont
        lbl_random_r=tk.Label(top1,text="",bg="#9ACD32",fg="#FF4500")
        lbl_random_r.grid(row=7,column=4)



        lbl_score_you=tk.Label(top1,text="0",bg='#9ACD32',fg='#9ACD32')
        lbl_score_you.grid(row=5,column=6)
        lbl_score_you['font']=myFont
        lbl_score_com=tk.Label(top1,text="0",bg='#9ACD32',fg='#9ACD32')
        lbl_score_com.grid(row=7,column=6)
        lbl_score_com['font']=myFont



        btn_exit=tk.Button(top1,text="EXIT GAME",command=btn_exit,bg="#FF0000",padx=10,pady=10)
        btn_exit.grid(row=0,column=0)



        lbl_tie=tk.Label(text='')
        lbl_tie.grid(row=8,column=5)
        lbl_tie['font']=myFont






        top1.mainloop()









top = tk.Tk()
top['bg'] ='#FFFACD'
myFont = font.Font(family='Helvetica', size=15, weight='bold')
myFont1 = font.Font(family='Helvetica', size=25, weight='bold')
myFont2 = font.Font(family='Helvetica', size=15, weight='bold')




top.title("Welcome To Rock Paper Scissor")
#top.geometry("600x600+320+320")
top.attributes('-fullscreen', True)
for i in range(5):
    top.columnconfigure(i, weight=1, minsize=75)
    top.rowconfigure(i, weight=1, minsize=50)

    for j in range(0,5):
        lbl_welcome=tk.Label(master=top,text="Welcome To Rock Paper Scissor Game",fg="#FF4500",bg="#FFFACD")
        #lbl_welcome.grid(row=i,column=j)
        lbl_welcome['font']=myFont1


        lbl_welcome.grid(row=1, column=2, padx=5, pady=5)


        rps=Image.open ("rps1.jpg")
        image2 = rps.resize((450, 250), Image.ANTIALIAS)
        my_img2 = ImageTk.PhotoImage(image2)

        frame=tk.Button(master=top,image=my_img2)
        frame.grid(row=2,column=2)

        #lbl_name = tk.Label(top,text="Enter Your Name")
        #lbl_name.grid(row=4,column=2)
        #lbl_name['font']=myFont
        #v = StringVar(root, value='default text')
        entry_name =tk.Entry(master=top,font=("Calibri 15"),bg="#4682B4",bd=5,fg='white')
        #entry_name.focus()

        entry_name.insert(0,"Please Type Your Name To Start The Game ")
        entry_name.bind("<Button-1>", on_click)
        entry_name.grid(row=4,column=2,padx=50,
               pady=10,
               ipady=20,
               ipadx=100)

        #label_btn = tk.Label(master=entry_name, text="Your Name Goes Here",padx=100,pady=20,bg="#B0C4DE",fg="#FF4500")
        #label_btn.bind("<1>", selfremove)
        #label_btn.pack(padx=10, pady=10)
        #label_btn['font']=myFont2

        arrow1=Image.open ("arrow.png")
        image_arrow = arrow1.resize((80, 80), Image.ANTIALIAS)
        arrow = ImageTk.PhotoImage(image_arrow)

        btn_name=tk.Button(master=top,image=arrow,bg="#BC8F8F",command=no_name)
        btn_name.grid(row=4,column=3)


        btn_exit=tk.Button(top,text="EXIT GAME",command=btn_exit1,bg="#FF0000",padx=10,pady=10)
        btn_exit.grid(row=0,column=0)

top.mainloop()






















































#top.rowconfigure([1,2,3,4,5,6,7,8],minsize=50)
#top.columnconfigure([2, 4, 6],minsize=50)
'''lbl_welcome=tk.Label(text="Welcome To Rock Paper Scissor Game")
lbl_welcome.grid(row=1,column=4)
lbl_welcome['font']=myFont

lbl_name = tk.Label(top,text="Enter Your Name")
lbl_name.grid(row=2,column=3)
lbl_name['font']=myFont
entry_name =tk.Entry(top)
entry_name.grid(row=2,column=6)


btn_reg = tk.Button(top,text="Start Play")
btn_reg.grid(row=3,column=5)
btn_reg['font']=myFont'''
