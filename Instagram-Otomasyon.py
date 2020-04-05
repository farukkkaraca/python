from selenium import webdriver
import time
giris_yontemi="""

    --->>>GİRİŞ YAPMA YÖNTEMLERİ:
    [1]-KULLANICI ADI VE PAROLA İLE GİRİŞ
    [2]-FACEBOOK İLE GİRİŞ
    ----------------------------------------------------- 
"""
islemler="""
    --->>>İŞLEMLER:
    [1]-KULLANICI TAKİP ETME
    [2]-KULLANICI TAKİPTEN ÇIKMA
    [3]-ÇOKLU KULLANICI TAKİP ETME
    [4]-ÇOKLU KULLANICI TAKİPTEN ÇIKMA
    [5]-KULLANICININ SON FOTOĞRAFINI BEĞENME
    [6]-KULLANICININ HESABINDAKİ TÜM FOTOĞRAFLARI BEĞENME

"""
class Insta:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(200,300)
        print(giris_yontemi)
        self.main()


    def login(self,username,password):
        self.browser.get("https://www.instagram.com")
        time.sleep(5)
        self.browser.find_element_by_name("username").send_keys(username)
        self.browser.find_element_by_name("password").send_keys(password)
        self.browser.find_element_by_css_selector("button[class='sqdOP  L3NKy   y3zKF     '").click()

        print("Giriş Başarılı")

    def loginWithFacebook(self,username,password):
        self.browser.get("https://www.instagram.com")
        time.sleep(5)
        self.browser.find_element_by_class_name("KPnG0").click()
        self.browser.find_element_by_id("email").send_keys(username)
        self.browser.find_element_by_id("pass").send_keys(password)
        self.browser.find_element_by_id("loginbutton").click()
        print("giriş başarılı")

    def follow(self,username=str):
        time.sleep(3)
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(3)
        follow=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button')
        if follow.text=="Takip Et":
            follow.click()
            print("Takip Edilen Kullanıcı:" +username)
        else:
            print("Kullanıcı zaten takip ediliyor")

    def unFollow(self,username=str):

        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(3)
        un_follow = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button')
        if un_follow.text == "Takiptesin":
            un_follow.click()
            print("Takipten Çıkarılan Kullanıcı: "+username)
        else:
            print("Kullanıcı zaten takipte değil")

    def followMany(self,username_list:list):
        for user in username_list:
            self.browser.get("https://www.instagram.com/"+user)
            time.sleep(3)
            follow = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button')

            if follow.text == "Takip Et":
                follow.click()
                print("Kullanıcı Takip Edildi.Takip Edilen Hesap: "+user)
            else:
                print("Kullanıcı zaten takip ediliyor")

    def unFollowMany(self,username_list:list):
        for user in username_list:
            self.browser.get("https://www.instagram.com/"+user)
            time.sleep(3)
            un_follow = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button')
            if un_follow.text == "Takiptesin":
                un_follow.click()
                print("Kullanıcı Takipten Çıkarıldı.Takipten Çıkarılan isim: "+user)
            else:
                print("Kullanıcı zaten takipte değil")

    def likeLastPhoto(self,usernanme=str):

        self.browser.get("https://www.instagram.com/"+usernanme)
        time.sleep(3)
        self.browser.find_element_by_css_selector("div[class*='eLAPa']").click()
        time.sleep(2)
        try:
            like = self.browser.find_element_by_css_selector("svg[aria-label='Beğen']")
            like.click()
        except:
            print("Foto zaten beğenilmiş...")

    def like(self,link=str):

        self.browser.get(link)
        time.sleep(2)
        try:
            like = self.browser.find_element_by_css_selector("svg[aria-label='Beğen']")
            like.click()
        except:
            print("Foto zaten beğenilmiş...")

    def likeAllPhotos(self,username=str):
        self.ScrollDown()
        time.sleep(5)
        photo_list=[]
        time.sleep(3)
        self.browser.get("https://www.instagram.com/" + username+"/")
        time.sleep(3)
        photos=self.browser.find_elements_by_xpath("//div[contains(@class,'v1Nh3 kIKUG  _bz0w')]/a")

        for i in photos:
            photo_list.append(i.get_attribute('href'))

        for i in photo_list:
            self.like(link=i)

    def ScrollDown(self):
        SCROLL_PAUSE_TIME = 1

        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                print("break")
                break
            last_height = new_height


    def main(self):
        x=input("GİRİŞ YAPMA YÖNTEMİ SEÇİNİZ:")

        if x=="1":
            u=input("Kullanıcı Adı Giriniz: ")
            p=input("Şifre Giriniz")
            self.login(u,p)

        elif x=="2":
            fu = input("Facebook Kullanıcı Adı Giriniz: ")
            fp = input("Facebook Şifre Giriniz")
            self.loginWithFacebook(fu,fp)
        else:
            print("YANLIŞ SEÇİM YAPTINIZ")
            quit()

        print(islemler)

        islem=input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:")
        if islem=="1":
            username=input("TAKİP EDİLECEK HESAP: ")
            self.follow(username)

        elif islem=="2":
            username = input("TAKİPTEN ÇIKILACAK HESAP: ")
            self.unFollow(username)

        elif islem=="3":
            username_list=[]
            usernames=input("TAKİP EDELECEK HESAPLARI VİRGÜL İLE YAZINIZ: ").split(",")
            for i in usernames:
                username_list.append(i)
            self.followMany(username_list)

        elif islem=="4":
            username_list = []
            usernames = input("TAKİPTEN ÇIKILACAK HESAPLARI VİRGÜL İLE YAZINIZ: ").split(",")
            for i in usernames:
                username_list.append(i)
            self.unFollowMany(username_list)

        elif islem=="5":
            username = input("SON FOTOĞRAFI BEĞENİLECEK HESAP:  ")
            self.likeLastPhoto(username)

        elif islem=="6":
            username = input("TÜM FOTOĞRAFLARI BEĞENİLECEK HESAP:  ")
            self.likeAllPhotos(username)

        else:
            print("YANLIŞ SEÇİM YAPTINIZ!!!")

insta=Insta()







