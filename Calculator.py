from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")
val= ""
A= 0
operator = ""
def b1_is_clicked():
    global val
    val=val+"1"
    data.set(val)
def b2_is_clicked():
    global val
    val=val+"2"
    data.set(val)
def b3_is_clicked():
    global val
    val=val+"3"
    data.set(val)
def b4_is_clicked():
    global val
    val=val+"4"
    data.set(val)
def b5_is_clicked():
    global val
    val=val+"5"
    data.set(val)
def b6_is_clicked():
    global val
    val=val+"6"
    data.set(val)
def b7_is_clicked():
    global val
    val=val+"7"
    data.set(val)
def b8_is_clicked():
    global val
    val=val+"8"
    data.set(val)
def b9_is_clicked():
    global val
    val=val+"9"
    data.set(val)
def b0_is_clicked():
    global val
    val=val+"0"
    data.set(val)
def b1_is_clicked():
    global val
    val=val+"1"
    data.set(val)

def btpl_is_clicked():
    global A
    global operater,val
    A = int(val)
    operater = "+"
    val = val + "+"
    data.set(val)

def btmin_is_clicked():
    global A
    global operater,val
    A = int(val)
    operater = "-"
    val = val + "-"
    data.set(val)

def btmul_is_clicked():
    global A
    global operater,val
    A = int(val)
    operater = "*"
    val = val + "*"
    data.set(val)

def btdiv_is_clicked():
    global A
    global operater,val
    A = int(val)
    operater = "/"
    val = val + "/"
    data.set(val)
    
def btc_is_clicked():
    global A
    global operater,val
    A = 0
    operater = ""
    val = ""
    data.set(val)

def result():
    global A,operater,val
    val2= val
    if operater == "+":
        x = int((val2.split("+")[1]))
        C =A+x
        val=str(C)
        data.set(C)
    if operater == "-":
        x = int((val2.split("-")[1]))
        C =A-x
        val=str(C)
        data.set(C)
    if operater == "*":
        x = int((val2.split("*")[1]))
        C =A*x
        val=str(C)
        data.set(C)
    if operater == "/":
        x = int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","can't divide number by 0")
            A =""
            val=""
            data.set(val)
        else:
            C =int(A/x)
            data.set(C)
        
data=StringVar()
l= Label(root,text="Label",anchor = SE,font=('Verdana',20),textvariable = data,background = "#ffffff",fg="#000000",)
l.pack(expand=True,fill = "both")
f1=Frame(root)
f1.pack(expand= True,fill="both")
f2=Frame(root)
f2.pack(expand= True,fill="both")
f3=Frame(root)
f3.pack(expand= True,fill="both")
f4=Frame(root)
f4.pack(expand= True,fill="both")
#button for frame 1
b1= Button(f1,text = "1",font=("Verdana", 22),relief = GROOVE,border =0,command = b1_is_clicked)
b1.pack(side=LEFT, expand= True ,fill="both",)

b2= Button(f1,text = "2",font=("Verdana", 22),relief = GROOVE,border =0,command = b2_is_clicked )
b2.pack(side=LEFT, expand= True ,fill="both",)

b3= Button(f1,text = "3",font=("Verdana", 22),relief = GROOVE,border =0,command = b3_is_clicked )
b3.pack(side=LEFT, expand= True ,fill="both",)

btpl= Button(f1,text = "+",font=("Verdana", 22),relief = GROOVE,border =0,command = btpl_is_clicked)
btpl.pack(side=LEFT, expand= True ,fill="both",)

#button for frame 2
b4= Button(f2,text = "4",font=("Verdana", 22),relief = GROOVE,border =0,command = b4_is_clicked )
b4.pack(side=LEFT, expand= True ,fill="both",)

b5= Button(f2,text = "5",font=("Verdana", 22),relief = GROOVE,border =0, command = b5_is_clicked)
b5.pack(side=LEFT, expand= True ,fill="both",)

b6= Button(f2,text = "6",font=("Verdana", 22),relief = GROOVE,border =0,command = b6_is_clicked )
b6.pack(side=LEFT, expand= True ,fill="both",)

btmin= Button(f2,text = "-",font=("Verdana", 22),relief = GROOVE,border =0,command = btmin_is_clicked )
btmin.pack(side=LEFT, expand= True ,fill="both",)

#button for frame3
b7= Button(f3,text = "7",font=("Verdana", 22),relief = GROOVE,border =0,command = b7_is_clicked )
b7.pack(side=LEFT, expand= True ,fill="both",)

b8= Button(f3,text = "8",font=("Verdana", 22),relief = GROOVE,border =0,command = b8_is_clicked )
b8.pack(side=LEFT, expand= True ,fill="both",)

b9= Button(f3,text = "9",font=("Verdana", 22),relief = GROOVE,border =0,command = b9_is_clicked )
b9.pack(side=LEFT, expand= True ,fill="both",)

btmul= Button(f3,text = "*",font=("Verdana", 22),relief = GROOVE,border =0,command = btmul_is_clicked )
btmul.pack(side=LEFT, expand= True ,fill="both",)

# button for frame 4

btc=Button(f4,text = "C",font= ("Veradana",22),relief =  GROOVE,border= 0,command = btc_is_clicked)
btc.pack(side= LEFT ,expand = True,fill="both",)

bt0=Button(f4,text = "0",font= ("Veradana",22),relief =  GROOVE,border= 0,command = b0_is_clicked)
bt0.pack(side= LEFT ,expand = True,fill="both",)

bteq=Button(f4,text = "=",font= ("Veradana",22),relief =  GROOVE,border= 0,command = result)
bteq.pack(side= LEFT ,expand = True,fill="both",)

btdiv=Button(f4,text = "/",font= ("Veradana",22),relief =  GROOVE,border= 0,command=btdiv_is_clicked)
btdiv.pack(side= LEFT ,expand = True,fill="both",)


root.mainloop()
