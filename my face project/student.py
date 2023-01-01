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



class Student:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
#variables_-----------------------------------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_std_division=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()



#first image
        img=Image.open(r"C:\Users\Manu\my face project\images\s4.Jfif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second image
        img1=Image.open(r"C:\Users\Manu\my face project\images\s2.JFIF")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

#third image
        img2=Image.open(r"C:\Users\Manu\my face project\images\s3.JPG")
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


        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

#left side frame
         
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Stuent Details",font=(" times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"C:\Users\Manu\my face project\images\s5.JPG")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)



#current course

        currentcourse_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=(" times new roman",12,"bold"))
        currentcourse_frame.place(x=5,y=135,width=720,height=150)
#department
        dep_label=Label(currentcourse_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0, padx=10)

        dep_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","computer","civil","Electronic","mechanic")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


#Course
        course_label=Label(currentcourse_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2, padx=10,sticky=W)

        course_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","BE","TE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#year
        year_label=Label(currentcourse_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0, padx=10,sticky=W)

        year_label=ttk.Combobox(currentcourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_label["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_label.current(0)
        year_label.grid(row=1,column=1,padx=2,pady=10,sticky=W)


#semester
        semester_label=Label(currentcourse_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2, padx=10,sticky=W)

        semester_label=ttk.Combobox(currentcourse_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_label["values"]=("Select Semester","Semester-1","Semester-2")
        semester_label.current(0)
        semester_label.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#student information
        classcourse_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=(" times new roman",12,"bold"))
        classcourse_frame.place(x=5,y=250,width=720,height=300)

        stuid_label=Label(classcourse_frame,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        stuid_label.grid(row=0,column=0, padx=10, pady=5,sticky=W)

        studentid_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1, padx=10,pady=5,sticky=W)

#student name
        stuname_label=Label(classcourse_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        stuname_label.grid(row=0,column=2, padx=10,pady=5,sticky=W)

        stuname_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        stuname_label_entry.grid(row=0,column=3, padx=10,pady=5,sticky=W)

#division
        stundiv_label=Label(classcourse_frame,text="Division",font=("times new roman",12,"bold"),bg="white")
        stundiv_label.grid(row=1,column=0, padx=10,pady=5,sticky=W)

       # stundiv_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_std_division,font=("times new roman",12,"bold"))
        #stundiv_label_entry.grid(row=1,column=1, padx=10,pady=5,sticky=W)gender_combo=ttk.Combobox(classcourse_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        div_combo=ttk.Combobox(classcourse_frame,textvariable=self.var_std_division,font=("times new roman",12,"bold"),state="readonly",width=15)
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


#Rollno
        sturollno_label=Label(classcourse_frame,text="Roll NO",font=("times new roman",12,"bold"),bg="white")
        sturollno_label.grid(row=1,column=2, padx=10,pady=5,sticky=W)

        sturollno_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_rollno,font=("times new roman",12,"bold"))
        sturollno_label_entry.grid(row=1,column=3, padx=10,pady=5,sticky=W)

#gender
        stugen_label=Label(classcourse_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        stugen_label.grid(row=2,column=0, padx=10,pady=5,sticky=W)

       
        gender_combo=ttk.Combobox(classcourse_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=15)
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

#DoB

        dob_label=Label(classcourse_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2, padx=10,pady=5,sticky=W)

        dob_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_label_entry.grid(row=2,column=3, padx=10,pady=5,sticky=W)

#email
        email_label=Label(classcourse_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0, padx=10,pady=5,sticky=W)

        email_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_label_entry.grid(row=3,column=1, padx=10,pady=5,sticky=W)



#phonenumber        
        phone_label=Label(classcourse_frame,text="Phonenumber",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2, padx=10,pady=5,sticky=W)

        phone_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_label_entry.grid(row=3,column=3, padx=10,pady=5,sticky=W)

#Address

        add_label=Label(classcourse_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0, padx=10,pady=5,sticky=W)

        add_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        add_label_entry.grid(row=4,column=1, padx=10,pady=5,sticky=W)


#Teachername

        Teacher_label=Label(classcourse_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2, padx=10,pady=5,sticky=W)

        Teacher_label_entry=ttk.Entry(classcourse_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        Teacher_label_entry.grid(row=4,column=3, padx=10,pady=5,sticky=W)


#radiobutton
        
        Radiobutton1=ttk.Radiobutton(classcourse_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        Radiobutton1.grid(row=6,column=0)
        
        Radiobutton2=ttk.Radiobutton(classcourse_frame,variable=self.var_radio1,text="No photo sample",value="No")
        Radiobutton2.grid(row=6,column=1)




        butn_frame=Frame(classcourse_frame,bd=2,bg="white",relief=RIDGE)
        butn_frame.place(x=0,y=215,width=715,height=70)

#save
        save_button=Button(butn_frame,text="save",command=self.add_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)


        update_button=Button(butn_frame,text="Update",command=self.update_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)


        delete_button=Button(butn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(butn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)



        tbutn_frame=Frame(classcourse_frame,bd=2,bg="white",relief=RIDGE)
        tbutn_frame.place(x=0,y=245,width=715,height=70)






        takephoto_button=Button(tbutn_frame,text="Take a photo",command=self.generate_dataset,width=45,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takephoto_button.grid(row=0,column=0)

        updatephoto_button=Button(tbutn_frame,text="Update photo",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatephoto_button.grid(row=0,column=1)

#right side frame
         
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Stuent Details",font=(" times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=730,height=580)


    

        img_right=Image.open(r"C:\Users\Manu\my face project\images\s5.JPG")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

#serCH SYSTEM++++++++=======_-----------------------------------------------------------------

        searchsystem_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=(" times new roman",12,"bold"))
        searchsystem_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(searchsystem_frame,text="Search by",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0, padx=10,pady=5,sticky=W)

        se_combo=ttk.Combobox(searchsystem_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        se_combo["values"]=("Select By","Name","ID","Rollno")
        se_combo.current(0)
        se_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        
        search_entry=ttk.Entry(searchsystem_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2, padx=10,pady=5,sticky=W)

        search1_button=Button(searchsystem_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search1_button.grid(row=0,column=3,padx=4)

        

        showall_button=Button(searchsystem_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_button.grid(row=0,column=4,padx=4)

#________________________table frame___________________________
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.Student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollno","gender","dob","phone","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)



        self.Student_table.heading("dep",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="semester")
        self.Student_table.heading("id",text="StudentID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("div",text="Division")
        self.Student_table.heading("rollno",text="Rollno")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("phone",text="Phone")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("address",text="Address")
        self.Student_table.heading("teacher",text="Teacher")
        self.Student_table.heading("photo",text="PhotoSampleStatus")
        self.Student_table["show"]="headings"

        self.Student_table.column("dep",width=100)
        self.Student_table.column("course",width=100)
        self.Student_table.column("year",width=100)
        self.Student_table.column("sem",width=100)
        self.Student_table.column("id",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("div",width=100)
        self.Student_table.column("rollno",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("phone",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("address",width=100)
        self.Student_table.column("teacher",width=100)
        self.Student_table.column("photo",width=150)
       
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_coursor)
        self.fetch_data()

# add functions_______________________________________________________________________________________________________________________________
   
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:
                        
                 conn=mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(    self.var_dep.get(),
                                                                                                                   self.var_course.get(),
                                                                                                                   self.var_year.get(),
                                                                                                                   self.var_semester.get(),
                                                                                                                   self.var_std_id.get(),
                                                                                                                   self.var_std_name.get(),
                                                                                                                   self.var_std_division.get(),
                                                                                                                    self.var_rollno.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                   
                                                                                                                    self.var_phone.get(),
                                                                                                                     self.var_email.get(),
                                                                                                                     self.var_address.get(),
                                                                                                                     self.var_teacher.get(),
                                                                                                                     self.var_radio1.get()
                                                                                                                     


                                                                                                                   
                                                                                                        
                                                                                                                   
                                                                                                                   
                                                                                                                    
                                                                                                                    
                                                                                                        
                                                                                                                
                                                                                                                ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Student Information stored succesfully") 
                except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



       ############Fetch data###############
              
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student ")
        data=my_cursor.fetchall()

        if len(data)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for i in data:
                        self.Student_table.insert("",END,values=i)
                conn.commit()
        conn.close()


        #####get coursor#######
    def get_coursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0]), 
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_std_division.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_email.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#update function

    def update_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
         my_cursor=conn.cursor()
         my_cursor.execute("update student set name=%s,course=%s ,gender=%s , rollno=%s , Teacher=%s ,Dep=%s, semester=%s,year=%s where studentid=%s",( 
                    self.var_std_name.get(),
                    self.var_course.get(),
                    self.var_gender.get(),
                    self.var_rollno.get(),
                    self.var_teacher.get(),
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_year.get(),
                    self.var_std_id.get()
                    
                    ))
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("Updated","Successfully updated the student",parent=self.root)
        
#delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student id must required",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("StudentDeleterequest","Do you want to delete this student",parent=self.root)
                        if delete>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
                           my_cursor=conn.cursor()
                           sql="delete from student where studentid=%s"
                           val=(self.var_std_id.get(),)
                           my_cursor.execute(sql,val)
                        else:
                                if not delete:
                                        return

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Successfully deleted the student",parent=self.root)
                except Exception as es:
                         messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)
     
 #Reset button       
    def reset_data(self):  
        self.var_dep.set("Select Department")      
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_std_division.set("")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("") 
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")          
                        

#Take photo samples

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myreslut = my_cursor.fetchall();
                id=0
                for x in myreslut:
                    id+=1

                my_cursor.execute("update student set name=%s,course=%s ,gender=%s , rollno=%s , Teacher=%s ,photo=%s ,DOB=%s,Dep=%s,year=%s where studentid=%s",( 
                    self.var_std_name.get(),
                    self.var_course.get(),
                    self.var_gender.get(),
                    self.var_rollno.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_dob.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_std_id.get()
                    
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("C:\\my face project\\haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==10:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 













     





     















































































































if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
