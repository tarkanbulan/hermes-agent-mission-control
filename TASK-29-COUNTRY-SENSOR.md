# 🤖 JULES — GÖREV KARTI (TASK-29-COUNTRY-SENSOR)

**Durum:** 🔄 SIRADA — Picard şartname yazdı, JULES kodlayacak
**Hedef Repo:** `hermes-agent-mission-control`
**Kaynak Motor (hazır, %100 kanıtlanmış):** `E:\T2SAIM_NEXUS_MIRROR\Macroekonomics\hermes_crisis_lab\BTF_AMNESIA\btf_v3_kalibre_tr_dei.py` → TR 8/8 kriz %100 yakalar, yanlış alarm %6.7, lead +9 gün

---

## GÖREV: HAZIR TR MOTORUNU 29 ÜLKEYE ÇOĞALT (kod yazma — uyarla+çalıştır)

### NEDEN
T2SAIM 29 ülke kriz erken uyarı sistemi. TR motoru zaten çalışıyor (%100). Aynı yöntem her ülkeye.

### KAYNAK MOTOR (birebir aynı mantık — değiştirme)
```
Parametreler (LOCKED): SIGMA=1.25 · LAMBDA=0.15 · WINDOW=5 yıl · SRI_ALARM=0.50/0.55
3 kanal:
  SRI_psy = 0.20(1−trust) + 0.20(pol/100) + 0.20·CA + 0.15·EFMI + 0.25·soc
  SRI_fin = 0.30·min(1,M2NIR/15) + 0.25·min(1,CDS/500) + 0.20·min(1,cred/30) + 0.25·min(1,vix)
  SRI_vol = 0.35·min(1,vol·100) + 0.35·min(1,inf/50) + 0.30·min(1,vix)
  SRI_total = 0.35·psy + 0.35·fin + 0.30·vol
  L6 = (psy>0.40 ∧ fin>0.40 ∧ vol>0.45)
  alarm = 2 if (total>0.50 ∧ L6) else 1 if total>0.50
  tevekkül = total·(1+CA)>0.70
  kriz = (alarm≥2 ∨ tevekkül)
  Amnesia: her ay mem×0.85
```

### ÇOĞALTMA
Aynı motoru 29 ülkeye uygula. Her ülke için:
- **Panel verisi:** ülke paketleri `E:\T2SAIM_NEXUS_MIRROR\000_SPARK\T2SAIM _OS\Prediction_Project\crises\Picard_Report\ulke_veri_paketleri\<ÜLKE>\data\FRED\*.csv`
- Haritala: FRED döviz→vol, CPI→enflasyon, faiz, rezerv→M2NIR proxy, CDS→(varsa)
- trust/polarization/CA: güven verisi yoksa ülkeye rasyonel varsayılan (L-023: uydurma yok, ≈ işaretle)
- **Kriz katalogları:** `BELLEK_KATALOGLARI\<ÜLKE>_KRIZ_KATALOGU.md` → `kriz_donem` pencereleri

### ÜLKELER (29)
TR US UK JP DE HK CN RU BR MX SA TW KR CH IN AU IT NL CL CD ID ZA KZ FR SG CA ES QA AE

### ÇIKTI
Her ülke için: BTF-Amnesia zaman serisi (sri_psy/fin/vol, sri_total, alarm, L6, kriz) → kriz yakalama raporu (X/ana kriz). Hedef: her ülke kendi krizlerini ≥%80 yakalasın.

### KISITLAMA
- HAZIR TR motorunun formüllerini DEĞİŞTİRME — sadece panel verisi ülke ülke değişir
- Fiziksel kanıt: çıktı CSV + yakalama raporu + kod
- Kaynaksız sayı ekleme (L-023)

## TESLİM
- 06_DASHBOARD/country_sensors/29 ülke motoru + çalıştırma
- PR açar, Picard doğrular

*Veritas Per Se — Komutan Picard 🖖*
