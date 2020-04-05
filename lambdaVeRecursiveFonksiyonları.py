def ucgenMi(a,b,hipotenus):
    if a**2+b**2==hipotenus**2:
        return True
    else:
        return False

#yukardaki fonksiyon lambda ile yazılabilir

ucgenKontrol=lambda a,b,hipotenus : a**2+b**2==hipotenus**2

#daha kolay ve basit bir şekide tanımlanabilir
#lambda fonksiyonları çok daha hızlı çalışır

print(ucgenKontrol(3,4,5))
print(ucgenMi(6,8,10))
print(ucgenKontrol(5,12,13))



#özyinelemeli(recoursive) fonksiyon örneği

def faktoriyel(sayi):
    if sayi==1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)
print(faktoriyel(5))
