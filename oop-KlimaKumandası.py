class KlimaKumanda():
    def __init__(self,Durum="açık",Derece=20,Modlistesi=["sicak","soğuk","fan","nem"],Mod="sıcak",SW=0):
        print("Klima Kumandası aktif!")
        self.Durum=Durum
        self.Derece=Derece
        self.Modlistesi=Modlistesi
        self.Mod=Mod
        self.SW=SW

    def Derece_arttir_azalt(self):
        while 1:
            derece=input("+ ile dereceyi yükseltebilir, - ile düşürebilirsiniz.İşlemi bitirmek için q'ye basabilirsiniz.")
            if derece=="+":
                if self.Derece!=30:
                    self.Derece+=1
                    print("Sıcaklık değeri: ",self.Derece)
            elif derece=="-":
                if self.Derece!=0:
                    self.Derece-=1
                    print("Sıcaklık değeri",self.Derece)
            elif derece=="q":
                print("Derece güncellendi")
                break

    def Klima_ac_kapa(self):
        if self.Durum=="kapalı":
            self.Durum="açık"
            print("klima açılıyor")
        else:
            self.Durum="kapalı"
            print("klima kapanıyor")

    def __str__(self):
        return "Klima Durumu : {} \n Derece : {} \n Mod : {} \n SW : {} ".format(self.Durum,self.Derece,self.Mod,self.SW)
    def Modsec(self):
        print("Modunuz : ",self.Mod)
        if self.Mod=="sıcak":
            self.Mod=self.Modlistesi[1]
        elif self.Mod=="soğuk":
            self.Mod=self.Modlistesi[2]
        elif self.Mod=="fan":
            self.Mod=self.Modlistesi[3]
        else:
            self.Mod=self.Modlistesi[0]
        print("modunuz :",self.Mod)

    def SW_durum(self):
        self.SW+=1
        if(self.SW>4):
            self.SW=0
        print("Sw Durumu",self.SW)

kumanda=KlimaKumanda()
print("""
        ****KLİMA KUMANDASI*****
           
1-Aç-Kapa
2-Bilgileri Goster
3-Derece Değişikliği
4-Mod Değişikliği
5-SW Ayarı


""")
while 1:
    secim=int(input("Seçim Yapınız"))
    if secim==1:
        kumanda.Klima_ac_kapa()
    elif secim==2:
        print(kumanda)
    elif secim==3:
        if kumanda.Durum=="açık":
            kumanda.Derece_arttir_azalt()
        else:
            print("Kumanda kapalı")
    elif secim==4:
        if kumanda.Durum=="açık":
            kumanda.Modsec()
        else:
            print("Kumanda kapalı")

    elif secim==5:
        if kumanda.Durum=="açık":
            kumanda.SW_durum()
        else:
            print("Kumanda kapalı")
    else:
        print("Geçersiz Seçim")
        break

