# LAYER 6: ÇAPRAZ KESİM VALİDASYONU & ENTEGRASYON

## 6A: EPİSTEMİK HİJYEN PROTOKOLÜ

> **Kaynak:** `06_CROSS_CUTTING/` + Layer 2C IntelOP kuralları  
> **Durum:** ✅ Verified yapı; ⚠️ Assumed kalibrasyon eşikleri

### 6A.1 Epistemic Mark Sistemi

| İşaret | Anlam | Aksiyon |
|--------|-------|---------|
| ✅ Verified | Çoklu bağımsız kaynak, ampirik kanıt | Doğrudan kullanım |
| 🔴 THE TEST | Test prosedürü tanımlı, henüz tamamlanmadı | Protokolü çalıştır |
| ⚠️ Assumed | Çalışma hipotezi, doğrudan kanıt yok | İşaretle, izle, güncelle |
| ❌ Invalid | Yanlışlandı veya hesaplanamaz | Reddedildi |
| ⛔ Ethics Flag | Yanlış kullanım potansiyeli yüksek | Kaptan onayı + McCoy |

### 6A.2 Evrensel Performans Eşikleri

| Metrik | Minimum | Tercih Edilen |
|--------|---------|--------------|
| AUROC | ≥ 0.85 | ≥ 0.92 |
| False Positive Rate | ≤ 0.08 | ≤ 0.03 |
| Brier Score | ≤ 0.15 | ≤ 0.08 |
| ECE | ≤ 0.10 | ≤ 0.05 |
| N_eff | ≥ 30 | ≥ 100 |
| Out-of-Sample | ≥ 24 ay | ≥ 60 ay |

### 6A.3 Çapraz Kirlilik Kontrolü

```
Multi-Gate hedefi: P(çapraz-kirlilik) = 0.0099

Kontrol:
  Her modül izole değerlendirme yapar
  Modüller arası geçiş yalnızca mühürlü arayüzler üzerinden
  Her birleşim noktasında kanıt kalitesi kontrolü
```

### 6A.4 Popper Yanlışlanabilirlik Metriği (MOD-5)
Karl Popper'ın sınır çekme ilkesine göre, bir iddianın bilimsel değeri onun hangi koşullar altında yanlışlanabileceğiyle (falsifiable) ölçülür. T2SAIM ACH (Analysis of Competing Hypotheses) matrisi kapsamında her analiz için en az beş rakip hipotez test edilir:
- **H1 — Organik/Masum:** Veri doğal süreçlerle tutarlıdır, dış müdahale yoktur.
- **H2 — Rassal Gürültü:** Anomaliler ölçüm hatası veya örnekleme gürültüsüdür.
- **H3 — Tek Aktörlü Aksaklık:** Koordine olmayan tekil bir aktörün hatası.
- **H4 — Kurumsal/Sistemik Başarısızlık:** Süreç/denetim hatası, liyakatsizlik.
- **H5 — Koordineli Manipülasyon:** Ortak çıkar doğrultusunda çoklu aktör koordinasyonu.

Popper Yanlışlanabilirlik Skoru $\mathcal{F}(H)$:
$$\mathcal{F}(H) = 1 - \frac{|\{h \in H : h \text{ mevcut kanıtlar } E \text{ altında henüz yanlışlanmadı}\}|}{|H|}$$
*   $\mathcal{F}(H) = 1.0$: En yüksek epistemik çözünürlük (tek bir hipotez hayatta kaldı).
*   $\mathcal{F}(H) < 0.40$: Yüksek epistemik risk (çürütülemeyen çok fazla hipotez var). Rapor belirsizlik bandı $\Delta$ otomatik olarak $+0.05$ artırılır.
*   **Yalancı-Bilimsel Hipotez Filtresi:** Eğer bir hipotezin yanlışlanmasını sağlayacak minimum kanıt kümesi ($E^*$) mantıksal veya fiziksel olarak gözlemlenemez şekilde tasarlanmışsa, o hipotez ACH matrisinden elenir.

#### 📑 Popper Metriği Falsifikasyon Matrisi (16 Senaryo)

| # | Senaryo | Beklenen Davranış | Başarısızlık Modu |
|---|---|---|---|
| 1 | H1 Caliper Testi | Yüksek CV → H1 elenir; Düşük CV → H1 kalır | Caliper testi uygulanmadan H1'in kabulü |
| 2 | H2 SDLE Testi | Rassal SDLE profili → H2 kalır | Kaotik veya deterministik yapıyı gürültü saymak |
| 3 | H3 G-NET Testi | Çoklu hub yapısı → H3 elenir | Tekil hub tespit edilemeyip H3'ün elenmesi |
| 4 | H4 L4-CSI Testi | Koordineli zamanlama → H4 elenir | Coincidental timing'in koordinasyon sayılması |
| 5 | H5 ZTJ-6 Testi | Koordinasyon tarihinde kırılma yoksa → H5 elenir | Kırılmanın yanlış tarihe atfedilmesi |
| 6 | Tüm H1-H5'in hayatta kalması | $\mathcal{F}(H) = 0$, belirsizlik $+0.10$ | Düşük F-skorunun gizlenmesi |
| 7 | Yalnızca H1'in kalması | $\mathrm{KE}_A \le 0.40$ (organik durum teyit edilir) | H1 hayattayken yüksek KE_A skoru üretilmesi |
| 8 | Yalnızca H5'in kalması | $\mathrm{KE}_A \ge 0.80$ (Daubert Supreme tetiklenir) | H5 kalmasına rağmen alt tierde işlem yapılması |
| 9 | Korelasyonlu Hipotezler | Katman korelasyon correction uygulanır | Korelasyonlu hipotezlerin bağımsız sayılması |
| 10 | Kanıtın kendisinin anomalik olması | Ontolojik Veto 2.1 check tetiklenir | Kirli kanıtla hipotez eleme yapılması |
| 11 | Kanıtların sansürlenmesi | Belirsizlik artırılır, sansür notu eklenir | Eksik verinin "yokluk kanıtı" sayılması |
| 12 | Testin hesaplama dışı kalması | Kısmi F-skoru raporlanır | Yapılamayan testi "geçti" olarak kodlamak |
| 13 | Uzman uyuşmazlığı | Adjudication protokolüyle kappa kontrol edilir | Düşük güvenilirlikte F-skoru kararlaştırmak |
| 14 | Tarihsel emsal eksikliği | baseline kohort karşılaştırması yapılır | baseline olmadan F-skoru kullanmak |
| 15 | Geçmişe dönük bakış sapması | BTF Amnesia protokolü uygulanır | Gelecek verinin geçmişe sokulması |
| 16 | Domain değişimi | Portabilite endeksiyle kalibre edilir | correction uygulamadan domain shift |

---

### 6A.5 Seçim Öngörülerinde 8 Başarısızlık Modu ve Raporlama Dili

Seçim tahminlerinde ve kamuoyu analizlerinde epistemik hataları, aşırı güven (overconfidence) sapmalarını ve metodolojik kısırlıkları engellemek amacıyla tanımlanan asgari denetim ve dil standartları şunlardır:

#### 📑 8 Başarısızlık Modu Kataloğu

| Hata Modu | Tanım | Önleme / Denetim Kuralı |
|:---|:---|:---|
| **Döngüsel Girdi (Circular Input)** | Modelin çıktısı olması gereken bir tahmini veya varsayımı modele girdi olarak beslemek (örn. V5'teki NOC tahmini). | Modeli sadece bağımsız anket ve demografi gibi birincil gözlemlerle beslemek; ara çıktıları mühürlemek. |
| **Gevşek NOC Şartı (Loose NOC)** | Simülasyonun neredeyse her koşulda NOC (kararsızlık) üreteceği şekilde gevşek kısıtlar tanımlamak. | Tarihsel UK seçim NOC oranları (45-65%) ile varyans katsayısı ($\sigma_{\text{ward}} = 0.11$) kalibrasyonu yapmak. |
| **Aşırı Güvenli Güven Aralığı** | Gauss dağılımını kalın kuyruklu (fat-tail) siyasi dalgalanmalarda körce kullanmak. | Dağılım kuyruk testi yapmak; gerekirse prior olarak Lévy kararlı dağılımına geçmek. |
| **Unverified'ı Verified Sunmak** | Temel kanıt seviyesi doğrulanmamış narratif veya anketleri kesin bilgi gibi sunmak. | Verified/Assumed/Unverified epistemik değerlendirme tablosunu zorunlu kılmak. |
| **Kör Model Transferi** | Bir fiziksel sistem modelini (örn. saf spin modelleri) sosyal kitlelere insan faktörünü hiçe sayarak uygulamak. | Model çıktısını Red Team ve McCoy Biyoplausibility testlerine tabi tutmak. |
| **Geriye Dönük Bakış Sapması** | Seçim bittikten sonra model parametrelerini geriye dönük bükerek "zaten bildik" iddiasında bulunmak. | Tüm tahminlerin seçimden en az 72 saat önce hash seal ile mühürlenmesi (Ante-dönem kilidi). |
| **Köksüz Sayı (Rootless Numbers)** | Nereden geldiği, hangi formülle türetildiği belirsiz ("Razor Gap 19.4" vb.) sihirli katsayılar kullanmak. | Her katsayı için açık bir türetim zinciri (derivation chain) zorunluluğu koymak. |
| **Red Team İhlali** | Tier düzeyini yüksek göstermek için Red Team ve bağımsız karşıt hipotez denetimini atlamak. | "No Red Team $\to$ No Tier" kuralını işletmek; analizi Candidate seviyesinde bırakmak. |

#### 📑 Raporlama Dili Kısıtlamaları

T2SAIM kapsamında kesinlik belirten ve yönlendirici olan ifadeler yasaktır. Raporlarda güvenli dil alternatifleri kullanılmalıdır:

| Yasaklı/İhlalli Dil | Güvenli/Standart Dil Alternatifi |
|:---|:---|
| "Labour seçimi kesinlikle kazanacak." | "Labour'ın tek başına çoğunluk kazanma olasılığı $\%P$ (99% CI: $[a, b]$) olarak simüle edilmiştir." |
| "Rus botları seçimleri manipüle etti." | "D-08 (Devlet destekli bilgi operasyonu) ile uyumlu dilsel simetri anomalileri tespit edilmiştir; nedensel etki doğrulanamamıştır." |
| "Modelimiz seçimleri 98% doğrulukla bildi." | "Post-hoc meclis bazlı ortalama sapma $\%D$ (14 eksen üzerinden) olarak hesaplanmıştır." |
| "Seçim gecesi büyük bir panik olacak." | "Finansal ve sosyo-politik rezonans endeksleri ($SRI$) alarm eşiği ($>3\sigma$) üzerindedir; oynaklık artışı beklenmektedir." |

---

## 6B: KALİBRASYON TEST BATARYASI

> **Durum:** 🔴 THE TEST — Her modül için ayrı test protokolü

### 6B.1 Fraud Detection — 8 Gate

| Gate | Hedef FPR | Hedef TPR | Test Seti |
|------|-----------|-----------|-----------|
| BOFA (Spoofing) | ≤ 0.02 | ≥ 0.97 | CFTC-2015 kayıtları |
| JPM (Iceberg) | ≤ 0.03 | ≥ 0.95 | SEC-2012 kayıtları |
| SARAO (HFT) | ≤ 0.02 | ≥ 0.98 | 2010 Flash Crash |
| PANTHER (Tuna Squish) | ≤ 0.04 | ≥ 0.93 | CFTC-2013 kayıtları |
| ATLAS (Momentum) | ≤ 0.03 | ≥ 0.95 | Sentez verisi |
| CITRON (Wash) | ≤ 0.05 | ≥ 0.92 | Sentez verisi |
| LIDINGO (Coordinated) | ≤ 0.04 | ≥ 0.94 | Sentez verisi |
| ZMQUANT (HFT-Adaptive) | ≤ 0.04 | ≥ 0.94 | Sentez verisi |

**Kümülatif hedef:** FP = 0.08% — tam validasyon bekliyor.

### 6B.2 FNRES Kalibrasyon

```
Brier Score: ≤ 0.15
AUROC: ≥ 0.85
FPR: ≤ 0.08
Claim-level precision (insan yargılaması): ≥ 0.80
Monte Carlo stres testi: ≥ 1M simülasyon
OOD testi: dağılım dışı içerik davranışı
Decision curve analizi: net fayda ≥ 0 tüm eşiklerde
```

### 6B.3 SNCX Kalibrasyon

```
Her node için: AUROC ≥ 0.85 VEYA İnsan-AI anlaşması ≥ 0.80
Final Tier → Gerçek Çıktı tutarlılığı: ≥ 0.75
Weakest Link doğrulaması: min(tier) = Final_tier
```

### 6B.4 Pascal C(t) Kalibrasyon

```
UK tarihsel şoklar: Brexit, COVID, Enerji Krizi 2022
Her şok için: R² ≥ 0.70 (ekonomik kanallar)
Zaman gecikmesi doğruluğu: ±2 ay
Parametre kurtarma: α, β, γ gerçekle uyum ≥ 0.80
```

### 6B.5 Kalibrasyon Disiplini ve ECE/DCA Metrikleri (MOD-6/7)
Doğru bir anomali analizi, tahmin edilen olasılıkların ve kararların gerçek dağılımlarla kalibre edilmesini gerektirir. T2SAIM kalibrasyon doğruluğunu iki temel metrikle izler:

#### 1. Expected Calibration Error (ECE - Beklenen Kalibrasyon Hatası)
ECE, tahmin edilen güven oranları ile gözlemlenen doğruluk oranları arasındaki farkı eşit büyüklükteki binler (gruplar) üzerinde ölçer:
$$\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} \left|\operatorname{acc}(B_m) - \operatorname{conf}(B_m)\right|$$
*   $M$: Bin sayısı (varsayılan $M = 10$).
*   $B_m$: $\left(\frac{m-1}{M}, \frac{m}{M}\right]$ güven aralığına düşen tahminler.
*   $\operatorname{acc}(B_m)$: $m$-binindeki gerçek doğruluk oranı.
*   $\operatorname{conf}(B_m)$: $m$-binindeki ortalama güven skoru.
*   *Kural:* Son $N \ge 1000$ veri üzerinde ECE $> 0.10$ olduğunda kalibrasyon uyarısı verilir; ECE $> 0.15$ ise model askıya alınır.

#### 2. Decision Curve Analysis (DCA - Karar Eğrisi Analizi)
DCA, anomali eşiklerine göre aksiyon almanın net faydasını (Net Benefit) ölçer:
$$\mathrm{NB}(p_t) = \frac{\mathrm{TP}}{N} - \frac{\mathrm{FP}}{N} \cdot \frac{p_t}{1 - p_t}$$
*   $p_t$: Müdahale/karar verme eşiği.
*   *Kural:* Modelin karar-faydalı olması için, karar aralığı olan $p_t \in [0.01, 0.20]$ bandında $\mathrm{NB}_{\mathrm{model}}(p_t) > \mathrm{NB}_{\mathrm{all}}(p_t)$ ve $\mathrm{NB}_{\mathrm{model}}(p_t) > 0$ olmalıdır.

#### 3. ECE/DCA Daubert Tier Eşlemesi

| Kalibrasyon Tier | ECE Eşik Değeri | DCA Şartı |
|---|---|---|
| Candidate | ECE < 0.10 | NB > NB_all (at $p_t < 0.10$) |
| Strong | ECE < 0.05 | NB > NB_all (at $p_t < 0.05$) |
| Supreme | ECE < 0.02 | NB > NB_all (at $p_t < 0.001$) |

---

## 6C: SPOR & VARLIK BENCHMARKLARİ (Sektör Validasyonu)

> **Durum:** 🔴 THE TEST — Tasarlandı, yürütülmedi

### 6C.1 Spor Benchmark Mantığı

Spor verisi neden ideal test alanı:
- Sonuçlar kesinlikle bilinir (gerçek skorlar)
- Veri büyüktür (binlerce maç)
- Karmaşık insan/grup dinamikleri içerir (Ψ analogları)
- Dış müdahale kontrol altında

```
Test Tasarımı:
  Giriş: Takım istatistikleri, baskı, ev/deplasman,
          son form, sakatlık, motivasyon endeksleri
  Çıktı: P(W), P(D), P(L)
  Değerlendirme: Brier skoru, AUROC, Kalibrasyon eğrisi
  Kıyaslama: Vegas odds
```

### 6C.2 Varlık Benchmark

```
Varlıklar: EURUSD, GBPUSD, FTSE 100, Altın, Petrol

Test Tasarımı:
  Giriş: EDS-32 X_t + Pascal P(t) + Ψ(t)
  Çıktı: h-adım getiri dağılımı
  Değerlendirme: Sharpe backtest, MDD, Calmar ratio
  Kıyaslama: Buy-and-hold, momentum baseline
  
⛔ Akademik kalibrasyon. T2SAIM yatırım tavsiyesi vermez.
```

---

## 6D: ENTEGRASYON MATRİSİ

### 6D.1 Sistem Veri Akışı

```
Ham Veri
    ↓
[Layer 1: Anomali Detektörleri]
  Fraud 8-Gate → A_sncx(t)
  FNRES L1-7 → KE_FNRES → C_gate(t)
  SNCX 7-Node → L7RI, PC, CR, K, PCCR, CEI, CRI
    ↓
[Layer 2-4: Durum & Nedensellik]
  Z(t) = [X, Ψ, O, A_sncx, C_gate, S_t]
  Pascal C(t) → P(t) = C(t) × X(t)
  EDS-32 → Finansal tahmin
  IntelOP 44 modül → Epistemik sınıflandırma
    ↓
[Layer 5: TARCOMAP Simülasyon]
  E_total(k,t) → CoA olasılıkları
  SDE dZ/dt → gelecek durumlar
  10M Monte Carlo → senaryo dağılımı
    ↓
[Çıktı: İstihbarat Ürünü]
  Senaryo konisi → Tarco'ya
  Epistemik işaretler → her iddiaya
  Belirsizlik U değeri → raporlanır
  Karar = Tarco
```

### 6D.2 Başarısızlık Modu Tablosu

| Başarısızlık | Sistem Tepkisi |
|-------------|---------------|
| Eksik veri > %40 | `insufficient_data`, dur |
| W_adj < W_min | `human_review` tetikle |
| U ≥ 0.50 | `HUMAN_REVIEW_REQUIRED` |
| Unknown Bütçesi > 0.60 | `UNKNOWN` / `UNCOMPUTABLE` |
| AUROC < 0.85 | Modülü devre dışı bırak |
| Çapraz-kirlilik > 0.01 | Gate karantina, insan incelemesi |

---

