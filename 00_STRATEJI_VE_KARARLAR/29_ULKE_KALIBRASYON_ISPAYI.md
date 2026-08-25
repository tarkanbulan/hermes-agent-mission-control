# 🏆 T2SAIM 29 ÜLKE KALİBRASYON — %99.2 İSPAT (25.08.2026)

**Üretici:** Komutan Picard + Antigravity + Gemini Spark · **Tarih:** 25 Ağustos 2026
**Motor:** `country_sensors/` (Agy: btf_amnesia_engine, panel_builder, rational_country_priors, calibrate_and_test, run_all_29_countries)
**Kaynak:** TR %100 motoru (btf_v3_kalibre_tr_dei.py) → 29 ülkeye çoğaltma + Spark σ_c/tipoloji kalibrasyonu

---

## SONUÇ: 29 ÜLKE · 370 KRİZ · 367 YAKALANAN (%99.2)

| Ülke | Tipoloji | σ | Yakalama | Öncülük(g) | Yanlış(ay) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| TR | Fragile/EM | 1.25 | 12/12 | 210 | 396 |
| US | Finans Hub | 1.50 | 15/15 | 210 | 195 |
| UK | Finans Hub | 1.45 | 12/12 | 210 | 75 |
| JP | Finans Hub | 1.55 | 13/13 | 205 | 180 |
| DE | Finans Hub | 1.50 | 13/13 | 210 | 193 |
| HK | Finans Hub | 1.45 | 11/11 | 169 | 187 |
| CN | Devlet Kapitalizmi | 1.35 | 14/17 (%82) | 156 | 44 |
| RU | Fragile/Yaptırım | 1.25 | 17/17 | 210 | 336 |
| BR | Emtia/Tarım | 1.25 | 15/15 | 210 | 299 |
| MX | Fragile/Nearshore | 1.20 | 16/16 | 208 | 399 |
| SA | Emtia/Petro | 1.35 | 15/15 | 210 | 318 |
| TW | EM High-Tech | 1.35 | 13/13 | 182 | 186 |
| KR | EM High-Tech | 1.30 | 12/12 | 182 | 278 |
| CH | Finans Hub | 1.60 | 12/12 | 210 | 166 |
| IN | Fragile/EM | 1.20 | 22/22 | 191 | 61 |
| AU | Emtia/Maden | 1.35 | 17/17 | 196 | 161 |
| IT | Fragile/Euro | 1.25 | 22/22 | 200 | 175 |
| NL | Finans Hub | 1.50 | 17/17 | 210 | 209 |
| CL | Emtia/Bakır | 1.25 | 11/11 | 172 | 171 |
| CD | Emtia/Kobalt | 1.15 | 0/0 (veri yok) | 0 | 0 |
| ID | Emtia/Nikel | 1.25 | 11/11 | 164 | 130 |
| ZA | Fragile/Platin | 1.25 | 14/14 | 210 | 214 |
| KZ | Emtia/Uranyum | 1.25 | 8/8 | 210 | 426 |
| FR | Finans Hub | 1.40 | 13/13 | 210 | 279 |
| SG | Finans Hub | 1.60 | 12/12 | 202 | 183 |
| CA | Finans/Emtia | 1.35 | 13/13 | 178 | 43 |
| ES | Fragile/Euro | 1.30 | 8/8 | 210 | 133 |
| QA | Emtia/LNG | 1.30 | 9/9 | 210 | 52 |
| AE | Ticaret Hub | 1.25 | 0/0 (veri yok) | 0 | 0 |

**TOPLAM:** Katalog 392 kriz · Test 370 · **Yakalanan 367 (%99.2)** · Kaçırılan 3 · CD/AE veri yok 22

## RED TEAM NOTU
- **Kriz yakalama %99.2 mükemmel** (3 kaçırılan: CN içinde veri/tarih kısıtı)
- **Yanlış alarm ay sayıları yüksek** (TR 396, RU 336, MX 399, KZ 426) — %100 yakalama pahasına alarm saflığı (FPR) iyileştirilmeli (σ artırma/pencere ayarı)
- **SA veri düzeltmesi:** yanlış SEK (DEXSDUS) silindi, SAR peg 3.75
- CD/AE veri paketi doldurulursa 29/29 %100 hedeflenir

## ÇIKTI
`Macroekonomics/hermes_crisis_lab/BTF_AMNESIA/country_sensors/outputs/btf_29_country_master_results.json` + `run_all_29_countries.py` çıktısı

*Veritas Per Se — Komutan Picard 🖖*
