# LAYER 11: KURUMSAL KIRILGANLIK & TOPLUMSAL ÇÜRÜME MATRİSİ

## 11A: TÜRKİYE KRİZ TAHMİN MODELİ (TR Crisis Prediction v0.1)

> **Kaynak:** `loop_001/TR_CRISIS_PREDICTION_MODEL_v0.1.md`  
> **Durum:** ⚠️ Assumed — Mimari tanımlandı, veri üretim aşaması

### 11A.1 Temel Ayrım

```
Klasik makro soru:        "Enflasyon kaç? Faiz kaç? Cari açık kaç?"
Bu modelin sorusu:        "İnsanlar ne zaman sessizce kaçmaya başlıyor?"
                          "Kurumsal commitment piyasa tarafından ne zaman inanılmaz bulunuyor?"
                          "Sistem hangi noktada 'baskılanmış ama sürdürülemez'den kırılmaya geçiyor?"
```

### 11A.2 Çıktı Tasarımı (Çoklu Horizon)

```
P_DEV_30 / P_DEV_60 / P_DEV_100          → Devalüasyon olasılığı
P_POLICY_BREAK_30 / 60 / 100             → Politika kopuşu
P_BANK_STRESS_30 / 60 / 100              → Bankacılık stresi
P_CAPCTRL_30 / 60 / 100                  → Sermaye kontrolü
P_SOC_TRUST_BREAK_30 / 60 / 100          → Sosyal güven kırılması

REJIM_POSTERIOR = {Normal, Carry, Inflation, FXStress, BankingStress, Crisis, Recovery}
EVENT_EXPLANATION = en etkili 5 sensör
```

### 11A.3 Altı Latent Baskı Katmanı

**MBP — Makro Kırılma Baskısı:**
```
Bileşenler:
  reserve_adequacy_düşüş      → Rezerv yeterliliği erimesi
  net_reserves_ex_swap        → Swap hariç net rezerv
  fx_deposit_share_artış      → Döviz mevduat payı artışı
  street_fx_gap               → Resmi/gayri resmi kur makası
  CDS_sıçraması               → Kredi risk primindeki artış
  negatif_reel_faiz           → Reel faiz eksi bölgede
  current_account_kırılganlık → Cari açık finansman riski
```

**ICF — Kurumsal Taahhüt Kırılması:**
```
Bileşenler:
  commitment_credibility_düşüş → İnanılırlık erozyonu
  info_asymmetry_artış         → Bilgi asimetrisi genişlemesi
  temporal_arrow_bozulması     → Politika tutarsızlığı (zaman tutarsızlığı)
  network_concentration_artış  → Güç ağı yoğunlaşması
  daron_inst_score_kötüleşme   → Acemoğlu kurumsal skor
```

**SDP — Sosyal Çürüme Baskısı:**
```
Bileşenler:
  conformity_pressure          → Uyum baskısı
  critical_thinking_strain     → Eleştirel düşünce gerilemesi
  authority_dependence         → Otorite bağımlılığı
  psychological_strain         → Psikolojik yük
  propaganda_susceptibility    → Propaganda duyarlılığı
  crisis_resilience            → (ters yönde) Kriz direnci
  reform_latency_years         → Reform gecikmesi (yıl)
```

**NRG — Anlatı-Gerçeklik Makası:**
```
Bileşenler:
  cpi_official - cpi_alt       → Resmi/alternatif enflasyon makası
  media_bias_score             → Medya yanlılık skoru
  frame_imbalance              → Çerçeveleme dengesizliği
  counterframe_absence         → Karşı-anlatı yokluğu
  public_opinion_delta         → Kamuoyu-davranış ayrışması
  trust_vs_market_davranışı    → Söylem-piyasa kopuşu
```

**EBP — Kaçış Davranışı Baskısı:**
```
Bileşenler:
  behavior_conversion_score    → Davranış dönüşüm skoru
  FX_alım_davranışı            → Döviz alım hızlanması
  altın_talebi_proxy           → Altın talebi artışı
  mevduat_dolarizasyonu        → Mevduat dolarizasyon oranı
  görünmez_piyasa_kaçışı       → Gayri resmi piyasa sinyalleri
```

**CCP — Karmaşıklık/Bulaşma Baskısı:**
```
Bileşenler:
  cross_series_korelasyon_sıkışması → Seri korelasyonlarının kilitlenmesi
  artan_varyans                      → Sistem varyansı artışı
  AC1_otokorelasyon                  → Otokorelasyon artışı
  tail_risk                          → Kuyruk riski yükselmesi
  piyasa_davranış_kilitlenmesi       → Piyasa ve davranış sensörlerinin aynı yönde hareketi
```

### 11A.4 Ana Kriz Tehlike Fonksiyonu

```
CRISIS_HAZARD_t(h) = sigmoid(
    a1 × MBP_t
  + a2 × ICF_t
  + a3 × SDP_t
  + a4 × NRG_t
  + a5 × EBP_t
  + a6 × CCP_t
  + a7 × (MBP_t × ICF_t)      ← Makro × Kurumsal etkileşim
  + a8 × (NRG_t × EBP_t)      ← Anlatı × Kaçış etkileşimi
  + a9 × (SDP_t × ICF_t)      ← Sosyal Çürüme × Kurumsal kilit
)

h = 30, 60, 100 gün için ayrı kalibre edilir.

Kritik iç görü:
  Makro bozulma tek başına yetmez.
  Kurumsal commitment erozyonu ile birleşince etkisi sertleşir.
  Sosyal çürüme + anlatı kopuşu → kırılma zamanlamasını öne çeker.
```

### 11A.5 Olay Tanımları (Etiketler)

```
E1: Devalüasyon Olayı
    30g pencerede USDTRY log getirisi ≥ tarihsel volatilite × k_eşik

E2: Rezerv Savunma Kırılması
    Net rezerv ani düşüş + kur ivmelenmesi eş zamanlı

E3: Politika Kopuşu
    Olağandışı faiz kararı / KKM-benzeri araç / ani sermaye kısıtı

E4: Bankacılık Stresi
    Kredi/mevduat + NPL + likidite + spread eş zamanlı bozulma

E5: Sosyal Güven Kırılması
    Anlatı-makro makası + kaçış davranışı + medya merkezileşmesi eş zamanlı
```

### 11A.6 Eğitim/Test Mantığı (Türkiye Tarihsel Pencereler)

```
Kriz pencereleri:
  1994, 2000-2001, 2008, 2018, 2021-2023, 2024-2026

Backtesting: Rolling-origin → her t noktasında yalnız geçmiş bilgi
Walk-forward: Amnesia çalıştırması → her gün posterior güncelleme

Performans metrikleri:
  Brier Score, Precision/Recall, Zaman-olay kalibrasyonu
  False calm / False panic ayrımı
```

---

## 11B: ACEMOĞLU KURUMSAL KATMANI

> **Kaynak:** `downloaded_resources/daron_math/` — 7 kitap işlenmiş  
> **Durum:** ⚠️ Assumed — Teorik çerçeve entegre edildi, sayısal parametre doğrulanmadı

**Acemoğlu ICF Bileşenleri:**

```
credible_commitment     → Bağlayıcı kurumsal taahhüt gücü
extractive_pressure     → Kaynak çıkartıcı baskı (elite el koyması)
state_capacity          → Devlet kapasitesi (delivery gücü)
society_counterweight   → Toplumsal denge gücü
information_asymmetry   → Bilgi asimetrisi
network_concentration   → Güç ağı yoğunlaşması

ICF_daron = f(credible_commitment, extractive_pressure, state_capacity, ...)
```

### 11B.1 T2SAIM Entegrasyonu ve Kurumsal Çürüme Denklemi

Acemoğlu kurumsal katmanının zamansal aşınmasını ve çürümesini temsil eden **Kurumsal Çürüme Katsayısı ($E_{decay}(t)$)**, toplumdaki İnanç Rejimi Basıncı ($BRP(t)$) ve ortalama Bilişsel Atrofi ($\langle C_{atrophy}(t) \rangle$) değişkenlerinin bir fonksiyonu olarak dinamikleştirilir:

$$E_{decay}(t) = E_{base} \cdot \left( 1 - \exp\left( -\gamma_e \cdot BRP(t) \cdot \langle C_{atrophy}(t) \rangle \right) \right)$$

*Açıklama: $\gamma_e > 0$ çürüme duyarlılık parametresidir. Toplumda dogmatik inanç baskısı ($BRP$) ve kronik stresin yol açtığı kolektif bilişsel körelme ($\langle C_{atrophy} \rangle$) arttıkça, rasyonel kurumsal mekanizmalar ve denetim organları devre dışı kalır; bu da devlet kapasitesinin aşınmasına ve sömürücü el koyma baskısının ($extractive\_pressure$) yükselmesine yol açarak kurumsal çürümeyi ($E_{decay}$) üstel olarak tetikler.*

---

## 11C: ERİCH HOFFER TOPLUMSAL ÇÜRÜME MATRİSİ

> **Kaynak:** `loop_002/ERICH_HOFFER_TOPLUMSAL_CURUME_GOSTERGE_MATRISI_2026-06-05.md`  
> **Durum:** ⚠️ Assumed — TÜİK/MEDAS serilerinden türetilen gözlemsel çerçeve

**Temel Sezi (Hoffer):** Kitle hareketlerini tetikleyen, salt yoksulluk değil — **ümitsizlik, köksüzlük ve umutsuzluktur.** Maddi yoksunluk + kurumsal adaletsizlik + kimlik sıkışması → kitlesel radikalleşme zemini.

### 11C.1 Sekiz Boyutlu Gösterge Matrisi

| Boyut | Teorik Anlam | TÜİK/MEDAS Ölçümleri | Risk İşareti |
|-------|-------------|---------------------|-------------|
| **A — Güvenlik Hissi** | Bireysel emniyet testi | Feel safe alone/environment, okul güvenliği, polis memnuniyeti | Güvenlik hissinde düşüş |
| **B — Kurumsal Meşruiyet** | Adalet sistemine güven | Yargı memnuniyeti, hukuka eşit uygulama, şeffaflık beklentisi | Adalet + şeffaflık çöküşü |
| **C — Aidiyet & Umut** | Gelecek ufku | Umut seviyesi, refah algısı, 5 yıl sonrası beklentisi | Umut + ülke geleceği iç içe bozulma |
| **D — Sosyal Baskı** | Normatif sıkışma | Gelenek/din/siyaset/gelir/cinsiyet baskı algısı | Çoklu kimlik eş zamanlı baskı |
| **E — Gençlik Çözülmesi** | Erken uyarı | Genç suçlu sayısı, genç mağduriyet, çocuk güvenlik birimlerine geliş | Genç suç + mağduriyet eş zamanlı artış |
| **F — Suç/Mahkûmiyet** | Sert çıktı | Cezaevine giren mahkûm sayısı, yerleşim dağılımı | Mekânsal yoğunlaşma |
| **G — Maddi Sıkışma** | Göreli yoksunluk | Yoksulluk oranı, Gini, gelir düşüşü, borçlanma | Yoksulluk + eşitsizlik + davranış birlikte kötüleşme |
| **H — Sert Sonuçlar** | Moral çözülme çıktısı | İntihar oranı, boşanma oranı | Her ikisi birlikte yükseliş |

### 11C.2 Operasyonel Çekirdek Endeks (12 + 6 Seri)

**Öncelikli 12 seri:**

```
1.  feel_safe_in_living_environment (%)
2.  feel_safe_when_sitting_at_home_alone (%)
3.  satisfaction_public_judicial_services (%)
4.  problems_law_fairly_impartially_to_all (%)
5.  level_of_hope (%)
6.  perceived_level_of_prosperity (%)
7.  perception_social_pressure_political_opinion (%)
8.  juvenile_offenders (count)
9.  incidents_juveniles_security_unit (count)
10. convicts_received_into_prison (count)
11. poverty_rate (%)
12. gini_coefficient
```

**İkinci halka (6 seri):**

```
13. crude_suicide_rate (per 100k)
14. crude_divorce_rate (per 1000)
15. borrowed_within_last_year (%)
16. income_decreased_within_last_year (%)
17. timely_intervention_police_gendarmerie (%)
18. problems_time_to_decide_on_case (%)
```

### 11C.3 Alarm Örüntüleri (Pattern Reading)

```
Örüntü 1 — Güvenlik + Adalet + Umut Çöküşü:
  feel_safe ↓ + yargı adaleti ↓ + umut ↓
  → Hoffer kitlesel radikalleşme zemini oluşuyor

Örüntü 2 — Gençlik Kırılması + Maddi Sıkışma:
  juvenile_offenders ↑ + çocuk güvenlik olayı ↑ + yoksulluk ↑ + eşitsizlik ↑
  → Nesil içi sosyal aktarım çöküşü

Örüntü 3 — Baskı Algısı + Meşruiyet Kaybı:
  siyasi/dini baskı ↑ + adalet ↓ + şeffaflık ↓ + güvenlik memnuniyeti ↓
  → Kurumsal güvenin yeniden inşası çok zor

Örüntü 4 — Sert Sonuçların Eş Zamanlı Yükselişi:
  intihar ↑ + boşanma ↑ + suç ↑
  → Hoffer çürümesinin ileri aşaması

Kural: Tek seri değil, örüntü oku. Üç veya daha fazla gösterge aynı anda bozulursa → SDP yükseliyor.
```

### 11C.4 T2SAIM Entegrasyonu

```
SDP_t ← Hoffer Endeks bileşenleri:
  conformity_pressure     ← Boyut D (sosyal baskı)
  authority_dependence    ← Boyut A/B (güvenlik + adalet)
  psychological_strain    ← Boyut C/H (umut + sert sonuçlar)
  crisis_resilience (-)   ← Boyut G (maddi sıkışma, ters)
  reform_latency_years    ← Boyut B/C (kurumsal gerileme yılları)
```

Erich Hoffer'in "Kesin İnançlılar" kitle psikolojisini simüle etmek için, ajan seviyesindeki **Fanatizm ($\text{Fanaticism}_i(t)$)** ve **Konformizm ($\text{Conformity}_i(t)$)** endeksleri Amigdala Siyaseti ve BRP değişkenlerine bağlanır:

$$\text{Fanaticism}_i(t) = \text{Fanaticism}_{base} + \omega_f \cdot T_{tribal, i}(t) \cdot A_{load, i}(t)$$

$$\text{Conformity}_i(t) = \text{Conformity}_{base} + \omega_c \cdot BRP_i(t) \cdot (1 - PFC_{control, i}(t))$$

*Açıklama: $\omega_f, \omega_c > 0$ ölçekleme katsayılarıdır. Bireyin kabileleşme seviyesi ($T_{tribal}$) ve amigdala yükü ($A_{load}$) arttıkça, rasyonel düşünce zayıflar ve fanatikleşme eğilimi yükselir. İnanç rejimi baskısı ($BRP$) altında olan ve prefrontal korteks denetimi ($PFC_{control}$) körelmiş ajanlarda ise toplumsal konformizm (sürüye kayıtsız şartsız uyum) üst seviyeye ulaşır.*

---

## 11D: KRİZ KRONOLOJİSİ — BİLEŞİK GÖSTERGE TABLOSU

> **Kaynak:** `TR_Macro_Crisis_Chronology_Report.md` + `TARCOMAP_NTZ49_Unified_Master_Report.md`

**Türkiye krizlerinin üçlü yapısı:**

```
Kriz Tipi 1 — Ani Likidite Krizi (2001 modeli):
  Tetikleyici: Makro Finansal Stres (MBP) + Kurumsal Çöküş (ICF)
  Hız:        Haftalık/aylık ölçekte patlama
  Örnek:      2001 Bankacılık ve Likidite Krizi

Kriz Tipi 2 — Uzun Dönemli Yapısal Kriz (2013-2024 modeli):
  Tetikleyici: Kurumsal çürüme (EFMI) + Sosyal çürüme (SDP) + Hiperenflasyon
  Hız:        Yıllık ölçekte birikim, anlık patlamalar
  Örnek:      2013-2024 kronik kriz platosu

Kriz Tipi 3 — Dışsal Şok Spillage:
  Tetikleyici: Küresel CCP + yerel kırılganlık
  Hız:        Haftalık ölçekte yayılım
  Örnek:      1998 Asya/Rusya krizi yayılımı
```

**En güçlü hipotez:**
```
Türkiye tipi kriz = Makro-Finansal Baskı (MBP)
                  ∧ Kurumsal Taahhüt Erozyonu (ICF)
                  ∧ Sosyal/Anlatısal Gerçeklik Kopuşu (NRG + SDP)

Makro tek başına "neden kötü"yü verir.
Sosyal-kurumsal katman "ne zaman kopacak" sorusuna katkı verir.
```

---

## 11E: UK RAPOR — KARŞILAŞTIRMALİ ÇERÇEVE

> **Kaynak:** `hermes_crisis_lab/UK RAPOR/` (91 dosya: 6 HTML analiz, 68 JSON, 15 World Bank CSV)  
> **Durum:** ⚠️ Assumed — Çerçeve hazır, sistematik kalibrasyon bekliyor

**T2SAIM TR-UK Karşılaştırmalı Metodoloji:**

```
Ortak çerçeve: Her iki ülkede de Pascal C(t) + Ψ(t) + EFMI bileşik kullanımı

Temel fark noktaları:
  Şok hızı:
    Türkiye: 1-2 hafta (kur, CDS, medya döngüsü)
    UK:      2-4 hafta (medya-siyaset döngüsü)
    Almanya: 6-12 hafta (kurumsal emici mekanizmalar)

  Kriz tipi:
    Türkiye: Döviz + kurumsal çürüme + hiperenflasyon
    UK:      Brexit kimlik bölünmesi + NHS + bölgesel eşitsizlik

  Ψ(t) baskın bileşeni:
    Türkiye: ATY_Load + TrustCollapse + FearLoad
    UK:      EnemyImage + IdentityThreat + GMI (Brexit kimliği)
```

**UK Kara Para Aklama Sinyali (Kanıt Dosyası):**

```
Anomali kategorileri:
  Şirket ağı yoğunlaşması
  Borsa/gayrimenkul eş zamanlı şüpheli işlem
  Uluslararası transfer örüntüleri
  Brexit sonrası düzenleyici boşluk
  
Metodoloji: FNRES L2N (kaynak yapısı) + B-Spine (ağ analizi) + CIB sinyalleri
```

---

*[Layer 9-11 tamamlandı.]*

*Tam Corpus Listesi:*
*Layer 0 (Foundation), 1A-1D (Anomali), 2A-2C (State Vector & Intel), 3A-3D (Domain), 4A-4D (Yayılım), 5A-5D (Simülasyon), 6A-6D (Validasyon), 7A-7F (Uygulamalar), 8A-8I (Otorite), 9A-9D (Kriz & Sosyofizik), 10A-10F (Veritas Ajan Filosu), 11A-11E (Kurumsal Kırılganlık)*

---

**Bu analiz, Science Officer Spock ve Kaptan Tarkan Bulan'a (Tarco) raporlanmak üzere yapılandırılmıştır.**

**Tevekkül Kırılma Tanımı:**
Tevekkül — Türk toplumsal sabır ve "Allah'a bırakma" eşiğinin tükenmesi anlamına gelir.
Ekonomik baskı + kurumsal güvensizlik + inanç sistemi içi çelişki birleştiğinde sosyal patlamanın önündeki son tampon çöker.

**Kırılma Koşulları (T2SAIM operasyonel tanımı):**

```
tevekkül_kırıldı = 1  EĞER:
  SRI_psy > 0.50
  VE reel_ücret_büyümesi < -0.15  (yıllık reel kayıp %15+)
  VE kurumsal_güven < 0.30
  VE son_18_ay içinde en az 1 majör şok (darbe girişimi, seçim krizi, döviz krizi)

tevekkül_kırıldı = 0  EĞER yukarıdaki koşullardan herhangi biri sağlanmıyorsa
```

**Türkiye Gözlemi (BTF arşivi):**

| Dönem | Kırılma | Tetikleyici |
|-------|---------|------------|
| 2001-Q1 | 1 | IMF krizi, %50 devalüasyon |
| 2013-Q3 | Kısmi (0.5) | Gezi / erken şok |
| 2018-Q3 | 1 | Döviz krizi, dolar 7.24 TL |
| 2021-Q4 | 1 | TCMB faiz indirimi, dolar 18 TL'ye ulaştı |
| 2022-Q2 | 1 | Enflasyon %85'i aştı |
| 2023-Q2 | Azalan (0.6) | Seçim sonrası yeni beklenti |

**SRI Entegrasyonu:**

```
IF tevekkül_kırıldı = 1:
  SRI_psy_adjusted = SRI_psy × 1.15   ← %15 amplifikasyon
  CRISIS_HAZARD_bonus = +0.08

IF tevekkül_kırıldı = 0:
  SRI_psy_adjusted = SRI_psy           ← değişiklik yok
```

⛔ **Etik Bayrak:** "Tevekkül kırılması" bir inanç kritiği değildir. Ölçülen şey sosyal sistem stres indikatorudur. Bir topluluk veya inanç grubuna yönelik negatif yargı içermez. HOW NOT WHO.

### 9A.7 Türkiye SRI Kıyaslama Tablosu (2005–2026)

| Yıl | SRI_psy | SRI_fin | SRI_vol | SRI_total | L6 | Durum |
|-----|---------|---------|---------|-----------|-----|-------|
| 2005 | 0.25 | 0.22 | 0.18 | 0.22 | 0 | Stabil |
| 2007 | 0.28 | 0.28 | 0.22 | 0.27 | 0 | Stabil |
| 2008 | 0.35 | 0.55 | 0.45 | 0.46 | 0 | Global kriz yayılımı |
| 2009 | 0.40 | 0.48 | 0.40 | 0.43 | 0 | Toparlanma |
| 2013 | 0.42 | 0.38 | 0.42 | 0.40 | 0 | Gezi şoku; finansal stabil |
| 2016 | 0.50 | 0.42 | 0.55 | 0.49 | 0 | Darbe girişimi; eşiğe yakın |
| 2018 | 0.55 | 0.65 | 0.72 | 0.65 | 1 | **ALARM — Döviz krizi** |
| 2019 | 0.48 | 0.50 | 0.45 | 0.48 | 0 | Stabilizasyon |
| 2020 | 0.50 | 0.42 | 0.48 | 0.46 | 0 | COVID şoku; yönetildi |
| 2021 | 0.58 | 0.55 | 0.50 | 0.55 | 1 | **ALARM — TCMB U-dönüşü** |
| 2022 | 0.68 | 0.72 | 0.75 | 0.72 | 1 | **ALARM — %85 enflasyon** |
| 2023 | 0.62 | 0.58 | 0.55 | 0.59 | 1 | **ALARM — Seçim+devalüasyon** |
| 2024 | 0.55 | 0.50 | 0.45 | 0.51 | 0 | Sıkılaştırma, azalan |
| 2026 | 0.52 | 0.48 | 0.40 | 0.48 | 0 | İzleme bandı |

**Kaynak:** BTF_AMNESIA/03_PARAMETRELER.md + James Methods/walkthrough.md backtest serisi

---

