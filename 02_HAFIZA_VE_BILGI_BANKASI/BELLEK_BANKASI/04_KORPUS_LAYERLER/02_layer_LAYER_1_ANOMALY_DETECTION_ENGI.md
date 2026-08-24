# LAYER 1: ANOMALY DETECTION ENGINES

## 1A: BORSA İHLAL TESPİT ALGORİTMALARI

> **Kaynak:** `02_FRAUD_DETECTION/T2SAIM_DETECTION_ALGORITHMS_MATEMATIK.md`  
> **Durum:** ✅ Verified — 8 case, 100% detection, 0.08% FP (12,100 event cross-validation)  
> **Daubert Uygunluğu:** ✅ A+ (mahkeme kanıt paketi olarak kullanılabilir)

### 1A.1 Genel Performans

| Gate | Vaka | Tespit | FP Oranı | KE Skoru |
|------|------|--------|----------|----------|
| V1 | BOFA Treasury | 100% | 0.30% | 78.1 |
| V2.0 | JPM Precious Metals | 100% | 0.00% | 92.0 |
| V2 | SARAO Flash Crash | 100% | 0.00% | 74.2 |
| V3.2 | PANTHER/COSCIA HFT | 100% | 0.30% | 77.8 |
| V4.3 | ATLAS/CONSTANTIN Sosyal Medya | 100% | 0.00% | 93.0 |
| V4.1 | CITRON/LEFT Short-Distort | 100% | 0.00% | 85.1 |
| V5 | LIDINGO/GALENA Anlatı | 100% | 0.00% | 85.1 |
| V6 | ZMQUANT Wash Trading | 100% | 0.00% | 60.6 |
| **ORT.** | **HEPSİ** | **100%** | **0.08%** | **80.7** |

### 1A.2 Gate V1: Basic Spoofing (BOFA Treasury)

**Fizik:** Hayalet emirler = iptal edilmiş + çok kısa ömürlü + piyasa etkisi yaratacak büyüklükte.

```
is_ghost(emir)  = θ(status = CANCELLED) ∧ θ(t_lifetime < 1.0s)
is_large(emir)  = θ(s_usd > 1,000,000)

DETECTION = is_ghost(emir) ∧ is_large(emir)
```

**Eşik Gerekçesi:**
- 1.0s: Gerçek emirler ortalama 10-60s piyasada kalır. 10× güvenlik marjı.
- $1M: Treasury piyasasında fiyat etkisi eşiği. BOFA case ortalaması $2-5M idi.

### 1A.3 Gate V2.0: Kalibre Multi-Product Spoofing (JPM Precious Metals)

**Kritik Kalibrasyon:** size_ratio eşiği 5.0 → 2.0

```
size_ratio = max(s_far, s_near) / min(s_far, s_near)

Mode A (Standart):
  is_ghost_A     = θ(status=CANCELLED) ∧ θ(t_lifetime < 20s)
  is_large_A     = θ(s_contracts > 30)
  is_asymmetric_A = θ(size_ratio > 2.0)   ← KRİTİK: 5.0'dan düşürüldü
  DETECT_A = is_ghost_A ∧ is_large_A ∧ is_asymmetric_A

Mode B (Küçük ama sık):
  is_ghost_B     = θ(status=CANCELLED) ∧ θ(t_lifetime < 15s)
  is_medium_B    = θ(10 < s_contracts ≤ 30)
  is_asymmetric_B = θ(size_ratio > 3.0)
  DETECT_B = is_ghost_B ∧ is_medium_B ∧ is_asymmetric_B

Mode C (Bariyer savunması):
  is_barrier_C    = θ(barrier_count ≥ 3)
  is_coordinated_C = θ(tüm emirler 5s içinde iptal)
  DETECT_C = is_barrier_C ∧ is_coordinated_C

DETECTION = DETECT_A ∨ DETECT_B ∨ DETECT_C
```

**Neden 2.0?** Normal piyasada gözlenen maksimum size_ratio: 1.89. 2.0 / 1.89 = %6 güvenlik tamponu. JPM sistematik manipülasyonunun gerçek aralığı 2-5× idi; 5.0 eşiği vakaların %66'sını kaçırıyordu.

### 1A.4 Gate V2: Layering Detection (SARAO)

```
L = {(pᵢ, sᵢ, tᵢ)} : Fiyat seviyelerindeki emirler kümesi

is_layered = θ(n_layers ≥ 3) ∧ θ(total_fake > 500) ∧ θ(spacing_σ < 0.5)

Piramit büyüklüğü: total_fake = Σᵢ sᵢ (tüm iptal edilenler)
Sarao deseni:      s₁ > s₂ > s₃ > ... > sₙ (azalan piramit)
```

### 1A.5 Gate V3.2: HFT Burst Detection (PANTHER)

**Kritik Fix:** `<` → `≤` (boundary condition)

```
is_ghost = θ(t_lifetime ≤ 2.0s)   ← KRİTİK: ≤ not <

DETECTION = is_cancelled ∧ is_ghost ∧ θ(s_contracts > 80)
```

**Ders:** Algoritmik yuvarlama tam sınırda (t=2.0s) yığılma yaratır. 48 event bu sınırda kayboluyordu.

### 1A.6 Gate V4.3: Social Media Manipulation (ATLAS)

**3 adımlı kalibrasyon:** 10× → 5× → 4.5×

```
social_spike = v_social > (baseline_median × 4.5)   ← İNCE AYAR
price_jump   = |Δprice| > 0.10

DETECTION = social_spike ∧ price_jump
```

**Güvenlik Doğrulaması:**
- Normal max: 99 post/saat
- Yeni eşik: 55 × 4.5 = 247.5 post/saat  
- Güvenlik marjı: 247.5 - 99 = 148.5 (büyük tampon ✅)

### 1A.7 Gate V4.1–V6 (Özet)

```
Short-and-Distort (CITRON):
  DETECTION = θ(t_cover < 20dk) ∧ θ(|Δprice| > 0.01) ∧ θ(media_24h = True)

Narrative Manipulation (LIDINGO):
  DETECTION = θ(cosine_similarity > 0.75) ∧ θ(target_price/actual_price > 2.5)
              ∧ θ(author_paid = True ∧ no_disclosure)

Wash Trading (ZMQUANT):
  DETECTION = θ(account_buy = account_sell) ∧ θ(|Δnet_position| < 0.01)
              ∧ θ(execution_ms < 100)
```

### 1A.8 Kalibrasyon Metodolojisi

```
ADIM 1: Başlangıç implementasyonu (literatürden eşik)
ADIM 2: Miss analizi (FN dağılımını incele)
ADIM 3: Eşik ayarı (dağılım 95. persentili kullan)
ADIM 4: Güvenlik marjı doğrulaması: max(normal) + 2σ < τ_yeni
ADIM 5: Çapraz validasyon (12,100 normal event)
ADIM 6: Yeniden test (100% detection + FP ≤ 0.5%)
```

**⚠️ Ethics Flag — 1A:**  
Bu algoritmalar piyasa gözetim amacıyla tasarlanmıştır. Manipülasyon iddiası üretmez, anomali skoru üretir. Hukuki değerlendirme insan uzmana ve yargıya aittir. Daubert uyumlu kanıt paketi oluşturulurken bu sınır korunmalıdır.

---

## 1B: FRAUD DETECTION ENHANCEMENT

> **Kaynak:** `02_FRAUD_DETECTION/FRAUD_MATHEMATICAL_ENHANCEMENT_v6.md`  
> **Durum:** ✅ Pilot-ready matematiksel genişletme. Mevcut XGBoost + Platt + gate mimarisini bozmaz.

### 1B.1 Yedi Geliştirme Ekseni (Özet Tablosu)

| Eksen | Matematiksel Araç | Bağlantı |
|-------|------------------|---------|
| Kısıtlı Bayes-Optimal Eşik | Lagrangian 3-eşik | BAF-B2, B3 |
| Gate Etkileşim Matematiği | Çarpımsal gate formülü | BAF-B4 |
| Bilgi-Kuramsal Doğallık | Zamansal entropi, NCD, burstiness | PS-P0 |
| Grafik Spektral Yöntemler | PPR, Fiedler değeri, bipartite yoğunluk | PS-P1, P2 |
| Ardışık Hipotez Testi (SPRT) | Sequential kanıt biriktirme | Canlı akış |
| TARCOMAP Potts Genişletme | Çok-rollü enerji modeli | PS-P3 |
| Pareto Eşik Optimizasyonu | Çok-amaçlı frontier | BAF-B3+ |

### 1B.2 Kısıtlı Bayes-Optimal Eşik

**Mevcut formül** (Appendix A.4):
$$c_i^\star = \mathbf{1}\{p_i A_i \ge C_a\}$$

**Problem:** Alarm bütçesi yok, analist kapasitesi yok.

**Kısıtlı formülasyon** — $B$ alarm bütçesi altında:

$$c_i^\star = \mathbf{1}\{p_i A_i \ge C_a + \lambda\}$$

Lagrange çarpanı $\lambda$, $\sum c_i = B$ koşulunu sağlayacak şekilde belirlenir.

**Üç-eşikli politika Lagrangian karşılığı:**

$$\tau_k = \frac{C_a + \lambda_k}{A_{\text{ref}}}$$

| Band | Lagrange Seviyesi | Karar |
|------|-----------------|-------|
| Auto-Block | $\lambda_3 = 0$ | Yüksek risk × yüksek tutar |
| Analyst Queue | $\lambda_2 > 0$ | Orta risk, inceleme |
| Soft-Flag | $\lambda_1 > \lambda_2$ | Düşük risk, izleme |
| Pass | — | Alarm yok |

### 1B.3 Gate Etkileşim Matematiği

**Doğrusal model (mevcut):**
$$S_{\text{pre}}(x) = w_N N(x) + w_C C(x) + w_G G(x) + w_F F(x)$$

**Çarpımsal gate modeli (geliştirilmiş):**
$$S_{\text{pre}}(x) = w_F F(x) \cdot \left[1 + \alpha_N (1 - N(x)) + \alpha_C (1 - C(x)) + \alpha_G G(x)\right]$$

**Özellik:** $F(x)$ düşükse (fraud head tetiklenmediyse) upstream kapılar tek başına yüksek alarm üretemez. Bu, "fraud etiketi süreç kırığının üstüne binen semantik etiket" ilkesiyle matematiksel uyumdur.

### 1B.4 Bilgi-Kuramsal Doğallık Ölçüleri

**Zamansal Entropi:**
$$H_e = -\sum_{k=1}^{24} \hat{p}_k \log_2 \hat{p}_k, \quad \hat{p}_k = h_k / \sum_j h_j$$

- $H_e \approx 4.58$: Doğal insan davranışı (eşit dağılım)
- $H_e \ll 4.58$: Bot/script sinyali

**Burstiness (Goh & Barabási, 2008):**
$$B_e = \frac{\sigma_g - \mu_g}{\sigma_g + \mu_g}$$

| $B_e$ | Anlam |
|-------|-------|
| $\to 1$ | Aşırı patlamalı → bot |
| $\approx 0$ | Poisson-benzeri → doğal |
| $\to -1$ | Aşırı düzenli → otomatik |

**Normalized Compression Distance (İşlem Dizisi için):**
$$\text{NCD}(D_{e_1}, D_{e_2}) = \frac{C(D_{e_1} \| D_{e_2}) - \min(C(D_{e_1}), C(D_{e_2}))}{\max(C(D_{e_1}), C(D_{e_2}))}$$

$\text{NCD} < 0.3$ → "tek mutfak" → aynı script ile üretilmiş işlem dizileri.

**Birleşik Naturalness Skoru:**
$$N(x) = \sigma\left(\beta_0 + \beta_H H_e + \beta_{\Delta H} |\Delta H_e| + \beta_B B_e + \beta_{\text{NCD}} \overline{\text{NCD}}_e + \beta_{\text{circ}} \text{Circ}(x) + \beta_{\text{fr}} \text{Fr}(x)\right)$$

### 1B.5 Grafik Spektral Yöntemler

**Personalized PageRank (PPR) — Risk Yayılımı:**
$$\mathbf{r} = \alpha (I - (1-\alpha) \tilde{A})^{-1} \mathbf{s}$$

- $\mathbf{s}$: Bilinen fraud düğümlerinden tohum vektörü
- $\alpha \in (0.1, 0.3)$: Restart olasılığı
- $O(|E|)$ karmaşıklıkla hesaplanabilir ✅

**Fiedler Değeri** $\lambda_2$ (Graf Laplacian'ından):
- $\lambda_2 \approx 0$: Zayıf bağlı → shell company yapısı
- Organize fraud ağları düşük $\lambda_2$ gösterir

**Temporal-Graph Birleşik Skor:**
$$G_{\text{temporal}}(x) = G(x) \cdot \left(1 + \gamma \cdot \mathbf{1}\{B_e > B_{\text{thresh}}\}\right)$$

Bu formül PaySim'de LM-1+LM-2 combined Lift@TopK'nın 1.339× → 2.313× artışını açıklar.

### 1B.6 Ardışık Hipotez Testi (SPRT)

Streaming veri için Wald testi:

$$\Lambda_n = \sum_{j=1}^{n} \log \frac{f_1(x_{e,j})}{f_0(x_{e,j})}$$

Karar kuralı:

$$\text{Karar} = \begin{cases}
\text{Alarm} & \Lambda_n \ge \log \frac{1-\beta}{\alpha} \\
\text{Temiz} & \Lambda_n \le \log \frac{\beta}{1-\alpha} \\
\text{Devam} & \text{aksi halde}
\end{cases}$$

### 1B.7 Elkan Cost-Sensitive Learning

$$w_i = \begin{cases} A_i / C_a & y_i = 1 \text{ (fraud)} \\ 1 & y_i = 0 \text{ (normal)} \end{cases}$$

$A_i$: Kaçan fraud tutarı, $C_a$: İnceleme maliyeti.  
XGBoost `sample_weight` parametresine doğrudan verilir.

### 1B.8 Kalibrasyon Drift Testi

$$\text{ECE}_t = \sum_{b=1}^{B} \frac{n_b}{N} \left| \bar{y}_b - \bar{p}_b \right|$$

$\text{ECE}_{t+\Delta} > \text{ECE}_t + \epsilon$ ise kalibrasyon bozulmuş → yeniden kalibrasyon tetiklenir.

### 1B.9 Epistemik Hijyen — 1B

| Bildiğim (Verified) | Varsaydığım (Assumed) | Doğrulayamadığım |
|--------------------|-----------------------|-----------------|
| Üç-eşikli politika Lagrangian çerçeveye oturur | Çarpımsal gate doğrusal modelden daha iyi | Potts parametrelerinin stabil olacağı |
| PPR $O(\|E\|)$ ile hesaplanabilir | Elkan ağırlıklaması XGBoost savings'i artıracak | SPRT'nin yüksek fraud oranı dışında çalışacağı |
| ECE zaman serisi drift tespiti için uygun | NCD işlem dizisi için de etkili | Kalibrasyon bozulma eşiği $\epsilon$ değeri |

---

## 1C: FALSE NARRATIVE DETECTION (FNRES)

> **Kaynak:** `FNRES_MISINFORMATION_DETECTION/10_VALIDATIONS/FNRES_SEALED_MATHEMATICAL_CORE_V1.md`  
> **Durum:** ✅ SEALED (2026-05-22) — Referans spesifikasyon, empirik classifier değil  
> **Onay:** Kaptan Tarkan Bulan, McCoy Epistemic Autonomy Review

### 1C.1 Sınır Koşulları (Critical Ethics Boundary)

⛔ **Ethics Flag — FNRES:**  
FNRES yalnızca şunları ölçer: iddia düzeyinde kanıt durumu, yanlış bilgi riski sinyalleri, yayılma davranışı, anlam kayması, düzeltme dinamikleri.

FNRES **şunları yapmaz ve yapamaz:**
- Sansür veya bastırma talimatı üretmek
- İdeoloji etiketi koymak
- Kimliğe dayalı suçlama yapmak
- ClaimEvidenceGate geçmeden final "sahte" etiketi üretmek
- Hiciv, metafor veya korunan ifadeyi cezalandırmak

### 1C.2 İçerik Nesnesi

```
x = (T, I, A, V, S, U, G, M, tau)

T   : metin
I   : görsel
A   : ses
V   : video
S   : kaynak metadata
U   : URL/provenance
G   : yayılma grafiği
M   : medya metadata
tau : zaman
```

İddia atomizasyonu: $C(x) = \{c_1, c_2, \ldots, c_n\}$

### 1C.3 Etkin Bağımsız Kanıt

Birbirine bağımlı kanıtlar bağımsız sayılamaz:

$$N_{\text{eff}} = \frac{m}{1 + \bar{\rho}(m - 1)}$$

Bu formül kaynak yıkama ve platform kopyalamasının güveni şişirmesini engeller.

### 1C.4 İddia Kanıt Kapısı (ClaimEvidenceGate)

```
ClaimEvidenceGate(c_i) = PASS ancak ve ancak:
  N_eff(c_i) >= N_min
  VE provenance(c_i) >= P_min
  VE Refute(c_i) >= R_min  (false/fake bulgusu için)
  VE çelişki doğrudan iddia düzeyinde eşlenmiş

Temel Kilit:
  Fake(c_i) = 1 ancak Y(c_i) = REFUTED VE Gate = PASS ise
```

Kapı başarısız olursa izin verilen çıktı: risk/belirsizlik/insan incelemesi (final sahte etiketi değil).

### 1C.5 T2SAIM Katman Eşlemesi

$$KE_{\text{FNRES}} = 0.40 \times ZTJ + 0.30 \times IUY + 0.30 \times SST$$

**Ontolojik Veto:**
```
if physically_impossible(c_i) = true:
    KE_FNRES = 0
    status = REFUTED_ON_ZTJ
```

**Eksik Veri Kuralı:**
```
missing_data ≠ evidence_of_absence
```

### 1C.6 FNRES Katman Skorları

**L1 — Anlatı-Dilbilimsel:**  
$S_{L1} = f(H_{text}, LexDiv, LLI, CSLO, SST)$

**L2-T — Zamansal Adli Tıp:**  
$S_{L2T} = f(\text{timestamp\_integrity}, \text{propagation\_lag}, \text{correction\_lag})$

**L2-N — Ağ ve Kaynak Yapısı:**  
$S_{L2N} = f(\text{source\_laundering}, \text{network\_authority}, \text{coordination})$

**L3 — Yayılma Ağı:**
$$\text{PVI} = \frac{\text{propagation\_volume}}{\max(\Delta t, \epsilon)}$$

**L6 — Anlam Kayması:**
$$\text{CMR} = \frac{\text{edits\_or\_variants}}{\max(\Delta t, \epsilon)}$$

**L7 — Epistemik Kontaminasyon:**
$$\text{ECS} = f(\text{contaminated\_citations}, \text{circular\_refs}, \text{low\_quality\_sources})$$
$$\text{CHL} = \text{düzeltmenin orijinal maruziyetin \%50'sine ulaşma süresi}$$

### 1C.7 FNRES Birleşik Skoru (v3, Sealed)

$$S_{\text{FNRES}} = 0.15 S_{L1} + 0.15 S_{L2T} + 0.15 S_{L2N} + 0.20 S_{L3} + 0.15 S_{L6} + 0.15 S_{L7} + 0.05 S_{FH}$$

$$CRS = \frac{S_{\text{FNRES}} + 100 \times KE_{\text{FNRES}}}{2}$$

**$S_{\text{FNRES}}$ bir risk ve inceleme skoru olup kendi başına gerçek etiketi değildir.**

### 1C.8 Popper Hipotez Katmanı

```
H1 = Organik / masum / yeterince doğru yayılım
H2 = Gürültü veya hata
H3 = Bağlam kaybı
H4 = Hiciv / metafor / sözel olmayan içerik
H5 = Koordineli yanlış bilgi / yıkama / manipülasyon
```

**H1 önce test edilmeli.** Çürütülemiyorsa final etiket ihtiyatlı olmalıdır.

### 1C.9 Çıktı Katmanları

| Tier | Anlamı |
|------|--------|
| CLEAR | Düşük risk, yeterli kanıt |
| WATCH | Orta risk veya eksik kanıt |
| REVIEW | Yüksek belirsizlik, hassas bağlam |
| REFUTED_CLAIM | Yalnızca ClaimEvidenceGate PASS sonrası |

**Teknik Kart Bağlantısı:**

| TC | Matematiksel Rol |
|----|----------------|
| TC-FNRES-001 | Yayılma hızı ve çapraz platform gecikmesi |
| TC-FNRES-002 | Kaynak yıkama grafiği ve bağımsızlık kaybı |
| TC-FNRES-003 | Anlam kayması ve iddia mutasyonu |
| TC-FNRES-004 | Bot ve amplifikasyon imzaları |
| TC-FNRES-005 | Anlatı entropisi ve epistemik kontaminasyon |
| TC-FNRES-006 | Düzeltme yarı-ömrü ve erişim |

---

## 1D: SNCX KISITLI-KAPSAM DOĞRULAMA ÇERÇEVESİ

> **Kaynak:** `03_UK_POLITICS_PREDICTION/SNCX_TEK_DOSYA_OPERASYON_KAPSULU_v01.md`  
> **Durum:** ✅ Tüm birincil node'lar: Restricted Approved  
> **Kapsam:** Forensic audit, anomali ayrımı, savunma simülasyonu, erken uyarı, backtesting

### 1D.1 Kapsam Sınırı

```
İzin verilen:   forensic audit, anomaly detection, defensive simulation,
                early warning, backtesting
Yasak:          intervention, manipulation, population steering,
                person-level blame, autonomous decision
Karar otoritesi: Tarco
```

### 1D.2 Final Tier Kuralı (En Zayıf Halka)

$$\text{SNCX\_Final\_Tier} = \min(\text{AUROC\_tier}, \text{FPR\_tier}, \text{FPR\_CP\_UB\_tier}, d'\text{\_tier}, \text{ECE\_tier}, \text{Brier\_tier}, \ldots)$$

Final rank = En zayıf geçerli kanıt halkası.

### 1D.3 Temel Metrikler

$$\text{ASA} = \text{Observed\_Behaviour} - \text{Expected\_Baseline}$$

$$\text{AUROC}_m = P(S_m^+ > S_m^-)$$

$$d' = \frac{\mu_+ - \mu_-}{\sigma_{\text{pooled}}}$$

$$\text{ECE}_m = \sum_b \frac{|B_b|}{N} \left|\bar{y}_b - \bar{p}_b\right|$$

$$\text{Expected\_Harm} = P(FP) \times Cost(FP) + P(FN) \times Cost(FN)$$

### 1D.4 7 Node Sistemi

| Node | AUROC | FPR | d' | Durum |
|------|------:|----:|---:|-------|
| SPHY_LuxMarchesi_PhaseRisk | 0.9689 | 0.42% | 3.54 | ✅ Restricted |
| SPHY_WealthExchange_GiniPareto | 0.9799 | 0.94% | 2.28 | ✅ Restricted |
| SPHY_KPR_MinorityGame | 0.9789 | 1.73% | 1.66 | ✅ Restricted |
| SPHY_SpeculationPattern_ASA | 0.9325 | 1.83% | 2.19 | ✅ Restricted |
| SPHY_PublicGood_CollectiveRisk | 0.9788 | 0.00% | 2.39 | ✅ Restricted |
| SPHY_Criticality_StylizedFacts | 0.9656 | 0.00% | 3.63 | ✅ Restricted |
| SPHY_ModelTransferRisk_Guardrail | — | — | — | Veto mekanizması |

### 1D.5 Node Formülleri

```
LuxMarchesi (Faz Riski):
  L7RI = z(NoiseTraderRatio) + z(Price_Fundamental_Gap)
         + z(VolatilityClustering) + z(TailRisk)
         - z(Fundamentalist_Stabilization)

WealthExchange (Gini-Pareto):
  PowerConcentration = z(Gini) + z(Pareto_Tail) + z(TopShare)
                       - z(Mobility) - z(Auditability)

KPR (Azınlık Oyunu):
  KPR_Risk = z(UtilizationPressure) + z(UnservedRate)
             + z(RepeatCallerRate) + z(WaitingTime) + z(FairnessGap)
             - z(ResolutionRate)

Speculation (ASA):
  ASA_spec = Observed_BubbleGeometry - Expected_BubbleGeometry

PublicGood (Kolektif Risk):
  CollectiveRisk = z(ThresholdGap) + z(ExternalityLoad)
                   + z(ContactIntensity) + z(FailureGrowth)
                   - z(CooperationRate) - z(RecoveryRate)

Criticality (Stilize Gerçekler):
  CriticalityRisk = z(VolatilityClustering) + z(TailThickness)
                    + z(CorrelationRise) + z(LongMemory) + z(SelfExcitation)

ModelTransfer (Gardiyan):
  TransferRisk = z(DomainDistance) + z(ProxyWeakness) + z(LabelUncertainty)
                 + z(NormativeOverreach) + z(InterventionTemptation)
                 - z(ExternalValidation)
  VETO: Metaphor ≠ Metric
```

### 1D.6 Monte Carlo Failure Kuralları

```
CP-UB FPR > 5%    → Experimental/Hold üstüne çıkamaz
d' < 1.0          → Discrimination quality doubtful
Post-hoc event window → AUROC/FPR geçersiz
Undefined baseline    → ASA geçersiz
No ModelTransfer_Audit → Promotion forbidden
```

### 1D.7 Promotion Eşikleri

| Metrik | Candidate-Validated | Strong |
|--------|--------------------:|------:|
| AUROC | ≥ 0.80 | ≥ 0.90 |
| FPR | ≤ 5.00% | ≤ 1.00% |
| FPR_CP_UB | ≤ 5.00% | ≤ 1.00% |
| d' | ≥ 1.25 | ≥ 1.78 |
| ECE | ≤ 0.10 | ≤ 0.05 |
| Brier | ≤ 0.20 | ≤ 0.10 |

**Strong için:** Simulation-only kanıt yasaktır. Gerçek veri zorunlu.

**Strong için:** Simulation-only kanıt yasaktır. Gerçek veri zorunlu.

---

## 1E: ZTJ TEST BATARYASI — ZAMAN-TOPOLOJİK JÜRİSİ (L1)

> **Kaynak:** `_PIPELINE_WORK/Corpus T2SAIM_v09_6_FULL_SPEC_SEALED.md` [Section 3]  
> **Durum:** ✅ SEALED — Zaman katmanındaki yedi bağımsız testin kanonik tanımı.

Zaman-Topolojik Jürisi (ZTJ), veri kümesinin zamansal yapısındaki anomali yoğunluğunu ölçer. Yedi bağımsız test paralel olarak ham zamansal katman $L_1(D)$ üzerinde çalıştırılır. Katman çıktısı, testlerin maksimum değeridir:

$$S_{\mathrm{ZTJ}}(D) = \max\bigl(S_{\mathrm{ZTJ,1}},\; S_{\mathrm{ZTJ,2}},\; \ldots,\; S_{\mathrm{ZTJ,7}}\bigr)$$

*   **Durağanlık Ön Geçidi (Stationarity Pre-Gate):** ZTJ testleri çalıştırılmadan önce serinin durağanlığı Augmented Dickey-Fuller (ADF) testi ile sorgulanır. Durağan olmayan ($p > 0.05$) seriler için fark alma (differencing) veya rejim-uyumlu baseline uygulanması zorunludur.

### 1E.1 ZTJ-1 — Kumpas Testi (Caliper Test)
*   **Çalışma İlkesi:** Doğal süreçlerde olaylar arası zaman aralıkları varyans gösterir. Otomatik bot üretimi timelines aşırı düzenli (metronomic) ya da yapay olarak yığınlanmış (clustered) yapılar sergiler. Caliper testi olaylar arası boşlukların değişim katsayısını (Coefficient of Variation) ölçer.
*   **Matematiksel Çerçeve:** Zaman sırasına göre olaylar arası farklar:
    $$\Delta t_i = t_{i+1} - t_i, \quad i = 1, \ldots, n-1$$
    $$\mathrm{CV}(\Delta t) = \frac{\sigma(\Delta t)}{\mu(\Delta t)}$$
    Doğal süreçlerde $\mathrm{CV} \approx 1.0 \pm 0.3$ aralığındadır. Anomali skoru dönüşümü:
    $$S_{\mathrm{ZTJ,1}}(D) = \begin{cases} 1.0, & \text{eğer } \mathrm{CV} < 0.1 \text{ veya } \mathrm{CV} > 2.5, \\ \min\!\bigl(1,\; |\mathrm{CV} - 1.0| / 0.5\bigr), & \text{diğer durumlarda.} \end{cases}$$
*   **Kısıt:** En az $n \ge 30$ olay olmalıdır; aksi halde $\mathrm{N/A}$ döner.

### 1E.2 ZTJ-2 — Kalım ve Tehlike Analizi (Survival & Hazard Analysis)
*   **Çalışma İlkesi:** Tekrarlayan olaylarda tehlike fonksiyonu (hazard function), olayların yeniden gerçekleşme anlık riskini tanımlar. Doğal örüntüler heterojen ve geçmişe bağımlı (path-dependent) iken; sahte timelines düz monotonik artış veya hafızasız (flat Poisson) bir dağılım gösterir.
*   **Matematiksel Çerçeve:** Weibull tehlike modeli:
    $$h(t \mid \alpha, \lambda) = \frac{\alpha}{\lambda} \left(\frac{t}{\lambda}\right)^{\alpha - 1}$$
    *   $\alpha = 1$: Sabit risk (Poisson süreci).
    *   $\alpha > 1$: Monoton artan risk.
    *   $\alpha < 1$: Azalan risk.
    Model katsayısı $\alpha$, referans kohort $\hat{\alpha}_{\mathrm{organic}}$ dağılımına karşı Likelihood Ratio (LR) testi ile sınanır:
    $$S_{\mathrm{ZTJ,2}}(D) = \begin{cases} \text{normalize edilmiş LR istatistiği} \in [0,1], & \text{eğer } N_{\mathrm{recurrent}} > 5, \\ \mathrm{N/A}, & \text{aksi halde.} \end{cases}$$

### 1E.3 ZTJ-3 — Stil-Kronometri (Stylchronometry)
*   **Çalışma İlkesi:** İnsan üretimi metinler zamanla evrilir. Uzun zaman dilimine yayılan bir korpusun kelime dağarcığı ve stili sıfır sapma (rigid stationarity) gösteriyorsa, bu durum toplu (batch) yazım veya makine üretimi işareti olabilir.
*   **Matematiksel Çerçeve:** Zamansal pencerelerde çıkarılan stilometrik özellik serisi $y_t$ için ADF birim kök testi uygulanır:
    $$\Delta y_t = \alpha + \beta t + \gamma y_{t-1} + \sum_{i=1}^{p} \delta_i \Delta y_{t-i} + \epsilon_t$$
    Birim kökün **reddedilmesi** (serinin durağan çıkması), uzun bir zaman dilimi iddiası altında anomali olarak değerlendirilir.
    $$S_{\mathrm{ZTJ,3}}(D) = \min\!\left(1,\; \frac{\overline{\cos(\theta_{\mathrm{adj}})} - \mu_{\mathrm{cos,organic}}}{\sigma_{\mathrm{cos,organic}}}\right) \cdot \mathbb{1}[\Delta t_{\mathrm{claimed}} > \tau_{t,\mathrm{min}}]$$

### 1E.4 ZTJ-4 — Çoklu-Fraktal Trendinden Arındırılmış Dalgalanma Analizi (MF-DFA)
*   **Çalışma İlkesi:** Doğal finansal ve sosyal süreçler çoklu fraktaldır (küçük ve büyük dalgalanmalar farklı ölçeklenir). Tek bir Hurst katsayısı bu yapıyı kaçırır. MF-DFA, dalgalanmaları $q$ dereceli momentlere genişleterek anomaliyi tespit eder.
*   **Matematiksel Çerçeve:** $N \ge 1000$ serisi için:
    1. Kümülatif profil: $Y(k) = \sum_{t=1}^{k}(x_t - \langle x \rangle)$.
    2. Trendden arındırılmış varyans $F^2(s,\nu)$ segment bazlı hesaplanır.
    3. Flüktüasyon fonksiyonu:
       $$F_q(s) = \left\{ \frac{1}{N_s} \sum_{\nu=1}^{N_s} \bigl[F^2(s,\nu)\bigr]^{q/2} \right\}^{1/q}$$
    4. Log-log grafiğinde $H(q)$ eğimi çıkarılır. Spektrum genişliği $\Delta H = \max_q H(q) - \min_q H(q)$ hesaplanır. Monofraktal (sabit $H(q)$) yapay veri işareti olarak kabul edilir.
       $$S_{\mathrm{ZTJ,4}}(D) = \min\!\left(1,\; \frac{\Delta H + |\Delta H_{\mathrm{asym}}|}{\Delta H_{\mathrm{ref}}(R)}\right)$$

### 1E.5 ZTJ-5 — Ölçeğe Bağlı Lyapunov Katsayısı (SDLE)
*   **Çalışma İlkesi:** Gürültülü, kısa ve durağan olmayan serilerde kaos ile rassal gürültüyü ayırt etmek için kullanılır.
*   **Matematiksel Çerçeve:** Faz uzayında başlangıçta $\epsilon$ mesafesinde olan iki yörünge için:
    $$\lambda(\epsilon) = \lim_{\Delta t \to 0} \frac{1}{\Delta t} \left\langle \ln \frac{\|x(t+\Delta t) - x'(t+\Delta t)\|}{\|x(t) - x'(t)\|} \right\rangle_{\|x - x'\| \approx \epsilon}$$
    *   $\lambda(\epsilon) \approx \text{const} > 0$: Deterministik kaos.
    *   $\lambda(\epsilon) \sim -\ln(\epsilon)$: Rassal/Brownian gürültü.
    *   **Anomali İmzası:** Küçük ölçekte sabit (doğal gürültü), büyük ölçekte yükselen (dışarıdan dayatılan yapay yapı) SDLE profili.
    $$S_{\mathrm{ZTJ,5}}(D) = \min\!\left(1,\; \frac{D_{\mathrm{KL}}\bigl(\lambda_{\mathrm{obs}}(\epsilon) \| \lambda_{\mathrm{ref}}(\epsilon)\bigr)}{D_{\mathrm{KL,ref}}(R)}\right)$$

### 1E.6 ZTJ-6 — Bai-Perron Çoklu Yapısal Kırılma Testi
*   **Çalışma İlkesi:** Veri içindeki bilinmeyen kırılma tarihlerini tespit ederek, resmi/narrative beyan edilen kırılma tarihleri ile kıyaslar. Bildirilmeyen gizli rejim değişiklikleri anomali olarak işaretlenir.
*   **Matematiksel Çerçeve:** $m$ adet kırılma noktası için:
    $$y_t = z_t' \beta_j + u_t, \quad t \in (T_{j-1}, T_j]$$
    Artıkların kareler toplamını global olarak minimize eden kırılma tarihleri $\hat{T}_j$ aranır:
    $$\hat{m}, \{\hat{T}_j\} = \arg\min_{m, \{T_j\}} \sum_{j=1}^{m+1} \sum_{t=T_{j-1}+1}^{T_j} \left(y_t - z_t' \beta_j\right)^2$$
    $$S_{\mathrm{ZTJ,6}}(D) = \min\!\left(1,\; \frac{|\{\hat{T}_j\} \setminus \{T_j^{\mathrm{claimed}}\}|}{\hat{m}+1} + 0.30 \cdot \mathbb{1}\bigl[\mathrm{SupF} > \mathrm{SupF}_{\mathrm{crit}}(\alpha)\bigr]\right)$$

### 1E.7 ZTJ-7 — Tekrarlanma Analizi (RQA - Recurrence Quantification Analysis)
*   **Çalışma İlkesi:** Dinamik sistem yörüngesindeki tekrarlanma yapısını inceler. DET (Determinism) oranı, sistemin rastgelelikten ne kadar uzaklaştığını gösterir.
*   **Matematiksel Çerçeve:** Gecikmeli faz uzayı yörüngesi $\vec{x}_i \in \mathbb{R}^m$ için tekrarlanma matrisi:
    $$R_{ij}(\varepsilon) = \mathbb{1}\!\left[\|\vec{x}_i - \vec{x}_j\| \leq \varepsilon\right]$$
    $$\mathrm{DET} = \frac{\sum_{l \geq l_{\min}} l \cdot P(l)}{\sum_{i,j} R_{ij}(\varepsilon)}$$
    $$S_{\mathrm{ZTJ,7}}(D) = \min\!\left(1,\; \frac{|\mathrm{DET}_{\mathrm{obs}} - \mathrm{DET}_{\mathrm{ref}}(R)|}{\sigma_{\mathrm{DET,ref}}(R)}\right) \qquad (N \ge 500)$$

---

## 1F: SST TESPİT GEÇİTLERİ — SİSTEMSEL SAPMALAR TOPLAMI (L2)

> **Kaynak:** `_PIPELINE_WORK/Corpus T2SAIM_v09_6_FULL_SPEC_SEALED.md` [Section 4]  
> **Durum:** ✅ SEALED — İlişkisel katmandaki M-serisi ve G-serisi geçitlerin kanonik spesifikasyonu.

SST katmanı, ilişkisel-topolojik yapıyı ikili geçitlerin ağırlıklı toplamıyla değerlendirir.

$$S_{\mathrm{SST}}(D) = \min\!\left(1,\; \frac{\sum_m g_m(D) \cdot w_m}{\sum_m w_m}\right)$$
*   $w_m = 1.0$: Standart geçitler.
*   $w_m = 1.5$: Ölümcül geçitler (tek başına Daubert Tier yükselten kritik devreler).
*   **Çapraz Bulaşma Sınırı (CCR):** $\mathrm{CCR} \le 0.005$ (%0.5) olmalıdır. Aksi halde geçitlerin parametreleri yeniden kalibre edilir.

### 1F.1 M-Serisi Geçitleri (Market Microstructure)

#### M1 — Hayalet Emir Geçidi (Order Lifetime Test)
Yapay emir yerleştirme ve anında iptal etme (spoofing/layering) örüntüsü:
$$g_{M1}(o) = \mathbb{1}\bigl[\mathrm{status}(o) = \mathrm{CANCELLED}\bigr] \cdot \mathbb{1}\bigl[t_{\mathrm{life}}(o) < \tau_{M1}(R)\bigr]$$
*   Eşik $\tau_{M1}(R)$: R1 (normal) < 5s, R2 (HFT) < 100ms, R3 < 1ms.

#### M2 — Emir Büyüklüğü Asimetrisi (Size Asymmetry)
Tek yönlü baskı kurma amaçlı derinlik dengesizliği:
$$\mathrm{AR}(t) = \frac{\max(Q_{\mathrm{bid}}(t), Q_{\mathrm{ask}}(t))}{\min(Q_{\mathrm{bid}}(t), Q_{\mathrm{ask}}(t))}$$
$$g_{M2}(t) = \mathbb{1}\bigl[\mathrm{AR}(t) > \tau_{M2}(R)\bigr] \qquad (\tau_{M2} \approx 3.0)$$

#### M3 — Katmanlama Tekdüzeliği (Layering Uniformity)
 incremental fiyat basamaklarına yapay ve eşit aralıklı emir yığma:
$$g_{M3}(D) = \mathbb{1}[n_{\mathrm{layers}} \geq 3] \cdot \mathbb{1}\!\left[\sum_i Q_{\mathrm{fake},i} > \tau_{M3,\mathrm{vol}}(R)\right] \cdot \mathbb{1}[\sigma_{\mathrm{spacing}} < \tau_{M3,\sigma}(R)]$$

#### M4 — Karşılıklı Eşleşme Geçidi (Wash Trading) - 🚨 ÖLÜMCÜL GEÇİT
Aynı nihai faydalanıcının alıcı ve satıcı tarafta olması:
$$g_{M4}(D) = \mathbb{1}\bigl[\exists\, (b,s) \in D : \mathrm{beneficiary}(b) = \mathrm{beneficiary}(s) \wedge |p_b - p_s| < \tau_{M4,p}(R)\bigr]$$

### 1F.2 G-Serisi Geçitleri (Structural & Topological)

#### G-B — Benford Kanunu Geçidi (First-Digit Test)
Verilerin ilk anlamlı basamağının Benford dağılımına uyumu:
$$P_B(d) = \log_{10}\!\left(1 + \frac{1}{d}\right), \quad d \in \{1, \ldots, 9\}$$
İki test birlikte uygulanır (Disjunctive):
$$\chi^2_B = N \sum_{d=1}^{9} \frac{(P_{\mathrm{obs}}(d) - P_B(d))^2}{P_B(d)} \qquad \mathrm{MAD}_B = \frac{1}{9} \sum_{d=1}^{9} |P_{\mathrm{obs}}(d) - P_B(d)|$$
$$g_{GB} = \mathbb{1}[\chi^2_B > \chi^2_{\mathrm{crit}}(8, \alpha)] \vee \mathbb{1}[\mathrm{MAD}_B > \tau_{\mathrm{MAD}}] \qquad (\text{MAD} > 0.015 \implies \text{Nonconforming})$$

#### G-NET — Ağ Topolojisi Analizi (Network Topology)
Ağ yoğunluğu ($\rho$), ortalama kümelenme ($C$) ve merkezileşme ($H$) indisleri:
$$\rho = \frac{2m}{n(n-1)}, \quad C = \frac{1}{n}\sum_i \frac{2e_i}{k_i(k_i-1)}, \quad H = \max_i \frac{k_i}{\langle k \rangle}$$
Bu üç parametre organik baselinedan anlamlı derecede saptığında geçit ateşlenir.

#### G-PH — Kalıcı Homoloji (Persistent Homology TDA)
Farklı ölçeklerdeki topolojik boşlukların Wasserstein mesafesiyle ölçülmesi:
$$W_p(\mathrm{PD}_{\mathrm{obs}}, \mathrm{PD}_{\mathrm{ref}}) = \left(\inf_{\gamma} \sum_{x \in \mathrm{PD}_{\mathrm{obs}}} \|x - \gamma(x)\|^p\right)^{1/p}$$
$$g_{GPH}(D) = \mathbb{1}\bigl[W_p > \tau_{PH}(R)\bigr] \cdot \mathbb{1}[N \geq 200]$$

#### G-HAW — Hawkes Kendinden Uyarım Geçidi (Hawkes Self-Excitation)
Olayların ardışık kaskad tetikleme yoğunluğu:
$$\lambda(t) = \mu + \sum_{t_j < t} \phi(t - t_j), \quad \phi(s) = \alpha e^{-\beta s}$$
$$g_{GHAW}(D) = \mathbb{1}\!\left[\frac{\hat{\alpha}}{\hat{\beta}} > 1\right] \vee \mathbb{1}[\hat{\alpha} < \alpha_{\mathrm{min,organic}}(R)]$$

#### G-VG — Yatay Görünürlük Grafiği (Horizontal Visibility Graph)
Zaman serisini ağa dönüştürerek affin-invariance (ölçekten bağımsızlık) koruması sağlar:
$$y_k < \min(y_i, y_j) \quad \forall\, t_k \in (t_i, t_j)$$
$$g_{GVG}(D) = \mathbb{1}[D_1 > \tau_1] \cdot \mathbb{1}[D_2 > \tau_2] \cdot \mathbb{1}[D_3 > \tau_3] \cdot \mathbb{1}[N \geq 1000]$$

---

## 1G: IUY ANALİZ MOTORLARI — İÇSEL UYUMSUZLUK YOĞUNLUĞU (L3)

> **Kaynak:** `_PIPELINE_WORK/Corpus T2SAIM_v09_6_FULL_SPEC_SEALED.md` [Section 5]  
> **Durum:** ✅ SEALED — Dilsel ve anlamsal katman hata tespit algoritmaları.

IUY katmanı, veri girdilerindeki anlamsal ve yapısal tutarsızlıkları inceler.

$$S_{\mathrm{IUY}}(D) = \max\!\bigl(S_{\mathrm{IUY,H}},\; S_{\mathrm{IUY,LZC}},\; S_{\mathrm{IUY,style}}\bigr)$$

### 1G.1 Shannon ve Yapısal Entropi Analizi
Doğal dil ve veri alanları karakteristik bilgi entropisine sahiptir. Aşırı tekdüzelik (sterility) veya aşırı yapay mükemmellik anomali olarak kodlanır.
$$H = -\sum_{w \in \mathcal{W}} p(w) \log_2 p(w)$$
*   Doğal metinler için: $H \approx 4.0 - 5.5$ bits/word.
$$S_{\mathrm{IUY,H}}(D) = \min\!\left(1,\; \frac{|H_{\mathrm{obs}} - H_{\mathrm{ref}}|}{\sigma_{H,\mathrm{ref}}}\right)$$

### 1G.2 Lempel-Ziv Karmaşıklığı (LZC)
Algoritmik karmaşıklığı ölçerek yapay tekrarları ve şablon kopyalamaları yakalar.
$$\mathrm{LZC}(s) = \frac{c(s) \log_2 n}{n}$$
*   $\mathrm{LZC} \to 1$: Maksimum karmaşıklık.
*   $\mathrm{LZC} \to 0$: Yüksek periyodik tekrar.
$$S_{\mathrm{IUY,LZC}}(D) = \min\!\left(1,\; \frac{|\mathrm{LZC}_{\mathrm{obs}} - \mathrm{LZC}_{\mathrm{ref}}|}{\sigma_{\mathrm{LZC,ref}}(R)}\right)$$

### 1G.3 Stilometrik Tutarlılık ve Kümeleme Analizi
Yazarların kelime frekansı, noktalama oranları ve cümle uzunluğu dağılımları ($x_i \in \mathbb{R}^d$) arasındaki KL Diverjansı:
$$D_{\mathrm{KL}}(P_{\mathrm{obs}} \| P_{\mathrm{ref}}) = \sum_x P_{\mathrm{obs}}(x) \log \frac{P_{\mathrm{obs}}(x)}{P_{\mathrm{ref}}(x)}$$
Kümeleme analizi sonucunda, farklı yazarlar tarafından yazıldığı iddia edilen metinlerin Silhouette skoru üzerinden tek bir kaynağa çökmesi ($s(i) > \tau_{s,\mathrm{collapse}}$) yapay şablon kullanımı olarak etiketlenir.
$$s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}$$

---

