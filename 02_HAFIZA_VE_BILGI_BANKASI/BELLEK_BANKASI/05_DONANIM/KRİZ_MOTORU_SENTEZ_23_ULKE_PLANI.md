# 🏛️ T2SAIM KRİZ MOTORU — MİMARİ SENTEZ + 23 ÜLKE GENİŞLETME PLANI (OKF)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026
**Kaynak:** `crises/Kaptan` külliyatı Red Team denetimi (400 formül + 3 motor + veri haritası)

---

## 1. MEVCUT SİSTEMİN TAM MİMARİSİ (3 Motor + 1 Harita)

```
┌────────────────────────────────────────────────────────────────────┐
│  T2SAIM KRİZ MOTORU EKOSİSTEMİ (jet değil, gün gün)               │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  MOTOR 1: t2saim_daily_life_simulation_engine.py (16KB)           │
│  → GÜN GÜN hayat ritmi · 16 çekirdek formül · TEK skor Φ           │
│  → Kriz rejimi + 60 günlük borsa bandı/hedef                       │
│  ⚠️ Demo veri hardcoded (THYAO 4 gün) — CANLI VERİ YOK!            │
│                                                                    │
│  MOTOR 2: t2saim_master_dzv_crisis_engine.py (12KB)               │
│  → 1900-2026 walk-forward · Amnesia λ=0.15 · A_load · Kuple R(t)   │
│  → 13 kriz %100 ispat (US_MASTER csv) · backtest                  │
│  ⚠️ US 1900-2026 CSV — canlı değil                                │
│                                                                    │
│  MOTOR 3: generate_crisis_data.py (11KB)                          │
│  → TR günlük kriz indeksi (formül 1-11) · B: veri okur             │
│  → USDTRY + vol + panel → CI/SRI/Amnesia → tarkan_index.html       │
│  ⚠️ 700 gün pencere · B kasa okuma                                 │
│                                                                    │
│  HARİTA: T2SAIM_HARISELDON_TUM_FORMULLER_VE_VERI_GIRDI_HARITASI    │
│  → 58 formül 8 katman + 20+ veri kaynağı eşlemesi                 │
│  → Her formülün CSV/API/DuckDB kaynağı                              │
└────────────────────────────────────────────────────────────────────┘
```

## 2. RED TEAM KRİTİK BULGULARI

| # | Bulgu | Durum |
| :--- | :--- | :--- |
| 1 | **"400 formül" = kavram**; çekirdek daily motorda ~16 formül; tam 400 ekosisteme (8 katman) dağılı | ⚠️ tek motorda değil |
| 2 | **3 motor demo/sabit veriyle**; canlı veri bağlantısı YOK | 🔴 Kaptan'ın "veri sistemi yok" tespiti DOĞRU |
| 3 | Borsa hedef formülleri **sabit çarpan** (%18/-%30/%45) — gerçek fiyat modeli değil | ⚠️ basit ama çalışır |
| 4 | Hurst **kural tabanlı** (0.62/0.45) — gerçek MFDFA değil | ⚠️ çekirdek için yeterli |
| 5 | `process_daily_step` point-in-time sızıntı kalkanı + Amnesia λ=0.15 DOĞRU | ✅ |
| 6 | A_load/PFC(κ=5.0464)/K_eff≥0.08/Hawkes DOĞRU | ✅ |
| 7 | 13 ABD krizi %100 yakalama, 60-90 gün lead time, yanlış alarm %7.3 | ✅ ispat |

## 3. 23 ÜLKEYE GENİŞLETME PLANI (Temel: bu 3 motor + harita)

### Adım A — Veri Katmanı (Kaptan'ın asıl eksiği)
Her ülke için:
```
ulke_veri_paketleri/{ÜLKE}/
├── data/FRED/*.csv      (döviz, CPI, faiz, rezerv — PACKAGE dizini)
├── data/LOCAL/*.csv     (borsa, takas, haber duygusu — yerel)
├── VERI_MANIFEST.md     (hangi değişken hangi dosyadan)
├── SARTNAME.md          (ülkeye özgü eşikler)
└── KRIZ_KATALOGU.md     (ülkenin kriz kronolojisi — kalibrasyon)
```
**Zaten var:** `Picard_Report/ulke_veri_paketleri/` 17 ülke (CN/RU/BR/MX/SA + TW/KR/CH/IN/AU/IT/NL + CL/CD/ID/ZA/KZ) + TR/JP/US/UK/DE/HK → **23 ülke**

### Adım B — Motor Bağlama
`t2saim_daily_life_simulation_engine.py` → 23 ülke:
- `DailyCountryTelemetry` (ülke telemetri) → `country_sensor.py` FRED verisiyle besle
- Her ülke günlük: telemetri → 16+ formül → Φ skor → karar → borsa bandı
- Kod: `t2saim_daily` motoru ülke-agnostik yap (şu an TR demo var)

### Adım C — Günlük Cron (jet değil, hayat)
- Her gün 09:00 UTC → 23 ülke için veri çek → motor çöz → Φ çıkar → karar
- Çıktı: `kriz_takvimi_{tarih}.md` (23 ülke günlük durum)
- Amnesia + sıfır sızıntı (λ=0.15)

### Adım D — Doğrulama (8 kriz standardı)
- 1900-2026 walk-forward ile **her ülkenin 8+ krizinin %100 yakalanması** ispatı
- Lead time 60-90 gün, yanlış alarm ≤%7.3

---

## 4. HEMEN YAPILACAKLAR (Picard — bu sentezden türeyen)

1. `t2saim_daily_life_simulation_engine.py`'yi **ülke-agnostik** yap (country telemetry → FRED → Φ)
2. `country_sensor.py` ile birleştir (2 UCI → Φ + sensör)
3. 23 ülke FRED verisi → günlük besleme scripti
4. Cron: günlük 09:00 UTC kriz takvimi
5. 8 kriz backtest doğrulaması (her ülke)

## 5. MİMARI İLKE (Kaptan'ın "jet değil")
- Her ülke **gün gün** işlenir (chronicle, cron)
- Tek skor → karar → borsa hedefi (60 günlük bant)
- Amnesia sıfır sızıntı + λ=0.15
- 23 ülke aynı formüllerle, farklı veri/eşikle

---

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
