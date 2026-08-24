# LAYER 18: JUMP DIFFUSION, DİJİTAL İKİZ SİMÜLASYON & CAMEL-S

## 18A: JUMP DIFFUSION & DİJİTAL İKİZ SİMÜLASYON

> **Kaynak:** `T2SAIM_TR_2M_JUMP_DIFFUSION_REPORT.html` (27 Mayıs 2026, V4.0)  
> **Durum:** ⚠️ Assumed — 2M Monte Carlo senaryo, Mayıs 2026-Mayıs 2028 ufku

### 18A.1 Metodoloji

```
Dijital İkiz (Digital Twin):
  Türkiye ekonomisinin sadece parasal değil;
    - kurumsal yorgunluk
    - yargı bağımsızlığı erozyonu
    - jeopolitik riskler
    - liyakat kaybı
  gibi "görünmez sürtünmeler" dahil 2.000.000 senaryo simülasyonu

IDIS (Institutional Decay Index Score) — Kurumsal Çürüme Parametresi:
  Standart modellere (JPMorgan, Goldman vb.) kıyasla IDIS dahil edilince:
    Drift katsayısı:        + %61   (aşağı yönlü sürüklenme artışı)
    Volatilite katsayısı:   + %26   (oynaklık artışı)
    Şok frekansı:           + %188  (kırılma sıklığı artışı)
```

### 18A.2 Temel Modelleme Yapısı

```
Standart Wiener süreciyle TRY/USD modellemesi:
  dA_t = μ × A_t × dt + σ × A_t × dW_t
  
T2SAIM Jump Diffusion eklentisi:
  dA_t = μ × A_t × dt + σ × A_t × dW_t + J_t × dN_t
  
  J_t = jump büyüklüğü (IDIS bağlantılı)
  dN_t = Poisson süreci (jump frekansı: λ_t = f(L3, L1, TAR_trigger))
```

#### T2SAIM Amigdala ve Sürüleşme Deformasyonu

Finansal varlık fiyatlarının drift ($\mu$), volatilite ($\sigma$) ve jump (şok) frekansı ($\lambda_{jump}$) parametreleri, amigdala stres yükü ($A_{load}$), finansal sürüleşme ($H_{herd}$) ve prefrontal kontrolün ($PFC_{control}$) durumuna göre dinamik olarak deforme edilir:

$$\mu(t) = \mu_0 \cdot \left( 1 + \alpha_\mu \cdot A_{load}(t) \cdot H_{herd}(t) \right)$$

$$\sigma(t) = \sigma_0 \cdot \left( 1 + \beta_\sigma \cdot A_{load}(t) \cdot \left(1 - PFC_{control}(t)\right) \right)$$

$$\lambda_{jump}(t) = \lambda_0 \cdot \left( 1 + \gamma_\lambda \cdot H_{herd}(t) \cdot \left(1 - PFC_{control}(t)\right) \right)$$

*Açıklama: $\alpha_\mu, \beta_\sigma, \gamma_\lambda > 0$ hassasiyet katsayılarıdır. Amigdala stres yükü ($A_{load}$) ve sürüleşme ($H_{herd}$) arttıkça, varlığın değer kaybetme yönünde sürüklenmesi (drift) hızlanır. Prefrontal korteks denetimi zayıfladıkça ($PFC_{control} \to 0$), amigdala yükünün etkisiyle volatilite ($\sigma$) ve ani fiyat sıçraması/şok yaşanma frekansı ($\lambda_{jump}$) üstel olarak artar. Bu durum piyasadaki kurgusal anomalilerin rasyonel fiyatlamayı tamamen ezmesine yol açar.*

IDIS etkisi:
  μ_standard = μ₀
  μ_IDIS = μ₀ × (1 + 0.61) = μ₀ × 1.61   (sürüklenme %61 artar)
  
  σ_IDIS = σ₀ × (1 + 0.26) = σ₀ × 1.26   (oynaklık %26 artar)
  
  λ_IDIS = λ₀ × (1 + 1.88) = λ₀ × 2.88   (jump frekansı %188 artar)

### 18A.3 Senaryo Projeksiyonu (Mayıs 2028)

```
Standart banka modeli tahmini: ~75 TRY/USD (Mayıs 2028)

T2SAIM Jump Diffusion medyan: %132 daha kötü
  → 75 × 2.32 ≈ 174 TRY/USD (medyan senaryo, Mayıs 2028)
  [⚠️ Assumed — 2M senaryo medyanı; rejim değişikliği olursa güncellenmeli]

T2SAIM güven aralığı dağılımı:
  %10 pesimist: hiperenflasyon/devalüasyon senaryosu (>200 TRY/USD)
  %50 medyan:   yapısal bozulma devam ediyor (~174 TRY/USD)
  %10 iyimser:  ortodoks politika kalıcılaşır (~90 TRY/USD)

Kritik not: Bu tahminler CDS piyasasının fiyatlamadığı
  IDIS (kurumsal çürüme) etkisini modele dahil etmektedir.
  Piyasa = 238bp (stabil)
  T2SAIM = +5.65σ L1 + +7.66σ L3 (sistematik çürüme devam ediyor)
```

### 18A.4 CAMEL-S Stratejik Boyutu

> **Kaynak:** Zambiya 1990-1998 bankacılık krizi analizi  
> **Durum:** ⚠️ Assumed — Türkiye adaptasyonu tamamlanmamış

```
CAMEL çerçevesi (bankacılık sağlığı):
  C = Capital adequacy (Sermaye yeterliliği)
  A = Asset quality (Aktif kalitesi / NPL)
  M = Management (Yönetim kalitesi)
  E = Earnings (Karlılık)
  L = Liquidity (Likidite)
  S = Sensitivity to market risk (Piyasa riski hassasiyeti)

T2SAIM CAMEL-S Zamanlaması (Zambiya dersinden):
  24 ay öncü sinyal: L (Likidite) bozulması → L1_t
  9-12 ay öncü:      C (Sermaye) erozyonu → L2_t (zombi birikimi)
  6-9 ay öncü:       A (NPL artışı) → L2_t yükseliyor
  
"Flight to Quality" → L4 psikososyal stres:
  Piyasa stresinin zirvelendiği anda risk iştahı tam kapanır
  Körfez fonlarının 2022'de %27 payı = "flight from Batı, to Körfez"
  Bu L3 coğrafi risk iştahı kayması + L1 likidite stresi bileşkesi

Önemli: Sektör bazlı risk = gecikmiş sinyal (NPL 6-9 ay gecikmeli)
         L1-L3 sistem sinyalleri = öncü (24 ay önce görünüyor)
```

---

