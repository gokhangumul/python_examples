def astop(a):
	sayac=0
	toplam=0
	asal=0
	for i in range(1,a+1):
		if a%i==0:
			sayac=sayac+1
	if sayac<=2:
		asal=asal+1
		toplam=toplam+a
	print(toplam,asal)

while True:
	sayı=int(input("sayı giriniz:"))
	if sayı!=0:
		astop(sayı)
	else:
		break

