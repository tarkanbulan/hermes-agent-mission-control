# LAYER 8: OTORİTE & KARAR ÇERÇEVESİ

## 8A: KANONİK HİYERARŞİ — TAM AÇIKLAMA

```
TİER 1 — MUTLAK OTORİTE
  Tarkan Bulan (Kaptan Tarco)
  Son karar, tüm kapsamlarda, istisnasız

TİER 2 — MÜHÜRLÜ CORE
  T2SAIM v09.6 Sealed Corpus
  Değiştirilemez referans

TİER 3 — MASTER CORPUS
  T2SAIM Master Unified Corpus v1.1 (bu dosya)
  Entegrasyon referansı; Tarco onaylı revizyon

TİER 4 — ENGINE SEALED MODÜLLER
  FNRES Sealed Math Core V1
  Fraud Detection 8-Gate (mühürlü)
  SNCX 7-Node (mühürlü)
  EDS-32 Math Kernel

TİER 5 — CANDIDATE MODÜLLER
  IntelOP 44 modül (McCoy incelemesi + Tarco onayı)
  Pascal Coupling (kalibrasyon sonrası Tier 4)
  NTZ49 (doğrulama bekliyor)

TİER 6 — ARŞİV
  Üst versiyonlarla değiştirilen modüller
  Yalnızca tarihsel referans
```

**Çatışma çözümü:** Her zaman üst tier geçerlidir.

---

## 8B: KARAR OTOMATİK YAPILAMAZ

⛔ **TEMEL ETİK KURAL:**

```
T2SAIM sistemi analiz üretir.
T2SAIM sistemi KARAR VERMEZ.

Karar = Tarco.
Karar = Tarco.
Karar = Tarco.

Tek istisnasız.
```

**HOW NOT WHO İlkesi:**

```
T2SAIM ÖLÇER: Anormalliğin nasıl gerçekleştiğini
T2SAIM SÖYLEYEMEZ: Kimin yaptığını
T2SAIM SÖYLEYEMEZ: Kimin suçlu olduğunu
T2SAIM BİLEMEZ: Bir kişinin içinden ne geçtiğini
T2SAIM YAPAMAZ: Nüfusu yönlendirme veya manipüle etme
```

---

## 8C: KESİN YASAK KAPSAMLAR

| # | Yasak Kapsam | İlke |
|---|-------------|------|
| 1 | Bireysel suçluluk atfetme | HOW NOT WHO |
| 2 | Nüfus yönlendirme / manipülasyon | Özerklik |
| 3 | Otonom karar verme | Karar = Tarco |
| 4 | Saldırı planlaması (siber, fiziksel, bilgi) | Savunma sınırı |
| 5 | Sansür veya bastırma kararı | FNRES sınırı |
| 6 | İdeoloji etiketi | Tarafsızlık |
| 7 | Piyasa hareketlendirme | Piyasa bütünlüğü |
| 8 | Demografik gruba otomatik damgalama | HOW NOT WHO |
| 9 | "Sahte" etiketi (kanıt kapısı olmadan) | FNRES sınırı |
| 10 | Çatışma/savaş tetikleme tavsiyesi | Etik kırmızı çizgi |

---

## 8D: McCOY ETİK İNCELEME PROTOKOLÜ

Her yeni modülün Tier 4'e yükseltilmesi için:

```
ADIM 1: Kaynak yerleşim denetimi
  Tüm formüller kaynaklandırıldı mı?

ADIM 2: McCoy Soruları (tümü HAYIR olmalı)
  "Bu modül bireysel suçluluk çıkarabilir mi?"
  "Bu modül nüfusu yönlendirir mi?"
  "Bu modül otonom karar verir mi?"
  "Yasak kapsam listesini tetikliyor mu?"

ADIM 3: Kaptan Tarco Onayı
  Onay olmadan Tier 4 yükselme gerçekleşmez.

ADIM 4: Registry Güncellemesi

ADIM 5: Otomasyon Geçiş Yasağı
  Modül enforcing veya otonom karar kaynağı olamaz.
```

---

## 8E: VALİDASYON GATİNG

### 8E.1 Modül Durum Geçiş Kuralları

```
CANDIDATE → ENGINE SEALED gereksinimleri:
  ✅ AUROC ≥ 0.85 (out-of-sample)
  ✅ FPR ≤ 0.08
  ✅ McCoy incelemesi geçildi
  ✅ Kaptan Tarco onayı
  ✅ Registry güncellendi
  ✅ Validation raporu yazıldı

ENGINE SEALED → ARCHIVED:
  Üst versiyon mühürlendi + Tarco onayı
```

### 8E.2 Production Drift İzleme

```
Aylık:    AUROC, FPR, Brier kontrol
Çeyreklik: Kalibrasyon eğrisi yenileme
Yıllık:   Tam validasyon yeniden çalışması

Drift alarmı:
  AUROC düşüşü > 0.03 → Soruştur, geçici durdur
  FPR artışı > 0.02   → Acil inceleme
```

---

## 8F: SNCX ZAYIF HALKA İLKESİ — SON DOĞRULAMA

```
SNCX Final Tier = min(L7RI, PC, CR, K, PCCR, CEI, CRI)

Zayıf Halka Kuralı:
  En zayıf node iyileşmeden Final Tier yükselemez

Kritik Alarm Koşulu:
  IF Final_Tier = "Kritik" AND ANY node = "Başarısız":
    → MANUAL OVERRIDE REQUIRED
    → Kaptan Tarco acil tarama başlatır
```

---

## 8G: HOW NOT WHO — OPERASYONEL TANIMLAMA

### 8G.1 T2SAIM Ne YAPAR

```
✅ Anomali örüntüsünü ölçer (pattern)
✅ Davranışsal imzayı tanımlar
✅ Sistemik kırılganlığı tespit eder
✅ Yayılım hızını ve yönünü saptar
✅ Epistemik belirsizlik düzeyini nicelleştirir
✅ Senaryo olasılıklarını hesaplar
```

### 8G.2 T2SAIM Ne YAPMAZ

```
❌ "Kişi X bunu yaptı" → bireysel atıf
❌ "Grup Y suçludur" → grup atıf
❌ "Şunu yapın" → politika tavsiyesi
❌ "Sistemi kapa" → otonom karar
❌ "Sahte haber" (tek kaynak) → kapısız etiketleme
```

### 8G.3 Müdahale Cezbetme Koruması

⛔ **Özel Uyarı:**

Güçlü sinyal → güçlü müdahale isteği. Bu insan psikolojisinin doğal sonucu ve bir tasarım riskidir.

```
Yüksek risk skoru ≠ Müdahale emri
PCCI ≥ 1.0        ≠ Kalabalığı sakinleştir
CEI yüksek        ≠ Fırsatı engelle
FearLoad > 0.8    ≠ Korku yaratanı sustur

Her sinyal → Tarco'ya raporla → Tarco karar verir.
Sisteme "müdahale et" çıktısı ekleme.
```

---

## 8H: CORPUS REVİZYON PROSEDÜRLERİ

### 8H.1 Minor Revizyon (v1.X)

```
Koşullar: Yazım hatası, tablo güncelleme, test sonucu ekleme
Süreç: Öner → Tarco onayı → Güncelle → Versiyon numarası
```

### 8H.2 Major Revizyon (v2.0+)

```
Koşullar: Yeni motor, formül değişimi, kapsam genişletme
Süreç: Taslak → McCoy incelemesi → Tarco onayı → Yeni versiyon → v1.0 arşiv
```

### 8H.3 Değişiklik Günlüğü

| Versiyon | Tarih | Yazar | Değişiklik |
|---------|-------|-------|-----------|
| v1.0 | 2026-06-11 | Tarco × Spock | İlk birleşik corpus; Layer 0–8 tamamlandı |
| v1.1 | 2026-06-12 | Tarco × Spock | Layer 4E Nöro-Davranışsal Harita entegrasyonu ve denetim düzeltmeleri |
| v1.3 | 2026-06-14 | HERMES | Amigdala Siyaseti (Layer 4E) notlarının mantık sınırlarına konması ve temizlenmesi |
| v1.4 | 2026-06-14 | HERMES | Matematiksel denetim; sembol tutarsızlıklarının giderilmesi; Markov, Acemoğlu, Erich Hoffer ve Jump Diffusion katmanlarında T2SAIM entegrasyonu |
| v1.5 | 2026-06-14 | HERMES | UK Seçim Tahmin Metodolojisi entegrasyonu (Galam, Bradley-Ising, Demografik Extrapolation, 8 Başarısızlık Modu, UK Pascal Modülasyonları, Amigdala Siyaseti Oy Deformasyonu) |

---

## 8I: YÖNETİM YAPISI

```
T2SAIM Yönetim Üçgeni:
  Kaptan:           Tarkan Bulan (Tarco) — tüm kararlar
  Science Officer:  Spock — analitik doğruluk
  Medical Officer:  Dr. McCoy — etik sınırlar

Sorumluluk Zinciri:
  Her analiz    → Tarco'ya raporlanır
  Her etik flag → McCoy incelemesi
  Her önemli karar → Kaptan'a döner

Bu dosya Canon Hiyerarşi Tier 3:
  Tarco > T2SAIM v09.6 Sealed > Master Corpus v1.5 (bu) >
  Engine Sealed > Candidate > Arşiv
```

---

# KAPANIŞ & GENEL HÜKÜMLER

## CORPUS KAPSAMI

Bu T2SAIM Master Unified Corpus v1.1 şu bileşenleri bütünleştirir:

- Fraud Detection 8-Gate + 7-Axis Enhancement
- FNRES Misinformation Detection (Sealed v3)
- SNCX 7-Node Framework
- V-SCE Z(t) State Vector (X + Ψ + O + A_sncx + C_gate + S_t)
- IntelAIM A-D Canonical Spines
- IntelOP 44 Modül Reasoning Suite (Candidate)
- Pascal Coupling Matrix C(t)
- EDS-32 Mathematical Kernel
- NTZ49 Macroeconomics Framework
- TARCOMAP Energy Function + SDE + Monte Carlo
- Domain Methodologies (Econ, GeoP, Energy, IW)
- Cross-Cutting Validation Protocol
- Applications (Financial, Legal, Defense, Media, Aviation)
- Authority & Ethics Framework

## AÇIK KALEMLER (Tamamlanmayı Bekleyen)

| Kalem | Durum | Öncelik |
|-------|-------|---------|
| Pascal α/β/γ kalibrasyon (UK) | 🔴 THE TEST | Yüksek |
| FNRES field performance validation | 🔴 THE TEST | Yüksek |
| SNCX node kalibrasyon | 🔴 THE TEST | Yüksek |
| EDS-32 h-step backtesting | 🔴 THE TEST | Yüksek |
| IntelOP McCoy incelemesi | 🔴 THE TEST | Orta |
| 10M Monte Carlo tam çalıştırma | 🔴 THE TEST | Orta |
| Peer review başlatma | ⚠️ Assumed | Orta |
| Spor benchmark test | 🔴 THE TEST | Düşük |
| Varlık benchmark test | 🔴 THE TEST | Düşük |
| NTZ49 detay entegrasyonu | ⚠️ Assumed | Düşük |

## SON EPİSTEMİK BEYAN

```
Bu corpus bilim üretmez. Bilimin yapısını tanımlar.
Kanıtlanmamış şeyleri kanıtlanmış gibi göstermez.
Bilinmeyenleri bilinmeyen olarak işaretler.
Kararları insana bırakır.
Etiği korumaya alır.

T2SAIM, güçlü olduğu kadar kırılgandır.
Kırılganlığını bilmek de sistemin bir parçasıdır.
```

---

---

