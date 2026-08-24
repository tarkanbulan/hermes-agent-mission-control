# LAYER 14: L1-L4 TR-UK KARŞILAŞTIRMALI BORU HATTI & SOSYAL GÜVEN EROZYONU

## 14A: L1-L4 TR-UK KARŞILAŞTIRMALI BORU HATTI

> **Kaynak:** `tr_uk_calculation_results.json` + `kriz gözlem.md` (Haziran 2026)  
> **Durum:** ✅ Doğrulandı — Hermes FinInt ham verileriyle çapraz teyit edildi  
> **Tarih:** 2026-06-04 (Haziran 2026 referans noktası)

### 14A.1 Dört Katmanlı Pipeline Mimarisi

```
L1 = Makro Likidite Stresi
     Formula: f(yield_spread, M2NIR, rezerv_yeterliliği, FX_volatilite, CDS)

L2 = Zombi Şirket / Reel Sektör Direnci
     Formula: f(NPL_oranı, kısa_vadeli_borç_çevrimi, reel_satış_büyümesi)
     Not: Yüksek enflasyon döneminde "hayalet ciro" L2'yi yapay olarak düşük gösterir

L3 = Kurumsal Çürüme Skoru (Acemoğlu ICF Uyumlu)
     Formula: f(WJP_rule_of_law, VDem_judicial, FH_courts, EFMI_t, info_asymmetry)

L4 = Psikososyal Toplumsal Stres
     Formula: f(street_FX_gap, social_trust, protest_frequency, savings_flight)
     Kritik: L4 < 0 = Öğrenilmiş Çaresizlik (yalancı istikrar) — panik YOK
             L4 > 0 = Aktif tepki modunda toplum
             L4 < -2σ = Tam donma rejimi (sistemik tampon yok)
```

### 14A.2 Türkiye — Haziran 2026 Değerleri

| Katman | Z-Skor | Alarm | Ana Sinyal |
|--------|--------|-------|------------|
| L1 Makro Likidite Stresi | **+5.6533σ** | EKSTREM ALARM | Fonlama kilidi, rezerv erimesi |
| L2 Zombi Şirket Riski | **+0.2879σ** | STABİL/NÖTR | Hayalet ciro makyajı geçici |
| L3 Kurumsal Çürüme | **+7.6587σ** | SİSTEMİK ÇÖKÜŞ | Hukuk + veri güveni sıfır |
| L4 Psikososyal Stres | **-1.1795σ** | TEPKİSİZ/PASİF | Öğrenilmiş çaresizlik |

**Ham Veriler (Haziran 2026):**
```
USDTRY:                  45.9649 (Hermes anlık: 45.97)
CDS 5Y:                  238.47 bp (<300 stabil, 300-400 prep, ≥400 kriz)
TCMB Politika Faizi:     %37.00
TR 2Y Tahvil Getirisi:   %43.59
TR 10Y Tahvil Getirisi:  %34.70
Yield Eğrisi (2Y-10Y):   +8.88 puan TERS (aşırı inversion)
Haftalık Rezerv Erimesi: -7 milyar USD (61.2 Mrd → 54.2 Mrd)
Street FX Gap:           %0.25 (panik seviyesinde DEĞİL)
Sosyal Güven Endeksi:    13.0/100 (2017 baz × 13.0 erimesi)
Daron Kurumsal Skor:     0.35/1.0
Resmi Enflasyon:         %15.00 (sokak gerçekliğinden çok ayrışıyor)
```

### 14A.3 UK — Haziran 2026 Değerleri

| Katman | Z-Skor | Alarm | Yapısal Karakter |
|--------|--------|-------|-----------------|
| L1 Makro Likidite | **-2.16σ** | STABİL | Fonlama piyasaları işlevsel |
| L2 Zombi Şirket | **+0.40σ** | ORTALAMA | Hafif birikim; Brexit sonrası yeniden yapılanma |
| L3 Kurumsal Çürüme | **+1.00σ** | KABUL EDİLEBİLİR | Kurumlar çalışıyor ancak gerilemede |
| L4 Psikososyal | **-1.09σ** | ORTALAMA-PASİF | Brexit yorgunluğu; geçici pasivizasyon |

```
Yapısal fark:
  UK L3 = +1.00σ → kurumlar hâlâ çalışıyor (hukuk, basın, parlamento)
  TR L3 = +7.66σ → kurumsal güven sistematik olarak sıfırlandı

UK L4 = -1.09σ → Brexit yorgunluğu + refah sistemi erozyonu
TR L4 = -1.18σ → öğrenilmiş çaresizlik + sosyal güven x13.0 erimesi
```

### 14A.4 Öğrenilmiş Çaresizlik — L4 Negatif Paradoksu

```
YANLIŞ OKUMA: "L4 negatif → Türkiye'de stres yok, toplum sakin"
DOĞRU OKUMA:  "L4 negatif → toplum hayatta kalma rutinine sıkışmış"

Öğrenilmiş çaresizlik mekanizması (Seligman → T2SAIM adaptasyonu):
  1. Uzun süreli kontrol yitimi → "değişemez" inancı yerleşiyor
  2. Tepki kapasitesi donuyor (aktif kaçış veya protesto yok)
  3. Sistem paniklemeden çöküşe gidebiliyor

Yalancı istikrar (false calm) tuzağı:
  Dışarıdan bakıldığında: "toplum sakin"
  İçeriden bakıldığında: "tampon mekanizmalar tükenmiş"

Tetikleyici gelince ne olur?
  → Gıda tedarik aksaması veya barınma krizi gibi somut tetikleyici
  → L4 negatif → pozitif geçişi: ani panik alımları, döviz hücumu, sistemik çözülme
  → L3 (+7.66σ) tamponları olmadığı için şok absorbe edilemez
```

### 14A.5 L1-L2 Bağlantısı: 3-6 Aylık Zombi Temerrüt Mekanizması

```
Mevcut durum (Haziran 2026):
  L1 = +5.65σ (likidite tamamen kilitli)
  L2 = +0.29σ (zombi görünmüyor — hayalet ciro makyajı)

Sürdürülemezlik mekanizması:
  Yüksek fonlama maliyeti (%43.59 2Y getiri)
  → Şirket borç yenilemesi imkansızlaşıyor
  → Nominal ciro şişirmesi gerçek nakit akışını gizliyor
  → 3-6 aylık periyotta L1 stresi L2'yi yukarı iterek
    zincirleme konkordato/temerrüt dalgası tetikleniyor

Simülasyon tahmini: L2 → +2.5-3.5σ bandı (Q3/Q4 2026 riski)
```

**⛔ Etik Bayrak:** L1-L4 skoru ülke düzeyinde yapısal ölçümdür. Sektör, firma, birey veya etnik grup düzeyinde atıf yapılamaz. Analiz birimi: ulusal ekonomi sistemi, dönem, rejim yapısı.

---

## 14B: SOSYAL GÜVEN EROZYONU — SAYISAL İZ

> **Kaynak:** WVS Wave 7 + `psychosocial_profile_panel.csv` + Hermes gözlem verileri

```
2017 Baz Yılı → 2026 Sosyal Güven Seyri:

  2017 Trust skoru: referans (1.0 normalized)
  2026 Trust skoru: 13.0/100 (x13.0 erime veya 0.13 normalized)

Bu ne demek?
  Her 7 kişiden 6'sı en temel kurumsal güveni yitirmiş.
  Sosyal yardımlaşma mekanizmaları (aile, komşuluk, kurum) içten kopuyor.
  Bu "görünmez kırılganlık" L4 negatif ile uyumlu ama L3 alarm seviyesiyle açıklanıyor.

Benzer tarihsel eşdeğer:
  Rusya 1998 temerrüdü öncesi → Trust çöküşü 18 ay önceden başladı
  Arjantin 2001 temerrüdü öncesi → Trust 2 yıl önce sıfırlandı
  
T2SAIM bağlantısı:
  Social Trust → SDP bileşenleri (authority_dependence, conformity_pressure)
  Trust_collapse → EBP amplifikatörü (kaçış davranışını hızlandırır)
```


---

