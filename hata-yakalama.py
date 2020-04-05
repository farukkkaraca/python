import datetime

#hata yakalama

try:
    a=int(input("2.sayiyi giriniz"))
    b=int(input("1.sayiyi giriniz"))
    print(a/b)
except ValueError:
    print("lütfen sayi giriniz,metin değil!")
except ZeroDivisionError:
    print("tam sayilari 0 a bölemezsiniz")

#except(ZeroDivisionError,ValueError):  #farklı hataları aynı yakalayıcıda yakalamak için
    #print("lütfen sayilari doğru girin")

finally:
    print("*************")
list=["345","seda","32a4","14","kemal"]  #listenin içinden sadece int değerleri almak için
for i in list:
    try:
        i=int(i)
        print(i)
    except:
        pass
list1=[1,2,45,66,7,33,65,76,67,]

def ciftMi(x):   
    if(x%2==0):
        return x
    else:
        raise ValueError
for i in list1:
    try:
        print(ciftMi(i))
    except ValueError:
        pass














