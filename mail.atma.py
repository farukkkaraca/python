import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
#denemeler yapıldı sorunsuz çalışıyor
try:
    myfile = open("mail_listesi.txt", "r", encoding="utf-8")
    mail_listesi = myfile.readlines()
except FileNotFoundError:
    print("dosya bulunamadı")

class MailAtma():
    def __init__(self,kimden="mail kimden gidecek",mailler=mail_listesi,konu="deneme",mesaj_icerigi=""):

        self.kimden=kimden
        self.mailler=mailler
        self.konu=konu
        self.mesaj_icerigi=mesaj_icerigi

    def bilgiler(self):
        print(self.mailler)

    def mail_atma(self):

        mail_dizisi=[]
        mail_dizisi.append(self.mailler)
        mesaj = MIMEMultipart()
        mesaj["From"] = self.kimden
        mesaj["Subject"] = self.konu
        self.icerik = "mesajın içeriğini buraya yaz"

        mesaj_govdesi = MIMEText(self.icerik, "plain")
        mesaj.attach(mesaj_govdesi)
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("mail adresi","mail şifresi")
            for i in mail_dizisi:
                for mail_adresi in i:
                    mail.sendmail(mesaj["From"],mail_adresi,mesaj.as_string())
                    print("Mail Gönderildi! Mail atılan adres: {}".format(mail_adresi))

            mail.close()
        except:
            sys.stderr.write("Bir sorun oluştu")
            sys.stderr.flush()

mail=MailAtma()
mail.mail_atma()



