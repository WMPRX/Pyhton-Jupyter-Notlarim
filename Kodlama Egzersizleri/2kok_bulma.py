""""
İkinci dereceden bilinmeyenli bir denklemin köklerini bulma

Denklem: ax^2 bx + c

Deltayı hesaplama: b ** 2 - 4 * a * c

Birinci kök: (-b - delta ** 0.5) / (2 * a)
İkinci kök: (-b + delta ** 0.5) / (2 * a)
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("birinci kök: {}\nikinci kök: {}\n".format(x1,x2))

