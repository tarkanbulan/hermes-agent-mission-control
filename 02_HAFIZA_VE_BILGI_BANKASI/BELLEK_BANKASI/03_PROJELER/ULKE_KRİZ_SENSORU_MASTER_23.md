# 🏛️ T2SAIM ÜLKE KRİZ SENSÖRÜ MASTER KÜLLİYATI — 23 ÜLKE (TAM)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar:** Kaptan Tarco
**Amaç:** "Ekonomi her yerde aynıdır, ismi değişir." Spark'ın ülke sensörleri + 5 kritik düğüm + külliyat → **23 ülkenin tamamı** tek organda.
**Metodoloji:** 5-boyutlu faz geçişi (Φ_Macro/Bank/Neuro/Gullini/Acemoglu) + UCI birleşik skor. Her ülke aynı şablon, ülkeye özgü ağırlık + veri kaynağı.

---

## 📊 23 ÜLKE KRİZ SENSÖRÜ TABLOSU

| # | Ülke | UCI k | w ağırlığı | Ülkeye Özgü Φ_Macro | Ülkeye Özgü Φ_Bank | Birincil İcra Sensörü | Kriz Sayısı |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | 🇹🇷 Türkiye | 1.45 | .25/.20/.20/.20/.15 | M2/NIR, DOLGAP, REER | LDR, NPL, TED | Kapalıçarşı, Çukur | 8+ |
| 2 | 🇺🇸 ABD | 1.45 | .25/.20/.20/.20/.15 | NetLiq, Fed, T2 | LDR, NPL, TED | BAA−AAA(1919), VIX | 13 |
| 3 | 🇬🇧 İngiltere | 1.45 | .25/.20/.20/.20/.15 | Ψ_Global→UK (10 düğüm) | LDI Gilt | D_M(SPV), Laundromat | 36 |
| 4 | 🇯🇵 Japonya | 1.45 | .25/.20/.20/.20/.15 | Ψ_Global→JP (10 düğüm) | BoJ, LDR | Baz Swap JPY, Yen Carry | 22 |
| 5 | 🇩🇪 Almanya/EU | 1.50 | .25/.25/.20/.15/.15 | **BTP-Bund, TTF, TARGET2** | Euribor-OIS, CRE, Insolvencies | VSTOXX, DAX | 11+20 |
| 6 | 🇭🇰 Hong Kong | 1.45 | **.30/.25/.20/.15/.10** | **Peg_Distance**, Agg_Balance | CCL, Negative_Equity | **Forward de-peg** | 10 |
| 7 | 🇨🇳 Çin | 1.55 | .25/.25/.20/.15/.15 | **LGFV**, PBOC_Fixation | **Shadow_WMP**, Property_NPL | CNH/CNY, Li Keqiang | 11 |
| 8 | 🇷🇺 Rusya | 1.60 | .25/.25/.20/.15/.15 | **Urals-Brent**, NWF | **Settlement**, RUONIA | Dark Fleet, Askeri-HHI | 9 |
| 9 | 🇧🇷 Brezilya | 1.50 | .25/.25/.20/.15/.15 | Gross_Debt, **Cupom** | **Inadimplencia**, Recuperacao | VXBR, EMBI+ | 10 |
| 10 | 🇲🇽 Meksika | 1.50 | .25/.25/.20/.15/.15 | **Pemex**, USDMXN | Foreign_Mbono, TIIE | Kartel maliyeti | 10 |
| 11 | 🇸🇦 Suudi | 1.50 | .25/.25/.20/.15/.15 | **PetroDollar** | LDR, NPL | TASI, Breakeven $85-90 | 11 |
| 12 | 🇹🇼 Tayvan | 1.45 | .25/.20/.20/.20/.15 | **TSMC Lead Time**, Boğaz riski | Kredi/IPO | TAIEX, TSMC sipariş/fatura | 8 |
| 13 | 🇰🇷 Güney Kore | 1.45 | .25/.20/.20/.20/.15 | **10 günlük ihracat**, HBM/DRAM | KOSPI yabancı çıkış | Won/Yen, HBM makası | 10 |
| 14 | 🇨🇭 İsviçre | 1.45 | .25/.20/.20/.20/.15 | **CHF ayrışması**, AT1 CoCo | Banka bilanço | Zürih altın primi | 8 |
| 15 | 🇮🇳 Hindistan | 1.45 | .25/.20/.20/.20/.15 | **Urals→rafineri makası** | NBFC, rezerv | MSCI India/China | 9 |
| 16 | 🇦🇺 Avustralya | 1.45 | .25/.20/.20/.20/.15 | **SGX demir**, AUD/JPY, Li/U | Banka (4 büyük) | Port Hedland, Çin nabzı | 8 |
| 17 | 🇮🇹 İtalya | 1.45 | .25/.20/.20/.20/.15 | **BTP-Bund spread** | NPL, MPS | BTP faizi, NPL oranı | 8+ |
| 18 | 🇳🇱 Hollanda | 1.45 | .25/.20/.20/.20/.15 | **TTF gaz**, ASML sipariş | ING bankacılık | Rotterdam, ASML backlog | 7 |
| 19 | 🇨🇱 Şili | 1.50 | .25/.25/.20/.15/.15 | **Bakır Codelco**, lityum | Banka döviz | LME bakır, madencilik | 6 |
| 20 | 🇨🇩 Kongo | 1.50 | .25/.25/.20/.15/.15 | **Kobalt %73** | Banka zayıf | Cobalt Institute, çatışma | 5 |
| 21 | 🇮🇩 Endonezya | 1.50 | .25/.25/.20/.15/.15 | **Nikel %55**, ihracat yasağı | LDR, NPL | LME nikel, Rupiah | 8 |
| 22 | 🇿🇦 Güney Afrika | 1.50 | .25/.25/.20/.15/.15 | **PGM %75**, Eskom | Banka | Platin/Rodyum, JSE | 9 |
| 23 | 🇰🇿 Kazakistan | 1.50 | .25/.25/.20/.15/.15 | **Uranyum %43** | BTA banka | PURANUSDM, Tenge | 7 |

---

## 🧮 ORTAK FORMÜL (tüm 23 ülke)

$$\Phi = 0.35 \cdot \text{Macro}_\text{ülkeye özgü} + 0.30 \cdot \text{Bank}_\text{ülkeye özgü} + 0.20 \cdot \text{Neuro} + 0.15 \cdot \text{Gullini} + 0.15 \cdot \text{Acemoglu}$$

$$UCI(t) = 1.0 - \exp(-k \cdot [w_1 \Phi_{Macro} + w_2 \Phi_{Bank} + w_3 \Phi_{Neuro} + w_4 \Phi_{Gullini} + w_5 \Phi_{Acemoglu}])$$

## 🔑 ÜLKEYE ÖZGÜ VERİ KAYNAĞI (her ülke kendi dilinde)

| Ülke | Kaynak | Kritik Eşik |
| :--- | :--- | :--- |
| TR | TCMB EVDS, Kapalıçarşı, MKK | M2/NIR>15 |
| US | FRED (BAA/AAA 1919+), LOBSTER | BAA−AAA 4pp |
| UK | BoE, DMO, Companies House | LDI Gilt, D_M>3σ |
| JP | BoJ, METI, TMA | Baz Swap >60bp |
| DE | Bund, BTP, ECB, TTF | BTP/Bund ≥%2.00 |
| HK | HKMA, Centaline, HIBOR | HIBOR %300, de-peg |
| CN | PBOC, NBS, CBIRC | LGFV 60T¥, Shibor |
| RU | CBR, Argus, Minfin | Urals iskontosu, NWF |
| BR | BCB SGS, Tesouro, Serasa | Borç >%85, EMBI |
| MX | Banxico SIE, Pemex, CNBV | Pemex 105Mr$, MXN 22 |
| SA | SAMA, Tadawul, GASTAT | Breakeven $85-90 |
| TW | TSMC, TrendForce, DGBAS | Lead time, Boğaz riski |
| KR | KCS, TrendForce, KOSPI | 10 günlük ihracat |
| CH | SNB, AT1 piyasası, rafineri | CHF ayrışması, CoCo |
| IN | RBI, Urals/Brent, MSCI | Çatlak makası, rezerv |
| AU | SGX, Port Hedland, BHP | Demir, AUD/JPY |
| IT | BdI, BTP, MPS | BTP/Bund, NPL |
| NL | TTF, ASML, DNB | Gaz, EUV backlog |
| CL | Codelco, LME, BCCh | Bakır, rezerv |
| CD | Cobalt Institute, ICGLR | Kobalt 58, çatışma |
| ID | LME, Bank Indonesia, ... | Nikel, Rupiah |
| ZA | Johnson Matthey, SARB, Eskom | PGM, elektrik |
| KZ | Kazatomprom, NBK | Uranyum, Tenge |

## ✅ TOPLAM KRİZ KATALOĞU: ~280 kriz (23 ülke, 50 yıl)

## 🗺️ BULAŞMA
- UK: Ψ_Global→UK 10 düğüm · JP: Ψ_Global→JP 10 düğüm· AB: Ω_EU 8 üye
- 23 ülke küresel ağ: US 0.20, CN 0.15, DE 0.10, UK 0.08, JP 0.08...

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
