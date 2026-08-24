# LAYER 3: DOMAIN METODOLOJİLERİ

> **Kaynak:** `Candidate_Corpus/ALT-MODULLER/` — Econ, GeoP, Energy, IntelAIM  
> **Durum:** ⚠️ Assumed — Candidate tier

## 3A: EKONOMİK İSTİHBARAT

> **Kaynak:** `T2SAIM_Econ_Methodology_v1.0.md`

**Temel Odak:**  
Ekonomik koşulların T2SAIM durum vektörüne nasıl girdiği ve istihbarat değeri taşıyan ekonomik sinyallerin nasıl belirleneceği.

**Temel Metrikler:**
- GDP büyüme oranı ve bileşenleri (iç talep, ihracat, yatırım)
- İşsizlik oranı + gizli işsizlik (NEET, part-time)
- Enflasyon bileşenleri (enerji, gıda, çekirdek)
- Gelir eşitsizliği (Gini katsayısı, top-share)
- Kredi spreadi ve finansal koşullar endeksi
- Cari açık ve dış borç yapısı

**İstihbarat Değeri Sinyalleri:**

```
Anomali sinyal seviyeleri:
  GDP sapmasi > 2σ   → Structural break ihtimali yüksek
  İşsizlik hızlanması > 1.5% 6-ayda → Rejim değişimi öncüsü
  Kredi spreadi > 200bps  → Finansal stres başlangıcı
  Gini > 0.42            → Sosyal gerginlik eşiği
```

⛔ **Ethics Flag — 3A:**  
Ekonomik tahminler politika tavsiyesi değildir. Bu metodoloji kırılganlık tespiti içindir; ekonomik müdahale veya piyasa hareketlendirme önerisi üretemez.

---

## 3B: JEOPOLİTİK İSTİHBARAT

> **Kaynak:** `T2SAIM_GeoP_Methodology_v1.0.md`

**Temel Odak:**  
Devlet ve devlet-dışı aktörlerin davranış örüntülerinin sistematik değerlendirmesi.

**Analiz Çerçevesi:**

```
Aktör Değerlendirmesi:
  - Kapasite (capability): askeri, ekonomik, diplomatik, bilgi
  - Niyet (intent): tarihsel örüntü, söylem, koalisyon
  - Kırılganlık (vulnerability): iç baskılar, bağımlılıklar
  - Fırsat penceresi (opportunity): konjonktür, rakip dikkati

Tehdit Eşiği:
  Yüksek = Yüksek Kapasite ∧ Yüksek Niyet ∧ Açık Fırsat Penceresi
```

**CARVER Çerçevesi (INTELOP-034 ile entegre):**

```
C = Criticality (kritiklik)
A = Accessibility (erişilebilirlik)
R = Recuperability (kurtarılabilirlik)
V = Vulnerability (kırılganlık)
E = Effect (etki)
R = Recognizability (tanınabilirlik)

⛔ Yalnızca kendi sistemlerin için savunma değerlendirmesi.
```

---

## 3C: ENERJİ JEOEKONOMİSİ

> **Kaynak:** `T2SAIM_Energy_GeoEcon_KHermes_Addendum_v1.0.md`

**Temel Odak:**  
Enerji arz güvenliği, fiyat oynaklığı ve jeopolitik bağlantıları.

**Temel Değişkenler:**
- Enerji ithalat bağımlılığı oranı
- Çeşitlendirme indeksi (Herfindahl-Hirschman)
- Enerji yoğunluğu (GDP başına enerji tüketimi)
- Enerji fiyatı → enflasyon geçişkenliği (pass-through katsayısı)

**T2SAIM Entegrasyonu:**  
Enerji şokları → G(t) jeopolitik bloğunu tetikler → P_pascal(t) yükselir → γ(t) bölgesel kırılganlık dağılımını deforme eder.

---

## 3D: DÜZENSİZ HARP DEĞERLENDİRMESİ

> **Kaynak:** `08_IntelAIM_Analysis/01_FOUNDATIONS/L5_Operational_Intel/`  
> **Durum:** ⚠️ Assumed

**Kapsam:** Simetrik olmayan tehdit aktörlerinin davranış örüntüleri, propaganda ağları, hibrit tehdit imzaları.

⛔ **Ethics Flag — 3D:**  
Bu metodoloji yalnızca savunma ve erken uyarı amaçlıdır. Saldırı planlaması, hedefleme veya karşı-operasyon tasarımı için kullanılamaz. Her değerlendirme Tarco onayı gerektiren kısıtlı kapsamdadır.

---

