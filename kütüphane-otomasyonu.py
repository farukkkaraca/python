import os
kitapListe=list()
menu="""
  1-kitap ekle
  2-kitap al
  3-tümünü listele
  4-çıkış
  
"""
kitap=("İnce Memed","Yaşar Kemal")


def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("kitap eklendi")
    print("Ana menuye donmek için entera basın")
    input()
def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False
def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("kitap çıkartma işlemi tamamlandı")
        input("ana manuye donmek için enterlayın")
    else:
        print("kitap mevcut değil")
        input("ana manuye donmek için enterlayın")
def listele(liste:list):
    for i in liste:
        print("Kitap adı:{}------>>> Yazar: {}".format(i[0],i[1]))


while 1:
    os.system("cls")  #terminal ekranını temizler
    print(menu)
    secim=input("işleminizi seçiniz")
    if secim=="1":
        kitap_adi=input("kitabın adını giriniz")
        kitap_yazar=input("yazarın adını giriniz")
        kitap=(kitap_adi,kitap_yazar)
        kitapEkle(kitap,kitapListe)

    elif secim=="2":
        kitap_adi = input("kitabın adını giriniz")
        kitap_yazar = input("yazarın adını giriniz")
        kitap = (kitap_adi, kitap_yazar)
        kitapCikar(kitap,kitapListe)
    elif secim=="3":
        listele(kitapListe)
    elif secim=="q" or secim=="Q":
        print("keyifli okumalar")
        quit()
    else:
        print("hatali giriş yaptınız")



