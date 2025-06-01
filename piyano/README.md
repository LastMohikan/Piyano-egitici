🎹 Piyano Eğitici Uygulaması (Python + Pygame)
Bu proje, klavye ile piyano çalmayı öğrenmek isteyenler için hazırlanmış interaktif bir Python uygulamasıdır.
Kullanıcılar gerçek zamanlı seslerle piyano çalabilir, şarkı rehberini takip ederek notaları öğrenebilir ve tamamladıkları şarkılardan sonra yeni şarkı seçebilirler.

📌 Özellikler
🎼 Şarkı Rehberi: Üstte sıradaki notaları gösterir (otomatik kaydırmalı).

🎵 Gerçek Sesler: .wav formatında nota sesleri.

⌨️ Klavye Etiketi: Tuşlar üzerinde nota + klavye harfi.

🔄 Şarkı Seçimi: Menüden şarkı seçebilir, ESC ile menüye dönebilirsiniz.

✅ Tamamlanma Mesajı: Şarkı bitince uyarı ve tekrar seçme ekranı.

📁 Klasör Yapısı
css
Kopyala
Düzenle
piyano_egitici/
├── main.py
├── sounds/
│   ├── c1.wav
│   ├── d1.wav
│   ├── ...
├── songs/
│   ├── twinkle.json
│   ├── mary.json
│   └── jingle.json
├── README.md
🚀 Kurulum ve Çalıştırma
Python 3.x yüklü olmalı

Gerekli kütüphaneleri kur:

bash
Kopyala
Düzenle
pip install pygame
Proje dizinine girip çalıştır:

bash
Kopyala
Düzenle
python main.py
🎶 Desteklenen Şarkılar
1 - Twinkle Twinkle Little Star

2 - Mary Had a Little Lamb

3 - Jingle Bells

Dilersen songs/ klasörüne yeni .json dosyaları ekleyerek kendi şarkılarını tanımlayabilirsin.

📄 JSON Şarkı Formatı Örneği
json
Kopyala
Düzenle
["c1", "c1", "g1", "g1", "a1", "a1", "g1"]
Her eleman bir nota adıdır (örneğin: c1, d1, e1, ...). Bu notalar klavye tuşlarıyla eşleşir ve sırasıyla çalınır.

👨‍💻 Geliştirici Notu
Bu proje hem müzik hem programlama öğrenimini birleştiren eğitici bir deneyim sunmayı hedefler.
Katkı yapmak, yeni şarkılar eklemek ya da farklı modüller entegre etmek isteyenler için açıktır!