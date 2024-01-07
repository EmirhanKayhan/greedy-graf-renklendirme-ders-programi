import mysql.connector
import networkx as nx
import matplotlib.pyplot as plt
import random

# MySQL bağlantı bilgileri
db_config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'dersprogrami'
}

# MySQL bağlantısını kur
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Derslerin hocalarını ve sınıflarını kontrol et
query = """
    SELECT d.ders_id, d.ders_adi, h.hoca_adi, s.sinif_id
    FROM dersler d 
    JOIN ders_hoca dh ON d.ders_id = dh.ders_id
    JOIN hocalar h ON dh.hoca_id = h.hoca_id
    JOIN ders_sinif ds ON d.ders_id = ds.ders_id
    JOIN siniflar s ON ds.sinif_id = s.sinif_id
"""
cursor.execute(query)
results = cursor.fetchall()

# Sınıf ve hoca çakışan dersler için adjacency matrix oluştur
adjacency_matrix = {}
for result in results:
    ders_id, ders_adi, hoca, sinif = result
    if (ders_id, ders_adi, hoca, sinif) not in adjacency_matrix:
        adjacency_matrix[(ders_id, ders_adi, hoca, sinif)] = []

# Networkx grafiği oluştur
G = nx.Graph()

# Dersleri node olarak ekle
for ders_id, ders_adi, hoca, sinif in adjacency_matrix:
    G.add_node(ders_id, label=ders_adi, hoca=hoca, sinif=sinif)

# Çakışan dersleri edgeler ile bağla
for (ders_id1, ders_adi1, hoca1, sinif1) in adjacency_matrix:
    for (ders_id2, ders_adi2, hoca2, sinif2) in adjacency_matrix:
        if (ders_id1 != ders_id2) and (hoca1 == hoca2 or sinif1 == sinif2):
            G.add_edge(ders_id1, ders_id2)

# Graph coloring algoritması uygula
coloring = nx.greedy_color(G, strategy="largest_first")

# Her bir dersin ders_id'si ile rengini eşle
ders_renkleri = {ders_id: coloring[ders_id] for ders_id in G.nodes}

# Her bir ders için gün, saat, derslik_no ve ders_kacincisinif bilgileri ata
ders_bilgileri = {}
derslikler = [1036, 1040, 1041, 1044, "Z023", 1050]
gun_saatler = [
    "Pazartesi 10:00", "Pazartesi 11:00", "Pazartesi 12:00", "Pazartesi 13:00", "Pazartesi 14:00", "Pazartesi 15:00",
    "Salı 10:00", "Salı 11:00", "Salı 12:00", "Salı 13:00", "Salı 14:00", "Salı 15:00",
    "Çarşamba 10:00", "Çarşamba 11:00", "Çarşamba 12:00", "Çarşamba 13:00", "Çarşamba 14:00", "Çarşamba 15:00",
    "Perşembe 10:00", "Perşembe 11:00", "Perşembe 12:00", "Perşembe 13:00", "Perşembe 14:00", "Perşembe 15:00",
    "Cuma 10:00", "Cuma 11:00", "Cuma 12:00", "Cuma 13:00", "Cuma 14:00", "Cuma 15:00"
]

for ders_id in ders_renkleri.keys():
    gun_saat = random.choice(gun_saatler)
    derslik_no = random.choice(derslikler)

    # İlgili ders_id'sine sahip satırın olup olmadığını kontrol et
    cursor.execute("SELECT COUNT(*) FROM dersler WHERE ders_id = %s", (ders_id,))
    row_count = cursor.fetchone()[0]

    # Eğer ders_id'sine sahip satır varsa UPDATE, yoksa INSERT işlemi yap
    if row_count > 0:
        cursor.execute(
            "UPDATE dersler SET ders_gunsaat = %s, derslik_no = %s WHERE ders_id = %s",
            (gun_saat, derslik_no, ders_id)
        )
    else:
        cursor.execute(
            "INSERT INTO dersler (ders_id, ders_adi, ders_gunsaat, derslik_no) VALUES (%s, %s, %s, %s)",
            (ders_id, ders_adi, gun_saat, derslik_no)
        )

    # Her bir dersin ders_id'si ile gün/saat/derslik bilgisini eşle
    ders_bilgileri[ders_id] = (gun_saat, derslik_no)

# Veritabanındaki değişiklikleri kaydet
connection.commit()

# Her bir dersin ders adı ile rengini ve gün/saat/derslik/ders_kacincisinif bilgisini konsola yazdır
for ders_id, color in ders_renkleri.items():
    ders_adi = G.nodes[ders_id]['label']
    print(f"Ders Adı: {ders_adi}, Renk: {color}, Bilgiler: {ders_bilgileri[ders_id]}")

# Grafik çizdir
pos = nx.spring_layout(G)
node_colors = [ders_renkleri[node] for node in G.nodes()]
node_labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, labels=node_labels, node_color=node_colors, cmap=plt.cm.rainbow, font_color="black")
plt.show()

# Veritabanı bağlantısını kapat
cursor.close()
connection.close()
