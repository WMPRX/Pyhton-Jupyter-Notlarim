print("""
*************************
Atm Makinesine Hoşgeldiniz..

1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme

Programdan çıkmak için 'q' ya basınız..
**************************
""")

bakiye = 1000

while True:
    işlem = input("İşlem Seçiniz: ")

    if (işlem == "q"):
        print("yine bekleriz..")
        break
    elif (işlem == "1"):
        print("bakiyeniz {} TL'dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Bakiye giriniz: "))
        bakiye += miktar
        bakiye -= miktar

    elif (işlem == "3"):
        miktar = int(input("Bakiye giriniz: "))

        if (bakiye - miktar < 0):
            print("Yetersiz bakiye..")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz işlem")