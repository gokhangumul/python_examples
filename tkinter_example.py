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
	if Id.get():
		sorgu="SELECT *FROM employes WHERE customer_id =%s"
		value=(Id.get())
		cursor.execute(sorgu,value)
		result=cursor.fetchone()
		Adi.delete(0,END)
		Adi.insert(0,result[1])
		combo.delete(0,END)
		combo.insert(0,result[2])
	else:
		Label(AraPencere,text="Id boş geçme")
def Guncelle():
	if Id.get():
		sorgu="UPDATE employes SET first_name=%s,type_name=%s WHERE customer_id=%s"
		degerler=(Adi.get(),combo.get(),Id.get())
		cursor.execute(sorgu,degerler)
		Label(GuncelPencere,text="Güncelleme başarılı bir şekilde gerçekleştirilmiştir").grid(row=4,column=2)
def Listele():
	liste.delete(*liste.get_children())
	sorgu="SELECT *FROM employes ORDER BY customer_id DESC"
	cursor.execute(sorgu)
	result=cursor.fetchall()
	for item in result:
		liste.insert('',0,text=item[0],values=(item[1],item[2]))


AraPencere=Tk()
GuncelPencere=Tk()

title=AraPencere.title("Ara")
AraPencere.geometry("500x500")
etiket=Label(AraPencere,text="Id:")
etiket.grid(row=1,column=1)

Id=Entry(AraPencere)
Id.grid(row=1,column=2)
AraButton=Button(AraPencere,text="Ara",command=Getir)
AraButton.grid(row=3,column=2)

liste=ttk.Treeview(AraPencere,height=10,column=0)
liste["columns"]=("sut1","sut2")
liste.heading("#0",text="Id")
liste.heading("sut1",text="Ad")
liste.heading("sut2",text="Tip")
liste.grid(row=5,column=1,columnspan=3)
liste.bind('<ButtonRelease-1>',"")
Listele()

title=GuncelPencere.title("Güncelle")
GuncelPencere.geometry("300x300")

Ad=Label(GuncelPencere,text="Adı:")
Ad.grid(row=1,column=1)
Adi=Entry(GuncelPencere)
Adi.grid(row=1,column=2)
Tip=Label(GuncelPencere,text="Şehir:")
Tip.grid(row=2,column=1)
combo=ttk.Combobox(GuncelPencere,width=5)
combo['values']=("Patron","Yonetici","Mudür")
combo.grid(row=2,column=2)
GuncelleButton=Button(GuncelPencere,text="Güncelle",command=Guncelle)
GuncelleButton.grid(row=3,column=2)

AraPencere.mainloop()
