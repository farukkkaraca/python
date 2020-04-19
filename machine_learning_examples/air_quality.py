import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree

"""     Proje Amacı:
        weight(ağırlık), humidity(nem oranı), temperature(sıcaklık) ve quality(kalite)
        dataset değişkenlerine göre ilgili ortam kalitesi
        good(iyi) ve poor(zayıf) olarak karar ağaçları ile tahmin edilmiştir.
        
"""

column_names = ['weight', 'humidity', 'temperature', 'quality']
data = pd.read_csv("air_quality.csv", names=column_names)

feature_cols = ['weight', 'humidity', 'temperature']
X = data[feature_cols]
y = data.quality 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

train_t = pd.DataFrame(clf.predict(X_train))
test_t = pd.DataFrame(clf.predict(X_test))
m_train = confusion_matrix(y_train, train_t)
m_test = confusion_matrix(y_test, test_t)

print("Eğitim Modeli:")
print(m_train)
print()
print("Test Modeli:")
print(m_test)
print()

train_accuracy=metrics.accuracy_score(y_train,train_t)
test_accuracy=metrics.accuracy_score(y_test,test_t)

print("Model eğitim başarısı: {}".format(train_accuracy) )
print("Model test başarısı: {}".format(test_accuracy) )

tree.export_graphviz(clf, out_file="air_tree.dot", feature_names=X_train.columns)



