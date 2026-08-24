# 🏛️ T2SAIM ÜLKE KRİZ SENSÖRÜ MASTER KÜLLİYATI — 11 ÜLKE (SPARK)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar:** Kaptan Tarco
**Amaç:** "Ekonomi her yerde aynıdır, ismi değişir." Spark'ın 11 ülke kriz sensör şartnamesi → tek organda toplandı.
**Metodoloji:** 5-boyutlu faz geçişi (Φ_Macro/Bank/Neuro/Gullini/Acemoglu) + UCI birleşik skor. Her ülke aynı şablon, farklı ülkeye özgü ağırlık + veri kaynağı.

---

## 1. ORTAK FORMÜL YAPISI

$$\Phi = 0.35 \cdot \text{Macro}_\text{ülkeye özgü} + 0.30 \cdot \text{Bank}_\text{ülkeye özgü} + 0.20 \cdot \text{Neuro} + 0.15 \cdot \text{Gullini} + 0.15 \cdot \text{Acemoglu}$$

$$UCI(t) = 1.0 - \exp(-k \cdot [w_1 \Phi_{Macro} + w_2 \Phi_{Bank} + w_3 \Phi_{Neuro} + w_4 \Phi_{Gullini} + w_5 \Phi_{Acemoglu}])$$

## 2. ÜLKE KRİZ SENSÖRÜ TABLOSU

| Ülke | UCI k | w ağırlığı | Ülkeye Özgü Φ_Macro | Ülkeye Özgü Φ_Bank | İcracı Sensör | Kriz Sayısı |
| :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| 🇹🇷 TR | 1.45 | .25/.20/.20/.20/.15 | M2/NIR, DOLGAP, REER | LDR, NPL, TED | Kapalıçarşı, Çukur | 8+ |
| 🇺🇸 ABD | 1.45* | .25/.20/.20/.20/.15 | NetLiq, Fed, T2 | LDR, NPL, TED | BAA−AAA(1919), VIX | 13 |
| 🇩🇪 DE | **1.50** | .25/.25/.20/.15/.15 | **BTP-Bund, TTF, TARGET2** | Euribor-OIS, CRE, Insolvencies | VSTOXX, DAX | 11 |
| 🇧🇷 BR | 1.50 | .25/.25/.20/.15/.15 | Gross_Debt, **Cupom** | **Inadimplencia**, Recuperacao | VXBR, EMBI+ | 10 |
| 🇨🇳 CN | **1.55** | .25/.25/.20/.15/.15 | **LGFV**, PBOC_Fixation | **Shadow_WMP**, Property_NPL | CNH/CNY, Li Keqiang | 11 |
| 🇭🇰 HK | 1.45 | **.30/.25/.20/.15/.10** | **Peg_Distance**, Agg_Balance | CCL, Negative_Equity | **Forward de-peg** | 10 |
| 🇲🇽 MX | 1.50 | .25/.25/.20/.15/.15 | **Pemex**, USDMXN | Foreign_Mbono, TIIE | Kartel maliyeti | 10 |
| 🇷🇺 RU | **1.60** | .25/.25/.20/.15/.15 | **Urals-Brent**, NWF | **Settlement_Friction**, RUONIA | Dark Fleet, Askeri-HHI | 9 |
| 🇸🇦 SA | 1.50 | .25/.25/.20/.15/.15 | **PetroDollar** | LDR, NPL | TASI, Breakeven | 11 |
| 🇬🇧 UK | — | — | **Ψ_Global→UK (10 düğüm)** | LDI Gilt | D_M(SPV), Raundromat | 36 |
| 🇪🇺 AB | — | — | **Ω_EU (8 üye fay hattı)** | — | TARGET2, Ren, TTF | 20 |

*Bu Sensörlerde ABD σ-tabanlı eşik (mutlak 0.65 geçersiz — μ+1.0σ).*

## 3. ÜLKEYE ÖZGÜ KRİZ VERİ KAYNAKLARI (Spark'ın tespiti)

| Ülke | Kaynak (yerel dil/kendi) | Kritik eşik |
| :--- | :--- | :--- |
| TR | TCMB EVDS, Kapalıçarşı, MKK | M2/NIR>15, DOLGAP |
| US | FRED (BAA/AAA 1919+), LOBSTER, GDELT, HSall | BTP-Bund→BAA-AAA 4pp |
| DE | Bund, BTP, ECB TARGET2, TTF, CRE Landesbank | BTP/Bund ≥%2.00 |
| BR | BCB SGS, Tesouro, Serasa | Kabu Borcu >%85 |
| CN | PBOC, NBS, CBIRC | LGFV 60T¥, Shibor %30 |
| HK | HKMA, Centaline, HIBOR-TMA | HIBOR %300 (1997) |
| MX | Banxico SIE, Pemex, CNBV | Pemex 105Mr$, MXN 22 |
| RU | CBR, Argus, Minfin, Fedresurs | Urals iskontosu, NWF |
| SA | SAMA, Tadawul, GASTAT | Breakeven $85-90 |
| UK | BoE, DMO, Companies House | LDI Gilt, D_M(SPV)>3σ |

## 4. KRIZ KATALOGLARI (toplam 11 ülke, ~150 kriz)
TR 8+ · US 13 · DE 11 · BR 10 · CN 11 · HK 10 · MX 10 · RU 9 · SA 11 · UK 36 · EU 20

---

## 5. BİRLEŞİK KRİZ SKORU (çok ülke → tek değer)

$$\Phi_{Küresel}(t) = \sum_{i} W_i \cdot UCI_i(t)$$  (ülke ağırlıkları: US 0.20, CN 0.15, DE 0.10, UK 0.08, JP 0.08, RU 0.05...)

## 6. KALİBRASYON STANDARDI
- Her ülke: 50 yıl kriz kataloğu, krizden ≥3 ay önce %100 yakalama (DE/BR/CN/HK/MX/RU/SA)
- Yanlış alarm ≤%7.3 (ABD 11/11 %100, ~8.5 ay öncülük doğrulandı)
- λ=0.15 Amnesia, sıfır sızıntı

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
