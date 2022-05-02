print(""""******************

1 - Toplama İşlemi
2 - Çıkarma İşlemi
3 - Çarpma İşlemi
4 - Bölme İşlemi
******************""")

a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

işlem = input("İşlem giriniz: ")

if işlem == "1":
    print("{} {}'nin toplamı {}'dir".format(a,b,a + b))
elif işlem == "2":
    print("{} {}'nin kalanı {}'dir".format(a,b,a - b))
elif işlem == "3":
    print("{} {}'nin çarpımı {}'dir".format(a,b,a * b))
elif işlem == "4":
    print("{} {}'nin bölümü {}'dir".format(a,b,a / b))
else:
    print("Geçersiz işlem...")