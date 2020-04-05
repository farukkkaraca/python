birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz","on"]
onlar=["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"]

def okunus(sayi):
    birler_basamagi=sayi%10
    onlar_basamagi=sayi//10
    yuzler_basamagi=sayi//100
    return birler[birler_basamagi]+onlar[onlar_basamagi]+birler[birler_basamagi]
print(okunus(59))

def pisagor(a,b):
    c=((a** 2) + (b ** 2))**0.5
    return c

print(pisagor(3,4))

class araba():
    model="huracan"
    renk="turuncu"
    beygir_gucu="1000"
    yakit_turu="elektrikli"
    silindir_sayisi="16"

lamborghini=araba()
print(lamborghini.model)
class parcalar():
    def __init__(self,adi,fiyati,seri_no,ozellikleri=""):  #özellikleri parametresine sabit deger (ön tanımlı değer) verildi
        self.parcanin_adi=adi
        self.parcanin_seri_nosu=seri_no
        self.parcanin_fiyati=fiyati
        self.parcanin_ozellikleri=ozellikleri


nvidia=parcalar(adi="geforce rtx 2080",fiyati="5000",seri_no="1111111",ozellikleri={"overclock","sıvı soğutmalı"})
amd=parcalar(adi="radeon 530",fiyati="4000",seri_no="222222")
print(nvidia.parcanin_ozellikleri)
print(amd.parcanin_ozellikleri)

class yazilimci():
    def __init__(self,isim,soyisim,no,maas,diller):
        self.yazilimcinin_ismi=isim
        self.yazilimcinin_soyismi=soyisim
        self.yazilimcinin_nosu=no
        self.yazilimcinin_maasi=maas
        self.yazilimcinin_bildigi_diller=diller

    def bilgileriGoster(self):
        print("""
                Çalışan Bilgileri:
                İsim:{}
                Soyisim:{}
                Numara:{}
                Maaş:{}
                Diller:{}
            
            """.format(self.yazilimcinin_ismi,self.yazilimcinin_soyismi,self.yazilimcinin_nosu,self.yazilimcinin_maasi,self.yazilimcinin_bildigi_diller))

    def dilEkle(self,dil):
        print("Dil Ekleniyor...")
        self.yazilimcinin_bildigi_diller.append(dil)

    def maasYukselt(self,maas):
        print("Maaş yükseltildi")
        self.yazilimcinin_maasi+=maas

yazilimci1=yazilimci("Faruk","Karaca","555555","13000",["python"])
yazilimci2=yazilimci("Fırat","Karaca","11111",19000,["python","c#"])


yazilimci2.maasYukselt(50)
yazilimci2.dilEkle("python")
yazilimci2.bilgileriGoster()






























