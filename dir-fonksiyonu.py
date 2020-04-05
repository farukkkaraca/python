liste=["deneme1","deneme2"]
# dir() fonksiyonu bir tanımın fonksiyonlarını görüntülemek içindir
# örneğin bir liste için kullanılabilecek fonksiyonları görüntüleyelim
for i in dir(liste):
    print(i)

#string ifadelerin fonksiyonları için
string=""
for i in dir(string):
    print(i)

#demet fonksiyonları için
demet=tuple()
for i in dir(demet):
    print(i)

#bu şekilde istediğiniz veri yapısının fonksiyonlarına ulaşabilirsiniz



