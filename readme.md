# DDİ Mail Spam Test 

**Projenin Amacı** 
 - Kullanıcı tarafından girilen mail mesajının spam bir mail mi yoksa ham bir mail mi olduğuna karar veren bir model eğitmek.
  
**Kullanılan Kütüphaneler**
 - Pandas
 - Sklearn
 - CGI
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




