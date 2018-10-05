import tkinter
from tkinter import *
from tkinter import ttk 
import pymysql
baglanti = pymysql.connect(
	host = 'host_adress',
    unix_socket = 'mysqld.sock_path', 
    user = 'your_user_name',
    passwd = 'your_user_pwd', 
    db = 'your_db_name'
   ,autocommit=True,
    charset='utf8')
cursor=baglanti.cursor()
def Listele():
	liste.delete(*liste.get_children())
	sorgu="SELECT *FROM employes ORDER BY customer_id DESC"
	cursor.execute(sorgu)
	result=cursor.fetchall()
	for item in result:
		liste.insert('',0,text=item[0],values=(item[1],item[2]))
def Goster(a):
	idno=liste.item(liste.selection()[0])['text']
	sorgu="SELECT *FROM employes WHERE customer_id=%s"
	cursor.execute(sorgu,idno)
	item=cursor.fetchone()
	Id.delete(0,END)
	Id.insert(0,item[0])
	ad.delete(0,END)
	ad.insert(0,item[1])
	combo.delete(0,END)
	combo.insert(0,item[2])
	
pencere=Tk()
pencere.geometry("500x500")


etiket=Label(pencere,text="Id").grid(row=1,column=1)
Id=Entry(pencere)
Id.grid(row=1,column=2)

etiket1=Label(pencere,text="Ad")
etiket1.grid(row=2,column=1)
ad=Entry(pencere)
ad.grid(row=2,column=2)

etiket2=Label(pencere,text="Tip")
etiket2.grid(row=3,column=1)
combo=ttk.Combobox(pencere,width=5)
combo['values']=("Patron","Yonetici","Mudür")
combo.grid(row=3,column=2)

liste=ttk.Treeview(pencere,height=15)
liste['columns']=("sut1","sut2")
liste.heading("#0",text="Id")
liste.heading("sut1",text="Ad")
liste.heading("sut2",text="Tip")
liste.grid(row=5,column=1,columnspan=3)
liste.bind('<ButtonRelease-1>',Goster)
Listele()
pencere.mainloop()