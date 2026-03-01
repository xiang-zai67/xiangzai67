import json
import tkinter  as t
import requests
win=t.Tk()#创建窗体对象
win.title('获取数据')
win.geometry('800x600')#设置窗体大小800x600
win.configure(bg="#87CEEB")
labtit=t.Label(text="智能消防监测报警系统",font=("Arial",15,"bold"),bg="#87CEEB",fg="#0000ff")
#labtit.place(x=300,y=50,width=250,height=50)
wd=t.Label(text='温度',bg="#87CEEB")
sd=t.Label(text='湿度',bg="#87CEEB")
o2=t.Label(text='氧气',bg="#87CEEB")
krqt=t.Label(text='可燃气体',bg="#87CEEB")
fire=t.Label(text='火焰',bg="#87CEEB")
smog=t.Label(text='烟雾',bg="#87CEEB")
txtwd=t.Entry()
txtsd=t.Entry()
txto2=t.Entry()
txtkrqt=t.Entry()
txtfire=t.Entry()
txtsmog=t.Entry()

def getdatam():
    txtwd.delete(0, t.END)
    txtsd.delete(0, t.END)
    txto2.delete(0, t.END)
    txtkrqt.delete(0, t.END)
    txtfire.delete(0, t.END)
    txtsmog.delete(0, t.END)
    r=requests.post("http://api.nlecloud.com/Users/Login",data={"Account": "18174094129", "Password": "123456", "IsRememberMe": "true"})
    token=json.loads(r.text)["ResultObj"]["AccessToken"]
    print(token)
    v=requests.get("http://api.nlecloud.com/devices/1268400/Sensors/m_oxygen",headers={"AccessToken":token})
    o2 = json.loads(v.text)["ResultObj"]["Value"]
    print(o2)
    txto2.insert(0,o2)
    v=requests.get("http://api.nlecloud.com/devices/1268400/Sensors/z_combustible",headers={"AccessToken":token})
    krqt= json.loads(v.text)["ResultObj"]["Value"]
    print()
    txtkrqt.insert(0,krqt)
    v=requests.get("http://api.nlecloud.com/devices/1268400/Sensors/z_humidity",headers={"AccessToken":token})
    sd = json.loads(v.text)["ResultObj"]["Value"]
    print(sd)
    txtsd.insert(0,sd)
    v=requests.get("http://api.nlecloud.com/devices/1268400/Sensors/z_temperature",headers={"AccessToken":token})
    wd = json.loads(v.text)["ResultObj"]["Value"]
    print(wd)
    txtwd.insert(0,wd)
    v=requests.get("http://api.nlecloud.com/devices/1268400/Sensors/m_fire",headers={"AccessToken":token})
    fire = json.loads(v.text)["ResultObj"]["Value"]
    print(fire)
    txtfire.insert(0,fire)
    v=requests.get("http://api.nlecloud.com/devices/1268400/Sensors/m_smoke",headers={"AccessToken":token})
    smog = json.loads(v.text)["ResultObj"]["Value"]
    print(smog)
    txtsmog.insert(0,smog)

btlogin=t.Button(text="获取",command=getdatam)
btlogin.place(relx=0.8,rely=0.8,width=50,height=30)
#设置文本框，创建按钮
labtit.place(relx=0.3,rely=0.1,width=300,height=50)#设置标签长宽高
wd.place(relx=0.1,rely=0.2,width=80,height=30)
sd.place(relx=0.1,rely=0.3,width=80,height=30)
o2.place(relx=0.1,rely=0.4,width=80,height=30)
krqt.place(relx=0.1,rely=0.5,width=80,height=30)
fire.place(relx=0.6,rely=0.2,width=80,height=30)
smog.place(relx=0.6,rely=0.3,width=80,height=30)
#设置文本框位置和大小
txtwd.place(relx=0.2,rely=0.2,width=200,height=30)
txtsd.place(relx=0.2,rely=0.3,width=200,height=30)
txto2.place(relx=0.2,rely=0.4,width=200,height=30)
txtkrqt.place(relx=0.2,rely=0.5,width=200,height=30)
txtfire.place(relx=0.7,rely=0.2,width=200,height=30)
txtsmog.place(relx=0.7,rely=0.3,width=200,height=30)


win.mainloop()