matris = [[21,34,49],
          [34,45,90],
          [11,23,38],
          [23,45,10]]

def maximax(x):#iyimserlik >>>her satırın en büyüğünün en büyüğü
    en_buyukler = []
    for i in x:
        s = 0
        for j in i:
            if s < j:
                s = j
        en_buyukler.append(s)
        k = en_buyukler[0]
    for i in en_buyukler:
        if k < i:
            k = i
    return k

def maximin(x):  #kötümserlik >>>her satırın en küçüğünün en büyüğü
    en_kucukler = []
    for i in x:
        s = 999999999999
        for j in i:
            if s > j:
                s = j
        en_kucukler.append(s)
        k = en_kucukler[0]
    for i in en_kucukler:
        if k < i:
            k = i
    return k

def minimax(x):#pişmanlık >>>her satırın en büyüğünün en küçüğü
    en_buyukler = []
    for i in x:
        s = 0
        for j in i:
            if s < j:
                s = j
        en_buyukler.append(s)
        k = 999999999
    for i in en_buyukler:
        if k > i:
            k = i
    return k

def laplace(x): #eşolasılık >>>her satırın ortalamasının en büyüğü
                
    ortalama = []
    for i in x:
        toplam=0
        for j in i:
            s = j /3
            toplam+=s
            ortalama.append(toplam)
        k =ortalama[0]
        for i in ortalama:
            if k < i:
                k= i
    return k

print("\n")
for i in matris:
    print(i)
print("\n")
print("Hesaplanan İyimserlik (maximax) degeri={}".format(maximax(matris)))
print("Hesaplanan kötümserlik (maximin) degeri={}".format(maximin(matris)))
print("Hesaplanan pişmanlık(minimax)değeri={}".format(minimax(matris)))
print("Hesaplanan eşolasılık(laplace) değeri={}".format(laplace(matris)))





