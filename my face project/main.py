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
from developer import Developer
from helpdesk import Help

class Face_Recognization_system:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
#first image
        img=Image.open(r"C:\Users\Manu\my face project\images\6.Jfif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second image
        img1=Image.open(r"C:\Users\Manu\my face project\images\5.Jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

#third image
        img2=Image.open(r"C:\Users\Manu\my face project\images\4.Jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


#bg image

        img3=Image.open(r"C:\Users\Manu\my face project\images\x.JPG")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#student button
        img4=Image.open(r"C:\Users\Manu\my face project\images\s1.JPG")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,command=self.student_deatils,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1=Button(bg_image,text="Student Details",command=self.student_deatils,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=300,width=200,height=40)

#Dtect face 
        img5=Image.open(r"C:\Users\Manu\my face project\images\f.JPG")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,command=self.face_deatils,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=200)

        b1=Button(bg_image,text="Face Detector", command=self.face_deatils,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=300,width=220,height=40)

#Attendace
        img6=Image.open(r"C:\Users\Manu\my face project\images\a.JPG")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,cursor="hand2",command=self.attendance_deatils)
        b1.place(x=800,y=100,width=220,height=200)

        b1=Button(bg_image,text="Attendance",command=self.attendance_deatils,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=300,width=220,height=40)

#help
        img7=Image.open(r"C:\Users\Manu\my face project\images\h.JPG")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=200)

        b1=Button(bg_image,text="Help Desk",command=self.help_deatils,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=300,width=220,height=40)

#Train
        img8=Image.open(r"C:\Users\Manu\my face project\images\d.JFIF")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,command=self.train_deatils,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=200)

        b1=Button(bg_image,text="Train Data",command=self.train_deatils,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=580,width=220,height=40)

#photoe

        img9=Image.open(r"C:\Users\Manu\my face project\images\p.JFIF")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=200)

        b1=Button(bg_image,text="Pictures",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=580,width=220,height=40)


#dEVELOPER
        
        img10=Image.open(r"C:\Users\Manu\my face project\images\d1.JFIF")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_image,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=200)

        b1=Button(bg_image,text="DEVELOPER",command=self.developer_deatils,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=580,width=220,height=40)


#exit       
        img11=Image.open(r"C:\Users\Manu\my face project\images\E.JPG")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_image,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=200)

        b1=Button(bg_image,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        self.new_window=Toplevel(self.root)
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognisation","are you ure you want to exit",parent=self.root)
        if self.iExit >0:
                self.root.destroy()
        else:
              return 



    
    




















    def train_deatils(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

                           




    def student_deatils(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

                           
    def face_deatils(self):
         self.new_window=Toplevel(self.root)
         self.app=Face(self.new_window)

    def attendance_deatils(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)


    def developer_deatils(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)


    def help_deatils(self):
         self.new_window=Toplevel(self.root)
         self.app=Help(self.new_window)





                           










        



























if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognization_system(root)
    root.mainloop()
