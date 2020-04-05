import datetime
#dosya okuma ve yazdırma işlemleri
file=open("Bilgiler.txt","a",encoding="utf-8")  #türkçe karakter sorunu düzeltmek için utf-8 kullanılır // w tüm dosyaya a sadece imlece ulaşır
file.write("Faruk Karaca\n")
file.close()
file1=open("C:/Users/karaca/Desktop/deneme.txt","w")
file1.close()

try:
    myfile = open("C:/Users/karaca/Desktop/deneme.txt", "r",encoding="utf-8")
    icerik=myfile.read()
    print(icerik)
    print(myfile.readline())

except:
    print("dosya bulunamadı")

try:
    with open("C:/Users/karaca/Desktop/deneme.txt", "r",encoding="utf-8") as file:  #dosya ile işlem bittikten sonra dosyanın otomatik kapanması için with kullanılır
        for i in file:
            print(i)
except FileNotFoundError:
    print("dosya bulunamadı")

def okuma(z):
    try:
        file=open(z+".txt","r")
        for i in file:
            print(i,end="")
    except FileNotFoundError:
        print("böyle bir kayıt bulunamadı")

    finally:
        AnaProgram()
def yazma(z):
    zaman=datetime.datetime.now().strftime("%d-%m-%y")
    file=open(zaman+".txt", "a")
    file.write(z+"\n")
def AnaProgram():
    x = input("Okumak için 1 yazmak için 2 yazın")

    if x=="1":
        gun=input("lütfen günü giriniz")
        okuma(gun)
    elif x=="2":
        while 1:
            gunluk=input("Günlüğe yazınız :")
            if gunluk=="+":
                AnaProgram()
            yazma(gunluk)
    elif x==3:
         pass

    else:
        print("hatalı seçim")
AnaProgram()