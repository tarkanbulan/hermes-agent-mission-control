# 📄 JULES ŞARTNAME — T2SAIM Mission Control Görsel Dashboard (Faz 1)

**Kaptan onaylı (24 Ağustos 2026) · Planlayan: Picard · Kodlayan: Jules · Denetleyen: Picard**

> Kaptan terminal beceremiyor; görsel/tıklamalı çalışmak istiyor. 3 monitör (2 dikey + 1 yatay): bir panele komut merkezi, başka panele bölünmüş terminal.

---

## 1. AMAÇ

Mission Control markdown dosyalarını (görevler, loglar, rüya havuzu) **görsel, tıklanabilir, tarayıcıda** gösteren tek sayfalık dashboard. Kaptan tıklayarak: görevleri görür, logları izler, raporu ekibin diğer üyelerine (Spark/Jules/Antigravity/Hermes) yönlendirir.

## 2. TESLİM EDİLECEK DOSYALAR (Mission Control repo kökünde `06_DASHBOARD/` altında)

```
06_DASHBOARD/
├── index.html          # Tek sayfa görsel kumanda masası (tıklanır)
├── server.py           # Yerel HTTP sunucusu (markdown → JSON API)
├── dagit_ekip.py       # Ekip köprüsü düğmelerinin arka ucu
└── README.md           # Nasıl çalıştırılır
```

## 3. `index.html` GEREKSİNİMLERİ

### 3.1 Üç Sütunlu Düzen (monitör-agnostik, responsive)
- **SOL PANEL — Görev Merkezi:** `01_GOREV_MERKEZI/*.md` dosyalarından görev listesini çek.
  - Sekmeler: Aktif | Bloklanan | Doğrulama(Bekleyen) | Biten
  - Her görev kartı: ID, ad, durum, sorumlu. Tıklanınca `02_HAFIZA/CONTEXT_SNAPSHOTS` güncel dosyayı açar.
- **ORTA PANEL — Canlı Log:** `05_LOG_MERKEZI/MASTER_LOG.md` + `HATA_LOGU.md`.
  - Otomatik yenileme (fetch her 5 sn) — canlı akış.
  - Olası hata satırları kırmızı vurgu.
- **SAĞ PANEL — Ekip Köprüleri:** 4 büyük düğme:
  - `[→ Spark'a gönder]` → `POST /api/kopru/spark {rapor_yolu}` → `dagit_ekip.py` raporu G-Drive hedefine kopyalar (config'te yazılır).
  - `[→ Jules'a gönder]` → `POST /api/kopru/jules {rapor_yolu}` → GitHub issue açılır (gh CLI) veya REPO `03_...` altına kopyalar.
  - `[→ Antigravity'ye gönder]` → `POST /api/kopru/agy {rapor_yolu}` → talimat dosyası oluşturur + `agy -p "talimat dosyasını oku" --print-timeout 8m` arka planda başlatır.
  - `[→ Hermes'e geri]` → `POST /api/kopru/geri {rapor_yolu}` → raporu `02_HAFIZA` aktif konuma taşır.

### 3.2 Monitör Görünümü Seçici (üst bar)
- 3 buton: `[Monitör 1] [Monitör 2] [Monitör 3]` → CSS ile panel **genişlikleri değişir**:
  - Monitör 1 (dikey): Tek sütun (Görev) — sol monitör.
  - Monitör 2 (yatay): 3-sütun (Görev + Log + Köprü) — ana komut merkezi.
  - Monitör 3 (dikey): Bölünmüş — üst: Log, alt: wterm terminal karesi.

### 3.3 wterm Entegrasyon Noktası
- Monitör 3'te alt panel = terminal karesi.
- wterm kuruluysa `<iframe>` veya terminal karesi; kurulu değilse "wterm bekliyor" placeholder.
- Renk: koyu tema (Solarized Dark / Monokai).

### 3.4 Teknik
- Saf HTML/CSS/JS, harici CDN yok (çevrimdışı çalışmalı).
- `fetch('/api/...')` ile markdown'ı JSON'dan çeker.
- Türkçe arayüz. Koyu tema. Büyük butonlar (Kaptan tıklayacak).

## 4. `server.py` GEREKSİNİMLERİ

- Python stdlib `http.server` (pip bağımlılığı yok — kapalı ortam).
- `GET /api/gorevler` → `01_GOREV_MERKEZI/*.md` içerik listesi (JSON).
- `GET /api/loglar` → `05_LOG_MERKEZI/*.md` içerik.
- `GET /api/ruya` → `04_RUYA_PROTOKOLU/KARBON_HAVUZU/*.md`.
- `POST /api/kopru/<hedef>` → `dagit_ekip.py` fonksiyonunu çağırır.
- Port **8080** (config'te değişebilir).
- Başlangıç mesajı: `Mission Control Dashboard: http://127.0.0.1:8080`

## 5. `dagit_ekip.py` GEREKSİNİMLERİ

- `kopru_spark(rapor_yolu)`: raporu config'teki G-Drive hedefine kopyala (`shutil.copy2`), yoksa logla.
- `kopru_jules(rapor_yolu)`: `gh issue create` (gh CLI) veya repo `00_STRATEJI/ADR` altına kopyala.
- `kopru_agy(rapor_yolu)`: `talimat_<zaman>.md` oluştur + `agy -p "OKU VE UYGULA: @<yol>" --print-timeout 8m` arka planda (subprocess Popen).
- `kopru_geri(rapor_yolu)`: `02_HAFIZA/OKF` veya CONTEXT'e taşı.
- Her kopru işlemi `05_LOG/MASTER_LOG.md`'ye EKLE (append) — izlenebilirlik.

## 6. KABUL KRİTERLERİ (Picard denetleyecek)

1. `python 06_DASHBOARD/server.py` çalışır → `http://127.0.0.1:8080` 200 döner.
2. Dashboard 3 paneli de markdown'dan içerik gösterir (görev/log/köprü).
3. `[Monitör 1/2/3]` düğmeleri düzeni değiştirir.
4. Köprü düğmesi tıklanınca ilgili hedefe kopyalar + MASTER_LOG'a kayıt eklenir.
5. wterm olmadan da çalışır (placeholder).
6. Türkçe, koyu tema, büyük butonlar.

## 7. YASAK / SINIR

- Harici CDN/modül YOK (çevrimdışı).
- `server.py`'de pip bağımlılığı YOK (stdlib only).
- Anahtarlar/secret'lar asla kod/dosyaya yazılmaz — config'ten okunur, loglanmaz.
- `main` branch'e doğrudan yazma YOK — Jules branch açar, Picard PR'ı denetler.

---

*Planlayan: Komutan Picard · 24 Ağustos 2026 · Veritas Per Se*
