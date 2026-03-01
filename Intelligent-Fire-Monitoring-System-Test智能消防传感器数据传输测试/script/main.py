import tkinter  as t
from tkinter import messagebox
import requests
import json
import subprocess
import sys
import os
win=t.Tk()#创建窗体对象
win.title('登录')
win.geometry('400x300')#设置窗体大小

def loginname():
    getname = usesname1.get()
    getpass = password1.get()
    print(getname)
    print(getpass)
    r=requests.post("http://api.nlecloud.com/users/login",data={"Account":getname,"Password":getpass,"IsRememberMe":"true"})
    State = json.loads(r.text)["Status"]
    print(State)
    if State==0:
        t.messagebox.showinfo("欢迎进入","用户名密码正确")
        win.destroy()
        import getdata
    else:
        t.messagebox.showinfo("请重试","用户名密码错误")
def reset1():
    txtusesname1.delete(0,t,END)
    txtpassword1.delete(0,t,END)
def rem1():
    if txtusesname1.get() !="" and txtpassword1.get()!="":
        txtusesname1.delete(0,t,END)
        txtpassword1.delete(0, t, END)
    elif txtusesname1.get()=="" and txtpassword1.get()=="":
        txtusesname1.insert(0,"18174094129")
        txtpassword1.insert(0,"123456")
usesname=t.Label(text="用户名")#创建用户名
usesname.place(x=50,y=50,width=50,height=30)
password=t.Label(text="密  码")
password.place(x=50,y=100,width=50,height=30)
usesname1=t.Entry()
usesname1.place(x=100,y=50,width=200,height=30)
password1=t.Entry(show='*')
password1.place(x=100,y=100,width=200,height=30)
login=t.Button(text="登录",command=loginname)
login.place(x=50,y=200,width=50,height=30)
chongzhi=t.Button(text="重置")
chongzhi.place(x=160,y=200,width=50,height=30)
remember=t.Checkbutton(text="记住密码")
remember.place(x=270,y=200,width=100,height=30)
win.mainloop()