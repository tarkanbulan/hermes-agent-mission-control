# 🛰️ ÇOKLU AJAN TOPOLOJİSİ ve GÖREV DEVİR KURALLARI

> Dörtlü Hibrit Düğüm: Antigravity (agy) · Jules · Gemini · Google Drive — tek SSOT (bu repo).

## 1. Ajanlar Arası Paslaşma Zinciri (Pipeline)

1. **Adım 1 (Fikir & Tasarım):** Kaptan ve Gemini strateji/şartname → `01_GOREV_MERKEZI/AKTIF_GOREVLER.md`
2. **Adım 2 (Kodlama - Jules):** Jules GitHub şartnamesini oku → geliştirme branch + PR
3. **Adım 3 (Doğrulama & İcra - Antigravity):** `agy` yerel makinede PR kodunu çek, veri/test ortamında çalıştır, doğrula
4. **Adım 4 (Hafıza & Senkronizasyon):** Sonuçlar `02_HAFIZA` + Google Drive'a işlenir

## 2. Çakışma Önleme

- **Jules:** Sadece kodlama branch'lerinde çalışır; `main` branch'e doğrudan müdahale etmez.
- **Antigravity:** Yerel ortamı yönetir; dış senkronizasyonu git komutlarıyla yapar.
- **Gemini:** Workspace dokümanlarını + hafıza özetlerini günceller; kod dosyasına dokunmaz.

## 3. Loglama (her düğüm)

Her düğüm işlemini `05_LOG/MASTER_LOG.md`'ye + hata varsa `HATA_LOGU.md`'ye kaydeder.
