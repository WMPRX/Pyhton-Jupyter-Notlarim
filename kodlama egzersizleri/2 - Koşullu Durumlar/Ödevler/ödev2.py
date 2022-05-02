# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

sayı1 = int(input("1. Sayı: "))
sayı2 = int(input("2. Sayı: "))
sayı3 = int(input("3. Sayı: "))

if (sayı1 >= sayı2 and sayı1 >= sayı3):
    print("En büyük sayı:",sayı1)
elif (sayı2 >= sayı1 and sayı2 >= sayı3):
    print("En büyük sayı:",sayı2)
elif (sayı3 >= sayı1 and sayı3 >= sayı1):
    print("En büyük sayı:",sayı3)