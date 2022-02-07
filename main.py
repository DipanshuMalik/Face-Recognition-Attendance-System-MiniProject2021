from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
from tkinter import messagebox

class Face_Recognition_Attendance_System:
    def __init__(self,root):
        self.root=root   
        self.root.geometry("1930x1080+0+0")
        self.root.title("Face Recognition Attendance system")
        

        #bg image
        img=Image.open(r"images\fras img2.jpeg")
        img=img.resize((1536,860),Image.ANTIALIAS)   
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)   
        bg_img.place(x=0,y=0,width=1536,height=860)
        
        title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=250,y=50,width=1000,height=70)
        
        #Student button
        img1=Image.open(r"images\fras button1.png")
        img1=img1.resize((220,220),Image.ANTIALIAS)  
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=200,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=400,width=220,height=40)
        
        
        #Detect Button
        img2=Image.open(r"images\fras button2.png")
        img2=img2.resize((220,220),Image.ANTIALIAS)  
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b1.place(x=650,y=200,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=400,width=220,height=40)
        
        
        #Attendance Button
        img3=Image.open(r"images\fras button3.jpg")
        img3=img3.resize((220,220),Image.ANTIALIAS)   
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendance_data)
        b1.place(x=1100,y=200,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=400,width=220,height=40)
       
       
       
        #Train Button
        img4=Image.open(r"images\fras button4.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)   
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=500,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=700,width=220,height=40)
       
       
       
        #photos Button
        img5=Image.open(r"images\fras button5.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)   
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_img)
        b1.place(x=650,y=500,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=700,width=220,height=40)
       
       
       
        #Exit Button
        img6=Image.open(r"images\fras button6.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)  
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=500,width=220,height=220)
        
        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=700,width=220,height=40)

    def open_img(self):
        os.startfile("data")        
 
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #===============Functions buttons=========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

 
        
        
       




      







if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_Attendance_System(root)
    root.mainloop()