print(""""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullanıcıAdı = "mehmet"
sys_sifre = "1234"
giris_hakki = 3

while True:
    kullanıcıAdı= input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")
    if (sys_kullanıcıAdı == kullanıcıAdı and sys_sifre != sifre):
        print("Şifre yanlış..")
        giris_hakki -= 1
    elif (sys_kullanıcıAdı != kullanıcıAdı and sys_sifre == sifre):
        print("Kullanıcı adı yanlış..")
        giris_hakki -= 1
    elif (sys_kullanıcıAdı != kullanıcıAdı and sys_sifre != sifre):
        print("Kullanıcı adı ve şifre yanlış..")
        giris_hakki -= 1
    else:
        print("Giriş başarılı..")
        break
    if (giris_hakki == 0):
        break