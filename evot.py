from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def dbn():
    global dapa,dana
    dapa=dp.get()
    dana=dn.get()
    datapas.destroy()

datapas=Tk()
datapas.title('ELECTION')
datapas.iconbitmap('ballot_box__5Lx_icon.ico')
datapas.configure(bg='#682957')
Label(datapas,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
Label(datapas,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()  
mtext='''ALL THE DATAS ARE STORED IN MYSQL DATABASE
SO INSTALL MYSQL'''
Label(datapas,text='DATABASE DETAILS',bg='#682957',font='Consolas 25 bold',fg='white').pack()
messagebox.showinfo('HELP',mtext)
Label(datapas,bg='#682957',font='Consolas 20 bold',fg='white').pack()
Label(datapas,bg='#682957',font='Consolas 20 bold',fg='white').pack()
Label(datapas,text='DATABASE PASSWORD',bg='#682957',font='Consolas 20 bold',fg='white').pack()
dp=StringVar()
de1=Entry(datapas,textvariable=dp,font='Consolas 20 bold',show='*')
de1.pack()
Label(datapas,bg='#682957',font='Consolas 20 bold',fg='white').pack()
Label(datapas,text='DATABASE NAME',bg='#682957',font='Consolas 20 bold',fg='white').pack()
dn=StringVar()
de2=Entry(datapas,textvariable=dn,font='Consolas 20 bold')
de2.pack()
Label(datapas,bg='#682957',font='Consolas 20 bold',fg='white').pack()
db1=Button(datapas,text='SUBMIT',command=dbn,font='Consolas 20 bold')
db1.pack()
datapas.mainloop()

try:
    z=mysql.connector.connect(host='localhost',user='root',passwd=dapa)
    a=z.cursor()
    a.execute("create database %s"%(dana))
    z=mysql.connector.connect(host='localhost',user='root',passwd=dapa,database=dana)
    a=z.cursor()

except:
    z=mysql.connector.connect(host='localhost',user='root',passwd=dapa,database=dana)
    a=z.cursor()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
try:
    a.execute('create table voterlist(rn int primary key,name varchar (30))')
    a.execute("create table spl (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table aspl (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table cul (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table acul (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table sport (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table asport (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table rtcap (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table rtvice (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table rtpre (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table cscap (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table csvice (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table cspre (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table cvrcap (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table cvrvice (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table cvrpre (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table mtcap (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table mtvice (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    a.execute("create table mtpre (reg_no int auto_increment primary key,name varchar(30),logo varchar(30),vote int)")
    messagebox.showinfo('HELP','WELCOME')
    
except:
    abcd=4

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def ok():
    res1.destroy()

def home():
    res.destroy()
    hp()
    
def home1():
    can2.destroy()
    hp()

def back():
    form.destroy()
    new_can2()
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def delvote():
    action=messagebox.askquestion('DELETE','ARE YOU SURE?',icon='warning')
    if action=='yes':
        a.execute('update spl set vote=0')
        z.commit()
        a.execute('update aspl set vote=0')
        z.commit()
        a.execute('update cul set vote=0')
        z.commit()
        a.execute('update acul set vote=0')
        z.commit()
        a.execute('update sport set vote=0')
        z.commit()
        a.execute('update asport set vote=0')
        z.commit()
        a.execute('update rtcap set vote=0')
        z.commit()
        a.execute('update rtvice set vote=0')
        z.commit()
        a.execute('update rtpre set vote=0')
        z.commit()
        a.execute('update cscap set vote=0')
        z.commit()
        a.execute('update csvice set vote=0')
        z.commit()
        a.execute('update cspre set vote=0')
        z.commit()
        a.execute('update cvrcap set vote=0')
        z.commit()
        a.execute('update cvrvice set vote=0')
        z.commit()
        a.execute('update cvrpre set vote=0')
        z.commit()
        a.execute('update mtcap set vote=0')
        z.commit()
        a.execute('update mtvice set vote=0')
        z.commit()
        a.execute('update mtpre set vote=0')
        z.commit()
        messagebox.showinfo('HELP','ALL VOTES DELETED')
    else:
        abcd=4
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def delcan():
    action=messagebox.askquestion('DELETE','ARE YOU SURE ?')
    if action=='yes':
        a.execute('drop table spl,aspl,cul,acul,sport,asport,rtcap,rtvice,rtpre,cscap,csvice,cspre,cvrcap,cvrvice,cvrpre,mtcap,mtvice,mtpre')
        z.commit()
        messagebox.showinfo('HELP','CANDIDATE LIST DELETED')
    else:
        abcd=4
#------------------------------------------------------------------------------------------------RESULT---------------------------------------------------------------------------------------------------------------#
def rspl():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()      
    Label(res1,text='SCHOOL PUPIL LEADER',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    a.execute('select * from spl')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def raspl():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()        
    Label(res1,text='Asst.SCHOOL PUPIL LEADER',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    a.execute('select * from aspl')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rcul():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()     
    Label(res1,text='CULTURAL SECRETARY',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from cul')
    rs=a.fetchall()


    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def racul():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()        
    Label(res1,text='Asst.CULTURAL SECRETARY',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack() 
    a.execute('select * from acul')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack() 
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rsport():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()    
    Label(res1,text="SPORTS CAPTAIN ",bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    a.execute('select * from sport')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rasport():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text='Asst.SPORTS CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from asport')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold',)
    b1.pack()
    
    res1.mainloop()

def rrtcap():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack() 
    Label(res1,text='RT CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from rtcap')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rrtvice():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()       
    Label(res1,text='RT VICE CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack() 
    a.execute('select * from rtvice')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack() 
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rrtpre():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()       
    Label(res1,text='RT PREFECT',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()  
    a.execute('select * from rtpre')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()  
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rcscap():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()         
    Label(res1,text='CS CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    a.execute('select * from cscap')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rcsvice():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()     
    Label(res1,text='CS VICE CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    a.execute('select * from csvice')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()   
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rcspre():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()     
    Label(res1,text='CS CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from cspre')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rcvrcap():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()        
    Label(res1,text='C.V.RAMAN CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from cvrcap')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rcvrvice():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()    
    Label(res1,text='C.V.RAMAN VICE CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from cvrvice')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()


def rcvrpre():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()    
    Label(res1,text='C.V.RAMAN PREFECT',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from cvrpre')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()    
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()


def rmtcap():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text='MT CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()    
    a.execute('select * from mtcap')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rmtvice():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold').pack()
    Label(res1,text='MT VICE CAPTAIN',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold').pack()
    a.execute('select * from mtvice')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 15 bold')
    b1.pack()
    
    res1.mainloop()

def rmtpre():
    global res1
    res1=Tk()
    res1.title('ELECTION')
    res1.iconbitmap('ballot_box__5Lx_icon.ico')
    res1.configure(bg='#682957')
    Label(res1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold').pack()
    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold').pack()
    Label(res1,text='MT PREFECT',bg='#682957',font='Consolas 25 bold',fg='white').pack()
    a.execute('select * from mtpre')
    rs=a.fetchall()

    scroll=Scrollbar(res1)
    scroll.pack(side='right',fill=Y)

    tab=ttk.Treeview(res1,columns=(1,2,3),show='headings',height=3,yscrollcommand=scroll.set)
    tab.pack()

    for i in rs:
        mnb=(i[0],i[1],i[3])
        tab.insert('',END,values=mnb)
    scroll.configure(command=tab.yview)

    tab.heading(1,text='REG_NO')
    tab.heading(2,text='NAME')
    tab.heading(3,text='VOTE')

    Label(res1,text=' ',bg='#682957',font='Consolas 25 bold').pack()
    b1=Button(res1,text='OK',command=ok,font='Consolas 20 bold')
    b1.pack()
    
    res1.mainloop()
    
def result2():
    global res
    res=Tk()
    res.title('ELECTION')
    res.iconbitmap('ballot_box__5Lx_icon.ico')    
    res.configure(bg='#682957')
    Label(res,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(res,text=' ',bg='#682957').pack()
    Label(res,text='ELECTION RESULTS ',bg='#682957',font='Broadway 28 bold',fg='white').pack()    
    Label(res,text=' ',bg='#682957').pack()
    Label(res,text=' ',bg='#682957').pack()
    mb=Menubutton(res,text='CATEGORIES',bg='black',font='Rockwell 25 bold',fg='white')
    mb.menu=Menu(mb)
    mb['menu']=mb.menu

    mb.menu.add_command(label='SPL',command=rspl,font='Rockwell 12 bold')
    mb.menu.add_command(label='ASPL',command=raspl,font='Rockwell 12 bold')
    mb.menu.add_command(label='CUL',command=rcul,font='Rockwell 12 bold')
    mb.menu.add_command(label='ACUL',command=racul,font='Rockwell 12 bold')
    mb.menu.add_command(label='SPORT',command=rsport,font='Rockwell 12 bold')
    mb.menu.add_command(label='ASPORT',command=rasport,font='Rockwell 12 bold')
    mb.menu.add_command(label='RT CAP',command=rrtcap,font='Rockwell 12 bold')
    mb.menu.add_command(label='RT VICE',command=rrtvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='RT PRE',command=rrtpre,font='Rockwell 12 bold')
    mb.menu.add_command(label='CS CAP',command=rcscap,font='Rockwell 12 bold')
    mb.menu.add_command(label='CS VICE',command=rcsvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='CS PRE',command=rcspre,font='Rockwell 12 bold')
    mb.menu.add_command(label='CVR CAP',command=rcvrcap,font='Rockwell 12 bold')
    mb.menu.add_command(label='CVR VICE',command=rcvrvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='CVR PRE',command=rcvrpre,font='Rockwell 12 bold')
    mb.menu.add_command(label='MT CAP',command=rmtcap,font='Rockwell 12 bold')
    mb.menu.add_command(label='MT VICE',command=rmtvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='MT PRE',command=rmtpre,font='Rockwell 12 bold')
    mb.pack()

    Label(res,text=' ',bg='#682957').pack()
    
    b1=Button(res,text='HOME',bg='black',font='Rockwell 20 bold',fg='white',command=home)
    b1.pack()

    Label(res,text=' ',bg='#682957').pack()

    res.mainloop()



    
def result1():
    user=un.get()
    passwd=ps.get()
    if user=='prasanth' and passwd=='anand':
        lp.destroy()
        result2()
    else:
        lp.destroy()
        hp()
        
    
def result():
    sgp.destroy()
    global lp
    lp=Tk()
    lp.title('ELECTION')
    lp.iconbitmap('ballot_box__5Lx_icon.ico')    
    lp.configure(bg='#682957')
    global un,ps
    Label(lp,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(lp,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()     
    l1=Label(lp,text='LOGIN PAGE',fg='white',bg='#682957',font='Ravie 30 bold')
    l1.pack()
    Label(lp,text=' ',bg='#682957').pack()

    l2=Label(lp,text='USERNAME',bg='#682957',font='Rockwell 25 bold',fg='white')
    l2.pack()
    un=StringVar()
    e1=Entry(lp,textvariable=un,bg='#675839',font='Rockwell 20 bold',fg='white')
    e1.pack()
    e1.focus()

    Label(lp,text=' ',bg='#682957').pack()

    l3=Label(lp,text='PASSWORD',bg='#682957',font='Rockwell 25 bold',fg='white')
    l3.pack()
    ps=StringVar()
    e2=Entry(lp,textvariable=ps,bg='#675839',show='*',font='Rockwell 20 bold',fg='white')
    e2.pack()
    Label(lp,text=' ',bg='#682957').pack()

    b1=Button(lp,text='SUBMIT',command=result1,font='Rockwell 25 bold')
    b1.pack()
    lp.mainloop()
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
'''-----------------------------------------------------------------------------------------------(MT PRE CAN)-----------------------------------------------------------------------------------------------------'''
def cmtprec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into mtpre (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def cmtpre():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#FA9027')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FA9027',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#FA9027').pack()
    Label(form,text='MT PREFECT  ',bg='#FA9027',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#FA9027').pack()
    Label(form,text=' ',bg='#FA9027').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#FA9027',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#FA9027',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#FA9027',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#FA9027',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=cmtprec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#FA9027').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''--------------------------------------------------------------------------------------------(MT VICE CAP CAN)-------------------------------------------------------------------------------------------------'''
def cmtvicec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into mtvice (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def cmtvice():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#FA9027')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FA9027',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#FA9027').pack()
    Label(form,text='MT VICE CAPTAIN',bg='#FA9027',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#FA9027').pack()
    Label(form,text=' ',bg='#FA9027').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#FA9027',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#FA9027',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#FA9027',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#FA9027',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=cmtvicec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#FA9027').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''-----------------------------------------------------------------------------------------------(MT CAP CAN)-----------------------------------------------------------------------------------------------------'''
def cmtcapc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into mtcap (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def cmtcap():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#FA9027')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FA9027',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#FA9027').pack()
    Label(form,text='MT CAPTAIN  ',bg='#FA9027',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#FA9027').pack()
    Label(form,text=' ',bg='#FA9027').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#FA9027',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#FA9027',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#FA9027',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#FA9027',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=cmtcapc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#FA9027').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''---------------------------------------------------------------------------------------------(CVR PRE CAN)-------------------------------------------------------------------------------------------------------'''
def ccvrprec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into cvrpre (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccvrpre():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#32F831')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#32F831',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#32F831').pack()
    Label(form,text='CVR PREFECT  ',bg='#32F831',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#32F831').pack()
    Label(form,text=' ',bg='#32F831').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#32F831',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#32F831',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#32F831',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#32F831',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=ccvrprec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#32F831').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''-------------------------------------------------------------------------------------------(CVR VICE CAP CAN)-------------------------------------------------------------------------------------------------'''
def ccvrvicec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into cvrvice (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccvrvice():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#32F831')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#32F831',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#32F831').pack()
    Label(form,text='CVR VICE CAPTAIN  ',bg='#32F831',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#32F831').pack()
    Label(form,text=' ',bg='#32F831').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#32F831',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#32F831',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#32F831',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#32F831',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=ccvrvicec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#32F831').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''--------------------------------------------------------------------------------------------(CVR CAP CAN)-------------------------------------------------------------------------------------------------------'''
def ccvrcapc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into cvrcap (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccvrcap():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#32F831')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#32F831',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#32F831').pack()
    Label(form,text='CVR CAPTAIN  ',bg='#32F831',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#32F831').pack()
    Label(form,text=' ',bg='#32F831').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#32F831',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#32F831',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#32F831',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#32F831',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=ccvrcapc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#32F831').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''-------------------------------------------------------------------------------------------(CS PRE CAP)-----------------------------------------------------------------------------------------------------------'''
def ccsprec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into cspre (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccspre():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#0FC3F2')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#0FC3F2',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#0FC3F2').pack()
    Label(form,text='CS PREFECT  ',bg='#0FC3F2',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#0FC3F2').pack()
    Label(form,text=' ',bg='#0FC3F2').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#0FC3F2',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#0FC3F2',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#0FC3F2',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#0FC3F2',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=ccsprec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#0FC3F2').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''----------------------------------------------------------------------------------------(CS VICE CAP CAN)------------------------------------------------------------------------------------------------------'''
def ccsvicec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into csvice (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccsvice():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#0FC3F2')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#0FC3F2',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#0FC3F2').pack()
    Label(form,text='CS VICE CAPTAIN  ',bg='#0FC3F2',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#0FC3F2').pack()
    Label(form,text=' ',bg='#0FC3F2').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#0FC3F2',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#0FC3F2',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#0FC3F2',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#0FC3F2',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=ccsvicec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#0FC3F2').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''------------------------------------------------------------------------------------------(CS CAP CAN)------------------------------------------------------------------------------------------------------------'''
def ccscapc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into cscap (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccscap():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#0FC3F2')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#0FC3F2',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#0FC3F2').pack()
    Label(form,text='CS  CAPTAIN  ',bg='#0FC3F2',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#0FC3F2').pack()
    Label(form,text=' ',bg='#0FC3F2').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#0FC3F2',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#0FC3F2',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#0FC3F2',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#0FC3F2',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=ccscapc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#0FC3F2').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''-------------------------------------------------------------------------------------------(RT PRE CAN)----------------------------------------------------------------------------------------------------------'''
def crtprec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into rtpre (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def crtpre():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#FF3131')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FF3131',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#FF3131').pack()
    Label(form,text='RT PREFECT ',bg='#FF3131',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#FF3131').pack()
    Label(form,text=' ',bg='#FF3131').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#FF3131',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#FF3131',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#FF3131',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#FF3131',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=crtprec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#FF3131').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()


'''---------------------------------------------------------------------------------------(RT VICE CAP CAN)------------------------------------------------------------------------------------------------------'''
def crtvicec():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into rtvice (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def crtvice():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#FF3131')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FF3131',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#FF3131').pack()
    Label(form,text='RT  VICE CAPTAIN  ',bg='#FF3131',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#FF3131').pack()
    Label(form,text=' ',bg='#FF3131').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#FF3131',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#FF3131',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#FF3131',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#FF3131',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=crtvicec,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#FF3131').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''-------------------------------------------------------------------------------------------(RT CAP CAN)---------------------------------------------------------------------------------------------------------'''
def crtcapc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into rtcap (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def crtcap():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#FF3131')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FF3131',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#FF3131').pack()
    Label(form,text='RT  CAPTAIN ',bg='#FF3131',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#FF3131').pack()
    Label(form,text=' ',bg='#FF3131').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#FF3131',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#FF3131',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#FF3131',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#FF3131',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=crtcapc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#FF3131').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''------------------------------------------------------------------------------------------(ASPORT CAN)---------------------------------------------------------------------------------------------------------'''
def casportc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into asport (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def casport():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#F4F570')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text='Asst.SPORT CAPTAIN ',bg='#F4F570',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text=' ',bg='#F4F570').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#F4F570',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#F4F570',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=casportc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#F4F570').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''------------------------------------------------------------------------------------------(SPORT CAN)-----------------------------------------------------------------------------------------------------------'''
def csportc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into sport (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def csport():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#F4F570')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text='SPORT CAPTAIN ',bg='#F4F570',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text=' ',bg='#F4F570').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#F4F570',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#F4F570',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=csportc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#F4F570').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''-------------------------------------------------------------------------------------------(ACUL CAN)------------------------------------------------------------------------------------------------------------'''
def caculc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into acul (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def cacul():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#F4F570')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text='Asst.CULTURAL SECRETARY ',bg='#F4F570',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text=' ',bg='#F4F570').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#F4F570',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#F4F570',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=caculc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#F4F570').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''-------------------------------------------------------------------------------------------(CUL CAN)--------------------------------------------------------------------------------------------------------------'''
def cculc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into cul (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def ccul():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#F4F570')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text='CULTURAL SECRETARY ',bg='#F4F570',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text=' ',bg='#F4F570').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#F4F570',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#F4F570',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=cculc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#F4F570').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''--------------------------------------------------------------------------------------------(ASPL CAN)------------------------------------------------------------------------------------------------------------'''
def casplc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into aspl (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def caspl():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#F4F570')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text='Asst.SCHOOL PUPIL LEADER ',bg='#F4F570',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text=' ',bg='#F4F570').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#F4F570',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#F4F570',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=casplc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#F4F570').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

'''-------------------------------------------------------------------------------(SPL CAN)------------------------------------------------------------------------------------------------------------------------------------------'''
def csplc():
    cname=name.get()
    cpic=pic.get()
    a.execute("insert into spl (name,logo,vote) values ('%s','%s',0)"%(cname,cpic))
    z.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    
def cspl():
    can2.destroy()
    global form,name,pic,e1,e2
    form=Tk()
    form.title('ELECTION')
    form.iconbitmap('ballot_box__5Lx_icon.ico')    
    form.configure(bg='#F4F570')
    Label(form,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 30 bold').pack()
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text='SCHOOL PUPIL LEADER ',bg='#F4F570',font='Broadway 28 bold').pack()    
    Label(form,text=' ',bg='#F4F570').pack()
    Label(form,text=' ',bg='#F4F570').pack()

    l1=Label(form,text='CANDIDATE NAME',bg='#F4F570',font='Consolas 25 bold')
    l1.pack()
    name=StringVar()
    e1=Entry(form,textvariable=name,font='Consolas 25 bold')
    e1.pack()

    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    l2=Label(form,text='LOGO',bg='#F4F570',font='Consolas 25 bold')
    l2.pack()
    pic=StringVar()
    e2=Entry(form,textvariable=pic,font='Consolas 25 bold')
    e2.pack()
    
    Label(form,text=' ',bg='#F4F570',font='Consolas 25 bold').pack()

    b1=Button(form,text='SUBMIT',command=csplc,font='Consolas 25 bold')
    b1.pack()

    Label(form,text=' ',bg='#F4F570').pack()

    b2=Button(form,text='BACK',command=back,font='Consolas 25 bold')
    b2.pack()    

    form.mainloop()

def new_can2():
    global can2
    can2=Tk()
    can2.title('ELECTION')
    can2.iconbitmap('ballot_box__5Lx_icon.ico')    
    can2.configure(bg='#682957')
    Label(can2,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(can2,text=' ',bg='#682957').pack()
    Label(can2,text='CANDIDATE FORM',bg='#682957',font='Broadway 28 bold',fg='white').pack()    
    Label(can2,text=' ',bg='#682957').pack()
    Label(can2,text=' ',bg='#682957').pack()
    mb=Menubutton(can2,text='CATEGORIES',bg='black',font='Rockwell 25 bold',fg='white')
    mb.menu=Menu(mb)
    mb['menu']=mb.menu

    mb.menu.add_command(label='SPL',command=cspl,font='Rockwell 12 bold')
    mb.menu.add_command(label='ASPL',command=caspl,font='Rockwell 12 bold')
    mb.menu.add_command(label='CUL',command=ccul,font='Rockwell 12 bold')
    mb.menu.add_command(label='ACUL',command=cacul,font='Rockwell 12 bold')
    mb.menu.add_command(label='SPORT',command=csport,font='Rockwell 12 bold')
    mb.menu.add_command(label='ASPORT',command=casport,font='Rockwell 12 bold')
    mb.menu.add_command(label='RT CAP',command=crtcap,font='Rockwell 12 bold')
    mb.menu.add_command(label='RT VICE',command=crtvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='RT PRE',command=crtpre,font='Rockwell 12 bold')
    mb.menu.add_command(label='CS CAP',command=ccscap,font='Rockwell 12 bold')
    mb.menu.add_command(label='CS VICE',command=ccsvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='CS PRE',command=ccspre,font='Rockwell 12 bold')
    mb.menu.add_command(label='CVR CAP',command=ccvrcap,font='Rockwell 12 bold')
    mb.menu.add_command(label='CVR VICE',command=ccvrvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='CVR PRE',command=ccvrpre,font='Rockwell 12 bold')
    mb.menu.add_command(label='MT CAP',command=cmtcap,font='Rockwell 12 bold')
    mb.menu.add_command(label='MT VICE',command=cmtvice,font='Rockwell 12 bold')
    mb.menu.add_command(label='MT PRE',command=cmtpre,font='Rockwell 12 bold')
    mb.pack()

    Label(can2,text=' ',bg='#682957').pack()
    
    b1=Button(can2,text='DELETE ALL CANDIDATES',bg='black',font='Rockwell 20 bold',fg='white',command=delcan)
    b1.pack()

    Label(can2,text=' ',bg='#682957').pack()
    
    b2=Button(can2,text='DELETE ALL THE VOTES',bg='black',font='Rockwell 20 bold',fg='white',command=delvote)
    b2.pack()

    Label(can2,text=' ',bg='#682957').pack()
    
    b3=Button(can2,text='BACK',bg='black',font='Rockwell 20 bold',fg='white',command=home1)
    b3.pack()

    Label(can2,text=' ',bg='#682957').pack()

    can2.mainloop()
    
    
def new_can1():
    user=un.get()
    pwd=ps.get()
    if user=='prasanth' and pwd=='anand':
        can1.destroy()
        new_can2()
    else:
        e1.delete(0,END)
        e2.delete(0,END)
        

def new_can():
    sgp.destroy()
    global can1,un,ps,e1,e2
    can1=Tk()
    can1.title('ELECTION')
    can1.iconbitmap('ballot_box__5Lx_icon.ico')    
    can1.configure(bg='#682957')
    Label(can1,text='VEDAVALLI VIDYALAYA RANIPET',bg='#682957',font='Broadway 30 bold',fg='white').pack()
    Label(can1,text=' ',bg='#682957',font='Consolas 25 bold',fg='white').pack()     
    l1=Label(can1,text='LOGIN PAGE',fg='white',bg='#682957',font='Ravie 30 bold')
    l1.pack()
    Label(can1,text=' ',bg='#682957').pack()

    l2=Label(can1,text='USERNAME',bg='#682957',font='Rockwell 25 bold',fg='white')
    l2.pack()
    un=StringVar()
    e1=Entry(can1,textvariable=un,bg='#675839',font='Rockwell 20 bold',fg='white')
    e1.pack()
    e1.focus()

    Label(can1,text=' ',bg='#682957').pack()

    l3=Label(can1,text='PASSWORD',bg='#682957',font='Rockwell 25 bold',fg='white')
    l3.pack()
    ps=StringVar()
    e2=Entry(can1,textvariable=ps,bg='#675839',show='*',font='Rockwell 20 bold',fg='white')
    e2.pack()
    Label(can1,text=' ',bg='#682957').pack()

    b1=Button(can1,text='SUBMIT',command=new_can1,font='Rockwell 25 bold')
    b1.pack()
    can1.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                                                                                                       #MT PREFECT VOTE
def vmtprev():
    voteval=mtpreval.get()
    a.execute('update mtpre set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    mtpre.destroy()
    hp()
    
    
def vmtpre():
    global mtpre,mtpreval
    mtpre=Tk()
    mtpre.configure(bg='#FA9027')
    wi, he = mtpre.winfo_screenwidth(), mtpre.winfo_screenheight()
    mtpre.overrideredirect(1)
    mtpre.geometry("%dx%d+0+0" % (wi, he))
    Label(mtpre,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FA9027',font='Broadway 20 bold').pack()
    Label(mtpre,text='ELECTION ',bg='#FA9027',font='Broadway 18 bold').pack()    
    Label(mtpre,text=' ',bg='#FA9027').pack()
    Label(mtpre,text='MT PREFECT',bg='#FA9027',font='Broadway 18 bold').pack()
    Label(mtpre,text=' ',bg='#FA9027').pack()
    
    a.execute('select * from mtpre')
    mtpreval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)      
        rb1=Radiobutton(mtpre,text=j[1],variable=mtpreval,value=j[0],bg='#FA9027',font='Consolas 20 bold')
        rb1.pack()
        
    Label(mtpre,text=' ',bg='#FA9027').pack()
    b1=Button(mtpre,text='SUBMIT',command=vmtprev,font='Consolas 20 bold')
    b1.pack()

    mtpre.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #MT VICE CAP VOTE
def vmtvicev():
    voteval=mtviceval.get()
    a.execute('update mtvice set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    mtvice.destroy()
    vmtpre()
    
    
def vmtvice():
    global mtvice,mtviceval
    mtvice=Tk()
    mtvice.configure(bg='#FA9027')
    wi, he = mtvice.winfo_screenwidth(), mtvice.winfo_screenheight()
    mtvice.overrideredirect(1)
    mtvice.geometry("%dx%d+0+0" % (wi, he))
    Label(mtvice,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FA9027',font='Broadway 20 bold').pack()
    Label(mtvice,text='ELECTION ',bg='#FA9027',font='Broadway 18 bold').pack()    
    Label(mtvice,text=' ',bg='#FA9027').pack()
    Label(mtvice,text='MT VICE CAPTAIN',bg='#FA9027',font='Broadway 18 bold').pack()
    Label(mtvice,text=' ',bg='#FA9027').pack()
    
    a.execute('select * from mtvice')
    mtviceval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)      
        rb1=Radiobutton(mtvice,text=j[1],variable=mtviceval,value=j[0],bg='#FA9027',font='Consolas 20 bold')
        rb1.pack()
        
    Label(mtvice,text=' ',bg='#FA9027').pack()
    b1=Button(mtvice,text='SUBMIT',command=vmtvicev,font='Consolas 20 bold')
    b1.pack()

    mtvice.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #MT CAP VOTE
def vmtcapv():
    voteval=mtcapval.get()
    a.execute('update mtcap set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    mtcap.destroy()
    vmtvice()
    
    
def vmtcap():
    global mtcap,mtcapval
    mtcap=Tk()
    mtcap.configure(bg='#FA9027')
    wi, he = mtcap.winfo_screenwidth(), mtcap.winfo_screenheight()
    mtcap.overrideredirect(1)
    mtcap.geometry("%dx%d+0+0" % (wi, he))
    Label(mtcap,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FA9027',font='Broadway 20 bold').pack()
    Label(mtcap,text='ELECTION ',bg='#FA9027',font='Broadway 18 bold').pack()    
    Label(mtcap,text=' ',bg='#FA9027').pack()
    Label(mtcap,text='MT CAPTAIN',bg='#FA9027',font='Broadway 18 bold').pack()
    Label(mtcap,text=' ',bg='#FA9027').pack()
    
    a.execute('select * from mtcap')
    mtcapval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)      
        rb1=Radiobutton(mtcap,text=j[1],variable=mtcapval,value=j[0],bg='#FA9027',font='Consolas 20 bold')
        rb1.pack()
        
    Label(mtcap,text=' ',bg='#FA9027').pack()
    b1=Button(mtcap,text='SUBMIT',command=vmtcapv,font='Consolas 20 bold')
    b1.pack()

    mtcap.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #CVR PREFECT VOTE
def vcvrprev():
    voteval=cvrpreval.get()
    a.execute('update cvrpre set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    cvrpre.destroy()
    hp()
    
    
def vcvrpre():
    global cvrpre,cvrpreval
    cvrpre=Tk()
    cvrpre.configure(bg='#32F831')
    wi, he = cvrpre.winfo_screenwidth(), cvrpre.winfo_screenheight()
    cvrpre.overrideredirect(1)
    cvrpre.geometry("%dx%d+0+0" % (wi, he))
    Label(cvrpre,text='VEDAVALLI VIDYALAYA RANIPET',bg='#32F831',font='Broadway 20 bold').pack()
    Label(cvrpre,text='ELECTION ',bg='#32F831',font='Broadway 18 bold').pack()    
    Label(cvrpre,text=' ',bg='#32F831').pack()
    Label(cvrpre,text='CVR PREFECT',bg='#32F831',font='Broadway 18 bold').pack()
    Label(cvrpre,text=' ',bg='#32F831').pack()
    
    a.execute('select * from cvrpre')
    cvrpreval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)   
        rb1=Radiobutton(cvrpre,text=j[1],variable=cvrpreval,value=j[0],bg='#32F831',font='Consolas 20 bold')
        rb1.pack()
        
    Label(cvrpre,text=' ',bg='#32F831').pack()
    b1=Button(cvrpre,text='SUBMIT',command=vcvrprev,font='Consolas 20 bold')
    b1.pack()

    cvrpre.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #CVR VICE CAP VOTE
def vcvrvicev():
    voteval=cvrviceval.get()
    a.execute('update cvrvice set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    cvrvice.destroy()
    vcvrpre()
    
    
def vcvrvice():
    global cvrvice,cvrviceval
    cvrvice=Tk()
    cvrvice.configure(bg='#32F831')
    wi, he = cvrvice.winfo_screenwidth(), cvrvice.winfo_screenheight()
    cvrvice.overrideredirect(1)
    cvrvice.geometry("%dx%d+0+0" % (wi, he))
    Label(cvrvice,text='VEDAVALLI VIDYALAYA RANIPET',bg='#32F831',font='Broadway 20 bold').pack()
    Label(cvrvice,text='ELECTION ',bg='#32F831',font='Broadway 18 bold').pack()    
    Label(cvrvice,text=' ',bg='#32F831').pack()
    Label(cvrvice,text='CVR VICE CAPTAIN',bg='#32F831',font='Broadway 18 bold').pack()
    Label(cvrvice,text=' ',bg='#32F831').pack()
    
    a.execute('select * from cvrvice')
    cvrviceval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)    
        rb1=Radiobutton(cvrvice,text=j[1],variable=cvrviceval,value=j[0],bg='#32F831',font='Consolas 20 bold')
        rb1.pack()
        
    Label(cvrvice,text=' ',bg='#32F831').pack()
    b1=Button(cvrvice,text='SUBMIT',command=vcvrvicev,font='Consolas 20 bold')
    b1.pack()

    cvrvice.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #CVR CAP VOTE
def vcvrcapv():
    voteval=cvrcapval.get()
    a.execute('update cvrcap set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    cvrcap.destroy()
    vcvrvice()
    
    
def vcvrcap():
    global cvrcap,cvrcapval
    cvrcap=Tk()
    cvrcap.configure(bg='#32F831')
    wi, he = cvrcap.winfo_screenwidth(), cvrcap.winfo_screenheight()
    cvrcap.overrideredirect(1)
    cvrcap.geometry("%dx%d+0+0" % (wi, he))
    Label(cvrcap,text='VEDAVALLI VIDYALAYA RANIPET',bg='#32F831',font='Broadway 20 bold').pack()
    Label(cvrcap,text='ELECTION ',bg='#32F831',font='Broadway 18 bold').pack()    
    Label(cvrcap,text=' ',bg='#32F831').pack()
    Label(cvrcap,text='CVR CAPTAIN',bg='#32F831',font='Broadway 18 bold').pack()
    Label(cvrcap,text=' ',bg='#32F831').pack()
    
    a.execute('select * from cvrcap')
    cvrcapval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)      
        rb1=Radiobutton(cvrcap,text=j[1],variable=cvrcapval,value=j[0],bg='#32F831',font='Consolas 20 bold')
        rb1.pack()
        
    Label(cvrcap,text=' ',bg='#32F831').pack()
    b1=Button(cvrcap,text='SUBMIT',command=vcvrcapv,font='Consolas 20 bold')
    b1.pack()

    cvrcap.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #CS PRE VOTE
def vcsprev():
    voteval=cspreval.get()
    a.execute('update cspre set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    cspre.destroy()
    hp()
    
    
def vcspre():
    global cspre,cspreval
    cspre=Tk()
    cspre.configure(bg='#0FC3F2')
    wi, he = cspre.winfo_screenwidth(), cspre.winfo_screenheight()
    cspre.overrideredirect(1)
    cspre.geometry("%dx%d+0+0" % (wi, he))
    Label(cspre,text='VEDAVALLI VIDYALAYA RANIPET',bg='#0FC3F2',font='Broadway 20 bold').pack()
    Label(cspre,text='ELECTION ',bg='#0FC3F2',font='Broadway 18 bold').pack()    
    Label(cspre,text=' ',bg='#0FC3F2').pack()
    Label(cspre,text='CS PREFECT',bg='#0FC3F2',font='Broadway 18 bold').pack()
    Label(cspre,text=' ',bg='#0FC3F2').pack()
    
    a.execute('select * from cspre')
    cspreval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)    
        rb1=Radiobutton(cspre,text=j[1],variable=cspreval,value=j[0],bg='#0FC3F2',font='Consolas 20 bold')
        rb1.pack()
        
    Label(cspre,text=' ',bg='#0FC3F2').pack()
    b1=Button(cspre,text='SUBMIT',command=vcsprev,font='Consolas 20 bold')
    b1.pack()

    cspre.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #CS VICE CAP VOTE
def vcsvicev():
    voteval=csviceval.get()
    a.execute('update csvice set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    csvice.destroy()
    vcspre()
    
    
def vcsvice():
    global csvice,csviceval
    csvice=Tk()
    csvice.configure(bg='#0FC3F2')
    wi, he = csvice.winfo_screenwidth(), csvice.winfo_screenheight()
    csvice.overrideredirect(1)
    csvice.geometry("%dx%d+0+0" % (wi, he))
    Label(csvice,text='VEDAVALLI VIDYALAYA RANIPET',bg='#0FC3F2',font='Broadway 20 bold').pack()
    Label(csvice,text='ELECTION ',bg='#0FC3F2',font='Broadway 18 bold').pack()    
    Label(csvice,text=' ',bg='#0FC3F2').pack()
    Label(csvice,text='CS VICE CAPTAIN',bg='#0FC3F2',font='Broadway 18 bold').pack()
    Label(csvice,text=' ',bg='#0FC3F2').pack()
    
    a.execute('select * from csvice')
    csviceval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)     
        rb1=Radiobutton(csvice,text=j[1],variable=csviceval,value=j[0],bg='#0FC3F2',font='Consolas 20 bold')
        rb1.pack()
        
    Label(csvice,text=' ',bg='#0FC3F2').pack()
    b1=Button(csvice,text='SUBMIT',command=vcsvicev,font='Consolas 20 bold')
    b1.pack()

    csvice.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #CS CAP VOTE
def vcscapv():
    voteval=cscapval.get()
    a.execute('update cscap set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    cscap.destroy()
    vcsvice()
    
    
def vcscap():
    global cscap,cscapval
    cscap=Tk()
    cscap.configure(bg='#0FC3F2')
    wi, he = cscap.winfo_screenwidth(), cscap.winfo_screenheight()
    cscap.overrideredirect(1)
    cscap.geometry("%dx%d+0+0" % (wi, he))
    Label(cscap,text='VEDAVALLI VIDYALAYA RANIPET',bg='#0FC3F2',font='Broadway 20 bold').pack()
    Label(cscap,text='ELECTION ',bg='#0FC3F2',font='Broadway 18 bold').pack()    
    Label(cscap,text=' ',bg='#0FC3F2').pack()
    Label(cscap,text='CS CAPTAIN',bg='#0FC3F2',font='Broadway 18 bold').pack()
    Label(cscap,text=' ',bg='#0FC3F2').pack()
    
    a.execute('select * from cscap')
    cscapval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)  
        rb1=Radiobutton(cscap,text=j[1],variable=cscapval,value=j[0],bg='#0FC3F2',font='Consolas 20 bold')
        rb1.pack()
        
    Label(cscap,text=' ',bg='#0FC3F2').pack()
    b1=Button(cscap,text='SUBMIT',command=vcscapv,font='Consolas 20 bold')
    b1.pack()

    cscap.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                                                                                                       #RT PRE VOTE
def vrtprev():
    voteval=rtpreval.get()
    a.execute('update rtpre set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    rtpre.destroy()
    hp()
    
    
def vrtpre():
    global rtpre,rtpreval
    rtpre=Tk()
    rtpre.configure(bg='#FF3131')
    wi, he = rtpre.winfo_screenwidth(), rtpre.winfo_screenheight()
    rtpre.overrideredirect(1)
    rtpre.geometry("%dx%d+0+0" % (wi, he))
    Label(rtpre,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FF3131',font='Broadway 20 bold').pack()
    Label(rtpre,text='ELECTION ',bg='#FF3131',font='Broadway 18 bold').pack()    
    Label(rtpre,text=' ',bg='#FF3131').pack()
    Label(rtpre,text='RT PREFECT',bg='#FF3131',font='Broadway 18 bold').pack()
    Label(rtpre,text=' ',bg='#FF3131').pack()
    
    a.execute('select * from rtpre')
    rtpreval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)  
        rb1=Radiobutton(rtpre,text=j[1],variable=rtpreval,value=j[0],bg='#FF3131',font='Consolas 20 bold')
        rb1.pack()
        
    Label(rtpre,text=' ',bg='#FF3131').pack()
    b1=Button(rtpre,text='SUBMIT',command=vrtprev,font='Consolas 20 bold')
    b1.pack()

    rtpre.mainloop()
    

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


                                                                                                       #RT VICE VOTE
def vrtvicev():
    voteval=rtviceval.get()
    a.execute('update rtvice set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    rtvice.destroy()
    vrtpre()
    
    
def vrtvice():
    global rtvice,rtviceval
    rtvice=Tk()
    rtvice.configure(bg='#FF3131')
    wi, he = rtvice.winfo_screenwidth(), rtvice.winfo_screenheight()
    rtvice.overrideredirect(1)
    rtvice.geometry("%dx%d+0+0" % (wi, he))
    Label(rtvice,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FF3131',font='Broadway 20 bold').pack()
    Label(rtvice,text='ELECTION ',bg='#FF3131',font='Broadway 18 bold').pack()    
    Label(rtvice,text=' ',bg='#FF3131').pack()
    Label(rtvice,text='RT VICE CAPTAIN',bg='#FF3131',font='Broadway 18 bold').pack()
    Label(rtvice,text=' ',bg='#FF3131').pack()
    
    a.execute('select * from rtvice')
    rtviceval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)     
        rb1=Radiobutton(rtvice,text=j[1],variable=rtviceval,value=j[0],bg='#FF3131',font='Consolas 20 bold')
        rb1.pack()
        
    Label(rtvice,text=' ',bg='#FF3131').pack()
    b1=Button(rtvice,text='SUBMIT',command=vrtvicev,font='Consolas 20 bold')
    b1.pack()

    rtvice.mainloop()
    

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


                                                                                                       #RT CAP VOTE
def vrtcapv():
    voteval=rtcapval.get()
    a.execute('update rtcap set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    rtcap.destroy()
    vrtvice()
    
    
def vrtcap():
    global rtcap,rtcapval
    rtcap=Tk()
    rtcap.configure(bg='#FF3131')
    wi, he = rtcap.winfo_screenwidth(), rtcap.winfo_screenheight()
    rtcap.overrideredirect(1)
    rtcap.geometry("%dx%d+0+0" % (wi, he))
    Label(rtcap,text='VEDAVALLI VIDYALAYA RANIPET',bg='#FF3131',font='Broadway 20 bold').pack()
    Label(rtcap,text='ELECTION ',bg='#FF3131',font='Broadway 18 bold').pack()    
    Label(rtcap,text=' ',bg='#FF3131').pack()
    Label(rtcap,text='RT CAPTAIN',bg='#FF3131',font='Broadway 18 bold').pack()
    Label(rtcap,text=' ',bg='#FF3131').pack()
    
    a.execute('select * from rtcap')
    rtcapval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)     
        rb1=Radiobutton(rtcap,text=j[1],variable=rtcapval,value=j[0],bg='#FF3131',font='Consolas 20 bold')
        rb1.pack()
        
    Label(rtcap,text=' ',bg='#FF3131').pack()
    b1=Button(rtcap,text='SUBMIT',command=vrtcapv,font='Consolas 20 bold')
    b1.pack()

    rtcap.mainloop()
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


                                                                                                       #ASPORT VOTE
def vasportv():
    voteval=asportval.get()
    a.execute('update asport set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    asport.destroy()
    if house=='rt':
        vrtcap()
    elif house=='cs':
        vcscap()
    elif house=='cvr':
        vcvrcap()
    else:
        vmtcap()
    
    
def vasport():
    global asport,asportval
    asport=Tk()
    asport.configure(bg='#F4F570')
    wi, he = asport.winfo_screenwidth(), asport.winfo_screenheight()
    asport.overrideredirect(1)
    asport.geometry("%dx%d+0+0" % (wi, he))
    Label(asport,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 20 bold').pack()
    Label(asport,text='ELECTION ',bg='#F4F570',font='Broadway 18 bold').pack()    
    Label(asport,text=' ',bg='#F4F570').pack()
    Label(asport,text='Asst.SPORT CAPTAIN',bg='#F4F570',font='Broadway 18 bold').pack()
    Label(asport,text=' ',bg='#F4F570').pack()

    a.execute('select * from asport')
    asportval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)     
        rb1=Radiobutton(asport,text=j[1],variable=asportval,value=j[0],bg='#F4F570',font='Consolas 20 bold')
        rb1.pack()
        
    Label(asport,text=' ',bg='#F4F570').pack()
    b1=Button(asport,text='SUBMIT',command=vasportv,font='Consolas 20 bold')
    b1.pack()

    asport.mainloop()
    

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


                                                                                                       #SPORT VOTE
def vsportv():
    voteval=sportval.get()
    a.execute('update sport set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    sport.destroy()
    vasport()
    
    
def vsport():
    global sport,sportval
    sport=Tk()
    sport.configure(bg='#F4F570')
    wi, he = sport.winfo_screenwidth(), sport.winfo_screenheight()
    sport.overrideredirect(1)
    sport.geometry("%dx%d+0+0" % (wi, he))
    Label(sport,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 20 bold').pack()
    Label(sport,text='ELECTION ',bg='#F4F570',font='Broadway 18 bold').pack()    
    Label(sport,text=' ',bg='#F4F570').pack()
    Label(sport,text='SPORT CAPTAIN',bg='#F4F570',font='Broadway 18 bold').pack()
    Label(sport,text=' ',bg='#F4F570').pack()
    
    a.execute('select * from sport')
    sportval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)    
        rb1=Radiobutton(sport,text=j[1],variable=sportval,value=j[0],bg='#F4F570',font='Consolas 20 bold')
        rb1.pack()
        
    Label(sport,text=' ',bg='#F4F570').pack()
    b1=Button(sport,text='SUBMIT',command=vsportv,font='Consolas 20 bold')
    b1.pack()

    sport.mainloop()
    

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


                                                                                                       #ACUL VOTE
def vaculv():
    voteval=aculval.get()
    a.execute('update acul set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    acul.destroy()
    vsport()
    
    
def vacul():
    global acul,aculval
    acul=Tk()
    acul.configure(bg='#F4F570')
    wi, he = acul.winfo_screenwidth(), acul.winfo_screenheight()
    acul.overrideredirect(1)
    acul.geometry("%dx%d+0+0" % (wi, he))
    Label(acul,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 20 bold').pack()
    Label(acul,text='ELECTION ',bg='#F4F570',font='Broadway 18 bold').pack()    
    Label(acul,text=' ',bg='#F4F570').pack()
    Label(acul,text='Asst.CULTURAL SECRETARY',bg='#F4F570',font='Broadway 18 bold').pack()
    Label(acul,text=' ',bg='#F4F570').pack()    
    

    a.execute('select * from acul')
    aculval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)   
        rb1=Radiobutton(acul,text=j[1],variable=aculval,value=j[0],bg='#F4F570',font='Consolas 20 bold')
        rb1.pack()
        
    Label(acul,text=' ',bg='#F4F570').pack()
    b1=Button(acul,text='SUBMIT',command=vaculv,font='Consolas 20 bold')
    b1.pack()

    acul.mainloop()
    

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


                                                                                                       #CUL VOTE
def vculv():
    voteval=culval.get()
    a.execute('update cul set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    cul.destroy()
    vacul()
    
    
def vcul():
    global cul,culval
    cul=Tk()
    cul.configure(bg='#F4F570')
    wi, he = cul.winfo_screenwidth(), cul.winfo_screenheight()
    cul.overrideredirect(1)
    cul.geometry("%dx%d+0+0" % (wi, he))
    Label(cul,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 20 bold').pack()
    Label(cul,text='ELECTION ',bg='#F4F570',font='Broadway 18 bold').pack()    
    Label(cul,text=' ',bg='#F4F570').pack()
    Label(cul,text='CULTURAL SECRETARY',bg='#F4F570',font='Broadway 18 bold').pack()
    Label(cul,text=' ',bg='#F4F570').pack()
    
    a.execute('select * from cul')
    culval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)      
        rb1=Radiobutton(cul,text=j[1],variable=culval,value=j[0],bg='#F4F570',font='Consolas 20 bold')
        rb1.pack()
        
    Label(cul,text=' ',bg='#F4F570').pack()
    b1=Button(cul,text='SUBMIT',command=vculv,font='Consolas 20 bold')
    b1.pack()

    cul.mainloop()
    

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
                                                                                                       #ASPL VOTE
def vasplv():
    voteval=asplval.get()
    a.execute('update aspl set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    aspl.destroy()
    vcul()
    
    
def vaspl():
    global aspl,asplval
    aspl=Tk()
    aspl.configure(bg='#F4F570')
    wi, he = aspl.winfo_screenwidth(), aspl.winfo_screenheight()
    aspl.overrideredirect(1)
    aspl.geometry("%dx%d+0+0" % (wi, he))
    Label(aspl,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 20 bold').pack()
    Label(aspl,text='ELECTION ',bg='#F4F570',font='Broadway 18 bold').pack()    
    Label(aspl,text=' ',bg='#F4F570').pack()
    Label(aspl,text='Asst.SCHOOL PUPIL LEADER',bg='#F4F570',font='Broadway 18 bold').pack()
    Label(aspl,text=' ',bg='#F4F570').pack()
    
    a.execute('select * from aspl')
    asplval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)
        rb1=Radiobutton(aspl,text=j[1],variable=asplval,value=j[0],bg='#F4F570',font='Consolas 20 bold')
        rb1.pack()
        
    Label(aspl,text=' ',bg='#F4F570').pack()
    b1=Button(aspl,text='SUBMIT',command=vasplv,font='Consolas 20 bold')
    b1.pack()

    aspl.mainloop()
    
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
                                                                                                         #SPL VOTE
def vsplv():
    voteval=splval.get()
    a.execute('update spl set vote=vote+1 where reg_no=%s'%(voteval))
    z.commit()
    spl.destroy()
    vaspl()
    
def vspl():
    global spl,splval
    spl=Tk()
    spl.configure(bg='#F4F570')
    wi, he = spl.winfo_screenwidth(), spl.winfo_screenheight()
    spl.overrideredirect(1)
    spl.geometry("%dx%d+0+0" % (wi, he))
    Label(spl,text='VEDAVALLI VIDYALAYA RANIPET',bg='#F4F570',font='Broadway 20 bold').pack()
    Label(spl,text='ELECTION ',bg='#F4F570',font='Broadway 18 bold').pack()    
    Label(spl,text=' ',bg='#F4F570').pack()
    Label(spl,text='SCHOOL PUPIL LEADER',bg='#F4F570',font='Broadway 18 bold').pack()
    Label(spl,text=' ',bg='#F4F570').pack()

    a.execute('select * from spl')
    splval=IntVar()
    b=a.fetchall()
    picvar=[]
    for j in b:
        picvar.append(j[1])
        lvar=len(picvar)-1
        canvas=Canvas(width=100,height=100,bg='black')
        canvas.pack()
        picvar[lvar]=PhotoImage(file=j[2])
        canvas.create_image(0,0,image=picvar[lvar],anchor=NW)    
        rb1=Radiobutton(spl,text=j[1],variable=splval,value=j[0],bg='#F4F570',font='Consolas 20 bold')
        rb1.pack()
        
    Label(spl,text=' ',bg='#F4F570').pack()
    b1=Button(spl,text='SUBMIT',command=vsplv,font='Consolas 20 bold')
    b1.pack()

    spl.mainloop()
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def chs():
    global house
    roll=rn.get()
    name=nm.get()
    house=h.get()
    if house=='':
        messagebox.showerror('HELP','SELECT YOUR HOUSE')
    else:
        try:
            a.execute("insert into voterlist values (%s,'%s')"%(roll,name))
            z.commit()
            sgp.destroy()
            vspl()
        except:
            messagebox.showerror('HELP','ALREADY VOTED')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def hp():
    global sgp,rn,nm,h
    sgp=Tk()
    sgp.title('ELECTION')
    sgp.iconbitmap('ballot_box__5Lx_icon.ico')
    wi, he = sgp.winfo_screenwidth(), sgp.winfo_screenheight()
    sgp.overrideredirect(0)
    sgp.geometry("%dx%d+0+0" % (wi, he))
    
    sgp.configure(bg='#923B8A')
    #sgp.resizable(False,False)
    rn=IntVar()
    nm=StringVar()
    h=StringVar()
    Label(sgp,text='VEDAVALLI VIDYALAYA RANIPET',bg='#923B8A',font='Broadway 20 bold').pack()
    Label(sgp,text='ELECTION ',bg='#923B8A',font='Broadway 18 bold').pack()
    Label(sgp,text=' ',bg='#923B8A').pack()
    #sgpl1=Label(sgp,text='CHECK IN PAGE',bg='#923B8A',font='Broadway 28 bold')
    #sgpl1.pack()

    Label(sgp,text=' ',bg='#923B8A').pack()

    l2=Label(sgp,text='ROLL NUMBER',bg='#923B8A',font='Consolas 15 bold')
    l2.pack()
    e1=Entry(sgp,textvariable=rn,font='Consolas 15 bold')
    e1.pack()

    l3=Label(sgp,text='NAME',bg='#923B8A',font='Consolas 15 bold')
    l3.pack()
    e2=Entry(sgp,textvariable=nm,font='Consolas 15 bold')
    e2.pack()

    Label(sgp,text='',bg='#923B8A').pack()
    
    rb1=Radiobutton(sgp,text='RABINDRANATH TAGORE',variable=h,value='rt',bg='#923B8A',font='Consolas 15 bold')
    rb1.pack(anchor=CENTER)
    
    rb2=Radiobutton(sgp,text='CHANDRASHEKHAR     ',variable=h,value='cs',bg='#923B8A',font='Consolas 15 bold')
    rb2.pack(anchor=CENTER)
        
    rb3=Radiobutton(sgp,text='C.V.RAMAN          ',variable=h,value='cvr',bg='#923B8A',font='Consolas 15 bold')
    rb3.pack(anchor=CENTER)
        
    rb4=Radiobutton(sgp,text='MOTHER TERESA      ',variable=h,value='mt',bg='#923B8A',font='Consolas 15 bold')
    rb4.pack(anchor=CENTER)

    Label(sgp,text=' ',bg='#923B8A').pack()

    b1=Button(sgp,text='SUBMIT',command=chs,font='Consolas 10 bold')
    b1.pack()

    Label(sgp,text=' ',bg='#923B8A').pack()

    b2=Button(sgp,text='RESULT',command=result,font='Consolas 10 bold')
    b2.pack()

    b3=Button(sgp,text=' NEW CANDIDATE ',command=new_can,font='Consolas 10 bold')
    b3.pack()

    sgp.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
hp()
