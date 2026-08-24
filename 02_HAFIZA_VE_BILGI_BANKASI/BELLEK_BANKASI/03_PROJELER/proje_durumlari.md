# 🗂️ PROJELER — Durum Haritası

> Kaynak: Hermes MEMORY.md (2026-08-24).

## Kriz Sistemi (17 ülke)
- Kriz SENSÖR = 17 ülke (TR/JP/US/EU/HK/UK HARİÇ): TW/KR/CH/IN/AU, IT/NL, CL/CD/ID/ZA/KZ, CN/RU/BR/MX/SA.
- Paket: `Picard_Report/ulke_veri_paketleri/` (manifest+şartname+katalog+FRED).
- Kod: `country_sensor.py` + overrides + extensions + `ubtf_walkforward.py` (BTF gün gün).
- İCRA 6 piyasa ayrı. ABD EWS σ-tabanlı eşik.

## Prediction_Project
- DEMO veri (B-1) — 35/35 test geçer. DNA = `GünlükBülten.md` 16×.
- Formüller CONFIDENTIAL. %160 ≈ %164.8.
- DZV'suz mekanik test şart (DuckDB + amnezi).
- FRED anahtarsız: `fredgraph.csv?id=X`. ABD_crises = şablon.

## state.db Temizliği (24 Ağu)
- picard 813 / cyberknife 750 / global 924MB → eski session yok.
- Kaptan 4-plan: yedek(db_yedek_20260824) + RAG entegre (.md dışa → NotebookLM/OpenViking) + Hermes KAPALIYKEN temizle(--gun14, VACUUM).
- state.db zaman EPOCH & ISO karışık → script otomatik algılar (temizle_state_db.py).
- Canlıda ASLA VACUUM. Hermes-Bot-Mode gömülü; `hermes update` gerekli (7148 geri).
