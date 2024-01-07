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

3. Veri tabanını oluşturmak için MySQL'de  bu kodları çalıştırın kodları çalıştırdıktan sonra gerekli ders verilerini girin.


   CREATE DATABASE dersprogrami;
   USE dersprogrami;
   
   CREATE TABLE dersler (
     ders_id int NOT NULL,
     ders_adi varchar(255) DEFAULT NULL,
     ders_gunsaat varchar(45) DEFAULT NULL,
     derslik_no varchar(45) DEFAULT NULL,
     ders_kacincisinif varchar(45) DEFAULT NULL,
     PRIMARY KEY (ders_id)
   );
   
   CREATE TABLE hocalar (
     hoca_id int NOT NULL,
     hoca_adi varchar(255) NOT NULL,
     PRIMARY KEY (hoca_id)
   );
   
   
   CREATE TABLE siniflar (
     sinif_id int NOT NULL,
     sinif_adi varchar(45) DEFAULT NULL,
     PRIMARY KEY (sinif_id),
     KEY idx_sinif_adi (sinif_adi)
   );
   
   CREATE TABLE ders_hoca (
     ders_id int NOT NULL,
     hoca_id int NOT NULL,
     PRIMARY KEY (ders_id,hoca_id),
     KEY hoca_id (hoca_id),
     CONSTRAINT ders_hoca_ibfk_1 FOREIGN KEY (ders_id) REFERENCES dersler (ders_id),
     CONSTRAINT ders_hoca_ibfk_2 FOREIGN KEY (hoca_id) REFERENCES hocalar (hoca_id)
   );
   
   CREATE TABLE ders_sinif (
     ders_id int NOT NULL,
     sinif_id int NOT NULL,
     PRIMARY KEY (ders_id,sinif_id),
     KEY sinif_id (sinif_id),
     CONSTRAINT ders_sinif_ibfk_1 FOREIGN KEY (ders_id) REFERENCES dersler (ders_id),
     CONSTRAINT ders_sinif_ibfk_2 FOREIGN KEY (sinif_id) REFERENCES siniflar (sinif_id)
   );



4. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazın:
   
   pip install mysql-connector-python networkx matplotlib

5. Proje dosyasını bir metin düzenleyici ile açın ve MySQL bağlantı bilgilerinizi güncelleyin (host, port, user, password, database).
   
6. Terminal veya komut istemcisinde projenin bulunduğu dizine gidin ve şu komutu çalıştırın:

   python proje_adi.py
(Not: proje_adi.py dosyanızın gerçek adını kullanın.)

7. Proje başarıyla çalıştırıldığında, konsol çıktısında ders adları, renkleri ve atanan gün/saat/derslik bilgilerini görebilirsiniz.

8. Ayrıca, matplotlib tarafından çizilen ders programı grafiğini görmek için bir pencere açılacaktır.

Bu adımları takip ederek proje başarıyla çalıştırılabilir ve ders programı oluşturulabilir.


