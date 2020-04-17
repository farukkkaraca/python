import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree

""" 
        weight(ağırlık), humidity(nem oranı), temperature(sıcaklık) ve quality(kalite)
        dataset değişkenlerine göre ilgili ortam kalitesi
        good(iyi) ve poor(zayıf) olarak karar ağaçları ile tahmin edilmiştir.
        
"""
#Değişken isimleri verildi
column_names = ['weight', 'humidity', 'temperature', 'quality']

#Veri okuma işlemi gerçekleştirildi
data = pd.read_csv("air_quality.csv", names=column_names)

# datadaki işleme girecek değişkenler ve tahmin edilecek değişken belirtildi
feature_cols = ['weight', 'humidity', 'temperature']
X = data[feature_cols] # işleme girecek değişkenler
y = data.quality # Hedef değişken (tahmin edilecek)

#Data ikiye bölündü
# %70 öğrenme ve %30 test olacak sekilde
#verilerin rastgele seçilmesi true döndürüldü.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#Pyhtondaki karar ağacı sınıfı çağırıldı ve kullanılmak için değişkene atandı
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

#modelleme yapıldı
test_t = pd.DataFrame(clf.predict(X_test))
train_t = pd.DataFrame(clf.predict(X_train))

m_train = confusion_matrix(y_train, train_t)
m_test = confusion_matrix(y_test, test_t)

print("Eğitim Modeli:")
print(m_train)
print()
print("Test Modeli:")
print(m_test)
print()

#Karar ağacı algoritmasına karşılaştırılması için test ve deneme verisi gönderildi
clf = clf.fit(X_train,y_train)

#Gönderilen veriler işlendikten sorna test verisi için tahmin yapıldı
y_pred = clf.predict(X_test)

#model değerlendirildi
accuracy=metrics.accuracy_score(y_test, y_pred)
print("Model Başarısı: {}".format(accuracy) )

#karar ağacı görselleştirildi
tree.export_graphviz(clf, out_file="air_tree.dot", feature_names=X_train.columns)
#Modek değerlendirildi ve başarı oranı iyi olarak belirlendi.Herhangi bir performans iyileştirme işlemine gerek duyulmadı.



