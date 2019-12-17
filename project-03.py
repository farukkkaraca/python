import speech_recognition as sr
from selenium import webdriver
import time

print(''' 
 
                        Hello! my friend
                        for calculate maximax say calculate 1
                        for calculate minimax say calculate 2
                        for calculate laplace say calculate 3
                        for calculate hurwicz say calculate 4
                        for calculate all say calculate all
                        for relaxing say open music please...

''')

a = [11, 29, 86,70,80,90]
b = [23, 45, 56,10,20,30]
c = [54, 69, 71,39,22,59]

x=0.4

print("\n")

print("1.seçenek",a)
print("2.seçenek",b)
print("3.seçenek",c)

print("\n")

def maximax():  #en büyüklerin en büyüğü
    max_deger = max(max(a), max(b), max(c))
    print("maximax değeri={}".format(max_deger))
    for i in a, b, c:
        if (max_deger in a):
            print("seçenek 1 seçilmeli\n")
            break
        elif (max_deger in b):
            print("seçenek 2 seçilmeli\n")
            break
        elif (max_deger in c):
            print("seçenek 3 seçilmeli\n")
            break

def minimax():  #en küçüklerin en büyüğü
    min_degerler=[]
    min_degerler.append(min(a))
    min_degerler.append(min(b))
    min_degerler.append(min(c))
    maximum=max(min_degerler)
    print("minimax değeri={}".format(maximum))
    for i in a,b,c:
        if (maximum in a):
            print("seçenek 1 seçilmeli\n")
            break
        elif(maximum in b):
            print("seçenek 2 seçilmeli\n")
            break
        elif (maximum in c):
            print("seçenek 3 seçilmeli\n")
            break
def laplace():  #satir ortalamalarinin en büyüğü
    ortalamalar=[]
    ort_a=float(sum(a)/len(a))
    ortalamalar.append(ort_a)
    ort_b=float(sum(b)/len(b))
    ortalamalar.append(ort_b)
    ort_c=float(sum(c)/len(c))
    ortalamalar.append(ort_c)
    laplace_degeri=max(ortalamalar)
    print("laplace değeri={}".format(laplace_degeri))
    if(laplace_degeri==ort_a):
        print("seçenek 1 seçilmeli\n")
    elif (laplace_degeri == ort_b):
        print("seçenek 2 seçilmeli\n")
    elif (laplace_degeri == ort_c):
        print("seçenek 3 seçilmeli\n")

def hurwicz():
    list=[]
    max_a=max(a)
    min_a=min(a)

    max_b=max(b)
    min_b=min(b)

    max_c=max(c)
    min_c=min(c)

    h_a=((max_a*x)+(min_a*(1-x)))
    h_b=((max_b*x)+min_b*(1-x))
    h_c=((max_c*x)+min_c*(1-x))

    list.append(h_a)
    list.append(h_b)
    list.append(h_c)

    maximum=max(list)
    print("hurwicz değeri={}".format(maximum))
    if(maximum==h_a):
        print("seçenek 1 seçilmeli\n")
    elif(maximum==h_b):
        print("seçenek 2 seçilmeli\n")
    elif(maximum==h_c):
        print("seçenek 3 seçilmeli\n")

def voiceCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("komutlarınızı bekliyorum")
        audio = r.listen(source)

    try:
        said = str(r.recognize_google(audio))
        if (said.find("calculate 1") != -1):
            maximax()
        elif (said.find("calculate 2") != -1):
            minimax()
        elif (said.find("calculate 3") != -1):
            laplace()
        elif (said.find("calculate 4") != -1):
            hurwicz()
        elif (said.find("calculate all") != -1):
            maximax()
            minimax()
            laplace()
            hurwicz()
        elif (said.find("open music") != -1):
            print("opening browser")
            browser = webdriver.Chrome()
            browser.get("https://www.youtube.com/watch?v=RxabLA7UQ9k")
            time.sleep(275)
            browser.close()




    except:
        print("sorry,i don't understand please talk again")


while 1:
    voiceCommands()
