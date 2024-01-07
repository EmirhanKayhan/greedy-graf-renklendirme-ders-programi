# README

Ders Programı Oluşturma Projesi 

Bu proje, ders programı oluşturmak için MySQL veritabanını kullanmakta ve Networkx kütüphanesi ile graf oluşturarak greedy coloring algoritması ile derslere gün ve saat bilgisi atamaktadır.

Proje Açıklaması
MySQL Bağlantısı:

db_config değişkeni üzerinden MySQL bağlantı bilgileri tanımlanmıştır (host, port, user, password, database).
mysql.connector kullanılarak MySQL bağlantısı kurulmuş ve bir cursor oluşturulmuştur.
Veritabanı Sorgusu:

Ders programı oluşturulması için gerekli bilgileri içeren bir SQL sorgusu yapılmıştır. Bu sorgu dersler, hocalar, sınıflar ve bu entiteler arasındaki ilişkileri içermektedir.
Adjacency Matrix Oluşturma:

Sınıf ve hoca çakışmalarını kontrol etmek için bir adjacency matrix kullanılmıştır.
Networkx Graf Oluşturma:

networkx kütüphanesi kullanılarak derslerin ve çakışan derslerin oluşturduğu bir graf oluşturulmuştur.
Greedy Coloring:

Oluşturulan graf, greedy coloring algoritması ile renklendirilmiştir. Her bir renk bir dersin gün ve saatini temsil etmektedir.
Gün ve Saat Atama:

Her bir ders için rasgele bir gün ve saat, bir dersliğe atandıktan sonra bu bilgiler MySQL veritabanına kaydedilmiştir.
Sonuçları Konsola Yazdırma:

Oluşturulan derslerin adı, rengi ve gün/saat/derslik bilgileri konsola yazdırılmıştır.
Grafik Çizimi:

Oluşturulan grafik, renklendirmeye dayalı olarak matplotlib kullanılarak çizdirilmiştir.
Veritabanı Bağlantısı Kapatma:

İşlemler tamamlandıktan sonra MySQL veritabanı bağlantısı kapatılmıştır.

Proje Çalıştırma Adımları

1. Projenin bulunduğu dizine gidin.

2. Python yüklü değilse Python'un resmi web sitesinden indirip yükleyin.

3. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazın:
   
pip install mysql-connector-python networkx matplotlib

4. Proje dosyasını bir metin düzenleyici ile açın ve MySQL bağlantı bilgilerinizi güncelleyin (host, port, user, password, database).
   
5. Terminal veya komut istemcisinde projenin bulunduğu dizine gidin ve şu komutu çalıştırın:

   python proje_adi.py
(Not: proje_adi.py dosyanızın gerçek adını kullanın.)

6. Proje başarıyla çalıştırıldığında, konsol çıktısında ders adları, renkleri ve atanan gün/saat/derslik bilgilerini görebilirsiniz.

7. Ayrıca, matplotlib tarafından çizilen ders programı grafiğini görmek için bir pencere açılacaktır.

Bu adımları takip ederek proje başarıyla çalıştırılabilir ve ders programı oluşturulabilir.


