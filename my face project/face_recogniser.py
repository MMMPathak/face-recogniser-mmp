from sys import path
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
import dlib
import face_recognition
from time import strftime
from datetime import datetime
from kivy.lang import Builder






class Face:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")



        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

   
         #first image
        img=Image.open(r"C:\my face project\images\x.jpg")
        img=img.resize((650,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=50,width=650,height=700)



        #second image
        bg1=Image.open(r"C:\my face project\images\img2.jpeg")
        bg1=bg1.resize((950,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(bg1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=55,width=950,height=700)


#button
        but1=Button(f_lbl,text="Face Recognisition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
        but1.place(x=360,y=620,width=200,height=40)


# face recogniser************************************************************
    
    def mark_attendance(self,n,r,i):
        
        with open("attendace1.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name=[]
            for data in myDatalist:
                ent = data.split(',')
                name.append(ent[0])
            if name not in name:
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n}, {r}, {i}, {dtString}, {d1}, Present")
                
            


                
        
            #if((n not in name_list)) and ((r not in name_list)) and ((i not in name_list)):
            #    now=datetime.now()
            #    d1=now.strftime("%d/%m/%Y")
                #dtString=now.strftime("%H:%M:%S")
            #    f.writelines(f"\n{n}, {r}, {i}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
                cursor = conn.cursor()
                print("Student id",id)
                cursor.execute("select studentid from facerecognization.student where studentid="+str(id))
                n=cursor.fetchone()
                print("Cursor fetch one result",n)
                n="+".join(n)

                cursor.execute("select name from facerecognization.student where studentid="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select rollno from facerecognization.student where studentid="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{n}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(n,r,i)
                    return [x,y,w,y]
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
             break
                
        videoCap.release()
        cv2.destroyAllWindows()









if __name__ =="__main__":
    root=Tk()
    obj=Face(root)
    root.mainloop()
