kitapListesi=list()
menu="""
   1-kitap ekle
   2-kitap çıkar
   3-kitapları listele
   0-çıkış
   
   """
def kitapEkle(kitap,liste):
    liste+=kitap
    print("kitap eklendi")
    input("ana menuye donmek için entere basın")
def kitapCikar():
    pass
def listele(liste):
    for i in liste:
        print(i)
    input("ana menuye donmek için entere basın")
def cik():
    quit()
while 1:
    print(menu)
    secim=input("secim yapiniz")
    if secim=="1":
        kitapAdi=input("kitap adi giriniz")
        kitapEkle(kitapAdi,kitapListesi)
    elif secim=="2":
        kitapCikar()
    elif secim=="3":
        listele(kitapListesi)
    elif secim== "q" or secim =="Q":
        cik()
    else:
        print("hatalı girdi")
        input("ana menuye donmek için entere basın")



