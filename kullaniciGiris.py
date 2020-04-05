kullanicilar={"faruk":"12345",
              "karaca":"67890"}
isimler=kullanicilar.keys()
kull_adi=input("Kullanıcı Adınız:")

if kull_adi in isimler:
    print("hoşgeldiniz {}".format(kull_adi))
    parola=input("Parolanız: ")
    if parola==kullanicilar[kull_adi]:
        print("Sisteme giriş yapıldı")
    else:
        print("parola hatalı")
else:
    print("Böyle bir kullanıcı yok")
