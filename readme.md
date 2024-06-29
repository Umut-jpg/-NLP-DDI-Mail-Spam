 <p align="center">
     <img src="https://github.com/Umut-jpg/MobileCurrencyApp/assets/77737561/fea3b1b3-5dd5-413b-9ca4-346d0b658057 " alt="Resim Adı" width="100" height="150">
</p>
<p align="center">
  <a href="https://www.yusaumut.com">YusaUmut.Com</a>
</p>

# DDİ Mail Spam Test 

**NOT !!!** Vercel.json ve Requirements.txt dosyalarım vercel  pro'da canlı olarak host etmek isteyenler için eklenmiştir

**Kullanılan Teknolojiler**
 - Html
 - TailwindCss
 - Python

**Projeyi Çalıştırma** 
index.py dosyasını (***python index.py***) komutu ile başlatarak  görebilirsiniz.

**Proje Anasayfa Ve Uygulama Görüntüleri**
```
https://hizliresim.com/labqr76
```
```
https://hizliresim.com/hu01rs9
```
```
https://hizliresim.com/pl78qj3
```

**Projenin Amacı** 
 - Kullanıcı tarafından girilen mail mesajının spam bir mail mi yoksa ham bir mail mi olduğuna karar veren bir model eğitmek.
  
**Kullanılan Kütüphaneler**
 - Pandas
 - Sklearn
 - CGI
 - Flask
 - Pickle
 - FlaskCors
 - OS(Veri Setini Oluştururken Kullanıldı)

**Veri Setinin Oluşturulması**
Veri setimiz için gerekli olan ham ve spam mail örneklerini çekebilecek yer bulamadığımdan  verileri elle eklemem veya 5-100 adet farklı yerlerden verilerimi bulup birleştirmem gerekti birbirinden farklı kaynaklardan aldığım örnek mail yazışmalarını txt,csv formatıyla toplayıp python (veri.py)  yardımı ile excel dosyasına yazdırdım. Veri Setinde 1700 veri bulunmaktadır.

**=>Yapım Aşaması**

**=>Veri Yükleme Aşaması :** 
Oluşturduğumuz "output.xlsx" adlı veri setimizin bulunduğu dosyamızdan veri, pandas DataFrame (df) içine okunur.

**=>Veri Ön İşleme Ve Veriyi Ayırma**
'Category' sütunundaki değerleri 'spam' ve 'ham' olarak sayısal değerlere dönüştürdük. (spam için 0, ham için 1) Daha sonra verimizi scikit-learn kütüphanesinde bulunan train_test_split fonksiyonu ile eğitim ve test setlerine ayırdık. Ve TF-IDF vektörleme kullanarak e-posta metnini sayısal özelliklere dönüştürdük. Bu işlem için scikit-learn kütüphanesinde bulunan TfidfVectorizer fonksiyonunu kullandık.

**=>Modelin Eğitilmesi, Değerlendirilmesi**
Sınıflandırma modeli olarak lojistik regresyon seçiminde bulunduk daha sonra eğitim verisi kullanılarak modelimizi eğittik.Eğitme aşaması bittikten sonra modelin ne kadar başarılı bir sonuç verdiğini anlamak için eğitim ve test setlerindeki doğruluğunu hesapladık.Gerekli başarı oranına ulaştığını gördüğümüzde eğitime son verip bir sonraki aşamaya geçiş yaptık.

**Sonuc => Modelin Kullanılması**
Modelimizi  verilen e-posta mesajlarının spammı yoksa hammı olduğunu  tahmin etmek için kullanırız .

**=>Yayına Alınması**
Flask yardımı ile modelin yayınlanması sağlandı.




