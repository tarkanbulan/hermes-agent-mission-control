# LAYER 13: NTZ-49 EWI, REJİM GEÇİŞİ MOTORU & VERİTAS KİLİTLERİ (CBC-07/09)

## 13A: NTZ-49 EWI — 60 GÜNLÜK ERKEN UYARI SİSTEMİ

> **Kaynak:** `B:\Classified\hybrid_crisis_model.py` + `efmi_pipeline_final.py` + walkthrough.md  
> **Durum:** ✅ Doğrulandı — 1996-2024 tarihsel backtestinde doğrulanmış  
> **Referans:** Kaminsky-Lizondo-Reinhart (KLR, 1998 IMF) + Back-to-Future Amnesia Protokolü

### 13A.1 NTZ-49 Nedir?

NTZ-49, 49 göstergelik bir sinyal ağıdır. Fonksiyonu: Kronik krizin Terminal Kırılma anını (T-0) 60 gün önceden tespit etmek.

```
Temel ayrım:
  KLR modeli sorusu:     "Döviz kriziyle karşı karşıya mıyız?"
  NTZ-49 sorusu:         "Kronik krizin fişi ne zaman çekilecek?"

Borsadan 100 gün önceden görüyoruz.
Limana yanaşan Kanada buğday gemisine bakıyoruz.
```

### 13A.2 Üç-Açık Kimlik (TRIDEF_t)

```
TRIDEF_t = Kamu_Açığı_t + Özel_Açık_t + Dış_Açık_t

Tanım: Kamu + Özel + Dış sektör açıklarının YEK ANDA ve YAPI OLARAK kilitlenmesi
Eşik:  Üç açık eş zamanlı pozitif → CRISIS_PRECONDITION_t = 1

CRISIS_PRECONDITION_t = 1 IF:
    Kamu_Açığı_t > 0  (bütçe açık)
  AND Özel_Açık_t > 0  (özel sektör net borçlu)
  AND Dış_Açık_t > 0  (cari açık + sermaye çıkışı)

Aksi hâlde → CRISIS_PRECONDITION_t = 0  (yapısal kırılganlık yok)
```

**Türkiye 2013-2024:** TRIDEF_t = 1 (üç açık eş zamanlı kilitleniyor)  
**Türkiye 2005-2012:** TRIDEF_t dönemsel olarak 0 (AB reformu / dış denge)

### 13A.3 Para Arzı / Rezerv Oranı (M2NIR_t)

```
M2NIR_t = M2_para_arzı_t / Net_Uluslararası_Rezerv_t

Veri kaynakları:
  M2  → EVDS: TP.HPBITABLO1.11 (TCMB para arzı)
  NIR → EVDS: TP.AB.N06 (net uluslararası rezerv)

Alarm eşiği:
  M2NIR_t < 1.0   → STABIL
  M2NIR_t = 1.0-3 → DIKKAT (izleme)
  M2NIR_t > 3.0   → ALARM (para tabanı rezerv kapasitesini aşıyor)
  M2NIR_t > 5.0   → KRİTİK ALARM

Yorumlama: M2NIR yükselince "sterlize edilemeyen likidite artışı" → devalüasyon baskısı artıyor.
```

### 13A.4 Kısa Vadeli Dış Borç / Rezerv (STEDNIR_t)

```
STEDNIR_t = Kısa_Vadeli_Dış_Borç_t / Net_Uluslararası_Rezerv_t

Alarm eşiği:
  STEDNIR_t < 1.0 → Stabil (rezervler borcu karşılıyor)
  STEDNIR_t > 1.0 → ALARM (kısa vadeli borç rezervi aşıyor)
  STEDNIR_t > 2.0 → KRİTİK (rezerv tamamen yetersiz)

KLR bağlantısı: Bu, klasik Kaminsky-Lizondo-Reinhart sinyal değişkenlerinden biridir.
Türkiye (2022 kriz zirvesi): STEDNIR yüksek → rezerv savunması sürdürülemez oldu.
```

### 13A.5 Panik Dolarizasyon Açığı (DOLGAP_t)

```
DOLGAP_t = Actual_FX_share_t - MVP_t

  Actual_FX_share_t = döviz mevduatı / toplam mevduat (EVDS: TCMB haftalık)
  MVP_t = Minimum Variance Portfolio döviz payı
        = Portföy kuramına göre optimal döviz payı (sadece finansal rasyonellik)

DOLGAP > 0: Hane halkı FX'i "koruma" için tutuyor (finansal tercihin ötesinde)
DOLGAP > θ_panic (eşik): → Sosyolojik kopuş başladı (kurumsal güven sıfır)

Yorumlama:
  DOLGAP küçük → Normal finansal dolarizasyon (getiri optimizasyonu)
  DOLGAP büyük → Panik dolarizasyon (ekonomik ölçüm değil, toplumsal korku ölçümü)
```

**⛔ Etik Bayrak:** DOLGAP, döviz tutma davranışını bireysel veya grupsal kararla ilişkilendirmez. Sistem düzeyinde toplumsal güven sinyalidir. HOW NOT WHO.

### 13A.6 TAR FX Şok Modeli (Kırılma Anı Algoritması)

```
TAR (Threshold Autoregressive) Model:

r_t = döviz kuru log-getirisi (günlük USDTRY değişimi)

Normal rejim (r_t < θ):
  r_t = α₁ + β₁ × r_{t-1} + ε_t      [AR(1) ile ölçülü dalgalanma]

Kırılma rejimi (r_t ≥ θ):
  r_t = α₂ + β₂ × r_{t-1} + γ × (r_{t-1} - θ) + ε_t  [şiddetlenen dinamik]

θ = kırılma eşiği (1999-2024 verisine göre kalibre)

Kırılma anı tespiti:
  r_t ≥ θ → Rejim geçişi başladı
  Ardışık ≥ 3 gün θ üzeri → KRIZ BAŞLAMA SINIFI (T-0 yakın)
```

### 13A.7 Kalman Filtresi Sürprizi (Kriz Anında Hızlı Öğrenme)

```
η_{t|t-1} = gözlenen değer - filtre tahmini

Kalman sürprizi (ölçüm artığı):
  küçük η → sistem beklendiği gibi hareket ediyor
  ani büyük η → öngörülmemiş şok (kriz sinyali)

Formülasyon:
  x̂_{t|t} = x̂_{t|t-1} + K_t × η_{t|t-1}
  K_t = P_{t|t-1} × H^T × (H × P_{t|t-1} × H^T + R)^{-1}

Kriz uygulaması:
  Kriz anında η sıfırlanmaz (sistem şoku absorbe edemez)
  Filtre hızlı güncelleme moduna geçer: K_t yükselir
  Bu davranış kriz başlamadan 7-14 gün önce gözlenebilir.
```

### 13A.8 Tarihsel Backtest Kalibrasyonu (1996-2024)

> **Kaynak:** `historical_backtest.py` + `psychosocial_profile_panel.csv` entegrasyonu

| Yıl | Hukuk (0-100) | CPI (0-100) | Yıllık Enflasyon % | Sigma (Z-skor) | Kriz Olasılığı % | Fiili Durum |
|-----|--------------|-------------|--------------------|----------------|-------------------|-------------|
| 1996 | 54.76 | 42.01 | 80.41 | **-1.67σ** | **4.10%** | Stabil |
| 1998 | 53.73 | 35.93 | 84.64 | **-0.83σ** | **16.37%** | Asya/Rusya spillage |
| 2001 | 55.52 | 40.62 | 54.40 | **+0.23σ** | **56.59%** | **2001 Bankacılık Krizi ✅** |
| 2004 | 59.33 | 44.53 | 8.60 | **+0.42σ** | **64.91%** | Geçiş (güven henüz toparlanmadı) |
| 2008 | 58.75 | 48.85 | 10.44 | **-0.66σ** | **20.82%** | Küresel kriz sınırlı etki |
| 2012 | 55.14 | 51.06 | 8.89 | **-0.84σ** | **16.09%** | Reformist dönem sonu (maks. stabilite) |
| 2013 | 54.99 | 50.69 | 7.49 | **-0.91σ** | **14.47%** | Gezi / 17-25 Aralık başlangıcı |
| 2018 | 44.76 | 43.16 | 16.33 | **+0.48σ** | **67.27%** | **2018 Döviz Krizi ✅** |
| 2021 | 43.62 | 39.77 | 19.60 | **+1.68σ** | **94.68%** | **TCMB Güven Kaybı ✅** |
| 2022 | 43.54 | 39.10 | 72.31 | **+1.97σ** | **96.78%** | **Hiperenflasyon ✅** |
| 2024 | 42.45 | 36.45 | 58.51 | **+1.81σ** | **95.73%** | Ortodoks sıkılaştırma |

**Epistemik bulgular:**
- 2005-2012 arası kriz olasılığı %11-17 bandı = AB çıpası + kurumsal güven tampon etkisi
- 2008 küresel kriz Türkiye'de yıkıcı olmadı: güven tampon çalıştı (Trust = 0.79)
- 2013 sonrası "güven erozyonu" kümülatif → 2018 şokuna sıfır direnç

---

## 13B: CBC-07 REJİM GEÇİŞİ MOTORU

> **Kaynak:** `loop_001/CBC_ARCHITECTURE.md` + session eksik bulgu analizi  
> **Durum:** ⚠️ Assumed — Kural yapısı tanımlandı, sayısal kalibrasyon bekliyor

### 13B.1 Rejim Kilitleme Kuralları

```
REJIM_LOCK_1 — Devalüasyon Tetikleyicisi:
  IF MBP_t ≥ 0.65 AND ICF_t ≥ 0.60 AND NRG_t ≥ 0.55
  THEN P_DEV_30 → kritik eşiği aşar
  MECHANISM: Makro + Kurumsal + Anlatı kopuşunun üçlü kilit

REJIM_LOCK_2 — Görünmez Kaçış Rejimi:
  IF MBP_t = 0.40-0.64 AND SDP_t ≥ 0.65 AND EBP_t ≥ 0.60
  THEN hane halkı "sessizce kayıt dışına kaçıyor"
  MECHANISM: Toplumsal çürüme + Kaçış baskısı → kurumsal sistem yok sayılıyor

REJIM_LOCK_3 — Kriz Bulaşması (CCP Döngüsü):
  IF CCP_t ≥ 0.55 AND (MBP_t ≥ 0.45 OR ICF_t ≥ 0.50)
  THEN Yayılım: bir piyasadan diğerine çapraz bulaşma başlar
  MECHANISM: Sistemik korelasyon kilitleniyor
```

### 13B.2 Veritas Kilitleri (CBC-09)

```
TEMPORAL_ARROW_VETO:
  Gelecek verisi geçmişe sokulamaz (Amnesia Protokolü)
  t+1 bilgisi t anında kullanılırsa → OTOMATİK VETOLANİR

DATA_GAP_LOCK:
  Gözlemlenmemiş dönemde çıkarım kilitlenir
  Kaynak: "Mevcut veri yok" → ⚠️ Assumed ile işaretleme zorunlu

SINGLE_SOURCE_LOCK:
  Tek kaynaktan gelen kritik bulgu otomatik olarak ⚠️ Assumed
  Çift kaynak doğrulaması olmadan ✅ statüsü YOK

UNIT_MISMATCH_LOCK:
  Farklı birim ölçeğindeki seriler birleştirilemez (örn. yıllık vs. aylık z-skor)

ALLEGATION_GUARD:
  Bireysel suç, örgütsel isnat veya kişi atıfı → OTOMATİK BLOK
  HOW NOT WHO ilkesi; sistem suç tayini yapmaz
```

**⛔ Etik Bayrak:** Veritas kilitleri baskı mekanizması değil, epistemik kalite güvencesidir. Bu kilitler devre dışı bırakılamaz; Kaptan bile kilitleri aşamaz; Kaptan kilitler çerçevesinde karar alır.


---

