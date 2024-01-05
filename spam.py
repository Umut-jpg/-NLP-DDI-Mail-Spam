# import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import cgi
import pickle

formdata = cgi.FieldStorage()
formyazı =  formdata.getvalue('w3review')
df=pd.read_excel("Hazirlanmis_Datam.xlsx")
# print(df['Category'])
data = df.where((pd.notnull(df)), '')

data.loc[data['Category'] == 'spam', 'Category',] = 0
data.loc[data['Category'] == 'ham', 'Category',] = 1

X = data['Message']
Y = data['Category']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)


with open("turkce-stop-words.txt", "r", encoding="utf-8") as file:
    turkish_stopwords = file.read().splitlines()

feature_extraction = TfidfVectorizer(min_df=1, stop_words=turkish_stopwords, lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

model = LogisticRegression()
model.fit(X_train_features, Y_train)


training_data = model.predict(X_train_features)
acctraining_data = accuracy_score(Y_train, training_data)


test_data = model.predict(X_test_features)
acctest_data = accuracy_score(Y_test, test_data)


input_yourmail = [" İşte Çocuğunun Gelişimini Destekleyecek Hizmetlerimiz! Armut Piş Ağzıma Düş! Temizlik Tadilat Nakliyat Tamir Özel Ders Sağlık Tamir ve Montaj İşlerini Hallet Çocuğunun Gelişimini Destekleyecek Hizmetlerimizle Yanındayız!  Yüzme Özel Ders HİZMET AL Piyano Özel Ders HİZMET AL Gitar Özel Ders HİZMET AL Resim Özel Ders HİZMET AL Oyun Ablası HİZMET AL Tenis Dersi Öğrenci Koçu HİZMET AL Her yaş seviyesine uygun yabancı dil derslerine de göz atabilirsin Online İngilizce Özel Ders HİZMET AL İspanyolca Özel Ders HİZMET AL Almanca Özel Ders HİZMET AL Fransızca Özel Ders HİZMET Al Çocuk odasının dekorasyonu için nelere ihtiyacın var?  Boya Badana Ustası HİZMET AL Özel Mobilya Yapımı HİZMET AL Marangoz"]
input_data_features = feature_extraction.transform(input_yourmail)


pred = model.predict(input_data_features)

if(pred[0]==1):
    print('Ham Mail ')
else:
    print('Spam Mail')
print(pred)

with open("tfidf_vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(feature_extraction, vectorizer_file)
filename="mymodel.sav"
pickle.dump(model,open(filename,"wb"))