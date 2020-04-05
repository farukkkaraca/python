import sqlite3

veriler=[("A","B"),
         ("C","D"),
         ("E","F"),
         ("G","H")]

db=sqlite3.connect("kutuphane.db") #yoksa kitaplar diye bir db oluşturur

imlec=db.cursor() #imlec oluşturur.Sql kodları imlec ile execute edilir

imlec.execute("CREATE TABLE if not exists kitaplar (yazar,kitap)") #tablo oluşturma

for veri in veriler:
    imlec.execute("INSERT INTO kitaplar VALUES (?,?)",veri)

db.commit() #değişikliğin commit edilmesi için kullanılır

imlec.execute("select * from kitaplar")
data=imlec.fetchall()  #tüm verileri çeker
print(data)

print(imlec.fetchone()) #tek veri yazdırır
print(imlec.fetchmany(5)) #kaç veri istersen o kadar yazdırır

imlec.execute("select * from kitaplar where yazar='A'") #yazar ismine göre sorgu
veri=imlec.fetchall()
print(veri)
db.close()

