from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()

def submit():
    print("THANK YOU FOR YOUR SUBMISSION")
    tmsg.showinfo("SUBMIT","Your submission has been noted")

root.geometry("800x600")
root.configure(bg="grey")
root.title("IMAGER")

l0=Label(root,text="WELCOME TO IMAGER! :)",font="lucida 20 bold")
l0.pack()
l1=Label(root,text="where strange is usual",font="lucida 15 bold italic",fg="red")
l1.pack()
#f0=Frame(root)
#f0.pack(side=LEFT)
l2=Label(root,text="NAME:",font="lucida 15 bold",relief=SUNKEN)
l2.place(relx=0.0,rely=0.2)
l3=Label(root,text="USERNAME:",font="lucida 15 bold",relief=SUNKEN)
l3.place(relx=0.0,rely=0.25)

namevalue=StringVar()
uservalue=StringVar()
nameentry=Entry(root,textvariable=namevalue)
userentry=Entry(root,textvariable=uservalue)
nameentry.place(relx=0.1,rely=0.2,width=150,height=25)
userentry.place(relx=0.165,rely=0.25,width=150,height=27.5)

yourmenubar=Menu(root)
m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="New Project")
m1.add_command(label="Open Project")
yourmenubar.add_cascade(label=".\n.\n.",menu=m1)
root.config(menu=yourmenubar)

Button(text="SUBMIT",relief=GROOVE,font="Algerian 15 bold",command=submit).place(relx=0.15,rely=0.32)



root.mainloop()