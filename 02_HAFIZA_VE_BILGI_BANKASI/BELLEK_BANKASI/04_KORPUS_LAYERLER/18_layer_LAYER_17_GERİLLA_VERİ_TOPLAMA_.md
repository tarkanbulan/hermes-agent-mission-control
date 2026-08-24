# LAYER 17: GERİLLA VERİ TOPLAMA PROTOKOLÜ

## 17A: GERİLLA VERİ TOPLAMA PROTOKOLÜ

> **Kaynak:** `kriz gözlem.md` oturum kayıtları + `implementation_plan.md`  
> **Durum:** ⚠️ Assumed — Protokol tanımlandı, tam otomasyon bekliyor

### 17A.1 Veri Toplama Mimarisi

```
Sorun (Kaptan tespiti):
  "Ferrari şasesi var ama benzin yok."
  EWI formülleri kalibre, ama veri beslemesi boş.
  
Çözüm: Gerilla Veri Toplama (Guerrilla Data Collection)
  Her akşam otomatik veri senkronizasyonu
  TCMB, EVDS, fveri.com CDS API entegrasyonu
  BTF Amnesia korumalı (gelecek veri sızıntısı engellendi)
```

### 17A.2 Temel Scriptler

```python
# SCRIPT 1: collect_evening.py
# TCMB rezerv ve döviz güncelleme (her akşam 20:00)
# Kaynak: EVDS API (TP.AB.N06, TP.HPBITABLO1.11)
# Hedef: daily_blind_flight_snapshot.csv

# SCRIPT 2: fetch_cds_data.py
# fveri.com CDS API (günlük)
# URL: https://fveri.com/api/v1/cds/turkiye/export
# Hedef: cds_turkiye.csv
# Eşikler: <300bp stabil | 300-400 prep | ≥400 kriz (κ≥+3σ satış şelalesi)

# SCRIPT 3: sync_tr_uk_data.py
# TR ve UK panel senkronizasyonu (haftalık)
# Kaynak: EVDS + World Bank + BDDK
# Hedef: tr_uk_panel_weekly.csv

# SCRIPT 4: tr_uk_pipeline.py
# L1-L4 hesaplama (veri güncellenince otomatik)
# Çıktı: tr_uk_calculation_results.json
# Format: {date, L1_zscore, L2_zscore, L3_zscore, L4_zscore, ...}
```

### 17A.3 BTF Amnesia Veri Ayrışması

```
BACKTEST verisi:   series_1994_2024.csv   (geçmiş — Amnesia güvenli)
REALTIME verisi:   series_2025_2026.csv   (anlık — canlı besleme)
YASAKLI birleşim:  series_1994_2026.csv   (geçmişi gelecekle kirletir)

Veri Güven Sicili (Data Trust Registry):
  A sınıfı: TCMB/BDDK resmi kayıt → ✅ güvenilir
  B sınıfı: dolaylı proxy (yfinance, Bloomberg screening) → ⚠️ Assumed
  C sınıfı: simüle/inferred → ⚠️ Assumed + C etiketi zorunlu
```

### 17A.4 Gerçek Zamanlı CDS Eşikleri

```
CDS_5Y < 300 bp   → Stabil rejim (düşük risk algısı)
CDS_5Y = 300-400  → L1 alarm hazırlık safhası (T2SAIM izleme modu)
CDS_5Y ≥ 400      → Sistemik kriz tetikleyici:
                     κ ≥ +3.00σ satış şelalesi başlar
                     Veritas Protokolü: L1 likidite çarpanı aktive

Haziran 2026 değeri: 238.47 bp (stabil bantda, ama L1=+5.65σ çelişkisi)
Neden çelişki? → CDS piyasası ortodoks politika geçiciliğini fiyatlamıyor
                  Ama yapısal stres (L1) EVDS verilerinde görünüyor
```

---

