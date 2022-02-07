from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from numpy.lib.npyio import save


class Train:
    def __init__(self,root):
        self.root=root    #line 1
        self.root.geometry("1930x1080+0+0")
        self.root.title("Face Recognition Attendance system")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1536,height=45)

        img_top=Image.open(r"images\training img1.png")       
        img_top=img_top.resize((1536,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1536,height=325)

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",40,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=0,y=380,width=1536,height=80)

        img_bottom=Image.open(r"images\training img2.jpg")       
        img_bottom=img_bottom.resize((1536,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=460,width=1536,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')    #convert to grayscale image
            imageNp=np.array(img,'uint8')      #uint is datatype\
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)                  #append
            ids.append(id)                                                                                       
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)         #numpy is used to increase the array performance by 88%

        # ===========Train the classifier and save====================
        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!")


        








if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()