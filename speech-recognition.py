import speech_recognition as sr


def sesliKomut():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("komutlarını bekliyorum")
        audio = r.listen(source)

    try:
        said = str(r.recognize_google(audio))
        if (said.find("hi") != -1):
            print("hello")
        elif (said.find("who are you") != -1):
            print("i am your personel asistant")
    except:
        print("error")


while 1:
    sesliKomut()

