import sqlite3
db=sqlite3.connect("kutuphane.db")
imlec=db.cursor()

menu="""
    [1] Kitap Ara
    [2] Yazar Ara
"""

print(menu)
islem=input("İşleminiz: ")
if islem=="1":
    isim=input("Kitap Adı:")
    sorgu=("select * from kitaplar where kitap='{}'".format(isim))
    imlec.execute(sorgu)
    veriler=imlec.fetchall()
    for veri in veriler:
        print(veri)
elif islem=="2":
    yazar=input("Yazar Adı Giriniz: ")
    sorgu=("select * from kitaplar where yazar='{}'".format(yazar))
    imlec.execute(sorgu)
    veriler=imlec.fetchall()
    for veri in veriler:
        print(veri)
else:
    print("Yanlış Seçim!")

db.close()