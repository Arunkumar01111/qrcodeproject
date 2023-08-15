from tkinter import*
import qrcode
from PIL import Image,ImageTk
import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x500+100+50")
        self.root.title("QR DEVELOPER | DEVELOPED BY ARUN")
        self.root.resizable(False,False)


        title=Label(self.root,text="                QR CODE GENERATOR",font=("times new roman ",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        
        #======employee details window=========
        #=====variables=====
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_number=StringVar()
        self.var_mailid=StringVar()


        
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=60,y=100,width=550,height=380)
        emp_title=Label(emp_Frame,text="    STUDENT DETAILS ",font=("goudy old style ",30),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        lbl_emp_code=Label(emp_Frame,text="   STUDENT REG NO",font=("times new roman ",15,'bold'),bg='white').place(x=20,y=80)
        lbl_name=Label(emp_Frame,text="   STUDENT NAME",font=("times new roman ",15,'bold'),bg='white').place(x=20,y=120)
        lbl_number=Label(emp_Frame,text="  PHONE NUMBER ",font=("times new roman ",15,'bold'),bg='white').place(x=20,y=160)
        lbl_mailid=Label(emp_Frame,text="   EMAIL ID",font=("times new roman ",15,'bold'),bg='white').place(x=20,y=200)


        txt_emp_code=Entry(emp_Frame,font=("times new roman ",15),textvariable=self.var_emp_code,bg='lightblue').place(x=250,y=80)
        txt_name=Entry(emp_Frame,font=("times new roman ",15,'bold'),textvariable=self.var_name,bg='lightblue').place(x=250,y=120)
        txt_number=Entry(emp_Frame,font=("times new roman ",15,'bold'),textvariable=self.var_number,bg='lightblue').place(x=250,y=160)
        txt_mailid=Entry(emp_Frame,font=("times new roman ",15,'bold'),textvariable=self.var_mailid,bg='lightblue').place(x=250,y=200)

        btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text='clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=300,y=250,width=120,height=30)

        self.msg='QR GENERATED SUCCESSFULLY!!!'
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)
        
        #=====STUDENT QR CODE=========
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=620,y=100,width=370,height=380)
        emp_title=Label(qr_Frame,text="STUDENT QR CODE ",font=("goudy old style ",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
     
       
        self.qr_code=Label(qr_Frame,text='no qr\navailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        
        self.qr_code.place(x=70,y=90,width=180,height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_number.set('')
        self.var_mailid.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

        
    def generate(self):
        if self.var_name.get()=='' or self.var_emp_code.get()=='' or self.var_number.get()=='' or self.var_mailid.get()=='':
            self.msg='All Fields are required!!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"STUDENT REG NO:{self.var_emp_code.get()}\nSTUDENT NAME :{self.var_name.get()}\nPHONE NUMBER :{self.var_number.get()}\nEMAIL ID:{self.var_mailid.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save('image9.png')
            #=====QR Code iamge update=======
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            
            #=====updating notification======
            self.msg='QR GENERATED SUCCESSFULLY!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
            

       
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
        
