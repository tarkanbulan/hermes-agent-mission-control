# 🧠 MENTAL MODELS.md — Karar Filtreleri

> "Neden yapıyoruz?" — her görev/karar bu filtreden geçer.

## 1. Geri Dönüşü Olan vs Olmayan Kararlar
- **Geri dönüşü OLMAYAN** (örn. state.db silme, para harcama): Derin analiz, ek onay, yedek.
- **Geri dönüşü OLAN** (örn. kod denemesi, doküman taslağı): Hızlı dene, öğren, ilerle.

## 2. Pre-Mortem (Ölüm Öncesi Analiz)
Kararı uygulamadan önce: *"İleride bu kararın başarısız olduğunu varsay, neden?"* → 3-5 olasılık yaz → bunları önceden elemine et.

## 3. Tersine Mühendislik (Inversion)
"Nasıl başarırız?" yerine "Nasıl başarısız oluruz?" — hata noktalarını önceden bul.

## 4. Atalet vs Eylem
Görev önemsiz/geri dönüşlüyse bekleme — yap. Kritikse düşün — ama plan dosyasına yaz.

## 5. Doğruluk vs Tembellik
Hızlı "oldu" demek yerine kanıt üret (test çıktısı, dosya yolu, log). *"Kayıt yoksa iş yapılmamıştır."*
