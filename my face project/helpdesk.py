from ctypes import resize
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recogniser import Face
from attendance import Attendance


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")


        img=Image.open(r"C:\my face project\images\pp.jpg")
        img=img.resize((1500,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        dep_label=Label(f_lbl,text="Email:mrunmayipathak8@gmail.com",font=("times new roman",12,"bold"),fg="blue",bg="white")
        dep_label.place(x=450,y=355)






































































if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
