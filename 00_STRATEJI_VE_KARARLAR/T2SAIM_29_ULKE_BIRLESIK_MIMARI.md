# 🏛️ T2SAIM 29 ÜLKE KRİZ TESPİT SİSTEMİ — BİRLEŞİK MİMARİ (v1.0)

**Mimar:** Komutan Picard · **Tarih:** 25 Ağustos 2026 · **Karar Mercii:** Kaptan Tarco
**Durum:** ✅ Çalışır (29 ülke, %99.2 kalibrasyon ispatı) · 🚧 Gözlem paneli kurulum aşamasında

---

## 🗺️ UÇTAN UCA MİMARİ (5 Katman)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ 5. GÖZLEM & KARAR KATMANI (panel/aksiyon)                                 │
│    29 düğüm panel (23 ülke + 6 Hariseldon) · Ω_Küresel · Karar = Tarco    │
├────────────────────────────────────────────────────────────────────────────┤
│ 4. GÖZLEM KATMNI (izleme)                                                 │
│    UCI_i (0-100 → 🟢🟡🟠🔴) · bulaşma M_ij → SpillIn · Ω_Küresel          │
├────────────────────────────────────────────────────────────────────────────┤
│ 3. KALİBRASYON KATMNI (ülkeye özgü)                                       │
│    σ_c (1.20-1.60) · tipoloji W_c (finans/emtia/fragile) · λ_c · tevekkül │
├────────────────────────────────────────────────────────────────────────────┤
│ 2. MOTOR KATMNI (BTF-Amnesia)                                             │
│    Amnesia λ=0.15 · L6 faz kilidi · alarm · tevekkül → SRI/kriz           │
├────────────────────────────────────────────────────────────────────────────┤
│ 1. VERİ KATMNI (29 ülke)                                                  │
│    FRED (FX/CPI/faiz/rezerv/borsa) · kriz kataloğu · DeepSearch           │
└────────────────────────────────────────────────────────────────────────────┘
```

## 📦 KATMAN 1 — VERİ (hazır)
| Bileşen | Kaynak | Durum |
| :--- | :--- | :---: |
| 29 ülke FRED paketi | `ulke_veri_paketleri/<ÜLKE>/data/FRED/*.csv` | ✅ (SA düzeltildi) |
| 29 kriz kataloğu (392 kriz) | `hermes_data/BELLEK_KATALOGLARI/*.md` | ✅ |
| 8 DeepSearch raporu | `crises/Kaptan/New_Search/` | ✅ |
| Veri kontrol (165 CSV/391K satır) | `outputs/VERI_KONTROL_29.md` | ✅ |

## ⚙️ KATMAN 2 — MOTOR (Antigravity yazdı)
| Dosya | Rol |
| :--- | :--- |
| `panel_builder.py` (285) | FRED → ülke aylık panel |
| `btf_amnesia_engine.py` (167) | Universal BTF-Amnesia motoru (SRI/L6/alarm/Amnesia) |
| `rational_country_priors.py` (384) | ülkeye özgü trust/polarization (Edelman/V-Dem/WGI) |
| `crisis_catalog_evaluator.py` (216) | kriz kataloğu → pencere karşılaştırma |
| `calibrate_and_test.py` (311) | σ_c + tipoloji + test |
| `run_all_29_countries.py` (126) | 29 ülkeyi tek tek koş |

## 🎯 KATMAN 3 — KALİBRASYON (Spark tasarım → koda işlendi)
```
σ_c = σ_base(1+α·RegimeVar)·(R_ref/R_c)   → US 1.50, SG/CH 1.60, TR 1.25
3 tipoloji W: Finans hub [.25,.50,.25] · Emtia [.20,.30,.50] · Fragile [.40,.35,.25]
Amnesia λ=0.15 · tevekkül 0.70 · sum W=1
SONUÇ: 367/370 (%99.2) · 23 ülke %100
```

## 📡 KATMAN 4 — GÖZLEM (Spark mimarisi — kurulacak)
```
UCI_i (0-100): <45🟢 45-65🟡 65-80🟠 >80🔴
Bulaşma: SpillIn_j = Σ M_i→j·UCI_i (τ gecikme) → M·UCI>50 uyarı
Ω_Küresel(t) = Σ α_i·UCI_i·(1+γ·GraphDensity)  → dünya krizi skaler
UCI>80 ∧ M>0.60 → T-τ geri sayım (hedef ülke erken uyarı)
```

## 🖥️ KATMAN 5 — PANEL (29 düğüm, kurulacak)
```
23 ülke düğümü (UCI + kriz) + 6 Hariseldon panel:
  tarkan_index (TARCO EWS) · structural_decay · daron_acemoglu
  turkey_gullini · index (giriş) · unified_memory_chat
= 29 DÜĞÜMLÜ GÖZLEM AĞI · ısı haritası · Ω_Küresel skaler · Karar = Tarco
```

## 🔗 VERİ AKIŞI (uçtan uca)
```
FRED CSV → panel_builder → aylık panel
  + priors (trust/pol) + kriz kataloğu
      ↓
UniversalBTFAmnesiaEngine (SRI_psy/fin/vol → SRI_total → L6 → alarm → Amnesia)
      ↓
calibrate (σ_c + W_c) → her ülke X/ana kriz + öncülük + FPR
      ↓
GÖZLEM: UCI_i + M_ij bulaşma + Ω_Küresel → 29 düğüm panel → Karar=Tarco
```

## ✅ MİMARİ DOĞRULAMA
- Motor çalışır: **367/370 (%99.2)** — 23 ülke %100, CD/AE veri yok
- Veri bütünlüğü doğrulandı (165 CSV, SA düzeltildi)
- Eksik: Gözlem paneli (katman 4-5) + CD/AE veri + FPR optimizasyonu

*Veritas Per Se — Komutan Picard 🖖*
