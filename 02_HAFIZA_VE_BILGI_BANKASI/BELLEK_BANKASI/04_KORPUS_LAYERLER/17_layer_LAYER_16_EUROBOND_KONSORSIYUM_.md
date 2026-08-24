# LAYER 16: EUROBOND KONSORSIYUM KRONOLOJİSİ (2020–2026)

## 16A: EUROBOND KONSORSIYUM KRONOLOJİSİ (2020–2026)

> **Kaynak:** `B:\Classified\walkthrough.md` Bölüm 7 + Hazine ihraç kayıtları  
> **Durum:** ✅ Doğrulandı — Resmi Hazine ve Bloomberg verileriyle örtüşüyor

### 16A.1 İhraç Kronolojisi ve Getiri/Spread Seyri

| Dönem | Olay | Getiri | Spread | Konsorsiyum |
|-------|------|--------|--------|-------------|
| **2020 İyimserliği** | Pre-pandemi, 5Y USD | %4.45 | Standart | Citi, Deutsche Bank, JP Morgan, SocGen |
| **2022 Kriz Zirvesi** | Heterodoks para + CDS 908bp | | | |
| → Mart 2022 | Kriz zirvesi | **%8.625** | **UST +645.1 bps** | Citi, Goldman Sachs, JP Morgan |
| → Ekim 2022 | Hiperenflasyon doruk | **%9.750** | Kriz spreadi | Citi, Goldman Sachs, JP Morgan |
| **2023-2024 Ortodoks Dönüş** | Şimşek politikası | Düşüş | Düşüş | Deutsche Bank, JPMorgan, SocGen |
| → Şubat 2024 | EUR ihracı rekor düşük spread | | Rekor | Deutsche Bank, JPMorgan, SocGen |
| **2025-2026 Normalleşme** | | | | |
| → Şubat 2026 | EUR ihraç | **%5.20** | **MS +242 bps** | Deutsche Bank, HSBC, JP Morgan, SocGen |

**Şubat 2026 spreadi: Son 15 yılın rekor düşüğü** ⚠️ 

### 16A.2 Konsorsiyum Yapısal Örüntüsü

```
Çekirdek (tüm dönemlerde):
  Citibank + JP Morgan + Goldman Sachs
  → İhraçların ezici çoğunluğunu yöneten konsorsiyum

Kriz dönemi (2022) coğrafi kayma:
  Batılı kurumsal yatırımcılar → Körfez fonları
  Körfez fonları payı: %27 (2022 kriz zirvesinde)
  Anlam: Batı risk iştahı kapandığında, Körfez fonları fiyat koyucu oldu

Normalleşme dönemi (2024-2026) risk tabanı genişlemesi:
  + Societe Generale
  + BBVA, BNP Paribas, ING Bank (Kıta Avrupası)
  + ADCB, Emirates NBD (Körfez bankacılığı)
  
T2SAIM bağlantısı:
  L3 coğrafi risk iştahı kayması → konsorsiyum kompozisyonu
  2022'de Körfez payı %27 → "Batı güvensizliği" L3 sinyali
  2026 spread rekor düşük → ortodoks politika geçicilik mi, kalıcılık mı?
  CDS 238bp (<300) → likidite strese rağmen egemen kredi güvenilir
```

### 16A.3 T2SAIM'de Eurobond Veri Entegrasyonu

```
Veri noktaları:
  eurobond_yield_t → dışsal borçlanma maliyeti (EBP bileşeni)
  eurobond_spread_vs_ust → risk priminin piyasa algısı (MBP bileşeni)
  consortium_composition_t → Körfez/Batı yatırımcı dengesi (CCP bileşeni)
  
Alarm sinyali oluşturma:
  Spread > 600 bps → CBC-01 MBP kritik alarm
  Körfez payı > %30 → Batı çekilmesi (L3 coğrafi risk)
  Spread normalleşmesi (< 250 bps) → L1 geçici toparlanma sinyali
  
Veri kaynağı:
  Bloomberg Sovereign Desk + Hazine.gov.tr ihraç duyuruları
```

---

