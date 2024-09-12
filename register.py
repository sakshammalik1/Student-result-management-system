from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from login import loginClass
import os
import sqlite3
class Register:
    def __init__(self, root):
       self.root=root
       self.root.title("Registeration Window")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="white")

       #===image===
       self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
       bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

       self.left=ImageTk.PhotoImage(file="images/side.png")
       left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

       frame1=Frame(self.root,bg="white")
       frame1.place(x=480,y=100,width=700,height=500)


       title=Label(frame1,text="Register Here",font=("times new roman",25,"bold"),bg="white",fg="green").place(x=50,y=30)
       fname=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
       self.txt_fname=Entry(frame1,font=("goudy old style",15, "bold"),bg="lightyellow")
       self.txt_fname.place(x=50,y=130,width=250)

       lname=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
       self.txt_lname=Entry(frame1,font=("goudy old style",15, "bold"),bg="lightyellow")
       self.txt_lname.place(x=370,y=130,width=250)

       password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
       self.txt_password=Entry(frame1,font=("goudy old style",15, "bold"),bg="lightyellow")
       self.txt_password.place(x=50,y=200,width=250)

       confirmpasss=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
       self.txt_confirmpass=Entry(frame1,font=("goudy old style",15, "bold"),bg="lightyellow")
       self.txt_confirmpass.place(x=370,y=200,width=250)

       self.btn_img=ImageTk.PhotoImage(file="images/register.png")
       btn_register=Button(frame1,image=self.btn_img,cursor="hand2",command=self.register_data).place(x=50,y=300)

       btn_login=Button(self.root,text="Sign In",font=("times new roman",20),cursor="hand2",command=self.add_login).place(x=200,y=460,width=180)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_confirmpass.delete(0,END)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_password.get()=="" or self.txt_confirmpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
        elif self.txt_password.get()!=self.txt_confirmpass.get():
            messagebox.showerror("Error","Password mismatch",parent=self.root) 
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select *from employee where fname=?",(self.txt_fname.get(),))
                row=cur.fetchone()
                if(row!=None):
                    messagebox.showerror("Error","User name already exist",parent=self.root)
                else:
                    cur.execute("insert into employee(fname,lname,password) values(?,?,?)",(
                    self.txt_fname.get(),
                    self.txt_lname.get(),
                    self.txt_password.get()    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Register Successfull",parent=self.root)
                self.clear()
            except Exception as ex:
                messagebox.showerror("error",f"error due to{str(ex)}")   
            
    def add_login(self):
        self.root.destroy()
        os.system("python login.py")
        
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()