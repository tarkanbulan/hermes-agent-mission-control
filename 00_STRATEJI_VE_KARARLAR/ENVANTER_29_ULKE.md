# 📊 T2SAIM BİLGİ BANKASI — 29 ÜLKE VERİ ENVANTERİ (26.08.2026)

**Üretici:** Komutan Picard · **Kaynak:** World Bank API + FRED · **Kapsam:** 29 ülke makro 50-yıl
**İlke:** Gerçek veri (World Bank/FRED), sentetik yok · Veritas Per Se

---

## 1️⃣ ULUSAL VERİ PAKETLERİ (World Bank API — 50 YIL 1976-2025)

**28/29 ülke TAM (5 gösterge):** CPI(enflasyon) · DOD(borç/GSYH) · FX(kur) · GDP(GSYH $) · RES(döviz rezerv)

| Ülke | Seri | Ülke | Seri | Ülke | Seri | Ülke | Seri |
|:---|:---:|:---|:---:|:---|:---:|:---|:---:|
| AE (BAE) | 5 | AU | 5 | BR | 5 | CA | 5 |
| CD (Kongo) | 5 | CH | 5 | CL | 5 | CN | 5 |
| DE | 5 | ES | 5 | FR | 5 | GB (İngiltere) | 5 |
| HK | 5 | ID | 5 | IN | 5 | IT | 5 |
| JP | 5 | KR | 5 | KZ | 5 | MX | 5 |
| NL | 5 | QA | 5 | RU | 5 | SA | 5 |
| SG | 5 | TR | 5 | US | 5 | ZA | 5 |

**Toplam:** 28 ülke × 5 = **140 ulusal seri** (1976-2025)

**EKSİK:**
- ❌ **TW (Tayvan):** World Bank'ta bu göstergeler yok (0) — IMF/yahoo alternatif gerek
- ⚠️ **UK klasörü:** boş kopya (İngiltere = GB olarak dolu)

---

## 2️⃣ FRED DATA KLASÖRÜ (Silvana/DATA) — 58 CSV

| Ülke | Seri | Ülke | Seri |
|:---|:---:|:---|:---:|
| JP | 7 (DEXJPUS/10Y/M2/JPNASSETS/RBJPBIS/tmp) | DE, CN, GB, FR, IT, ES... | 1-2 |
| TR | US serileri (DEXTHUS/CPI/faiz/ity...) | AE,AU,BR,CA,CD,CH,CL,DE,HK,ID,IN,IT,KR,KZ,MX,NL,QA,RU,SA,SG | 1'er |

**Kritik FRED serileri (50-yıl):** TR_DEXTHUS, TR_CPI, US_GS10/M2/T10Y2Y/TB3MS/TEDRATE/VIX, JP_DEXJPUS/10Y/M2

---

## 3️⃣ TOPLAM
- **Ulusal (World Bank):** 28 ülke / 140 seri / 50-yıl
- **FRED:** 58 CSV (TR+JP+US zengin + diğer ülkeler FX/CPI)
- **Eksik:** TW (Tayvan) — World Bank'ta veri yok

---

## 4️⃣ KAYNAK YOLLARI
- Ulusal paketler: `Picard_Report\ulke_veri_paketleri\{CO}\data\*_50y.csv`
- FRED: `Silvana\DATA\*.csv`

*Veritas Per Se — Envanter kalıcı bilgi bankası kaydı 🖖*
