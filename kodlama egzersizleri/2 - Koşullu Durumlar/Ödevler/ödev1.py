""""

Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

boy = float(input("Boyunuz: "))
kilo = int(input("Kilonuz"))

index = kilo / boy * boy

if index < 18.5:
    print("Zayıf")
elif index < 25:
    print(("Normal"))
elif index < 30:
    print("fazla kilolu")
elif index > 30:
    print("fazla kilolu")