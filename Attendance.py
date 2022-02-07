from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root    #line 1
        self.root.geometry("1930x1080+0+0")
        self.root.title("Face Recognition Attendance system")


        #===========variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img1=Image.open(r"images\Attendance 1.jpg")
        img1=img1.resize((768,250),Image.ANTIALIAS)   #line 2
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=768,height=250)

        img2=Image.open(r"images\attendance 2.jpg")       
        img2=img2.resize((768,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=768,y=0,width=768,height=250)

        title_lbl=Label(self.root,text="Attendance Management System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=255,width=1536,height=55)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=15,y=315,width=1500,height=600)

        #Left frame
        Left_frame=LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=5,width=750,height=460)

        img_left=Image.open(r"images\attendance 3.png")       
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=140,width=720,height=290)

        #=====Labels and Entries===========
        #Attendance ID
        AttendanceID_label=Label(left_inside_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        AttendanceID_entry=ttk.Entry(left_inside_frame,width=23,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        rolllabel=Label(left_inside_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=10,pady=8,sticky=W)
        
        Atten_roll=ttk.Entry(left_inside_frame,width=23,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        Atten_roll.grid(row=0,column=3,pady=5,sticky=W)

        #Name
        namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        namelabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Atten_name=ttk.Entry(left_inside_frame,width=23,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        Atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Atten_dep=ttk.Entry(left_inside_frame,width=23,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        Atten_dep.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        # Time
        timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timelabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        Atten_time=ttk.Entry(left_inside_frame,width=23,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        Atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        datelabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Atten_date=ttk.Entry(left_inside_frame,width=23,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        Atten_date.grid(row=2,column=3,padx=0,pady=5,sticky=W)

        #Attendance 
        attendancelabel=Label(left_inside_frame,text="Attendance:",font=("times new roman",13,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",13,"bold"),width=21,textvariable=self.var_atten_attendance,state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        self.atten_status.current(0)

        #Buttons
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=185,width=710,height=50)

        importcsv_btn=Button(btn_frame,text="Import CSV",command=self.csv_import,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        importcsv_btn.grid(row=0,column=0,padx=15,pady=5)

        exportcsv_btn=Button(btn_frame,text="Export CSV",command=self.csv_export,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        exportcsv_btn.grid(row=0,column=1,padx=10,pady=5)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_csv,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10,pady=5)





        #Right frame
        Right_frame=LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=5,width=730,height=460)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=420)

        # =========Scrollbar Table===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReporttable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReporttable.xview)
        scroll_y.config(command=self.AttendanceReporttable.yview) 

        self.AttendanceReporttable.heading("id",text="Student ID")
        self.AttendanceReporttable.heading("roll",text="Roll No")
        self.AttendanceReporttable.heading("name",text="Name")
        self.AttendanceReporttable.heading("department",text="Department")
        self.AttendanceReporttable.heading("time",text="Time")
        self.AttendanceReporttable.heading("date",text="Date")
        self.AttendanceReporttable.heading("attendance",text="Attendance")

        self.AttendanceReporttable["show"]="headings"
        self.AttendanceReporttable.column("id",width=100)
        self.AttendanceReporttable.column("roll",width=100)
        self.AttendanceReporttable.column("name",width=100)
        self.AttendanceReporttable.column("department",width=100)
        self.AttendanceReporttable.column("time",width=100)
        self.AttendanceReporttable.column("date",width=100)
        self.AttendanceReporttable.column("attendance",width=100)


        self.AttendanceReporttable.pack(fill=BOTH,expand=1)

        self.AttendanceReporttable.bind("<ButtonRelease>",self.get_cursor)

        # =====================Fetch Data=======
    def fetch_data(self,rows):
        self.AttendanceReporttable.delete(*self.AttendanceReporttable.get_children())
        for i in rows:
            self.AttendanceReporttable.insert("",END,values=i)
    
    #import csv
    def csv_import(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)                                           #cwd Current working directory
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)         
    
    #export csv
    def csv_export(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root) 
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile)
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ==========get cursor==========
    def get_cursor(self,event=""):
        Cursor_row=self.AttendanceReporttable.focus()
        content=self.AttendanceReporttable.item(Cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    #=========reset data================
    def reset_csv(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")











if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()