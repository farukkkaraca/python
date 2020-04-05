sayi=5
sayi1=3.3
print(sayi.bit_length()) #sayinin kaç bitte yazialabildigini gosterir
print(sayi1.as_integer_ratio()) #float sayinin hangi en yakın sayilarin birbirine bölümü
#olduğunu göstermek için kullanılır

karmasik_sayi=12+4j #karmasik sayilar icin
print(karmasik_sayi.imag) #imag ve real class icindeki birer degiskendir metot degildirler
print(karmasik_sayi.real)

print(abs(-3)) #mutlak deger alır
print(max(23,33))  #max döndürür
print(min(23,33))   #min döndürür
print(divmod(30,3)) #bölüm ve kalan verir
liste=[2,5,35,5323,33]
print(sum(liste))  #liste elemanlarını toplar