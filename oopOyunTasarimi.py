import random
class Dusman():
    def __init__(self):
        self.sagmi=True
        self.saglik=random.randint(30,70)
        self.kalkan=random.randint(0,10)
        self.guc=random.randint(20,50)

    def vur(self,player):
        damage=self.guc-player.kalkan
        player.saglik-=damage
        if player.saglik<=0:
            player.sagmi=False


class Player():
    def __init__(self):
        self.sagmi=True
        self.saglik=500
        self.kalkan=20
        self.guc=55

    def vur(self,dusman):
        damage=self.guc-dusman.kalkan
        dusman.saglik-=damage
        if dusman.saglik<=0:
            dusman.sagmi=False
            dusmanlar.remove(dusman)

dusmanlar=list()
for i in range(10):
    dusmanlar.append(Dusman())
player=Player()

while True:
    print("Player Durumu ---> Sağlık: {} ---- Güç:{} ---- Kalkan:{}".format(player.saglik,player.guc,player.kalkan))
    print()
    if player.sagmi==False:
        print("Game Over :(((")
        quit()
    if not dusmanlar:
        print("Tebrikler kazandınız")
    for i in dusmanlar:
        print("{}. Düşman ---> Sağlık: {} ---- Güç: {} ---- Kalkan: {}".format(dusmanlar.index(i),i.saglik,i.guc,i.kalkan))

    secim=int(input("Düşman Seçiniz:"))
    dusman=dusmanlar[secim]
    player.vur(dusman)
    if dusmanlar:
        saldiran=dusmanlar[random.randint(0,len(dusmanlar)-1)]
        saldiran.vur(player)
        print("{} canınız azaldı".format(saldiran.guc-player.kalkan))





