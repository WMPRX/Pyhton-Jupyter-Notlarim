# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

a = int(input("yıl: "))
b = int(input("gün"))
c = int(input("tarih: "))

toplam = a * b * c

print("{} + {} + {} = {} ' dir".format(a,b,c,toplam))

