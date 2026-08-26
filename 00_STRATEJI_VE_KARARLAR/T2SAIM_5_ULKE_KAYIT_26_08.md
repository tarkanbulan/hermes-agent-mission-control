# 📋 T2SAIM ÜLKELER — 5 ÜLKE KAYIT (Kılavuz + Ek Bilgiler + Analiz) — 26.08.2026

**Üretici:** Komutan Picard · **Kapsam:** TR/JP/US/TW/SA EWS kılavuzları okundu + analiz + ek bilgi talepleri

---

## 1️⃣ ÜLKE EWS KILAVUZLARI (hepsi production kodlu, v5.0)

| Ülke | Dosya | UCI formülü | Ağırlıklar (k) | Ana kanal |
|:---|:---|:---|:---|:---|
| 🇹🇷 **TR** | `t2saim-turkiye-ews-mimari-kilavuz` | 1−e^(−1.45·[...]) | k=1.45 [.25/.20/.20/.20/.15] | Kur/borç + Gullini (G_def .782) + Minsky t*=18Kas7 |
| 🇯🇵 **JP** | `t2saim-japonya-ews-mimari-kilavuz.md` | 1−e^(−1.45·[...]) | k=1.45 [.25/.20/.25/.15/.15] | Yen Carry + Basis Swap (>60bp) + BoJ holding |
| 🇺🇸 **US** | `t2saim-abd-ews-mimari-kilavuz.md` | 1−Π(1−Φ) | Ω_US = 1−prod | Yield curve + NetLiq (WALCL-TGA-RRP) + dinamik σ |
| 🇹🇼 **TW** | `t2saim-tayvan-ews-mimari-kilavuz.md` | 1−e^(−1.50·[...]) | k=1.50 [.30/.25/.15/.20/.10] | TSMC lead + enerji %98 ithal + Boğaz |
| 🇸🇦 **SA** | `t2saim-suudi-arabistan-ews-mimari-kilavuz.md` | 1−e^(−1.50·[...]) | k=1.50 [.25/.25/.20/.15/.15] | Petrol breakeven $85-90 + SAMA + de-peg + PIF |

**Ortak:** λ=0.15 amnezi · Σ=1.25 · sıfır sızıntı BTF · 5 katman (Macro/Bank/Neuro/Gullini/Acemoglu) · walk-forward

---

## 2️⃣ EK BİLGİ TALEPLERİ (toplu — 5 ülke)

### TR
1. TCMB EVDS API key (CBRT_EVDS_API_KEY) · 2. CDS 5Y canlı · 3. Güven/kutuplaşma (TÜİK+WGI/V-Dem) · 4. 191B$ dış borç itfa · 5. 52 olay kriz zaman damgaları

### JP
1. JP 5Y CDS · 2. BoJ JGB holding share (>50?) · 3. CFTC JPY limit (50k) · 4. Teikoku iflas serisi · 5. Watanabe/FX marjin (FFAJ) · 6. 3M USD/JPY basis

### US
1. US 5Y CDS · 2. Sole-Source oranı (USAspending) · 3. SEC restatement LM-2 · 4. EPU (USEPUINDXD) · 5. FERC trafo kuyruğu · 6. MMF v_run

### TW
1. TSMC lead time (TEJ/proxy) · 2. Enerji rezerv marjı (Taipower) · 3. Boğaz WRP (Lloyd's) · 4. ADIZ sorti (MND) · 5. DEXTWUS+^TWII+SOX tarihsel

### SA
1. SAR 12M fwd puanları (canlı) · 2. Brent $71 vs breakeven $88.5 · 3. SAMA NFA (410 vs eşik 550) · 4. Bank LDR (%%) · 5. PIF ihale HHI kaynak · 6. Hürmüz v_run (MarineTraffic AIS) · 7. Sukuk 5Y CDS canlı

---

## 3️⃣ VERİ DURUMU (Karargâh'ta mevcut)
- **14 seri mevcut:** B:\Classified\veriler\FRED_DATA (DEXTHUS/DEXJPUS/WALCL/TEDRATE/TB3MS) + macro_data (M2SL/T10Y2Y/DGS10) + ABD_crises\data\FRED (SOFR/RRPONTSYD) + Veri_Bankasi VIXCLS + Digital_SIM TR CPI
- **Eksik:** JP RBJPBIS/JPNASSETS, TW kılavuz verileri, SA SAMA/SAIBOR/forward — temin edilecek

---

*Veritas Per Se — Komutan Picard · 5 ülke EWS kayıt + ek bilgi toplu talep + veri durumu.*
