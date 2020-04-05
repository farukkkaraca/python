from PyQt5 import QtWidgets
import sys
import sqlite3
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.grafik()

    def baglanti_olustur(self):
        baglanti=sqlite3.connect("veritabani.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("CREATE Table if not exists Kullanicilar (Kullaniciadi TEXT,Sifre TEXT)")
        baglanti.commit()

    def grafik(self):
        self.kaydol=QtWidgets.QPushButton("Kaydol")
        self.kullaniciadi=QtWidgets.QLineEdit()
        self.kullanicisifre=QtWidgets.QLineEdit()
        self.kullanicisifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giris Yap")
        self.yazi_alani=QtWidgets.QLabel("")

        assagidogrusirala=QtWidgets.QVBoxLayout()
        assagidogrusirala.addWidget(self.kullaniciadi)
        assagidogrusirala.addWidget(self.kullanicisifre)
        assagidogrusirala.addWidget(self.yazi_alani)
        assagidogrusirala.addStretch()
        assagidogrusirala.addWidget(self.giris)
        assagidogrusirala.addWidget(self.kaydol)

        yataysirala=QtWidgets.QHBoxLayout()
        yataysirala.addStretch()
        yataysirala.addLayout(assagidogrusirala)
        yataysirala.addStretch()

        self.setLayout(yataysirala)
        self.setWindowTitle("Kullanıcı Giriş Ekranı")
        self.giris.clicked.connect(self.girisFonksiyonu)
        self.kaydol.clicked.connect(self.kayitFonksiyonu)
        self.show()

    def kayitFonksiyonu(self):
        k_adi = self.kullaniciadi.text()
        k_sifre = self.kullanicisifre.text()
        if k_adi!="" and k_sifre !="":
            self.cursor.execute("Insert into Kullanicilar(Kullaniciadi,Sifre) values(?,?)",(k_adi,k_sifre))
            self.yazi_alani.setText("Kullanıcı Kaydedildi")


    def girisFonksiyonu(self):
        k_adi=self.kullaniciadi.text()
        k_sifre=self.kullanicisifre.text()
        self.cursor.execute("Select * From kullanicilar where Kullaniciadi=? and Sifre=?",(k_adi,k_sifre))
        data=self.cursor.fetchall()
        if len(data)==0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok")
        else:
            self.yazi_alani.setText("Hoşgeldiniz "+k_adi)

    def yazdir(self):
        print("yazdirma")


uygulama=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(uygulama.exec())














