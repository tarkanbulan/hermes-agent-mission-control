# LAYER 9: KRİZ DİNAMİĞİ & SOSYOFİZİK MOTORU

> **Kaynak:** `B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\james Methods\` + `BTF_AMNESIA\`  
> **Durum:** ✅ Yapı doğrulandı, Türkiye backtesti çalışır durumda; 🔴 THE TEST ağırlık kalibrasyonu

## 9A: ÜÇ KANALLI SİSTEMİK REZONANS İNDEKSİ (SRI)

> **Çekirdek fikir:** Kriz, üç kanalın eş zamanlı rezonansa girmesiyle tetiklenir. Tek kanal yetmez.

### 9A.1 SRI Genel Formülü

```
SRI_total = 0.35 × SRI_psy + 0.35 × SRI_fin + 0.30 × SRI_vol

Alarm eşikleri:
  SRI_total > 0.55 VE L6 = 1  → KRİZ YAKIN
  SRI_total > 0.50 VE tevekkül_kirildi = 1  → SOSYAL SABIR TÜKENDİ
  SRI_total > 0.60 (tek başına)  → ALARM
```

### 9A.2 Kanal 1 — Psiko-Sosyal (SRI_psy)

```
SRI_psy = 0.30 × (1 - trust) 
        + 0.35 × (polarization/100)
        + 0.35 × CA
```

| Değişken | Açıklama | Kaynak |
|----------|---------|--------|
| trust | Kurumsal güven endeksi [0, 1] | Anket (TÜİK Life Satisfaction) |
| polarization | Siyasi kutuplaşma yoğunluğu [0, 100] | Medya/anket proxy |
| CA | Bilişsel Atrofi = 1 − trust_institutional | Türkiye: 0.654 (2026 itibarıyla) |

**v3 Sosyal Şok Güçlendirmesi (kalibrasyon sonrası):**

```
SRI_psy_v3 = 0.20 × (1 - trust)
           + 0.20 × (polarization/100)
           + 0.20 × CA
           + 0.15 × EFMI_norm
           + 0.25 × social_shock          ← Artırıldı (v1: 0.15)
```

**Sosyal Şok Tablosu (Sürekli Etki — Türkiye referans):**

```
2008-09 → 2009-02: shock = 0.30 / süre = 6 ay
2013-05 → 2013-07: shock = 0.35 / süre = 3 ay
2016-07 → 2016-10: shock = 0.45 / süre = 4 ay
2020-03 → 2020-05: shock = 0.25 / süre = 3 ay
```

**Türkiye Referans Değerleri:**

| Yıl | Trust | Polarization | CA | SRI_psy |
|-----|-------|-------------|-----|---------|
| 2005 | 0.25 | 55 | 0.20 | 0.30 |
| 2013 | 0.18 | 70 | 0.35 | 0.38 |
| 2018 | 0.15 | 80 | 0.45 | 0.42 |
| 2022 | 0.14 | 82 | 0.55 | 0.48 |
| 2026 | 0.14 | 85 | 0.654 | 0.52 |

### 9A.3 Kanal 2 — Finansal (SRI_fin)

```
SRI_fin = 0.40 × min(1.0, M2NIR / 15)
        + 0.30 × min(1.0, CDS / 500)
        + 0.30 × min(1.0, credit_growth / 30)
```

| Değişken | Açıklama | Alarm Eşiği |
|----------|---------|------------|
| M2NIR | M2 para arzı / Net Uluslararası Rezerv | > 15 → full stress |
| CDS | 5 yıllık kredi risk primi (bps) | > 500 → full stress |
| credit_growth | Yıllık iç kredi büyüme hızı (%) | > 30% → full stress |

**Veri Kaynakları (Türkiye):**

```
M2:          EVDS TP.HPBITABLO1.11 (haftalık, bin TL)
NIR:         EVDS TP.AB.N06 (haftalık, bin TL)
Kredi:       EVDS TP.HPBITABLO6.19 (haftalık, bin TL)
Ölçek:       Her iki seriyi milyon TL'ye çevir (1000'e böl) → rasyon ~12.98

En son gözlem (2026-W22):
  M2/NIR_observed = 12.983816
  Kredi büyüme YoY = 36.10%
```

### 9A.4 Kanal 3 — Volatilite (SRI_vol)

```
SRI_vol = 0.35 × vol_30d_normalized 
        + 0.35 × min(1.0, inflation / 50) 
        + 0.30 × min(1.0, global_VIX / 40)
```

**Asimetrik Şok Amplifikasyonu (Horizon Lab / EGARCH mantığı):**

```
Negatif şok geldiğinde:
  IF δ_system_shock > 1.0:
    temp_t = min(temp_{t-1} × 0.85 + 3.0 × δ_system_shock, max_temp)

Etki: Toplumsal panik dalgası şok geçtikten sonra da sistemde asılı kalır.
      (Histerezis / kalıcı iz etkisi)
```

**CDS Eşik Tablosu:**

```
CDS < 300 bp    → Stabil rejim
300 ≤ CDS < 400 → T2SAIM L1 likidite stresi: hazırlık
CDS ≥ 400       → Sistemik kriz → κ ≥ +3.00σ → satış şelalesi tetikleyicisi
```

### 9A.5 L6 Faz Kilit Kapısı

```
IF SRI_psy > 0.50 AND SRI_fin > 0.45 AND SRI_vol > 0.50:
    L6_phase_lock = 1   → "KİLİTLENDİ — KRİZ KESİN"
ELSE:
    L6_phase_lock = 0

Sıfır-Alarm İlkesi (Zero-Alarm):
  L6_gate geçilmeden → alarm üretilmez (gürültü filtrelenir)
  L6_gate geçilince  → asimetrik volatilite amplifikatörü devreye girer
```

### 9A.6 Tevekkül Kırılma Kontrolü

```
system_shock = SRI_total × (1 + CA)

IF system_shock > 0.70:
    tevekkül_kirildi = 1
    uyarı: "TOPLUMSAL SABIR TÜKENDİ"

Temel parametre tablosu:
  λ (amnesia)             = 0.15
  τ (politika gecikmesi)  = 0.45  (Türkiye)
  θ (elite capture)       = 0.35  (kamu kaynağı → elite transfer)
```

---

## 9B: EFMI — ETİK-FİNANS UYUŞMAZLIK İNDEKSİ

> **Kaynak:** `james Methods/efmi_pipeline_final.py` + `efmi_transformer_scorer.py`  
> **İlke:** Resmi söylem ile fiili kurumsal bozulma arasındaki makas ne kadar açıksa, kriz o kadar yaklaşmış demektir.

### 9B.1 Temel Formül

```
EFMI_t = B_t - S_t

S_t  = Söylemsel Etik Yoğunluğu  (ne kadar etik konuşuluyor?)
B_t  = Davranışsal Bozulma İndeksi (fiilen ne kadar çürüme var?)

Yorum:
  EFMI → 0   : Makas kapandı, söylem artık çürümeyi örtemiyor → kriz tehlikesi
  EFMI → -0.3: Sağlıklı dönem (söylem bozulmayı aşıyor)
```

### 9B.2 Söylemsel Etik Yoğunluğu S_t

```
S_t = 0.40 × Discourse + 0.35 × News + 0.25 × Trends
```

**Discourse (NLP 4 katman):**

```
Katman 1: savasy/bert-base-turkish-sentiment-cased
          → Duygu analizi, Türkçe                  Ağırlık: 0.35
Katman 2: yeniguno/democracy-sentiment-analysis-turkish-roberta
          → Demokrasi/yönetişim söylemi             Ağırlık: 0.30
Katman 3: AnasAlokla/multilingual_go_emotions
          → Çok etiketli duygu analizi              Ağırlık: 0.20
Katman 4: LexiconOnlyScorer
          → Siyasal etik sözlük yoğunluğu (fallback) Ağırlık: 0.15
```

**News:** Kamu harcamalarındaki "israf vs yolsuzluk" söylemsel ayrışması.

**Trends:** Google Trends — sivil toplumun "hesap verebilirlik, şeffaflık, yolsuzluk" arama yoğunluğu.

### 9B.3 Davranışsal Bozulma İndeksi B_t

```
B_t = 0.40 × İhale_Anomali + 0.30 × CPI_inv + 0.30 × Yargı_İhlali
```

**İhale Anomali İndeksi (Çiğdem Toker çerçevesi):**

```
İhale_Anomali = 0.35 × Pazarlık_Oranı_(21b)
              + 0.30 × Firma_Yoğunlaşması
              + 0.25 × Fiyat_Şişirme
              + 0.10 × İkmal_Oranı
```

**CPI_inv:** Şeffaflık Örgütü CPI'ının tersi: `CPI_inv = (100 - CPI) / 100`

**Yargı İhlali endeksi:** 2013 müdahalesi: 0.50 → 2016 darbe sonrası 4.000+ hakim ihracı: 0.90+

### 9B.4 EFMI Türkiye Scorecard

| Yıl | CPI | Yargı İhlali | İhale Anomalisi | B_t | S_t | EFMI_t | Dönem |
|-----|-----|-------------|----------------|-----|-----|--------|-------|
| 2005 | 55 | 0.12 | 0.15 | 0.2310 | 0.5945 | **-0.3635** | AB Reforma Çıpası |
| 2009 | 44 | 0.20 | 0.20 | 0.3080 | 0.6185 | **-0.3105** | Fasıl blokajı |
| 2012 | 49 | 0.30 | 0.23 | 0.3350 | 0.6225 | **-0.2875** | Reform dönem sonu |
| 2013 | 50 | 0.50 | 0.25 | 0.4000 | 0.6688 | **-0.2688** | 17-25 Aralık kırılması |
| 2016 | 40 | 0.90 | 0.36 | 0.5940 | 0.6793 | **-0.0853** | 4.000+ hakim ihracı |
| 2017 | 40 | 0.92 | 0.38 | 0.6080 | 0.6773 | **-0.0693** | 21/b %81'e çıkışı |
| 2018 | 41 | 0.94 | 0.41 | 0.6230 | 0.6813 | **-0.0583** | AB "standstill" |
| 2024 | 34 | 0.98 | 0.46 | 0.6760 | 0.6983 | **-0.0223** | Aksiyonel kilit |

**Yorumlama:** EFMI −0.32'den −0.02'ye sıfıra yaklaştı. Makas kapanıyor. Söylem artık çürümeyi örtemiyor.

---

## 9C: BTF-AMNESIA VALİDASYON PROTOKOLÜ

> **Kaynak:** `BTF_AMNESIA/` tüm dosyalar  
> **Durum:** ✅ Protokol mühürlendi; 🔴 THE TEST UK ve üçüncü ülke kalibrasyonu

### 9C.1 Back to Future (BTF) İlkesi

```
KESİN KURAL: t anında yalnız (t-1)'e kadar olan veriyi kullan.
Gelecek verisi = KEPSİN YASAK

Backtest döngüsü (Python):
  DOĞRU:
    for year in range(1999, 2025):
        data = df[df['tarih'] <= current_date]   ← sadece şimdiye kadar
        z_score = calc(data)

  YANLIŞ:
    for year in range(1999, 2025):
        data = df  ← tüm veri → gelecek sızar
```

### 9C.2 Amnesia — Bellek Sönümleme

```
M_t = S_t + (1 - λ) × M_{t-1}

λ = 0.15  (her ay şok belleğinin %15'i silinir, %85 kalır)
S_t = t anındaki şok seviyesi
M_t = birikimli bellekteki şok ağırlığı

Yorumlama: Eski şoklar zamanla bulanıklaşır, 
           sistem geçmiş krizleri unutarak ileriye bakar.
```

### 9C.3 Beklenen Backtest Performansı (Türkiye, v3 hedefleri)

| Kriz | v1 | v2 | v3 Hedef |
|------|:--:|:--:|:--------:|
| 2008 Küresel | %0 | %8-16 | **>%70** |
| 2013 17-25 Aralık | %0 | %0 | **>%60** |
| 2016 Darbe Girişimi | %0 | %0 | **>%65** |
| 2018 Döviz Krizi | %83 | %100 | **%100** |
| 2022 Hiperenflasyon | %100 | %100 | **%100** |

### 9C.4 L6 Faz Kilit Doğrulanan Sinyaller (Türkiye Tarihsel)

| Dönem | SRI_psy | SRI_fin | SRI_vol | L6 Kapısı | Fiili Kriz |
|-------|---------|---------|---------|-----------|-----------|
| 1994 Krizi | 0.518 | 0.536 | 1.000 | ✅ Tetiklendi | ✅ Doğrulandı |
| 2021-2022 Şok | 0.576 | 0.453 | 0.568 | ✅ Tetiklendi | ✅ Doğrulandı |
| 2001 Bankacılık | (pasif) | (M2/NIR düzleşti) | — | Tetiklenmedi | 🔴 TEST bekliyor |
| 2018 Döviz | (pasif) | 0.401 (eşik altı) | — | Tetiklenmedi | 🔴 TEST bekliyor |

### 9C.5 Veri Ayrışma Kuralı (Backtest/Realtime)

```
series_1994_2024.csv   → Backtest (YENİLEME YASAK)
series_2025_2026.csv   → Real-time (güncel)
series_1994_2026.csv   → YASAK (karışık veri = leakage riski)

Parametre sabitlik kuralı:
  λ = 0.15        (hardcoded — değiştirilemez)
  threshold = 0.55 (hardcoded — değiştirilemez)
  window = 5 yıl   (hardcoded — değiştirilemez)
```

### 9C.6 Bilimsel Reprodüktibilite (Replication Mandate)

```
T2SAIM dışındaki herhangi bir üçüncü taraf AI veya araştırmacı
bu protokolü izlediğinde birebir aynı sayısal sonuçları almalıdır.

Bu: geriye dönük uydurma (retrospective bias) iddiasını reddeder.
```

---

## 9D: JAMES METHODS — SOSYOFİZİK & EKONOFİZİK MOTORU

> **Kaynak:** `james Methods/historical_backtest.py` + `walkthrough.md`  
> **Durum:** ✅ Backtest çalışıyor; 🔴 THE TEST UK kalibrasyonu

### 9D.1 Model Mimarisi

```
[MAKRO & DÜZENLEYİCİ ŞOKLAR]
              ↓
[Sosyofizik: Ising] ↔ [Ekonofizik: Kinetik] ↔ [Nöro-Ekonomi: RPE]
      ↓                       ↓                       ↓
  Uyum (Spin)             Gini / Sıcaklık         Wanting-Liking
                               ↓
                [M_t: Algı Manipülasyonu (Coxall)]
```

### 9D.2 WVS Tabanlı Zihin Yapısı Arketipleri (4 Tip)

| Arketip | Başlangıç Payı | Özellikler |
|---------|---------------|-----------|
| **Geleneksel/İtaatkâr** | %38 | Yüksek otorite bağımlılığı, propaganda duyarlılığı yüksek, mahalle baskısına en açık |
| **Eleştirel Düşünür** | %22 | Propaganda duyarlılığı düşük, EFMI ve kurumsal sızıntılara hassas, seküler-formasist |
| **Kaygılı/Kırılgan** | %20 | Yüksek belirsizlikten kaçınma, enflasyon/kur şoklarında ilk kaçan |
| **Dirençli/Pragmatist** | %20 | Şoklara en dayanıklı, 8 adım ileriye rasyonel düşünür (γ_td = 0.92) |

**Dinamik Kayma:** Paylar sabit değil. `psychosocial_profile_panel.csv` aylık güncellemesiyle her adım değişir.

### 9D.3 Ising Sosyal Uyum Modeli

```
Spin s_i = ±1   (uyum = +1, deviance = -1)

Glauber geçiş olasılığı:
  P(s_i → +1) = sigmoid(2β × (J_i × Σ s_j + h_ext))

Kutuplaşma altında uyum baskısı:
  J_i = (1.0 + 1.2 × conformity_pressure/100) × agent.conformity_mult 
        × (1.0 + 0.40 × polarization_load/100)

Kaçış stratejisi (Kurnazlık):
  evasion_propensity = tax_rate + 0.15 × system_shock × agent.kurnazlık_bias
```

### 9D.4 Deffuant Güven Yayılımı

```
Güven o_i ∈ [0, 1]   (1 = tam güven, 0 = tam güvensizlik)

Güven erimesi:
  NRG_t = resmi_anlatı - saha_gerçekliği   (anlatı boşluğu)
  o_i(t+1) = o_i(t) - μ × NRG_t × (1 - o_i(t))

Kaçış tetikleyicisi:
  IF o_i < 0.25 → EBP = 1  (sermaye kaçışı / dolarizasyon)

Bilişsel Atrofi Cezası:
  Yüksek kurumsal aşınma dönemlerinde manipülasyon/kurtarma etkisi baskılanır:
  ca_modifier = f(cognitive_atrophy_penalty_modifier) ∈ [0.6, 1.0]
```

### 9D.5 Kinetik Servet Değiş-Tokuşu (Ekonofizik)

```
Servet değişimi iki ajan arasında:
  Δw = ε × (w_j - w_i) + yolsuzluk_kanalı

Yolsuzluk kanalı:
  Nepotizm Ω (kayırmacı ağ dominansı)
  Rant θ (kamu kaynağı → elite transfer)

Çıktı: Gini katsayısı ↑, Sosyal Sıcaklık T ↑
```

### 9D.6 Nöro-Ekonomi: RPE Dopaminerjik Asimetri

```
Reward Prediction Error (RPE):
  RPE_t = Gerçek_çıktı - Beklenen_çıktı

Temporal Difference Öğrenme Hızı:
  Stabil rejim: α = 0.15
  Kriz / amigdala uyarımı: α → 0.85  (son şoklara aşırı tepki)

Wanting-Liking Asimetrisi (W - L):
  "İsteme" (dopaminerjik arzu) > "Hoşlanma" (tüketim tatmini)
  Gap genişlediğinde: sistemik kriz tetikleyicisi

Kayıp Aversiyonu (Mindset bazlı):
  rpe_effective = rpe × agent.loss_aversion  (rpe < 0 ise)
  Katsayılar: Geleneksel = 1.8, Kaygılı = 2.5, Pragmatist = 1.2
```

### 9D.7 Kaçış Davranışı (EBP)

```
Zenginliğe bağlı kaçış eşiği:
  escape_threshold_i = base_threshold × (1.0 + 0.30 × (1.0 - agent.wealth) 
                        × agent.psych_strain_mult)

Daha yoksul ajan → daha erken dolarize eder ve kaçar.
```

### 9D.8 Malcolm Coxall Algı Manipülasyonu (4 Mekanizma)

**1. Gündem Kontrolü & Dikkat Dağıtma (Coxall Bölüm 8, 14):**
```
NRG_{i,t} = NRG_t × (1.0 - κ_i × M_t)

κ_i = propaganda duyarlılığı (Geleneksel'de en yüksek)
M_t = manipülasyon bütçesi = f(NRG_t)

Etki: Geleneksel ajanlar reel ekonomik bozulmayı fark etmez.
```

**2. Günah Keçisi İlan Etme (Coxall Bölüm 24, 55):**
```
Suç "faiz lobileri, spekülatörler, dış mihraklar"a yıkılır.
Kutuplaşma artışı:
  J_{i,t} = J_social × (1.0 + β_i × polarization_load_t)

Etki: Geleneksel ajanlar güvenleri düşse dahi uyumlu kalmaya devam eder.
```

**3. Salıncak Ajan Hedeflemesi (Coxall Bölüm 9):**
```
Sosyal faz geçişlerini engellemek için:
  - Kırılma sınırındaki ajanlar hedeflenir: o_i ≈ 0.25
  - Manipülasyon bütçesi bu ajanlara yığılır
  - Amaç: Sistemden kopuşu geciktirmek
```

**4. Geri Tepme Efekti (Coxall Bölüm 5, 50.5.8):**
```
IF M_t × inflation_t > threshold:
    → Algı yönetimi patlar (backfire)
    → Geleneksel ve Kaygılı ajanlar aldatıldıklarını anlar
    → Non-lineer panik dalgası
    → Ani sermaye kaçışı (escape_behavior = True)
```

### 9D.9 Tarihsel Backtest Sonuçları (Türkiye 1996-2024)

| Yıl | Z-Score | Hazard % | Kriz Durumu |
|-----|---------|---------|------------|
| 1996 | -3.50σ | %39 | Stabil / Rejim İçi |
| 1998 | +0.07σ | %16 | Asya/Rusya spillage |
| 2001 | +0.93σ | **%95** | ✅ 2001 Bankacılık Krizi |
| 2008 | +0.05σ | %88 | Küresel (Türkiye'de sınırlı) |
| 2013 | +0.25σ | %91 | Gezi + 17-25 Aralık başlangıcı |
| 2018 | +0.46σ | **%92** | ✅ Döviz ve Borç Krizi |
| 2022 | +1.48σ | **%97** | ✅ Hiperenflasyon + Negatif Rezerv |
| 2024 | +1.13σ | %96 | Ortodoks sıkılaştırma |

**Sosyokültürel Prior Kalibrasyon (28 kaynak entegre):**

```
Echo Chambers (Taklit/Yenilik Karşıtlığı):
  ε_i = ε_trust × uncertainty_avoid_mult × (1 - 0.50 × polarization_load/100)

Sürü Davranışı:
  IF system_shock > 1.2 AND random < 0.25 × conformity_mult:
    spin_i = mean_neighbor_spin   (sürü etkisi)

Kısa Vadecililik (Plansızlık):
  Geleneksel/Formasist: γ_td = 0.72-0.75
  Pragmatist:           γ_td = 0.92

Tevekkül/Kadercilik:
  escape_prob = (0.1 + 0.8 × BCS/100) / agent.fatalism_buffer
```

---

