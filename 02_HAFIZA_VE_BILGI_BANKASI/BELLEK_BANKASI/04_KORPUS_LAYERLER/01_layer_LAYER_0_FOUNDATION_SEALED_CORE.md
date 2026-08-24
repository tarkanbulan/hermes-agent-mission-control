# LAYER 0: FOUNDATION (SEALED CORE)

> **Kaynak:** `01_NUCLEUS_SEALED/Corpus T2SAIM_v09_6_FULL_SPEC_SEALED.md`  
> **Durum:** ✅ SEALED — Değiştirilemez. Tüm diğer katmanlar buna dayanır.

## 0.1 T2SAIM Nedir?

T2SAIM (Tarco 2 Socio-Analytical Intelligence Machine), gözlemlenebilir örüntü sapmalarını anomali skoru olarak ölçen, niyet ya da suçluluk atıf yapmayan bir **analiz motorudur**.

**Temel Ayrım:**

```
Anomali:  Gözlemlenebilir örüntü sapması [T2SAIM ölçer]
İhlal:    Niyet + Anomali + Yasal ihlal [İnsan yargılar]

T2SAIM çıktısı: Anomali skoru ∈ [0, 100]
Karar:          İnsan analisti → Tarco
```

## 0.2 Temel Mimari İlkeleri

**İlke 1 — HOW NOT WHO:**  
T2SAIM "kim yaptı?" sorusunu sormaz. "Nasıl bir örüntü var?" sorusunu sorar.  
⛔ *Ethics Flag:* Kişi düzeyinde niyet atfı yasaktır.

**İlke 2 — Katmanlı Kanıt:**  
Tek bir sinyal alarm üretmez. Birden fazla bağımsız kapıdan geçen kanıt birikimi gerekir.

**İlke 3 — Tarco Otoritesi:**  
Sistem analiz sunar. Karar vermez. Karar = Tarco.

**İlke 4 — En Zayıf Halka Kuralı:**  
Bir iddianın güvenilirliği en güçlü kanıtıyla değil, en zayıf halkasıyla belirlenir.

**İlke 5 — Tek Değişkenli Ablation:**  
Her yeni bileşen, tek değişkenli deney ile ölçülür. Birden fazla şeyi aynı anda değiştirme.

## 0.2A Matematiksel Altyapı ve Veri Ayrıştırma

T2SAIM, analiz edilen veri kümesini üç bağımsız ve dikey katmana ayrıştırır.

Tanım 0.2A.1: Analiz edilecek ham veri kümesi:
$$D = \{(t_i, s_i, v_i) : i = 1, \ldots, n\}$$
şeklinde ifade edilir. Burada:
- $t_i \in \mathbb{R}$: Zamansal koordinat (zaman damgası, işlem saati vb.),
- $s_i \in S$: İlişkisel veya yapısal kimlik (hesap, düğüm, IP adresi, organizasyon),
- $v_i \in \mathbb{R}^k$: İlişkili veri vektörü (fiyat, hacim, metin özellikleri, metaveri).

Veri kümesi $D$, analiz aşamasında aralarında veri sızıntısı olmayacak şekilde üç bağımsız katmana ayrıştırılır:
- **Zaman-Topolojik Katmanı ($L_1(D)$):**
  $$L_1(D) = \{(t_i, s_i) : i = 1, \ldots, n\}$$
  Bu katman **ZTJ** (Zaman-Topolojik Jürisi) tarafından analiz edilir.
- **İlişkisel-Topolojik Katman ($L_2(D)$):**
  $$L_2(D) = \{(s_i, s_j, w_{ij}) : \text{ilişkisel grafik kenarları}\}$$
  Bu katman **SST** (Sistemsel Sapmalar Toplamı) tarafından analiz edilir.
- **Yapısal-Dilsel Katman ($L_3(D)$):**
  $$L_3(D) = \{(v_i, e_i) : e_i = \operatorname{entropy}(v_i)\}$$
  Bu katman **IUY** (İçsel Uyumsuzluk Yoğunluğu) tarafından analiz edilir.

Katmanlar arası dikey izolasyon esastır. Bir katmanı işleyen modül, sentez aşamasına kadar diğer katmanlardan veri okuyamaz veya yazamaz.

## 0.2B Ontolojik Veto Geçitleri (Pre-Substantive Veto)

Herhangi bir analiz başlamadan önce, veri kümesi fiziksel ve nedensel yasalara göre test edilir. Veto geçitleri ikilidir (0 veya 1). Kısmi veto kabul edilmez. Tek bir veto tetiklendiğinde analiz durdurulur ve hata kodu döndürülür.

### 1. Zaman Oku İhlali (V1.1 — Temporal Arrow Violation)
Nedensel bağımlılık haritası ($\tau(i,j)$) ile zaman sıralaması çelişirse veto tetiklenir:
$$\exists\, i,j : \quad t_j > t_i \quad \text{AND} \quad s_i \text{ nedensel olarak } s_j \text{'ye bağımlı}$$
- **Çıktı:** `Status = INVALID_CAUSAL_ORDER; KE_A = N/A`

### 2. Fiziksel İmkansızlık (V1.2 — Physical Impossibility)
Aynı kimliğin ($s_i = s_j$) iki olay arasındaki mesafeyi ($d(s_i, s_j)$) aşma hızı, o varlık sınıfı için izin verilen maksimum hızı ($v_{\max}$) aşarsa veto tetiklenir:
$$\exists\, i,j : \quad \frac{d(s_i, s_j)}{|t_j - t_i|} > v_{\max} \quad \text{AND} \quad s_i = s_j$$
*Burada $v_{\max}$ değerleri: veri paketi için $c$ (ışık hızı), hava ulaşımı için 900 km/h, kara ulaşımı için 200 km/h olarak kalibre edilmiştir. Ölçüm hatası için %10 tampon payı eklenir.*
- **Çıktı:** `Status = IMPOSSIBLE_TRAVEL; KE_A = N/A`

### 3. Kanıt Zinciri Kopukluğu (V1.3 — Chain-of-Custody Rupture)
Veri bütünlüğü doğrulaması ($\operatorname{CoC}(D)$) başarısız olduğunda ve bu kopukluğun kapsamı belirsiz olduğunda tetiklenir:
$$\operatorname{CoC}(D) = \text{BROKEN} \quad \text{AND} \quad \text{extent\_unknown} = \text{TRUE}$$
- **Çıktı:** `Status = PROVENANCE_UNKNOWN; KE_A = N/A`

---

## 0.3 Karar Kalitesi Endeksi (KE)

Birleşik anomali skoru, üç ana katmanın ağırlıklı sentezidir:

$$\mathrm{KE}_A = w_1 \cdot S_{\mathrm{ZTJ}} + w_2 \cdot S_{\mathrm{IUY}} + w_3 \cdot S_{\mathrm{SST}}$$

Kanonik varsayılan ağırlıklar:
$$w_1 = 0.40, \quad w_2 = 0.30, \quad w_3 = 0.30$$

*Herhangi bir katman N/A dönerse (veri eksikliği veya veto nedeniyle), ağırlıklar aktif katmanlara göre normalize edilir. Sadece tek bir katman aktifse, belirsizlik payı $\Delta_{\mathrm{reduction}} = +0.10$ eklenir.*

### 0.3.1 Belirsizlik Nicelendirmesi (Uncertainty Quantification)
Toplam belirsizlik bandı $\Delta$ üç ana bileşenden oluşur:
$$\Delta = \sqrt{\Delta_{\mathrm{stat}}^2 + \Delta_{\mathrm{analyst}}^2 + \Delta_{\mathrm{param}}^2}$$
- **İstatistiksel Belirsizlik (Statistical Uncertainty):**
  $$\Delta_{\mathrm{stat}} = \sqrt{\sum_i w_i^2 \cdot \sigma_{S_i}^2}$$
- **Analist Belirsizliği (Analyst Uncertainty):** Aynı analizi yapan bağımsız analistler arası sapma (eğer inter-rater güvenilirlik $\kappa < 0.70$ ise zorunludur):
  $$\Delta_{\mathrm{analyst}} = \frac{\max_j(\mathrm{KE}_A^j) - \min_j(\mathrm{KE}_A^j)}{2}$$
- **Parametrik Hassasiyet (Parameter Sensitivity):** Eşik perturbationlarının etkisi:
  $$\Delta_{\mathrm{param}} = \frac{1}{2} \left|\frac{\partial \mathrm{KE}_A}{\partial \tau_m}\right| \cdot \epsilon_{\tau}$$

Raporlama formatı: $\mathrm{KE}_A \pm \Delta$ şeklinde sunulur.

### 0.3.2 Katman-Korelasyon Düzeltmesi (Layer-Correlation Correction)
İki katman aynı yapısal anomaliyi farklı enstrümanlarla ölçtüğünde oluşan mükerrer sayımı engellemek için korelasyon düzeltmesi uygulanır:
$$\mathrm{KE}_A^{\mathrm{corrected}} = \mathrm{KE}_A - \rho_{ij} \cdot \min(w_i \cdot S_i, w_j \cdot S_j)$$
*Burada $\rho_{ij}$ kalibrasyon kohortundan hesaplanan Pearson korelasyon katsayısıdır. Eğer $\rho_{ij} > 0.70$ ise katmanlardan biri askıya alınır.*

### 0.3.3 KE Yorumlama ve Daubert Tier Tablosu

| $\mathrm{KE}_A$ Skoru | Anomali Yoğunluğu / Yorum | Daubert Tier Sınıfı |
|:---:|---|---|
| $[0.00, 0.20)$ | Düşük anomali yoğunluğu. Veri organik süreçlerle tutarlıdır. | Below Candidate |
| $[0.20, 0.40)$ | Orta derece anomali. İnceleme tavsiye edilir. | Candidate (marginal) |
| $[0.40, 0.60)$ | Yüksek anomali yoğunluğu. Çoklu katman uyarısı. | Candidate |
| $[0.60, 0.80)$ | Çok yüksek anomali. Katmanlar arası güçlü yakınsama. | Strong |
| $[0.80, 1.00]$ | Kritik anomali. Ölümcül geçit uyarısı veya sistemik manipülasyon. | Supreme (Seldon J(θ) onayı ile) |

## 0.4 Multi-Gate Mimari

T2SAIM, farklı anomali tiplerine farklı matematiksel kapılar atar.

```
Matematiksel İzolasyon İlkesi:
∀ gate_i, gate_j where i ≠ j:
P(gate_i tetiklenir | gate_j'nin test verisi) ≈ 0

Çapraz kontaminasyon: 12/12,100 = 0.0099% (doğrulandı)
```

**Temel Yapı Taşları:**

```
Eşik Fonksiyonu:  θ(x, τ) = 1 if x > τ, else 0
Mantık Kapıları:  AND (∧), OR (∨)
Normalize Metrik: z = (x - μ) / σ
Bileşik Skor:     KE = Σ wᵢ · componentᵢ  (Σwᵢ = 1)
```

## 0.5 Durum Vektörü X(t) — 19 Aile

Sealed corpus'un temel gözlem kümesi 19 aileye ayrılmıştır:

| # | Aile | Kapsam |
|---|------|--------|
| 01 | Demografi | Nüfus yapısı, yaş dağılımı, bağımlılık oranı |
| 02 | Ekonomi & İşgücü | İşsizlik, ücret büyümesi, eşitsizlik |
| 03 | Finansal & Ödeme | Kredi spreadleri, piyasa stresi, ödeme sistemi |
| 04 | Konut & İnşaat | Konut fiyatları, tahliye, evsizlik zinciri |
| 05 | Yoksulluk & Refah | Yoksulluk derinliği, gıda güvensizliği |
| 06 | Seçimler & Protestolar | Oy kayması, mobilizasyon, güven |
| 07 | Haber & Olaylar | Medya duyarlılığı, anlatı yoğunluğu |
| 08 | Aile & Sosyal Kırılganlık | Aile çözülmesi, sosyal izolasyon |
| 09 | Doğum & Doğurganlık | TFR, yaş yapısı değişimi |
| 10 | Ölümlülük | İntihar oranı, pandemi, yaşam beklentisi |
| 11 | Eğitim | Okuryazarlık, devamsızlık, eğitim sistemindeki baskı |
| 12 | Konut Erişilebilirliği | Kira/gelir oranı, evden çıkarılma |
| 13 | Dış & Jeopolitik | Dış tehdit, bilgi operasyonları |
| 14 | Göç & Beyin Göçü | Net göç, beceri kaybı |
| 15 | Sağlık & Yaşam Kalitesi | NHS baskısı, ruh sağlığı, erişim |
| 16 | Din & Topluluk Yapısı | Sosyal bağ, kutuplaşma |
| 17 | Sosyal Atalet | Yapısal gecikmeler, reform direnci |
| 18 | Teknoloji & Kurumsal Kapasite | Devlet etkinliği, kurumsal güç |
| 19 | Stres Göstergeleri | Bütünleşik sosyal stres endeksi |

## 0.6 Validation Kapıları (Sealed Rules)

```
SEALED_RULE_01: Event window sonradan seçildiyse AUROC/FPR geçersizdir.
SEALED_RULE_02: Baseline tanımsızsa ASA claim geçersizdir.
SEALED_RULE_03: Label yoksa supervised metric claim geçersizdir.
SEALED_RULE_04: Lineage zayıfsa final tier yükselemez.
SEALED_RULE_05: Simulation-only Strong yasaktır.
SEALED_RULE_06: Model transfer audit yoksa promotion forbidden olur.
SEALED_RULE_07: Human oversight yoksa final karar yalnız technical draft kalır.
```

---

