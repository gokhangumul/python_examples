import tkinter
from tkinter import *
from tkinter import ttk 
import pymysql
baglanti = pymysql.connect(
	host = 'host_adress',
    unix_socket = 'mysqld.sock_patch', 
    user = 'your_user_name',
    passwd = 'your_user_pwd', 
    db = 'your_db_name'
   ,autocommit=True,
    charset='utf8')
cursor=baglanti.cursor()
def Ekle():
	sorgu="INSERT INTO calısan (name, address) VALUES (%s,%s)"
	deger=(adi.get(),combo.get())
	cursor.execute(sorgu,deger)
	Liste()
def Liste():
	liste.delete(*liste.get_children())
	sorgu="SELECT *FROM calısan ORDER BY name DESC"
	cursor.execute(sorgu)
	sonuc=cursor.fetchall()
	for item in sonuc:
		liste.insert('',0,text=item[0],values=(item[1]))

nesne=Tk()
Label(nesne,text="Adı:   ").grid(row=1,column=1)
adi=Entry(nesne)
adi.grid(row=1,column=2)

Label(nesne,text="Şehir:").grid(row=2,column=1)
combo=ttk.Combobox(nesne,width="15")
combo['values']=("Manisa","İzmir","Hatay")
combo.current(0)
combo.grid(row=2,column=2)

btn=Button(nesne,text="Ekle",command=Ekle)
btn.grid(row=3,column=2)


nesne1=Tk()
liste=ttk.Treeview(nesne1,height=10,column=0)
liste['columns']=("sut1")
liste.grid(row=5,column=1,columnspan=3)
liste.heading("#0",text="Adı")
liste.heading("sut1",text="Şehir")
liste.bind('<ButtonRelease-1>',"")
Liste()
nesne.mainloop()