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
def Getir():
	if adi.get():
		sorgu="SELECT *FROM calısan WHERE name=%s"
		values=adi.get()
		cursor.execute(sorgu,values)
		sonuc=cursor.fetchone()
		adi1.delete(0,END)
		adi1.insert(0,sonuc[1])
	else:
		Label(pencere,text="AD BOŞ").grid(row=3,column=2)
def Guncelle():
	if adi1.get():
		sorgu="UPDATE calısan SET address=%s WHERE address=%s"
		degerler=(adi1.get(),adi1.get())
		cursor.execute(sorgu,degerler)
	else:
		Label(pencere,text="AD BOŞ").grid(row=4,column=2)
def Listele():
	liste.delete(*liste.get_children())
	sorgu="SELECT *FROM calısan ORDER BY address DESC"
	cursor.execute(sorgu)
	sonuc=cursor.fetchall()
	for item in sonuc:
		liste.insert('',0,text=item[0],values=(item[1]))
def Sil():
	sorgu="DELETE FROM calısan WHERE address=%s"
	deger=adi1.get()
	cursor.execute(sorgu,deger)
def Goster(event):
	adr=liste.item(liste.selection()[0])['text']
	sql="SELECT *FROM calısan where address=%s"
	cursor.execute(sql,adr)
	sonuc=cursor.fetchone()
	adi1.delete(0,END)
	adi1.insert(sonuc[0])
	address1.delete(0,END)
	address1.insert(sonuc[1])
pencere=Tk()
pencere1=Tk()
pencere1.title("Gelen Kayıt")
pencere1.geometry("200x200")
baslik=pencere.title("Arama")
pencere.geometry("200x200")
name=Label(pencere,text="Adınız:")
name.grid(row=1,column=1)

adi=Entry(pencere)
adi.grid(row=1,column=2)

adi1=Entry(pencere1)
adi1.grid(row=1,column=2)

address1=Entry(pencere1)
address1.grid(row=2,column=2)

button1=Button(pencere,text="Ara",command=Getir)
button1.grid(row=3, column=2)

button2=Button(pencere1,text="Guncelle",command=Guncelle)
button2.grid(row=3,column=2)

button3=Button(pencere1,text="Sil",command=Sil)
button3.grid(row=3,column=3)

liste=ttk.Treeview(pencere1,height=10,column=0)
liste['columns']=("sut1")
liste.grid(row=5,column=1,columnspan=3)
liste.heading("#0",text="Adı")
liste.heading("sut1",text="Şehir")
liste.bind('<ButtonRelease-1>',Goster)
Listele()
pencere.mainloop()
pencere1.mainloop()