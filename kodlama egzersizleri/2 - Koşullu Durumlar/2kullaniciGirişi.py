print("""***************
Kullanıcı Girişi
***************
""")

kullanıcı = "mehmet"
şifre = "12345"

sysKullanici = input("Kullanıcı adı giriniz: ")
sysSifre = input("Şifre giriniz: ")

if (kullanıcı == sysKullanici and şifre != sysSifre):
    print("Şife yanlış")
elif (kullanıcı != sysKullanici and şifre == sysSifre):
    print("Kullanıcı adı yanlış..")
elif (kullanıcı != sysKullanici and şifre != sysSifre):
    print("Kullanıcı adı ve şifre yanlış..")
else:
    print("Giriş başarılı..")