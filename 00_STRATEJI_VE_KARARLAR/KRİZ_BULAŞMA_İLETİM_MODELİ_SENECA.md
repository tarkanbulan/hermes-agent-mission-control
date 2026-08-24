# 🦠 KRİZ BULAŞMA / İLETİM MODELİ — SENECA SIR BULGUSU ENTEGRASYONU

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar:** Kaptan Tarco
**Amaç:** Seneca'nın bulaşıcı-hastalık vs ekonomik kriz simülasyonu (20 ülke, ~10 bin veri, katsayı 0.99) → 23 ülke kriz contagion modeline entegrasyon.

---

## 1. SENECA BULGUSU (doğrulandı)

SIR-tipi yayılım modeli (aynı 20-ülke ağında):
- **Hastalık:** β=0.35, γ=0.12
- **Kriz:** β=0.60, γ=0.05 (panik hızlı, stabilizasyon yavaş)
- **Sonuç:** İvme korelasyonu **r=+0.999 (≈0.99)**, hız +1.000, MSE 0.0018

**Dürüst yorum:** Bu, **mekanizma benzetmesi** (model kendi SIR varsayımının benzerliğini üretir). Kriz yayılımı hastalıkla **aynı ivme fiziğini** (hızlı hızlanma → pik → üstel yavaşlama) paylaşıyor — hipotezi destekler, kanıtlamaz. Gerçek veri gerekir.

## 2. 23 ÜLKE KRİZ BULAŞMA MİMARİSİ (Kaptan vizyonu)

```
┌────────────────────────────────────────────────────────────┐
│ KRİZ = SALGIN (epidemiyolojik contagion)                  │
├────────────────────────────────────────────────────────────┤
│ S(t)  = duyarlı ülkeler (henüz krize girmemiş)            │
│ I(t)  = krizdeki ülkeler (UCI yüksek / amigdala panik)    │
│ R(t)  = stabilizasyon / kriz sonrası                      │
├────────────────────────────────────────────────────────────┤
│ BULAŞMA: ülke i krize girince → komşu ülke j'ye iletim     │
│  dI_j/dt = β_ij · I_i · S_j  (hastalık gibi)              │
│  β_ij = ticaret bağlantısı + finansal bağ + coğrafya       │
│  γ_j  = ülkenin stabilizasyon hızı (rezerv, politika)      │
└────────────────────────────────────────────────────────────┘
```

### Ülke-ülke iletim matrisi (β_ij) — Kaptan örnekleri
| Kaynak | İletim kanalı | Alıcı | Gecikme |
| :--- | :--- | :--- | :--- |
| Şili | bakır rezerv → Çin erişimi | Çin/elektronik | günler-hafta |
| Brezilya | devalüasyon | ABD/EM | ~4 gün |
| Nadir element | GPU/askeri sektör | dijital/askeri | hızlı |
| Hürmüz | enerji boğaz | küresel | günler |

### SKALA (gradient/derecelendirme)
```
Kriz iletim şiddeti skala (0-1):
  0.00-0.20  yerel (tek ülke, minimal iletim)
  0.20-0.45  bölgesel (komşu bulaşma başladı)
  0.45-0.70  küresel eşik (çok ülke eş zamanlı)
  0.70-1.00  SİSTEMİK (dünya krizi) 
```

## 3. DÜNYA KRİZİ ÖLÇÜMÜ (eklektik — tüm veri birleşimi)

```
Omega_Küresel(t) = Σ_i W_ülke_i · UCI_i(t) · Iletim_Potansiyeli_i(t)

W: US 0.20 · CN 0.15 · DE 0.10 · UK 0.08 · JP 0.08 · RU 0.05 ...
Iletim_Potansiyeli: ülkenin dışa bulaştırma hızı (hub ise yüksek)

Omega > 0.70 → DÜNYA EKONOMİK KRİZİ YAKIN
Eş zamanlı çok ülke UCI yüksekse = küresel kriz
```

## 4. ENTEGRASYON PLANI (23 ülke → simülasyon)

1. **Her ülke ~50 formül** (K1-K6 + CRISIS_HAZARD + NTZ-49) → yerel UCI
2. **İletim matrisi β_ij** — ticaret/finansal/coğrafi iletim katsayıları
3. **SIR koşusu:** 23 ülkeyi hastalık gibi yay — hangi ülke başlarsa ne olur
4. **Skala + gecikme:** β_ij → gün cinsinden iletim süresi (BR→US 4 gün)
5. **Omega_Küresel:** tüm verinin eklektik birleşimi → dünya krizi olasılığı
6. **Amigdala hızı:** korku endeksi virüs gibi hızlı yayılır (Covid/İspanyol gribi)

## 5. KRİTİK (Seneca bulgusunun sistemle bağı)
- **Hastalık modeli = kriz bulaşma modeli** (aynı ivme fiziği) → contagion katmanı sağlam
- **Ancak gerçek veri gerekiyor** (COVID yayılım + GFC ülke CDS zaman serisi) — iddiadan kanıta
- **23 ülke simultane koşmak:** her ülke ~50 formül → hepsi günlük → Omega_Küresel

## 6. ÖNCELİKLİ EKLEME (Kaptan'ın "1-2 ülke daha" fikri)
Nadir element ülkeleri (nadir toprak: Çin başta; GPU: TW) → dijital/askeri zincir. Şili örneğiyle bakır (Codelco) → Çin rezerv → elektronik. Bu, emtia tekelleri katmanına zaman-iletim skala ekler.

---

*Veritas Per Se — Komutan Picard · 24 Ağustos 2026 · Seneca bulgusu → 23 ülke contagion entegrasyonu*
