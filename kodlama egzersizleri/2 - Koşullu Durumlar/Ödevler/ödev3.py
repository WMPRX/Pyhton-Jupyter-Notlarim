# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

vize1 = int(input("Vize1 Notunuz: "))
vize2 = int(input("Vize 2 Notunuz: "))
vize3 = int(input("Vize 3 notunuz: "))

toplam1 = vize1 * 0.30
toplam2 = vize2 * 0.30
toplam3 = vize3 * 0.40

toplam = toplam1 + toplam2 + toplam3

if (toplam >= 90):
    print("AA")
elif (toplam >=85):
    print("BA")
elif (toplam >= 80):
    print("BB")
elif (toplam >= 75):
    print("CB")
elif (toplam >= 70):
    print("CC")
elif (toplam >= 65):
    print("DC")
elif (toplam >= 60):
    print("DD")
elif (toplam >= 55):
    print("FD")
else:
    print("Kaldınız...")
