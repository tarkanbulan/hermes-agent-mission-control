# LAYER 10: VERİTAS AJAN FİLOSU (Loop_004)

> **Kaynak:** `B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\loop_004\agents\`  
> **Durum:** ⚠️ Candidate — Kurgusal Şema Analizi boru hattı, Tarco onayı ile aktive edilir  
> **Motto:** *Veritas Per Se* — Hakikat kendiliğindendir

## 10A: BORU HATTI GENEL AKIŞ

```
HAM KORPUS (tarih kitabı / haber / sosyal medya akışı)
    ↓
[00_KAPTAN_VERITAS — Orkestratör]
    ├─ Metin         → [01_NARRATIVE_EXTRACTOR]
    ├─ Olay grafı    → [02_MEMETIC_POWER]
    ├─ Sosyal medya  → [03_CIB_MAPPER]
    ├─ Olaylar       → [04_SEQUENCE_DETECTOR]
    ├─ Sekanslar     → [05_RISK_SCORECARD]
    └─ Çıktılar      → [06_TEMPLATE_ARCHIVIST]
    ↓
KURGUSAL ŞEMA RAPORU → Tarco'ya
```

**İş Bölümü:**
| Görev | sPoCK | DATA |
|-------|-------|------|
| Anlatı çıkarımı, memetik/güç yorumu, ZTJ/ASA | ✅ | — |
| Şema doğrulama, sekans madenciliği, KE/risk hesabı | — | ✅ |

## 10B: AJAN KATALOG (21 Ajan)

### Çekirdek Boru Hattı (00-06)

| ID | Ajan | Rol | Giyen |
|----|------|-----|-------|
| 00 | KAPTAN_VERITAS | Orkestratör, epistemik hakem | sPoCK |
| 01 | NARRATIVE_EXTRACTOR | Anlatı → Olay → Mikro-anlatı | sPoCK |
| 02 | MEMETIC_POWER | Güç yapısı, EFMI, ZTJ/ASA | sPoCK |
| 03 | CIB_MAPPER | Koordinasyon ağı (koordineli davranış) | sPoCK + DATA |
| 04 | SEQUENCE_DETECTOR | S1→S2→S3 sekans tespiti | sPoCK + DATA |
| 05 | RISK_SCORECARD | Risk puanı + bant hesabı | DATA + sPoCK |
| 06 | TEMPLATE_ARCHIVIST | Şablon bankası + drift tespiti | DATA |

### Genişletilmiş Operasyonel Ajanlar (07-21)

| ID | Ajan | Rol |
|----|------|-----|
| 07 | OYUN_CIKARICI | Bağımsız güç-oyunu çıkarımı |
| 08 | TARIHSEL_TARAYICI | Tarihsel vaka karşılaştırması |
| 09 | CAPRAZ_ULKE_TARAYICI | Çapraz ülke örüntüsü analizi |
| 10 | GUNLUK_PSYOP_MONITORU | Günlük psikolojik operasyon izleme |
| 11 | EKONOMIK_MIKRO_SOK | Mikro ekonomik şok tespiti |
| 12 | ATAMA_TAKIP | Kurumsal atama örüntüsü izleme |
| 13 | MEDYA_ONCU_TARAMA | Medya öncü gösterge taraması |
| 14 | LEAD_LAG | Öncü-gecikmeli gösterge analizi |
| 15 | JEOPOLITIK_KIRILMA | Jeopolitik kırılma tespiti |
| 16 | ASKERI_GERGINLIK | Askeri gerilim izleme |
| 17 | ENERJI_JEOPOLITIGI | Enerji jeopolitiği analizi |
| 18 | YOUTUBE_TRANSCRIPT | YouTube transkript analizi |
| 19 | STEALTH_SCRAPER | Gizli veri toplama (etik sınırlar içinde) |
| 20 | BORSA_VERI_TOPLAYICI | Borsa verisi toplama |
| 21 | VERI_KOORDINATORU | Veri koordinasyonu ve kalite kontrolü |

## 10C: SEKANS MODELİ (S1-S2-S3)

**Temel Tanım:**
```
S1 — Sembolik Tetik:
  espri, demeç, tweet, kitap, afiş, mahkeme kararı

S2 — Kurumsal/Kitlesel Refleks:
  savcılık, RTÜK, denetim, linç kampanyası, manşet, koordineli hashtag

S3 — Zarar Üretici Sonuç:
  silahlı saldırı, boykot, kundaklama, itibar/piyasa çöküşü
```

**Tamamlanma Kuralı:**
```
completed = true IF:
  1. Aynı hedefe bağlı S1 var
  2. ≤ 7 gün içinde S1'e atfen S2
  3. ≤ 14 gün içinde aynı hedefe S3
```

**Risk Formülü:**
```
R = 0.20×signal + 0.25×coordination + 0.20×legal + 0.15×prior + 0.20×weak

Bantlar:
  R ≥ 0.75 → Kırmızı
  R ≥ 0.50 → Turuncu
  R ≥ 0.25 → Sarı
  R < 0.25 → Yeşil
```

## 10D: ŞABLON BANKASI (Template Bank)

| ID | Şablon Adı | Makine Tipi |
|----|-----------|------------|
| T-01 | Dış Güç + Yerel İşbirlikçi | Vekalet/Komprador |
| T-02 | Söylem-Gerçeklik Makası (EFMI) | Legitimasyon/Erozyon |
| T-03 | Anti-Komünizm → Din Araçsallaştırması | Ortak Düşman/Kutsal Kalkan |
| T-04 | Aşağıdan Kurum Ele Geçirme | Gülen Vakası türetildi |
| T-S | Sinyal → Saldırı (S1-S2-S3) | Sinyal/Saldırı zinciri |

**Drift Tespiti:** Hiçbir bankaya uymayan yeni örüntü `aday` statüsünde kaydedilir.
3 bağımsız vakada tekrarlanırsa → `onayli` → bankaya T-0X olarak eklenir.

## 10E: CIB AĞLIĞI (Koordineli İnorganik Davranış)

```
cib_likelihood = 0.30×sync_score + 0.30×network_density + 0.25×language_fingerprint + 0.15×cross_platform

Güvenilir sinyal koşulları:
  - En az 2 zaman penceresinde test edilmiş (5dk / 30dk / 6sa / 24sa)
  - Organik viral olasılığı (baz oran) elenmiş
  - Tek platform değil, çok bağımsız kaynak
```

## 10F: EPIST EMİK DİSİPLİN (Veritas Kuralları)

```
Ajan 00-07 arası tüm ajanlar için zorunlu:
  1. "Kim yaptı?" sorusunu sorma → "Hangi sekans/şablon?" sorusunu sor
  2. İsimli suç isnadı yok → Rol-graf ve yapısal oyun var
  3. VERIFIED / ASSUMED / UNVERIFIED her iddiaya
  4. Taraf yok → Makas/ölçüm var
  5. Veri kısıtı açıkça yaz → Uydurma YOKTUR
  6. İnsan karar yetkisi korunur → Kaptan Tarco karar verir
```

⛔ **Ethics Flag — 10:**  
CIB_MAPPER ve STEALTH_SCRAPER yalnızca savunma ve erken uyarı amaçlıdır. Koordineli manipülasyon tespiti için tasarlanmıştır, koordineli manipülasyon üretimi için değil. Her aktivasyon Kaptan onayı gerektirir.

---

