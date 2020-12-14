import tkinter.messagebox
from tkinter import *

root=Tk()
root.title('X-O Game')
root.geometry('1300x750')
root.configure(background='cadet blue')

taps=Frame(root,bg='cadet blue',pady=2,width=1300,height=100,relief=RIDGE)
taps.grid(row=0,column=0)

labltitle=Label(taps,font=('arial',50,'bold'),text='   X-O Game',bd=21,bg='cadet blue',fg='cornsilk',justify=CENTER)
labltitle.grid(row=0,column=0)

mainframe=Frame(root,bg='powder blue',bd=10,width=1300,height=600,relief=RIDGE)
mainframe.grid(row=1,column=0)

leftframe=Frame(mainframe,bd=10,bg='cadet blue',pady=2,padx=10,width=750,height=500,relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe=Frame(mainframe,bd=10,bg='cadet blue',pady=2,padx=10,width=560,height=500,relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1=Frame(rightframe,bd=10,bg='cadet blue',pady=2,padx=10,width=560,height=200,relief=RIDGE)
rightframe1.grid(row=0,column=0)

rightframe2=Frame(rightframe,bd=10,bg='cadet blue',pady=2,padx=10,width=560,height=200,relief=RIDGE)
rightframe2.grid(row=1,column=0)

playerx=IntVar()
playero=IntVar()
playerx.set(0)
playero.set(0)
#===========================creat the fonctions=========================================
buttons=StringVar()
click=True
def checker(buttons):
    global  click
    if buttons['text']==" " and click==True:
        buttons['text']='X'
        click=False
    elif buttons['text']==" " and click==False:
        buttons['text']='O'
        click=True
    scoregame()

def rest():
    button1['text']=' '
    button2['text']=' '
    button3['text']=' '
    button4['text']=' '
    button5['text']=' '
    button6['text']=' '
    button7['text']=' '
    button8['text']=' '
    button9['text']=' '
    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')
def Newgame():
    rest()
    playerx.set(0)
    playero.set(0)

def scoregame():

    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')
    if button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
        button4.configure(background='powder blue')
        button5.configure(background='powder blue')
        button6.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')
    if button7['text']=='X' and button8['text']=='X' and button9['text']=='X':
        button7.configure(background='powder blue')
        button8.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')

    if button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
        button1.configure(background='powder blue')
        button4.configure(background='powder blue')
        button7.configure(background='powder blue')
        n = int(playerx.get())
        score =n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'Congradulation you won the game !')
    if button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
        button2.configure(background='powder blue')
        button5.configure(background='powder blue')
        button8.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')
    if button3['text']=='X' and button6['text']=='X' and button9['text']=='X':
        button3.configure(background='powder blue')
        button6.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')

    if button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
        button1.configure(background='powder blue')
        button5.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')
    if button3['text']=='X' and button5['text']=='X' and button7['text']=='X':
        button3.configure(background='powder blue')
        button5.configure(background='powder blue')
        button7.configure(background='powder blue')
        n=int(playerx.get())
        score=n+1
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','Congradulation you won the game !')
#==============pour O==================
    if button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
        button1.configure(background='green')
        button2.configure(background='green')
        button3.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')
    if button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':
        button4.configure(background='green')
        button5.configure(background='green')
        button6.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')
    if button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O':
        button7.configure(background='green')
        button8.configure(background='green')
        button9.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')

    if button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':
        button1.configure(background='green')
        button4.configure(background='green')
        button7.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')
    if button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':
        button5.configure(background='green')
        button5.configure(background='green')
        button8.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')
    if button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':
        button3.configure(background='green')
        button6.configure(background='green')
        button9.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')

    if button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':
        button1.configure(background='green')
        button5.configure(background='green')
        button9.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')
    if button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
        button3.configure(background='green')
        button5.configure(background='green')
        button7.configure(background='green')
        n = int(playero.get())
        score = n + 1
        playero.set(score)
        tkinter.messagebox.showinfo('Winner O', 'Congradulation you won the game !')

#=========================creat label=================

lablplayerx=Label(rightframe1,font=('arial',30,'bold'),text='Player X :',padx=2,pady=2,bg='cadet blue')
lablplayerx.grid(row=0,column=0,sticky=W)
lablplayero=Label(rightframe1,font=('arial',30,'bold'),text='Player O :',padx=2,pady=2,bg='cadet blue')
lablplayero.grid(row=1,column=0,sticky=W)

txtplayerx=Entry(rightframe1,font=('arial',30,'bold'),fg='black',bg='gainsboro',
                 textvariable=playerx,width=12,justify=CENTER).grid(row=0,column=1)
txtplayero=Entry(rightframe1,font=('arial',30,'bold'),fg='black',bg='gainsboro',
                 textvariable=playero,width=12,justify=CENTER).grid(row=1,column=1)


buttonRest=Button(rightframe2,text="Rest",font=('Time',26,'bold'),height=1,width=12,bg='gainsboro',command=rest)
buttonRest.grid(row=2,column=0,padx=6,pady=11)
buttonNew=Button(rightframe2,text="New Game",font=('Time',26,'bold'),height=1,width=12,bg='gainsboro',command=Newgame)
buttonNew.grid(row=3,column=0,padx=11,pady=6)

#=======================creat buttons==============
button1=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)
button7=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9=Button(leftframe,text=" ",font=('Time',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)  # sticky for direction

root.mainloop()