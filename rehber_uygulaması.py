rehber={"karakter1":{"ev adresi":"cumhuriyet caddesi no 10",
                     "iş adresi":"feridiye mahallesi no 15",
                     "ev telefonu":"021244400000",
                     "iş telefonu":"05300000000",
                     "cep telefonu":"05355555500"
                     }
        }
isimler=rehber.keys()
arananKisi=input("Aranan isim: ")
if arananKisi in isimler:
    flag=True
else:
    flag=False
arananOzellik=input("Aranan bilgi: ")
if flag:
    print(rehber.get(arananKisi).get(arananOzellik,"Bilgi bulunamadı"))
else:
    print("Aranılan kişi rehberde kayıtlı değil")

