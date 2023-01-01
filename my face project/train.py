from ctypes import resize
from tkinter import*
from tkinter import ttk
import tkinter
from tokenize import String
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os




class Train:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")




        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#first image
        img=Image.open(r"C:\my face project\images\3.JFIF")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=100,width=600,height=130)

#second image
        img1=Image.open(r"C:\my face project\images\im1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=100,width=600,height=130)

#third image
        img2=Image.open(r"C:\my face project\images\4.jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=100,width=600,height=130)

       
        img3=Image.open(r"C:\my face project\images\b.png")
        img3=img3.resize((1530,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=300,width=1530,height=600)




        
        but=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        but.place(x=0,y=380,width=1530,height=40)



    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
                img=Image.open(image).convert('L')#gray scale image
                imagenp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imagenp)
                ids.append(id)
                cv2.imshow("TRAINING",imagenp)
                cv2.waitKey(1)==13
        ids=np.array(ids)



        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed !")






































if __name__ =="__main__":
    root=Tk()
    obj=Train (root)
    root.mainloop()
