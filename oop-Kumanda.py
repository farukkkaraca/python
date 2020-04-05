import time
import random
class kumanda():
    def __init__(self,tv_durum="kapali",tv_ses=0,kanal_listesi=["kanal1"],kanal="fox"):
        print=("kumanda oluşturuluyor...")
        time.sleep(3)
        self.tv_ses=tv_ses
        self.tv_durum=tv_durum
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def sesSeviyesi(self):
        while 1:
            karakter=input("sesi açmak için artıya(+) kısmak için eksiye(-)basın çıkmak için q'ya başın")
            if(karakter=="-"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("ses seviyesi",self.tv_ses)
            elif(karakter=="+"):
                if(self.tv_ses!=32):
                    self.tv_ses+=1
                    print("ses seviyesi", self.tv_ses)
            else:
                print("ses seviyesi güncellendi=",self.tv_ses)
                break
    def tvKapat(self):
        print("tv kapatılıyor...")
        time.sleep(3)
        self.tv_durum="KAPALI"
    def tvAc(self):
        print("tv açılıyor")
        time.sleep(3)
        self.tv_durum="AÇIK"
    def __str__(self):
        return "TV DURUM :{}\nSES :{}\nKANALLAR :{}\nŞUANKİKANAL :{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def rasgeleKanal(self):
        rasgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rasgele]
        print("kanal :",self.kanal)
    def kanalEkle(self,kanal):
        self.kanal_listesi.append(kanal)
kumanda=kumanda()
print("""
    *************************
    TELEVİZYON UYGULAMASI
    1.TELEVİZYONU AÇ
    2.TELEVİZYONU KAPAT
    3.TELEVİZYON BİLGİLERİ
    4.KANAL SAYISINI ÖĞRENME
    5.KANAL EKLE
    6.RASGELE KANKAL AÇ
    7.SES SEVİYESİ DEĞİŞTİR
    *************************
    """)
while 1:
    islem=input("işlem seçiniz : ")
    if(islem=="q"):
        print("KUMANDA KAPANIYOR")
        break
    if(islem=="1"):
        kumanda.tvAc()
    elif (islem == "2"):
        kumanda.tvKapat()
    elif (islem == "3"):
        print(kumanda)
    elif (islem == "4"):
        print("kanal sayısı: ",len(kumanda))
    elif (islem == "5"):
        kanallar=input("eklemek istediğiniz kanalların arasına virgül(,) koyarak giriniz...")
        eklenecekler=kanallar.split(",")#ekleneceklerin arasına , leri anlamak için
        for i in eklenecekler:
            kumanda.kanalEkle(i)
        print("BAŞARILI BİR ŞEKİLDE KANAL LİSTESİ GÜNCELLENDİ")
    elif (islem == "6"):
        kumanda.rasgeleKanal()
    elif (islem == "7"):
        kumanda.sesSeviyesi()
    else:
        print("GEÇERSİZ İŞLEM")
    
