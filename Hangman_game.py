from tkinter import *
from tkinter import messagebox
root=Tk() 
root.title("Hangman Game")
root.geometry("900x600")
root.configure(background="light pink")
icon=PhotoImage(file="download.png")
root.tk.call("wm",'iconphoto',root._w,icon)

#frame=Frame(root)
#frame.pack()

#bottomframe=Frame(root)
#bottomframe.pack(side=top)


chances=4;
answer_arr=[]
def clicked(alphabet):
    global chances
   
chances=4;
#answer_arr=[]
def clicked(alphabet):
    global chances
    answer="LIZARD";
    if alphabet in answer:
        if alphabet=='L':
            btn1['text']=alphabet;
        elif alphabet=='I':
            btn2['text']=alphabet;
        elif alphabet=='Z':
            btn3['text']=alphabet;
        elif alphabet=='A':
            btn4['text']=alphabet;
        elif alphabet=='R':
            btn5['text']=alphabet;
        elif alphabet=='D':
            btn6['text']=alphabet;

        
        
    
    else:
        txt="chances remaining"+str(chances);
        chances=chances-1;
        if chances<0:
            messagebox.showinfo("hanged")
            root.destroy()
    if btn1['text']=='L' and btn2['text']=='I'  and btn3['text']=='Z' and btn4['text']=='A' and btn5['text']=='R' and btn6['text']=='D':
         msg=messagebox.showinfo("Hangman Game","congratulation")
    
         root.destroy()
    print(chances)

















    

label_1=Label(text="!!!!!!!!!!!!!!Welcome To Hangman Game!!!!!!!!!!",font=("bold",15),fg="white",bg="black")
label_1.place(relx=0.7,rely=0.10,anchor=E)

   
#Botton for taking input

btn1=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn1.place(relx=0.5,rely=0.25,anchor=E)
btn2=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn2.place(relx=0.55,rely=0.25,anchor=E)
btn3=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn3.place(relx=0.60,rely=0.25,anchor=E)
btn4=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn4.place(relx=0.65,rely=0.25,anchor=E)
btn5=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn5.place(relx=0.70,rely=0.25,ancho=E)
btn6=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn6.place(relx=0.75,rely=0.25,anchor=E)
btn7=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn7.place(relx=0.80,rely=0.25,anchor=E)
btn8=Button(text=" ",bg="white",fg="black",width=3,height=1)
btn8.place(relx=0.85,rely=0.25,anchor=E)
btn9=Button(text="A",bg="blue",fg="black",width=3,height=1,activebackground='silver',command=lambda: clicked('A'))
btn9.place(relx=0.2,rely=0.6,anchor=W)
btn10=Button(text="B",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('B'))
btn10.place(relx=0.27,rely=0.6,anchor=W)
btn11=Button(text="C",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('C'))
btn11.place(relx=0.34,rely=0.6,anchor=W)
btn12=Button(text="D",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('D'))
btn12.place(relx=0.41,rely=0.6,anchor=W)
btn13=Button(text="E",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('E'))
btn13.place(relx=0.48,rely=0.6,anchor=W)
btn14=Button(text="F",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('F'))
btn14.place(relx=0.55,rely=0.6,anchor=W)
btn15=Button(text="G",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('G'))
btn15.place(relx=0.62,rely=0.6,anchor=W)
btn16=Button(text="H",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('H'))
btn16.place(relx=0.2,rely=0.68,anchor=W)
btn17=Button(text="I",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('I'))
btn17.place(relx=0.27,rely=0.68,anchor=W)
btn18=Button(text="J",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('J'))
btn18.place(relx=0.34,rely=0.68,anchor=W)
btn19=Button(text="K",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('K'))
btn19.place(relx=0.41,rely=0.68,anchor=W)
btn20=Button(text="L",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('L'))
btn20.place(relx=0.48,rely=0.68,anchor=W)
btn21=Button(text="M",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('M'))
btn21.place(relx=0.55,rely=0.68,anchor=W)
btn22=Button(text="N",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('N'))
btn22.place(relx=0.62,rely=0.68,anchor=W)
btn23=Button(text="O",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('O'))
btn23.place(relx=0.2,rely=0.76,anchor=W)
btn24=Button(text="P",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('P'))
btn24.place(relx=0.27,rely=0.76,anchor=W)
btn25=Button(text="Q",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('Q'))
btn25.place(relx=0.34,rely=0.76,anchor=W)
btn26=Button(text="R",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('R'))
btn26.place(relx=0.41,rely=0.76,anchor=W)
btn27=Button(text="S",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('S'))
btn27.place(relx=0.48,rely=0.76,anchor=W)
btn28=Button(text="T",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('T'))
btn28.place(relx=0.55,rely=0.76,anchor=W)
btn29=Button(text="U",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('U'))
btn29.place(relx=0.62,rely=0.76,anchor=W)
btn30=Button(text="V",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('V'))
btn30.place(relx=0.27,rely=0.84,anchor=W)
btn31=Button(text="W",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('W'))
btn31.place(relx=0.34,rely=0.84,anchor=W)
btn32=Button(text="X",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('X'))
btn32.place(relx=0.41,rely=0.84,anchor=W)
btn33=Button(text="Y",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('Y'))
btn33.place(relx=0.48,rely=0.84,anchor=W)
btn34=Button(text="Z",bg="blue",fg="black",width=3,height=1,command=lambda: clicked('Z'))
btn34.place(relx=0.55,rely=0.84,anchor=W)


#button for new image
btn35=Button(text="Image 5",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn35.place(relx=0.9,rely=0.35,anchor=E)

btn36=Button(text="Image 4",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn36.place(relx=0.8,rely=0.35,anchor=E)

btn37=Button(text="Image 3",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn37.place(relx=0.7,rely=0.35,anchor=E)

btn38=Button(text="Image 2",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn38.place(relx=0.6,rely=0.35,anchor=E)

def image_1():
    canvas=Canvas(width=300,height=200)
    canvas.place(x=0.5,y=0.5)
    gif1=PhotoImage(file='panda.gif')
    canvas.create_image(20,30,image=gif1,anchor=NW)
    canvas.place(x=0.5,y=0.5)

btn39=Button(text="Image 1",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn39.place(relx=0.5,rely=0.35,anchor=E)

btn40=Button(text="Image 10",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn40.place(relx=0.9,rely=0.45,anchor=E)

btn40=Button(text="Image 9",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn40.place(relx=0.8,rely=0.45,anchor=E)

btn40=Button(text="Image 8",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn40.place(relx=0.7,rely=0.45,anchor=E)

btn40=Button(text="Image 7",bg="deep skyblue",fg="black",width=10,height=1,relief=RAISED)
btn40.place(relx=0.6,rely=0.45,anchor=E)
def image():
    canvas=Canvas(width=300,height=200)
    canvas.pack(expand=YES,fill=BOTH)
    gif1=PhotoImage(file='download.png')
    canvas.create_image(50,50,image=gif1,anchor=NW)
    canvas.place(relx=0.0,rely=0.3,anchor=W)

btn40=Button(text="Image 6",bg="deep skyblue",fg="black",width=10,height=1,relief='raised' , command=image)
btn40.place(relx=0.5,rely=0.45,anchor=E)



canvas=Canvas(width=300,height=200,bg='deep skyblue')
canvas.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file='startt.gif')
canvas.create_image(50,50,image=gif1,anchor=NW)
canvas.place(relx=0.0,rely=0.3,anchor=W)




#image






root.mainloop()
