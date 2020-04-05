class Musteri():
    def __init__(self,ID,ISIM,PAROLA):
        self.isim=ISIM
        self.id=ID
        self.parola=PAROLA
        self.bakiye=0

class Banka():
    def __init__(self):
        self.musteriler=list()
    def musteri_ol(self,ID:str,PAROLA:str,ISIM:str):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("kayıt yapıldı")

def main():
    banka=Banka()
    while True:
        print("""
                1-Banka Müşterisiyim
                2-Banka Müşterisi Olmak İstiyorum
                """)
        secim=input("Seçiminiz")
        if secim=="1":
            ids=[i.id for i in banka.musteriler]
            ID=input("ID: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID==musteri.id:
                        print("Hoşgeldiniz {}".format(musteri.isim))
                        parola=input("Parolanız: ")
                        if parola==musteri.parola:
                            print("Giriş Başarılı!!")
                            while True:
                                print("""
                                            1-Bakiye Sorgula
                                            2-Para Yatır (havale)
                                            3-Para Yatır (eft)
                                            4-Para Çek            
                                                       
                                                        """)
                                secim2 = input("İşleminin>:")
                                if secim2 == "1":
                                    print("Bakiyeniz: {}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için 'enter' e basın")

                                elif secim2 == "2":

                                    miktar=int(input("Miktar: "))
                                    onay=input("Kendi hesabınıza {} TL para yatırma işlemini onaylıyor musunuz?:E\H\n".format(miktar))
                                    if onay=="E" or onay=="e":
                                        musteri.bakiye+=miktar
                                        print("Paranız Yatırıldı")
                                    elif onay=="H" or onay=="h":
                                        print("İşlem iptal edildi")
                                    else:
                                        print("Hatalı girildi işlem iptal")

                                elif secim2=="3":

                                    arananID=input("Müşteri ID:")
                                    if arananID in ids:
                                        for digerMusteri in banka.musteriler:
                                            if arananID==digerMusteri.id:
                                                miktar=int(input("Miktar: "))
                                                if miktar<=musteri.bakiye:
                                                    onay = input("{} adlı müşteriye {} Tl para yatırma işlemini onaylıyor musunuz? E\H\n".format(digerMusteri.isim,miktar))
                                                    if onay == "e" or onay == "E":
                                                        digerMusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                    elif onay == "h" or onay == "H":
                                                        print("İşlem iptal edildi")
                                                        input("Ana menüye dönmek için 'enter'e basın!")
                                                    else:
                                                        print("Hatalı giriş işlem iptal!")
                                                        input("Ana menüye dönmek için 'enter'e basın!")
                                                else:
                                                    print("Bakiyeniz bu işlem için yetersiz!")
                                                    input("Ana menüye dönmek için 'enter'e basın!")

                                    else:
                                        print("Müşteri Bulunamadı")
                                        input("Ana menüye dönmek için 'enter'e basın!")

                                elif secim2=="4":

                                    miktar=int(input("Miktar:"))
                                    if miktar<=musteri.bakiye:
                                        musteri.bakiye-=miktar
                                        print("İşlem tamamlandı, paranızı alınız!")
                                        input("Ana menüye dönmek için 'enter'e basın!")
                                    elif miktar=="0":
                                        print("Yanlış miktar girdiniz!")
                                        input("Ana menüye dönmek için 'enter'e basın!")
                                    else:
                                        print("Bakiyeniz bu işlem için yetersiz!")
                                        input("Ana menüye dönmek için 'enter'e basın!")

                                elif secim2=="q" or secim2=="Q":
                                    break
                        else:
                            print("Parola Yanlış Girildi")
                            input("Ana menüye dönmek için 'enter'e basın!")

            else:
                print("id bulunamadı!,Tekrar deneyin!")
        elif secim=="2":
            ID=input("Id:")
            ISIM=input("İsminiz: ")
            PAROLA=input("Parola: ")
            banka.musteri_ol(ID,ISIM,PAROLA)

if __name__ == '__main__':
    main()


