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
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        #variables__________________________________________
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()




#first image
        img=Image.open(r"C:\my face project\images\aa.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second image
        img1=Image.open(r"C:\my face project\images\bb.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#third image
        img2=Image.open(r"C:\Users\Manu\my face project\images\s5.JPG")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
#bg image

        img3=Image.open(r"C:\Users\Manu\my face project\images\x.JPG")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=200,width=1530,height=710)


        title_lbl=Label(bg_image,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

#LEft side frame
         
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Stuent Attendance Details",font=(" times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\Manu\my face project\images\s5.JPG")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=180,width=720,height=300)

#label entry 
        attendanceid_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0, padx=10, pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1, padx=10,pady=5,sticky=W)

        Name_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=0,column=2, padx=4, pady=8,sticky=W)

        attendancename_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=22,font=("times new roman",12,"bold"))
        attendancename_entry.grid(row=0,column=3,pady=8,sticky=W)


        roll_label=Label(left_inside_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0, padx=4, pady=8,sticky=W)

        attendanceroll_entry=ttk.Entry(left_inside_frame,textvariable= self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        attendanceroll_entry.grid(row=1,column=1,pady=8,sticky=W)
        

        time_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0, padx=4, pady=8,sticky=W)

        attendancetime_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        attendancetime_entry.grid(row=2,column=1,pady=8,sticky=W)

        Date_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2, padx=4, pady=8,sticky=W)

        attendancedate_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        attendancedate_entry.grid(row=2,column=3,pady=8,sticky=W)


        #attendance
        attendanceLable=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLable.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_status,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)



        #save

        butn_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        butn_frame.place(x=0,y=215,width=715,height=70)

        import_button=Button(butn_frame,text="Import csv", command=self.importCsv,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_button.grid(row=0,column=0)


        export_button=Button(butn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_button.grid(row=0,column=1)


        update_button=Button(butn_frame,text="Update",command=self.update_csv,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=2)

        reset_button=Button(butn_frame,text="Reset",command=self.reset_dta,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        tbutn_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        tbutn_frame.place(x=0,y=245,width=715,height=70)


        save_button=Button(tbutn_frame,text="Save",command=self.add_datacsv,width=45,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)




        




       

        








#right side frame
         
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=(" times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)


        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=710,height=455)


       # ***************scroll bar*****************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","name","rollno","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text=" Attendance ID")
        self.AttendanceReportTable.heading("name",text=" Student name")
        self.AttendanceReportTable.heading("rollno",text=" RollNo")
        self.AttendanceReportTable.heading("time",text=" Time")
        self.AttendanceReportTable.heading("date",text=" Date")
        self.AttendanceReportTable.heading("attendance",text=" Attendance Status")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("rollno",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=150)




        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
#import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                        mydata.append(i)
                self.fetchData(mydata)


#export csv
    def exportCsv(self):
        try:
                if len(mydata)<1:
                        messagebox.showerror("NoData","No data found to export",parent=self.root)
                        return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                        export_wrt=csv.writer(myfile,delimiter=",")
                        for i in mydata:
                                export_wrt.writerow(i)
                        messagebox.showinfo("Data Export"," your data exported to "+ os.path.basename(fln)+"sucessfully")
        except Exception as es:
                         messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content["values"]

         self.var_atten_id.set(rows[0]),
         self.var_atten_name.set(rows[1]),
         self.var_atten_roll.set(rows[2]),
         self.var_atten_time.set(rows[3]),
         self.var_atten_date.set(rows[4]),
         self.var_atten_status.set(rows[5])

    def reset_dta(self):
        self.var_atten_id.set(""),
        self.var_atten_name.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_status.set("")
     
    def add_datacsv(self):

       
        try:
                        
                 conn=mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into studentattendance values(%s,%s,%s,%s,%s,%s)",(     self.var_atten_id.get(),
                                                                                                   self.var_atten_name.get(),
                                                                                                   self.var_atten_roll.get(),
                                                                                                   self.var_atten_time.get(),
                                                                                                   self.var_atten_date.get(),
                                                                                                   self.var_atten_status.get()
                                                                                                                     


                                                                                                                   
                                                                                                        
                                                                                                                   
                                                                                                                   
                                                                                                                    
                                                                                                                    
                                                                                                        
                                                                                                                
                                                                                                                ))
                 
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Success","Student Information stored succesfully") 
        except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)




    def update_csv(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="manu",database="facerecognization")
        my_cursor=conn.cursor()
        my_cursor.execute("update studentattendance set name=%s , time=%s , date=%s , status=%s where id=%s",( 
                    self.var_atten_name.get(),
                    self.var_atten_time.get(),
                    self.var_atten_date.get(),
                    self.var_atten_status.get(),
                    self.var_atten_id.get()
                    
                    ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Updated","Successfully updated the student",parent=self.root)







































if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
