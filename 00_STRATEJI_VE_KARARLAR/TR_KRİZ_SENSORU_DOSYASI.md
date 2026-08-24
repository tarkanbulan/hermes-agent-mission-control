# 🇹🇷 TÜRKİYE (TR) — KRİZ SENSÖRÜ DOSYASI (Spark'a verilecek TEK dosya)

**Amaç:** Türkiye finansal/ekonomik kriz erken uyarı sistemi. Formüller + veri envanteri + tarihsel endeksler + BTF-Amnezi.
**Karar:** Kaptan Tarco · **Hazırlayan:** Komutan Picard · **Tarih:** 24 Ağustos 2026

---

## 1. TÜRKİYE'YE ÖZGÜ FORMÜLLER

**5-boyutlu faz geçişi (TR):**
```
Φ_Macro = 0.35·M2_NIR + 0.30·DOLGAP + 0.20·REER_sarkaç + 0.15·Cari_Açık
Φ_Bank  = 0.35·LDR + 0.30·NPL + 0.20·Gecelik_Makas + 0.15·Döviz_Kaçış
Φ_Neuro = A_load(CDS, vol, haber) · PFC · Kalman K_eff · v_run
Φ_Gullini = G_def(0.782) · Minsky t* · TrustDeficit_TCMB
Φ_Acemoglu = Sömürücü IDIS(0.741) · DarKoridor · TCMB bağımsızlık erozyonu(LM-1)

UCI_TR(t) = 1 − exp(−1.45·[w1·Φ_Macro + w2·Φ_Bank + w3·Φ_Neuro + w4·Φ_Gullini + w5·Φ_Acemoglu])
w = [0.25, 0.20, 0.20, 0.20, 0.15]
Amnesia: M_t = S_t + 0.85·M_{t−1}  (λ=0.15)
Eşik: μ_12ay(TR_UCI) + 1.0·σ  (ülkeye özgü — TR başkadır, ABD değil)
```

**TR'e özgü kritik eşikler:**
- M2/NIR > 15 → kur patlama alarmı
- DOLGAP (Kapalıçarşı−Resmi)/Resmi → ikili kur makası
- G_def = 0.782 (%78.2 merkez bankası inançsızlık)
- IDIS = %74.1 sömürücü kurum dengesi
- REER sarkaç, v_run mevduat kaçışı, tevekkül tamponu

## 2. VERİ ENVANTERİ (TR — 10 FRED + EVDS gerekli)

```
data/FRED/ (10 CSV):
  IR3TIB01TRM156N  (3A faiz)      IRSTCI01TRM156N  (kısa faiz)
  SPASTT01TRM661N  (borsa)        TRESEGTRM052N    (rezerv)
  TURCPIALLMINMEI  (TÜFE endeks)  TURGDPRQPSMEI    (GSYH)
  TURPPDMMINMEI    (PPI)          TURPROMANMISMEI  (sanayi)
  TURB6BLTT02STSAQ (cari)         TURB6CRSE03STSAQ (cari)
M2/NIR, DOLGAP, Kapalıçarşı, CDS, KKM → EVDS (TCMB) gerekli (FRED'te yok)
```

## 3. TARİHSEL KRİZ ENDEKSLERİ (FRED doğrulamalı)

| Kriz | Dönem | Enflasyon zirve | Kur/Deval | GSYH | Öncü sensör |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Döviz+Petrol | 1977-78 | %120.1 (1980-03) | 15→47 | −%1.5 | Φ_Acemoglu |
| 5 Nisan | 1994 | %125.9 (1995-01) | ~%170 | −%5.5 | Φ_Bank |
| Bulaşma+Deprem | 1999 | %68.8 | — | −%3.4 | Φ_Bank |
| Kara Çarşamba | 2001 | %68.5 | TL −%38 | **−%5.7** | Φ_Gullini t* |
| Küresel | 2008-09 | %10.1 | 1.60 | −%4.8 | Φ_Neuro VIX |
| Kur Krizi | 2018 | %25.2 | 4.8→7.2 | −%2.4 | Φ_Neuro+Gullini+Acemoğlu |
| COVID | 2020 | %14.6 | 7.4 | +%1.8 | M2/NIR |
| Kur/Enflasyon | 2021-22 | **%85.5 (2022-10)** | TL −%40 | +%5.5 | tevekkül tamponu |

## 4. BTF-AMNEZİ (TR — sıfır gelecek sızıntısı)
- Her gün: t-1'e kadar bil, t için UCI üret, t+1'de gerçek gelince hata hesapla
- λ=0.15, 4.62 yıl yarı ömür; eski kriz sahte alarm üretmez
- 8 ana kriz etiketi kalibrasyon penceresi (crisis_label=1)
- Enflasyon referans: TURCPIALLMINMEI

---

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
