from tkinter import *
from PIL import Image,ImageTk  #pip install pillow
from course import CourseClass
from student import StudentClass
from result import Result
from tkinter import messagebox
from report import Report_class
import os

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

#---------------------------------------ICONS-------------------------------------------
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")


#---------------------------------------TITLE-------------------------------------------
        title=Label(self.root,text="Student Result Management System",compound=LEFT,padx=10,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

#---------------------------------------MENU-------------------------------------------
        M_frame=LabelFrame(self.root,text="menus",font=("times new roman",15),bg="white")
        M_frame.place(x=10,y=70,width=1340,height=80)
        btn_course=Button(M_frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_exit).place(x=1120,y=5,width=200,height=40)

#---------------------------------------FOOTER-------------------------------------------
        footer=Label(self.root,text="SRMS-Student Result Management System\n Graphic Era deemed to be university.",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

#---------------------------------------CONTENT WINDOW-------------------------------------------
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

#---------------------------------------UPDATE DETAILS-------------------------------------------
        self.lbl_course=Label(self.root,text="Total courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Result(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Report_class(self.new_win)
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    def add_exit(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
