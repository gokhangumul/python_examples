import pymysql
baglanti = pymysql.connect(host = '', unix_socket = '', user = '', passwd = '', db = '',autocommit=True, charset='utf8')
cursor = baglanti.cursor()

while True:
	print("""
	Veritabanında yer alan kayıtları listelemek için 1'e basınız..
	Veritabanına kayıt eklemek için 2'ye basınız..
	Veritabanından where ile kayıt listelemek için 3'e basınız..
	Veritabından kayıt silmek için 4'e basınız..
	Veritabanında güncelleme yapmak için 5'e basınız..
	Çıkış için q'ya basınız...
	""")
	seçim=input("Hangi işlemi yapmak istersiniz..")
	if seçim=="1":
		sorgu="SELECT *FROM calısan"
		cursor.execute(sorgu)
		sonuc=cursor.fetchall()
		for i in sonuc:
			print(*i)
	if seçim=="2":
		ad=input("Çalışan adını giriniz:")
		adres=input("Çalışanın adresini giriniz:")
		sorgu="INSERT INTO calısan (name, address) VALUES (%s, %s)"
		values=(ad,adres)
		cursor.execute(sorgu,values)
	if seçim=="3":
		adr=input("Adres?")
		sorgu="SELECT *FROM calısan WHERE address=%s"
		cursor.execute(sorgu,adr)
		sonuc=cursor.fetchall()
		for i in sonuc:
			print(*i)

	if seçim=="4":
		deger=input("İsim ile silme yapacaksanız 1'e adres ile silme yapacaksanız 2'ye basınız\n")
		if deger=="1":
			isim=input("İsmi giriniz..")
			sorgu="DELETE FROM calısan WHERE name=%s"
			cursor.execute(sorgu,isim)
		if deger=="2":
			adr=input("Adres giriniz..\n")
			sorgu="DELETE FROM calısan WHERE address=%s"
			cursor.execute(sorgu,adr)
	if seçim=="5":
		deger=input("Adresi güncellemek için 1'e adı güncellemek için 2'ye basınız\n")
		if deger=="1":
			adres=input("Güncellemek istediğiniz adresi giriniz...\n")
			adres1=input("Güncel adresi giriniz...\n")
			sorgu="UPDATE calısan SET address=%s WHERE address=%s"
			val=(adres1,adres)
			cursor.execute(sorgu,val)
		if deger=="2":
			isim=input("Güncellemek istediğiniz kişinin adını yazınız..\n")
			isim1=input("Güncel ismi yazınız..\n")
			sorgu="UPDATE calısan SET name=%s where name=%s"
			val=(isim1,isim)
			cursor.execute(sorgu,val)
	if str(seçim)=="q":
		quit()
