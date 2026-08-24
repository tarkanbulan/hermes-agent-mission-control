# 🚨 EŞSİZ ERKEN KRİZ TESPİT SİSTEMİ — OKF MİMARİSİ (10 korpus bölümü → tek sistem)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar:** Kaptan Tarco
**Kaynak:** Korpus L0-L9 16-geçiş öğrenmesi + 23 ülke kriz sensörü + T2SAIM külliyatı
**Amaç:** "Ekonomi her yerde aynıdır, ismi değişir" — her ülkeye uygulanabilir EŞSİZ erken kriz tespit motoru.

---

## 🧱 MİMARİ — 6 EŞSİZ KATMAN

```
┌──────────────────────────────────────────────────────────────┐
│  EŞSİZ ERKEN KRİZ TESPİT MOTORU (23 ülke)                    │
├──────────────────────────────────────────────────────────────┤
│  K1 VERİ DÜRÜSTLÜĞÜ (L0 veto + L1 kumpas/benford)           │
│  → Sahte veri ele: sızıntı veto, CV kumpas, Benford          │
│  K2 FİNANSAL REZONANS (L9 SRI + L3 eşikler)                 │
│  → 0.35psy + 0.35fin + 0.30vol · kredi>200bp, Gini>0.42     │
│  K3 TOPLUMSAL (L2 PCCI + L9 tevekkül + L4 r_temporal)       │
│  → toplum kriz-eğilimi makro'dan ÖNCE · sebat tamponu       │
│  K4 KRİZ OLASILIĞI (L2 Markov P23 + L5 E[kriz_süresi])     │
│  → "kriz geliyor + kaç gün + ne olasılıkla"                  │
│  K5 KALİBRASYON (L6 ECE/DCA + L1 veriden eşik)              │
│  → güven-hizalı, arıza'da DUR, elek veriden                 │
│  K6 KARAR (L8 Karar=Tarco + L7 Daubert + drift)             │
│  → sistem sinyal, karar Kaptan; drift'te dur                    │
└──────────────────────────────────────────────────────────────┘
```

## 🔑 KATMAN FORMÜLLERİ (EŞSİZ BİRLEŞİM)

### K1 Veri Dürüstlüğü (girdi temizliği)
```
Ontolojik veto:  t_j > t_i ∧ s_i↔s_j nedensel → KE=N/A (BTF koruması)
Kumpas:          CV(Δt)=σ/μ → CV<0.1 ∨ >2.5 = sentetik
Benford:         MAD_B > 0.015 = nonconforming
```
**Eşsiz:** Kriz verisi (kur/enflasyon/hacim) mani̇püle edilmişse yakala — UCI'ye sokma

### K2 Finansal Rezonans (SRI = ülke UCI çekirdeği)
```
SRI_total = 0.35·psy + 0.35·fin + 0.30·vol
SRI_fin   = 0.40·min(1,M2NIR/15) + 0.30·min(1,CDS/500) + 0.30·min(1,credit/30)
SRI_vol   = 0.35·vol + 0.35·min(1,inf/50) + 0.30·min(1,VIX/40)
M2/rezerv>8 ∨ M2/NIR<0 → doğrudan kırmızı (Spark düzeltme)
```

### K3 Toplumsal öncü (makro'dan ÖNCE kriz-eğilimi)
```
PCCI = z(Fear)+z(IdThreat)+z(MotivDef)+z(Indoctr)+z(Ritual)+z(ATY)−z(EpistImm)−z(SGA)
SRI_psy = 0.30(1−trust) + 0.35(polar/100) + 0.35·CA      [TR 2026: 0.52]
tevekkül_kirildi = SRI_total·(1+CA) > 0.70
r_temporal = r_base + α_r[(CT·A_load)/(PFC·(1−C_atrofi)+ε)]^β_r  [zaman çökmesi]
```
**Eşsiz:** Toplum geleceğe inancını kaybediyor mu (r_temporal)? = krizin halka alımlanma öncüsü

### K4 Kriz Olasılığı + Süre (Markov, nicel)
```
P₀₁ = 1/(1+e^(−α[A_load−θ]))            Normal→Stressed
P₁₂ = 1/(1+e^(−α[T_tribal·A_load−θ]))   →Critical (kutuplaşma)
P₂₃ = 1/(1+e^(−α[A_load/KE_adj−θ]))     →FAILURE (KE çökünce)
E[kriz_süresi] = 1/(1−P₃₃)
```
**Eşsiz:** "Kriz geliyor + kaç gün + hangi olasılıkla" — uyarıdan nicel tahmine

### K5 Kalibrasyon (doğru alarmlar)
```
ECE = Σ|B_m|/N·|acc−conf|  → ECE<0.05 Strong, <0.02 Supreme
NB(p_t) = TP/N−(FP/N)(p_t/1−p_t)  → karar eğrisi, eşik net fayda
Eşik veriden (1A): dağılım %95 + güvenlik marjı max+2σ
Drift: AUROC>0.03 dur, FPR>0.02 acil
```
**Eşsiz:** kriz eşiği "at gibi" değil, veriden + güven-hizalı + drift'te dur

### K6 Karar & Rapor (etimik)
```
Karar = Tarco (sistem analiz, karar Kaptan)
Daubert: denetlenebilir + hata oranı + peer review
Arıza: eksik veri>%40 dur, U≥0.50 human_review, AUROC<0.85 devre dışı
Çıktı: CLEAR / WATCH / REVIEW / KRİZ_ALARM
```

## 🎯 EŞSİZ DEĞER (neden kimse yapamaz)
1. **Ekonomi+toplum+istihbarat 3-tek katmanda** — sadece finansal değil
2. **BTF sıfır sızıntı + Amnesia + veto** — gelecek tahmini değil, şimdiki kırılganlık
3. **Markov kriz OLASILIK + SÜRESİ** — "kriz geliyor" değil "şu olasılıkla, kaç gün"
4. **Eşik veriden + ECE kalibre** — uydurma eşik yok (Kaptan L-023)
5. **23 ülke → aynı motor, ülkeye özgü veri/eşik** (ekonomi her yerde aynı)

## 📋 UYGULAMA
- `country_sensor.py` + `t2saim_daily_23_ulke_kopru.py` → bu 6 katman
- L9 SRI → Φ hesaplama · L2 Markow → olasılık · L5 E[kriz] → süre
- L8 → karar = Tarco · Kumpas/Benford → K1 girdi temizliği
- ECE/DCA → kalibrasyon

*Veritas Per Se — Komutan Picard · 10 bölüm öğrenmesi → EŞSİZ sistem*
