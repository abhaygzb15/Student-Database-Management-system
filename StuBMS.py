from tkinter import * #tkinter is a library used to build GUI in python
from PIL import Image,ImageTk #Python Imaging Library - 2 functions built in
import mysql.connector  #msql
W=''
W1=''
W2=''
W3=''
W4=''

def Search():
    W1=''
    def Found():
        Roll_Number = int(Txt1.get())
        con= mysql.connector.connect(
            user="root",password="tiger",database="SDBMS")
        cur= con.cursor()
        query="SELECT * FROM records where Roll_number=({})".format(Roll_Number)
        cur.execute(query)
        items=cur.fetchall()
        if not items:
            text_widget = Text(W3, width=40, height=5)
            text_widget.place(x=130, y=250)
            text_widget.insert(END, f"Roll Number {Roll_Number} not found!")
            text_widget.config(state=DISABLED)
        else:
            text_widget=Text(W3,width=50,height=10)
            text_widget.place(x=200,y=200)
            for i in items:
                text_widget.insert(END,f"Roll Number: {i[0]}\nMarks: {i[1]}\nName: {i[2]}\nCourse: {i[3]}\n\n")
            text_widget.config(state=DISABLED)
                                            
    def Console():
        W3.destroy()
        GUI()
        
    W.destroy()
    global W3
    W3=Tk()
    W3.geometry("350x350")
    W3.configure(bg="#9A32CD")
    W3.title("SEARCHING RECORDS")
    L1=Label(W3,text="S E A R C H I N G",bg="light green",font=("Arial",25,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0)

    F=Frame(W3,bg="orange",width=310,height=150)
    F.place(x=13,y=80)
    Lb1=Label(F,text="TYPE THE ROLL NUMBER YOU WANT TO SEARCH",width=45,font=("Times New Roman",10,"bold"))
    Lb1.place(x=0,y=20)
    Txt1=Entry(F,width=10,font=("Times New Roman",15,"bold"))
    Txt1.place(x=20,y=80)
    B1=Button(F,text="PROCEED",bg="light blue",fg="red",command=Found,font=("Arial",10,"bold")).place(x=145,y=80)
    B2=Button(F,text="BACK",bg="light blue",fg="red",command=Console,font=("Arial",10,"bold")).place(x=240,y=80)



def Show():
    def Console():
        W4.destroy()
        GUI()
        
    W.destroy()
    global W4
    W4=Tk()
    W4.geometry("450x450")
    W4.configure(bg="#9A32CD")
    W4.title("RECORDS FOUND")
    L1=Label(W4,text="R E C O R D S   F O U N D",bg="light green",font=("Arial",25,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0)
    B2=Button(W4,text="BACK",bg="light blue",fg="red",command=Console,font=("Arial",10,"bold")).place(x=240,y=80)
    con= mysql.connector.connect(
            user="root",password="tiger",database="SDBMS")
    cur= con.cursor()
    query="SELECT * FROM records"
    cur.execute(query)
    items=cur.fetchall()
    text_widget=Text(W4,width=50,height=20)
    text_widget.place(x=100,y=150)
    for i in items:
        text_widget.insert(END,f"Roll Number: {i[0]}\nMarks: {i[1]}\nName: {i[2]}\nCourse: {i[3]}\n\n")
    text_widget.config(state=DISABLED)

def Deletion():
    W1=''
    def Delete():
        Roll_Number = int(Txt1.get())
        con= mysql.connector.connect(
        user="root",password="tiger",database="SDBMS")
        cur= con.cursor()
        query="DELETE FROM RECORDS WHERE Roll_number=({})".format(Roll_Number)
        cur.execute(query)
        if cur.rowcount==0:
            text_widget.config(state=NORMAL)
            text_widget.delete('1.0', END)
            text_widget.insert(END, "Roll Number not found")
            text_widget.config(state=DISABLED)
        else:
            text_widget.config(state=NORMAL)
            text_widget.delete('1.0', END)
            text_widget.insert(END, f"Roll Number {Roll_Number} Deleted Sucessfully")
            text_widget.config(state=DISABLED)
            cur.execute("commit") #commit to reach successfully
            con.close()
      
    def console():
        W2.destroy()
        GUI()
    
    W.destroy()
    global W2
    W2=Tk()
    W2.geometry("350x350")
    W2.configure(bg="#9A32CD")
    W2.title("DELETION OF EXISTING RECORDS")
    L1=Label(W1,text="D E L E T I O N",bg="light green",font=("Arial",25,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0)

    F=Frame(W1,bg="orange",width=310,height=150)
    F.place(x=13,y=100)
    Lb1=Label(F,text="TYPE THE ROLL NUMBER YOU WANT TO DELETE ",width=45,font=("Times New Roman",10,"bold"))
    Lb1.place(x=0,y=20)
    Txt1=Entry(F,width=10,font=("Times New Roman",15,"bold"))
    Txt1.place(x=20,y=80)
    B1=Button(F,text="PROCEED",bg="light blue",fg="red",command=Delete,font=("Arial",10,"bold")).place(x=145,y=80)
    B2=Button(F,text="BACK",bg="light blue",fg="red",command=console,font=("Arial",10,"bold")).place(x=240,y=80)
    global text_widget
    text_widget=Text(W2,width=50,height=2)
    text_widget.place(x=80,y=270)
    text_widget.config(state=DISABLED)
     
def Insertion():
    def Create():
        global head
        Roll_Number = Txt1.get()
        Marks = Txt2.get()
        Name = Txt3.get()
        Course = Txt4.get()
        con= mysql.connector.connect(
        user="root",password="tiger",database="SDBMS")
        cur= con.cursor()
        query="INSERT INTO records VALUES ({},{},'{}','{}')".format(Roll_Number,Marks,Name,Course)
        cur.execute(query)
        cur.execute("commit") #commit to reach successfully
        con.close()
        
    def Clear():
        Txt1.delete("0",END)
        Txt2.delete("0",END)
        Txt3.delete("0",END)
        Txt4.delete("0",END)
          
    def console():
        W1.destroy()
        GUI()
     
    W.destroy()
    global W1
    W1=Tk()
    W1.geometry("500x500")
    W1.configure(bg="#9A32CD")
    W1.title("INSERTION OF NEW RECORDS")
    image=Image.open("R.png")    
    R=image.resize((400,200))     
    R1=ImageTk.PhotoImage(R)     
    Lb=Label(W1,image=R1)          
    Lb.place(x=50,y=60)
    L1=Label(W1,text="I N S E R T I O N",bg="light green",font=("Arial",25,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0)

    F=Frame(W1,bg="orange",width=450,height=200,bd=10)
    F.place(x=23,y=280)
    Lb1=Label(F,text="TYPE YOUR ROLL NUMBER",width=28,font=("Times New Roman",10,"bold"))
    Lb1.place(x=7,y=20)
    Txt1=Entry(F,width=30)
    Txt1.place(x=240,y=20)

    Lb2=Label(F,text="TYPE YOUR MARKS OUR OF 500",width=28,font=("Times New Roman",10,"bold"))
    Lb2.place(x=7,y=50)
    Txt2=Entry(F,width=30)
    Txt2.place(x=240,y=50)

    Lb3=Label(F,text="TYPE YOUR NAME",width=28,font=("Times New Roman",10,"bold"))
    Lb3.place(x=7,y=80)
    Txt3=Entry(F,width=30)
    Txt3.place(x=240,y=80)

    Lb4=Label(F,text="TYPE YOUR COURSE NAME",width=28,font=("Times New Roman",10,"bold"))
    Lb4.place(x=7,y=110)
    Txt4=Entry(F,width=30)
    Txt4.place(x=240,y=110)
     
    B1=Button(F,text="SAVE",bg="light blue",fg="red",command=Create,font=("Arial",10,"bold")).place(x=260,y=145)
    B2=Button(F,text="RESET",bg="light blue",fg="red",command=Clear,font=("Arial",10,"bold")).place(x=350,y=145)
    B3=Button(F,text="BACK TO PREVIOUS",bg="light blue",fg="red",command=console,font=("Arial",10,"bold")).place(x=25,y=145)
    W1.mainloop()


def GUI():
    global W
    W=Tk() #creates a window stored in W
    W.geometry("840x540")
    W.configure(bg="#9A32CD")
    W.title("STUDENT RECORD MANAGEMENT SYSTEM")
    image=Image.open("cover_dbms.png")   #open func to take image 
    R=image.resize((400,400))     #crop and it is pixels
    R1=ImageTk.PhotoImage(R)      #type of image that can be displayed in a Tkinter window.
    Lb=Label(W,image=R1)          #box where image is to be displayed on window
    Lb.place(x=20,y=100)
    L1=Label(W,text="STUDENT RECORD MANAGEMENT SYSTEM",bg="yellow",font=("TIMES NEW ROMAN",27,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0) #label so pad , and to start and end filled completely.fill both means take both xy

    F=Frame(height=400,bg="#E066FF",width=350)
    F.place(x=460,y=100)

    B1=Button(F,text="I N S E R T",relief=SUNKEN,bg="#E0FFFF",command=Insertion,fg="black",font=("Arial",20,"bold")).place(x=85,y=30)
    B2=Button(F,text="D E L E T E",relief=GROOVE,bg="#E0FFFF",command=Deletion,fg="black",font=("Arial",20,"bold")).place(x=85,y=120)
    B3=Button(F,text="S E A R C H",relief=GROOVE,bg="#E0FFFF",command=Search,fg="black",font=("Arial",20,"bold")).place(x=85,y=215)
    B4=Button(F,text="S H O W",relief=GROOVE,bg="#E0FFFF",command=Show,fg="black",font=("Arial",18,"bold")).place(x=185,y=310)
    B5=Button(F,text="E X I T",relief=GROOVE,bg="#E0FFFF",command=W.destroy,fg="black",font=("Arial",18,"bold")).place(x=65,y=310)
    W.mainloop() #interactions in a timely and efficient manner.
     #relief is txt on button how to display - raised , flat,etc.

GUI()
