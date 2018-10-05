import tkinter
from tkinter import *
from tkinter import ttk 
import pymysql
baglanti = pymysql.connect(
	host = 'host_adress',
    unix_socket = 'mysqld.sock_path', 
    user = 'your_username',
    passwd = 'your_pwd', 
    db = 'your_db_name'
   ,autocommit=True,
    charset='utf8')
cursor=baglanti.cursor()
def getir(a):
	adres=a
	sorgu="SELECT *FROM calısan WHERE address=%s"
	cursor.execute(sorgu,adres)
	sonuc=cursor.fetchall()
	i=1
	for item in sonuc:
		Label(nesne1,text="Adı-Şehir").grid(row=i,column=0)
		ad=Entry(nesne1,textvariable=StringVar(nesne1,value=item[0]))
		ad.grid(row=i,column=1)
		combo=ttk.Combobox(nesne1,width="15")
		combo['values']=("Manisa","İzmir","Hatay")
		combo.current(0)
		combo.grid(row=i,column=2)
		i=i+1

def guncelle(a,b):
	ad=a
	sehir=b
	sql="UPDATE calısan SET name='%s',address='%s' WHERE address='%s' "
	values=(a,b,b)
	cursor.execute(sql,values)
nesne=Tk()
nesne.title("SEARCH")
nesne.geometry("200x200")
Label(nesne,text="Id:").grid(row=1,column=1)
adi=Entry(nesne)
adi.grid(row=1,column=2)
button1 = Button(nesne, text="ARA", command=lambda: getir(adi.get()))
button1.grid(row=3,column=2)


nesne1=Tk()
nesne1.title("Detail")
nesne1.geometry("400x400")
btn2=Button(nesne1,text="Güncelle",command=lambda: guncelle(ad.get(),combo.get()))
btn2.grid(row=3,column=1)


nesne.mainloop()
nesne1.mainloop()