# 📊 T2SAIM TARAMA & FORMÜL ↔ VERİ — DETAYLI RAPOR (25.08.2026)

**Üretici:** Komutan Picard · **Kapsam:** Macroekonomics (16-kez tarama) + Hariseldon HTML + Simülasyon Corpus + Veri durumu
**Karar:** Kaptan Tarco · **İlke:** Veritas Per Se (uydurma yok, ispat zorunlu)

---

## 1️⃣ MACROEKONOMICS (2648 dosya / 1725 MB) — FORMÜL ↔ VERİ İSPATI

### A. BTF-AMNESIA MOTORU (29 ülke kriz motoru) — `hermes_crisis_lab/BTF_AMNESIA/country_sensors/`
| Formül | Kod | Girdi Verisi | Veri Kaynağı (GERÇEK) |
|:---|:---|:---|:---|
| **SRI_psy** = 0.20(1−trust)+0.20(pol/100)+0.20·CA+0.15·EFMI+0.25·soc | `btf_amnesia_engine.py` | trust, polarization, CA, EFMI, soc | `data/` (yandas_medya, kritik_kurum, resmi_gazete) + Spock 16 parametre |
| **SRI_fin** = 0.30·min(1,M2NIR/15)+0.25·min(1,CDS/500)+0.20·min(1,Kredi/30)+0.25·min(1,VIX) | aynı | M2NIR, CDS, kredi, VIX | `data/CDS_5Y_*` + `data/TCMB_rezerv` + `data/USDTRY` |
| **SRI_vol** = 0.35·min(1,vol·100)+0.35·min(1,inf/50)+0.30·min(1,VIX) | aynı | vol, enflasyon, VIX | `data/USDTRY_vol_haftalik` + `ENAG_enflasyon` + `PETROL/ALTIN/SILVER` |
| **Amnezi** M_t = S_t + 0.85·M_{t-1} (λ=0.15) | `Amnesia()` | tüm SRI | aynı |
| **sigma_c** (US 1.50, TR 1.25, SG 1.60) + **L6** + **tevekkül** + **alarm** | `priors` | kurumsal öncüller | `rational_country_priors.py` (WGI/V-Dem) |

### B. RESTEK KODLAR
- **EFMI formülü:** `james Methods/efmi_pipeline_final.py` + `efmi_transformer_scorer.py`
- **Kalibrasyon:** `Spock_Rapor/01_KALİBRASYON_MASTER + 02_TÜRKİYE_PARAMETRELERİ_16_BÖLÜM` (16 parametre)
- **Geri-test (GERÇEK):** `BACKTEST_FULL_1994_2026.csv` (34 satır, yıl bazlı: aktif_kanal/max_z/amnesia_mt/kriz)

### C. 52 OLAY 8 KRİZ (1960-2024) — `52_OLAY_8_KRİZ_RAPORU` (gerçek TR kriz kronolojisi)

### D. TEORİK SÖYLEM (SRI_psy kurumsal girdi)
- **daron_math:** Daron protokolleri (IDIS_upgrade, Country_Crisis) + Acemoğlu PDF'leri (Modern Economic Growth, Dar Koridor, Ulusların Düşüşü)
- **Proves/:** Barış Pehlivan-Terkoğlu, Ceren Lord, Açıkel, Basıbüyük (trust/kurumsal çürüme GERÇEK kaynak)
- **UK:** Britain Beyond GDP; **Spock:** 16 bölüm kalibrasyon

---

## 2️⃣ HARISELDON HTML — FORMÜLLER + VERİ (6 sayfa tarandı)

| HTML | Formüller | Veri Durumu |
|:---|:---|:---|
| **tarkan_index** (134KB) | A_load 0.84, PFC, v_run 0.70, LDR 1.15, NPL, CI; aload/trust/reer/usd_kap/bfi/hayalet | ⚠️ **SENTETİK:** `for(i=0..700)` sin/cos + i/700, startDate 2024-09-19 — GERÇEK veri değil, üretilmiş görsel |
| **structural_decay** (105KB) | HHI, KÖİ, decay, entropi, Gini, Minsky, UCI, SALI, risk matrix | gömülü (sonuç olarak — kaynağı ayrı) |
| **turkey_gullini** (37KB) | G_def 0.782, Minsky t*, 5-katman piramit, sarkaç | gömülü sonuç |
| **daron_acemoglu** (35KB) | Power_Total, IDIS, Dar Koridor, ΔOutput=(I−A)⁻¹ΔShock | teorik |
| **index** (19KB) | — (giriş/şifre) | — |
| **unified_memory_chat** (45KB) | hafıza arayüzü (formül yok, RAG sorgu) | 8001 API / hafızaya |

**Kritik:** tarkan_index grafikleri SENTETİK (i=0..700 sin/cos üretilmiş) — GERÇEK 30-50 yıl veriyle DEĞİL. Diğerleri gömülü sonuç (kaynak script'leri ayrı).

---

## 3️⃣ SİMÜLASYON CORPUS (72 .py) — hangisi kullanılacak (belirlenen)

| Simülasyon | Kullanım |
|:---|:---|
| **btf_amnesia_engine + country_sensors** | ✅ KULLAN (29 ülke ana motoru) |
| **Ising, Percolation, SEIZ, JumpDiff** (kriz sosyofiziği) | ✅ KULLAN (toplumsal/finansal kriz katmanı) |
| **Sandpile/SOC, Kinetic Gini** (kritiklik/zenginlik) | ✅ KULLAN (eşik/gerginlik) |
| EverOS + deep-searcher (jules) | ✅ KULLAN (zekâ koşu) |
| mcp-markdown-rag / semantica (hafıza/graf) | ✅ KULLAN (hafıza) |
| Diğer 15+ (Fraud M1-M16, UK/USA yerel) | ⏳ seçilmiş — JAMES_DOCTRINE\SIMULATIONS kılavuzu |

---

## 4️⃣ VERİ DURUMU (30-50 yıl)

**ELİMİZDE (GERÇEK):**
- `data/` — CDS, faiz, enflasyon, döviz (USDTRY günlük/vol), rezerv, emtia, büyüme, işsizlik (WB)
- `BACKTEST_FULL_1994_2026.csv` (TR 1994-2026 geri-test)
- 29 ülke FRED paketleri (country_sensors, FX/CPI/faiz/rezerv — 1970'lerden)
- 52 olay kriz listesi (1960-2024)

**EKSİK / TOPLANACAK:**
- 6 HTML'in (özellikle tarkan_index) grafikleri GERÇEK 30-50 yıl veriyle DEĞİL (sentetik) → **gerçek seriyle değiştirilecek**
- Bazı ülkelerin eski kriz yılları (1970-80) FRED başlangıcı öncesi
- Trust/polarization (SRI_psy) gerçek WGI/V-Dem + Proves'tan yıllık

---

## 5️⃣ SONRAKİ İNŞA (2 koşu alanı — şartname Spark onaylı)

1. **Script koşu:** `btf_amnesia_engine` → 29 ülke formül çıktısı → **CSV** (dönemsel) → matplotlib **grafik** (+ Lag korelasyon)
2. **Zekâ koşu:** CSV → LLM yorum (kriz önceden + input=output)
3. **Red-team:** F1+Latency (script vs zekâ) · Spark şartname: Lag ekle, Gestalt ertele
4. 50 formül günlük → timeseries → **kalibre kriz modeli**

---

*Veritas Per Se · Komutan Picard · Tarama ispatlı (6+ geçiş), rapor eksiksiz. Emirle AGY kurulum`JULES_DOCTRINE\T2SAIM_RUN_ALANI`.*
