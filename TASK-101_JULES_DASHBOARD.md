# 🤖 JULES — GÖREV KARTI (TASK-101)

**Durum:** 🔄 SIRADA — Picard planladı, Jules kodlayacak.

---

## GÖREV ADI
**T2SAIM Mission Control — Görsel Dashboard (Faz 1)**

## ŞARTNAME (tam detay — oku)
`00_STRATEJI_VE_KARARLAR/ADR/PHASE1_DASHBOARD_SARTNAME.md`

---

## ÖZET (Jules'a kısa)
Kaptan terminal beceremiyor → görsel/tıklanabilir panel ister. Mission Control markdown dosyalarını (görev + log + rüya) tarayıcıda gösteren tek sayfa dashboard kur.

## TESLİM EDİLECEKLER (repoda `06_DASHBOARD/` altında)
1. `index.html` — 3 sütunlu görsel kumanda masası:
   - SOL: Görev Merkezi (`01_GOREV_MERKEZI/*.md`)
   - ORTA: Canlı Log (`05_LOG_MERKEZI/MASTER_LOG.md` + `HATA_LOGU.md`)
   - SAĞ: Ekip Köprüleri — 4 düğme (Spark / Jules / Antigravity / Hermes)
   - ÜST: Monitör seçici `[Monitör 1] [Monitör 2] [Monitör 3]` (dikey/yatay)
   - Monitör 3: alt panel wterm terminal karesi (placeholder OK)
2. `server.py` — Python stdlib HTTP sunucusu (port 8080). Markdown → JSON API:
   - `GET /api/gorevler` · `/api/loglar` · `/api/ruya`
   - `POST /api/kopru/<hedef>` → dagit_ekip.py
3. `dagit_ekip.py` — köprü arka ucu:
   - `kopru_spark` → raporu G-Drive hedefine kopyala
   - `kopru_jules` → GitHub issue/PR'ya yönlendir veya ADR altına kopyala
   - `kopru_agy` → talimat dosyası + `agy -p --print-timeout 8m` arka planda
   - `kopru_geri` → `02_HAFIZA`'ya taşı
   - Her kopru `05_LOG/MASTER_LOG.md`'ye append (izlenebilirlik)
4. `README.md` — nasıl çalıştırılır

## KURALLAR (Kaptan/Picard sınırları)
- `pip` bağımlılığı YOK (Python stdlib only — kapalı ortam)
- Harici CDN YOK (çevrimdışı çalışmalı)
- Anahtar/secret dosyalara yazılmaz, loglanmaz
- Türkçe arayüz, koyu tema, BÜYÜK butonlar (Kaptan tıklayacak)
- **`main` branch'e DOĞRUDAN YAZMA** — kodlama branch'i aç (`feat/dashboard`), bitince PR oluştur. Picard denetleyip merge eder.

## KABUL KRİTERLERİ (Picard denetler — şartname Bölüm 6)
1. `python 06_DASHBOARD/server.py` → http://127.0.0.1:8080 → 200
2. 3 panel markdown içeriği gösterir
3. Monitör düğmeleri düzeni değiştirir
4. Köprü düğmesi hedefe kopyalar + MASTER_LOG kaydı
5. wterm'siz çalışır (placeholder)

---

*Kart: Picard · 24 Ağustos 2026 · Veritas Per Se*
