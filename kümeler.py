kume3=set() #set sınıfı kullanılıyor
#küme içinde liste demet ve sözlük string kullanılabilir ama (int)sayısal değerler kullanılamaz

kume3={"deneme","deneme2","deneme3"} #sözlük gibi karşılığı yoktur bu şekilde tanımlanır

kume=set([1,2,3,4]) #küme içerisine liste tanımlama örneği

kume.add("deneme") #eleman ekler
kume.discard(3) #eleman varsa çıkartır yoksa yoluna devam eder
kume.remove(1)  #eleman varsa çıkartır yoksa hata verir

a=set([1,2,3,4,5])
b=set([4,5,6,7])

print(a)
print(b)
print(25*"=")
print(a.difference(b)) #a nın b den farkı
print(b.difference_update(a)) #b a dan farkına eşitlenir

print(a.intersection(b)) #kesişim kümesi
