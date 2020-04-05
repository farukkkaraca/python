import os
masalar=dict()

for i in range(10):
    masalar[i]=0

def hesapEkle():
    masaNo=int(input("Masa No:"))
    gecerli=masalar[masaNo]
    eklenecek=float(input("Eklenecek ücret :"))
    toplam=gecerli+eklenecek
    masalar[masaNo]=toplam

def hesapSil():
    masaNo=int(input("Masa No:"))
    gecerli=masalar[masaNo]
    eksilecek = float(input("Eksilecek ücret :"))
    toplam = gecerli - eksilecek
    if toplam<0:
        print("işlemde hata var tekrar deneyin")
    else:
        masalar[masaNo] = toplam

def hesapKontrol(dosya_adi):
    try:
        dosya=open(dosya_adi)
        veriler=dosya.read()
        veriler=veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag=True
    except FileNotFoundError:
        dosya=open(dosya_adi,"w")
        dosya.close()
        print("kayıt dosyası oluşturuldu")
        flag=False
    if flag:
        for i in enumerate(veriler):
            masalar[i[0]]=float(i[1])
    else:
        pass
def kayitGuncelle():
    dosya=open("kayitlar.txt","w")
    for i in range(10):
        ucret=masalar[i]
        ucret=str(ucret)
        dosya.write(ucret +"\n")
    dosya.close()

def main():
    hesapKontrol("kayitlar.txt")
    while True:
        os.system("cls")
        print("""
              1-Masaları Görüntüle
              2-Hesap Ekle
              3-Hesap Sil
              Q-Çıkış


              """)
        secim = input("İşleminiz")
        if secim == "1":
            for i in range(10):
                print("Masa {} için hesap={}".format(i, masalar[i]))
            input("İşlem tamamlandı.Ana menüye dönmek için enterlayın")

        elif secim == "2":
            hesapEkle()
            kayitGuncelle()
        elif secim == "3":
            hesapSil()
        elif secim == "q" or secim == "Q":
            print("Çıkılıyor...")
            quit()


main()