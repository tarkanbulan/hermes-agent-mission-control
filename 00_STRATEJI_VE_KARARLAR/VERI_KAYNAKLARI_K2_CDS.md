# 📊 K2 FİNANSAL REZONANS — DOĞRU VERİ KAYNAKLARI EŞLEMESİ (23 ülke)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **İlke:** "Önemli olan doğru birinin vermiş olması"
**Kaptan dersi:** "Bazı veriler bulamayız diye korkma; aramadan söyleyemeyiz. Her ülkeninki ayrı değişik olabilir."

---

## K2 SRI_fin Girdileri → DOĞRU KAYNAK (ülke ülke)

### CDS (5Y) — K2 SRI_fin CDS/500
CDS tek merkezi yerde değil; **her ülke doğru kaynağından**:

| Ülke | Doğru CDS Kaynağı | Kolaylık |
| :--- | :--- | :--- |
| ABD | **FRED BAA−AAA spread (1919+)** proxy | ✅ mevcut |
| TR | **FRED `CCDS` hayır; TCMB EVDS / İstanbul CDS** | aramalı |
| DE/FR/NL/IT | **ECB / FRED IR* (10Y spread)** | aramalı |
| JP | BoJ CDS / Japanese CDS index | aramalı |
| BR/MX/CN/RU | **FRED DCOIL? hayır; Country Default Spread (CB bond yield−US)** | aramalı |
| TW/KR/CH | AT1/KOSPI/CDS — finansal spread | aramalı |

### M2/NIR — K2 SRI_fin M2NIR/15
- **TR:** EVDS TP.HPBITABLO1.11 (M2) / TP.AB.N06 (NIR) — ✅ L9'da var (12.98)
- **Diğer:** Her ülke merkez bankası M2 + rezerv (BCB, PBOC, BoJ, ECB...)

### Kredi Büyüme — K2 SRI_fin credit/30
- **TR:** EVDS TP.HPBITABLO6.19 (%36.1 — L9'da)
- **Diğer:** her merkez bankası kredi istatistiği

---

## K3 Toplumsal (PCCI/trust/polarizasyon/tevekkül) → doğru kaynaklar
CDS zor değil; tüm toplumsal veri de bulunabilir (TR EVDS + TÜİK anket; JP METI; BR IBGE...). "Bulunamaz" demeden ARA.

## K1 Enflasyon → FRED CPI (ülke başına, L-023: kaynaktan indir)
Şu an sadece 1 ülke CPI'i var (pakette) ama FRED'te **her ülke CPIALLMINMEI var** — indirilebilir (arayıp buldum, sormadan).

---

## SONUÇ (Kaptan dersiyle)
- **CDS/M2NIR/kredi/toplumsal** → her ülke **doğru kaynağından aranıp indirilebilir** (FRED/EVDS/merkez bankası)
- **"Bulunmaz" demem** — sürekli ara, doğru kaynağı bul, indir
- **Bir ülke verisi diğerinden farklı olabilir** → sistem ülke-agnostik, kaynak-özgü
- **Önemli olan DOĞRU kaynaktan gelmesi** (uydurma değil)

*Veritas Per Se — Komutan Picard · 24 Ağustos 2026*
