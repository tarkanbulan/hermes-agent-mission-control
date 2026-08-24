# 🎯 29 ÜLKE TAM KALİBRASYON SETİ — 18 KRİZ → TÜM ÜLKELER (eksik kapanış)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar:** Kaptan Tarco
**Amaç:** 18 krizlik kronolojide 29 ülkeden bazıları düğüm değildi; her ülkenin kendi krizi eklenerek 29 ülkenin TAMAMI kalibrasyon setine girer.

---

## 18 KRONOLOJİDE DÜĞÜM OLAN ÜLKELER
US, UK, DE, JP, CN, RU, MX, BR, TR, HK, KR, ID, SA, IN, AU, IT, NL, CL(2015 emtia), CH(2023 CS) → **çoğu var**

## 🔥 EKSİK — 29'da olup 18'de DÜĞÜM OLMAYAN (kendi krizi eklenecek)
| Ülke | Eklenmesi gereken kendi krizi (50 yıl) | Öneri (kaynak bekliyor) |
| :--- | :--- | :--- |
| **FR** | 1968 Mayıs, 1992 ERM, 2008, Fransa borç | FR 2008 (BNP Paribas) — GFC |
| **SG** | 1997 Asya, 2013 | SG 1997 (Asya bulaşması) |
| **CA** | 1982, 2008 | CA 2008 (bankacılık) |
| **ES** | 2010-12 Euro, 2008 emlak | ES 2012 (Euro borç, BBVA) |
| **QA** | 2016? petrol, 2022 | QA 2020 (petrol+COVID) |
| **AE** | 2008 Dubai, 2020 | AE 2009 Dubai debt (Nakheel) |
| **TW** | 1997 Asya, 2020 | TW 1997/2020 |
| **CL** | 1982 LatAm, 1973, 2015 | CL 1982 (bakır/borç), 2015 (bakır çöküşü) |
| **CD** | 1990'lar savaş, 2016 | CD 2016 kobalt krizi |
| **ID** | 1997 Asya (var ama düğüm değil), 1998 | ID 1997 (Asya — düğüm olarak da ekle) |
| **ZA** | 1985, 1998, 2008 | ZA 1985 (borç moratoryum) |
| **KZ** | 1998, 2015, 2022 | KZ 2015 (tenge devalüasyon) |

**Sonuç:** 18 + ~12 eksik ülke krizi = **~30 krizlik TAM kalibrasyon seti** (29 ülkenin hepsi ≥1 krizle).

## NEDEN ÖNEMLİ
- Erken uyarı sistemi her ülkenin **kendi kriz desenini** öğrenmeli (backtest = her ülke kendi krizini önceden yakalamalı)
- Spark'ın "FR/SG/CA/ES ağ kapanış" + "QA/AE TR 1. derece" bulgusu bu eksik krizleri zorunlu kılıyor
- Alt ajanlar (29 ülke kriz kataloğu) bu eksik ülkelerin krizlerini getiriyor → kalibrasyon setine işlenecek

## UYGULAMA
- 3 alt ajan sonucu gelince → her ülkenin krizi 18'lik kronolojiye eklenir → 29 ülke tam kalibrasyon
- Alt ajanlar `BELLEK_KATALOGLARI/` ülke KRIZ_KATALOGU.md yazıyor, oradan birleşik set

*Veritas Per Se — Komutan Picard · 24 Ağustos 2026*
