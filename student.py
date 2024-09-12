from tkinter import *
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1120,height=35)

#---------------------------------------VARIABLES------------------------------------------

        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_ad=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        

#---------------------------------------WIDGETS------------------------------------------

        lbl_rollno=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=220,width=150)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=380,y=220,width=100)
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)
        txt_pin=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=560,y=220,width=100)

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=260)
        #lbl_=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

#---------------------------------------ENTRY FIeLDS------------------------------------------


        self.text_roll=Entry(self.root,textvariable=self.var_rollno,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.text_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,font=("goudy old style",15,"bold"),values=("Select","Male","Female","Other"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)

        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,width=540,height=100)

#---------------------------------------COLUMN 2------------------------------------------

        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)
        lbl_admission=Label(self.root,text="Addmission",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        self.course_list=[]
        self.fetch()

        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=460,y=60,width=200)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=460,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_ad,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=460,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),values=self.course_list,state="readonly",justify=CENTER)
        self.txt_course.place(x=460,y=180,width=200)
        self.txt_course.set("Select")

#---------------------------------------BUTTONS------------------------------------------
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),command=self.add,fg="white",cursor="hand2",bg="#2196f3")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),fg="white",cursor="hand2",bg="#4caf50",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),fg="white",cursor="hand2",bg="#f44336",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),fg="white",cursor="hand2",bg="#608d8b",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)


#---------------------------------------SEARCH PANEL------------------------------------------
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_rollno,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),fg="white",cursor="hand2",bg="#03a9f4",command=self.search).place(x=1070,y=60,width=120,height=28)
        
#---------------------------------------CONTENT------------------------------------------
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.course_table=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)
        
        self.course_table.heading("roll",text="Roll No")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("email",text="Email")
        self.course_table.heading("gender",text="Gender")
        self.course_table.heading("dob",text="D.O.B")
        self.course_table.heading("contact",text="Contact")
        self.course_table.heading("addmission",text="Addmission")
        self.course_table.heading("course",text="Course")
        self.course_table.heading("state",text="State")
        self.course_table.heading("city",text="City")
        self.course_table.heading("pin",text="PIN")
        self.course_table.heading("address",text="Address")

        self.course_table["show"]='headings'

        self.course_table.column("roll",width=100)
        self.course_table.column("name",width=100)
        self.course_table.column("email",width=100)
        self.course_table.column("gender",width=100)
        self.course_table.column("dob",width=100)
        self.course_table.column("contact",width=100)
        self.course_table.column("addmission",width=100)
        self.course_table.column("course",width=100)
        self.course_table.column("state",width=100)
        self.course_table.column("city",width=100)
        self.course_table.column("pin",width=100)
        self.course_table.column("address",width=200)

        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        


#---------------------------------------DATABASE------------------------------------------

    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_ad.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.text_roll.config(state=NORMAL)
        self.var_search.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll No name should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Plz select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def get_data(self,ev):
        self.text_roll.config(state="readonly")
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content["values"]
        self.var_rollno.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_ad.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)        
        self.txt_address.insert(END,row[11])

    
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,addmission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_rollno.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_ad.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student added successfully",parent=self.root)
                    self.show()                    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,addmission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_ad.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.txt_address.get("1.0",END),
                        self.var_rollno.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update successfully",parent=self.root)
                    self.show()                    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()           
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)                
                  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()  
            v=[]
            if len(rows)!=0:
                for row in rows:
                    self.course_list.append(row[0])
            
                 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where roll=?",(self.var_rollno.get(),))
            rows=cur.fetchone() 
            if rows!=None:          
                self.course_table.delete(*self.course_table.get_children())
                for row in rows:
                    self.course_table.insert('',END,values=row) 
            else:
                messagebox.showerror("Error","No record found",parent=self.root)               
                  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()