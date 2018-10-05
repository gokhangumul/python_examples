def basamak(a):
	toplam=0
	while a>0:
		basamak=a%10
		toplam=toplam+basamak
		a=a/10
	return toplam
sayı=int(input("Bir sayı giriniz"))
print(int(basamak(sayı)))
		
