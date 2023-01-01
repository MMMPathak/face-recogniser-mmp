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


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")


        img=Image.open(r"C:\my face project\images\sss.jpg")
        img=img.resize((1500,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"C:\my face project\images\tt.JPEG")
        img_top1=img.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)



        dep_label=Label(main_frame,text="Hello my name is Mrunmayi Pathak",font=("times new roman",12,"bold"),bg="white")
        dep_label.place(x=0,y=5)


        dep_label=Label(main_frame,text="I am full stack developer",font=("times new roman",12,"bold"),bg="white")
        dep_label.place(x=0,y=40)


        img2=Image.open(r"C:\my face project\images\tt.jpeg")
        img2=img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)



        

       

























































































if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
