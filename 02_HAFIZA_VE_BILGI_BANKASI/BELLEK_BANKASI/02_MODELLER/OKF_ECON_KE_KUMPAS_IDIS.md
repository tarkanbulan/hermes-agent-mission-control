# 📚 OKF — T2SAIM EKONOMİ METODOLOJİSİ + KE/KUMPAS/IDIS (ÖZ)

**Konum:** Mission Control OKF Bilgi Bankası · **Hazırlayan:** Komutan Picard · **Tarih:** 24 Ağustos 2026
**Kaynaklar:** `T2SAIM_Econ_Methodology_v1.0.md` (1104 satır) · `T2SAIM_MASTER_UNIFIED_CORPUS_v2.0` (KE/Kumpas) · `Daron v2.1` (IDIS)

---

## 1. EKONOMİ METODOLOJİSİ (12 katman, 44 modül, 34 kaynak)

**Epistemik yöntemler:** Dedüksiyon(Smith) / Endüksiyon(Keynes) / Abduksiyon(Hayek)
**Keywords:** Lucas Critique · 8-durum epistemik (V/P/PL/A/C/U/UN/UC) · 10-gate filtre (EG-00..09)
**Hijyen:** Correlation≠Causation · Model uncertainty · Aggregation fallacy · Goodhart's Law

| Katman | Öz | Kritik formül |
| :--- | :--- | :--- |
| 2 Analitik | Arz-talebin dengesi, 5 piyasa başarısızlığı | Esneklik, Pigou/Coase |
| 3 Pipeline | 10-gate ekonomik filtre | EG-00..09 |
| 4 Makro | GDP, enflasyon, işsizlik, faiz, mali | Taylor Kuralı, Okun, r vs g |
| 5 Finans | EMH, davranışsal, **Minsky** | **FFI=0.40Ponzi+0.30Lev+0.20Mat+0.10Balb>0.60** |
| 6 Ticaret | Karşılaştır, ticaret savaşı, GVC | ToT, Nash tarife oyunu |
| 7 Kalkınma | Solow, kurumsal | P(kurumsal değişim) |
| 8 Ekonofizik | Power-law, Levy, fat tail | P(X>x)=C·x⁻ᵅ |
| 9 Oyun | Nash, açık artırma, bilgi asimetrisi | Vickrey |
| 10 Davranış | Prospect, nudge | v(x), λ=2.25 |
| 11 Tahmin | State-space, BSTS, nowcast | Kalman |
| 12 Red Team | Black Swan, stress test, antifragility | AFI, EG-09 |

## 2. KE (Karar Kalitesi Endeksi) — SENTETİKLİK

```
KE = 0.40·ZTJ + 0.30·IUY + 0.30·SST
KE_final = max(KE_fuzzy, KE_dynamic)
IDIS = 100/(1+KE_final)   [100=sağlık, 46.5=çöküş]
```

**ZTJ = Zaman-Topolojik Jüri (L1), 7 testi içerir; 1.si KUMPAS:**

## 3. KUMPAS ENDEKSİ (ZTJ-1 Caliper Testi = SENTETİKLİK ORANI)

```
Δtᵢ = tᵢ₊₁ − tᵢ        (olaylar arası zaman)
CV(Δt) = σ(Δt)/μ(Δt)   (değişim katsayısı, n≥30)
S = 1.0  eğer CV<0.1 ∨ CV>2.5   (metronomik/yığın = sentetik)
   min(1, |CV−1.0|/0.5)          (doğal: CV≈1.0±0.3)
```

**Anlam:** Doğal süreçlerde olaylar arası süre varyanslıdır (CV≈1). Aşırı düzenli (CV<0.1) = bot/metronomik; aşırı yığınlı (CV>2.5) = yapay. **Sentetiklik/kumpas oranı.**

**Diğer ZTJ testleri:** ZTJ-2 Survival/Weibull · ZTJ-3 Stylchronometry · ZTJ-4 MF-DFA · ZTJ-5 SDLE · ZTJ-6 Bai-Perron · ZTJ-7 RQA

**SST = L2 Ağ (M-serisi emir + G-serisi)** · **IUY = L3 dil**

## 4. IDIS — İKİ FARKLI (korpus kritik notu)

⚠️ **Korpus satır 6557:** "Layer 18A IDIS (makro şok çarpanı) ≠ kurumsal IDIS (100/(1+KE))" — aynı ad, farklı formül. Kodda karıştırılmamalı.

## 5. MINSKY FFI (kriz sistemiyle doğrudan)
FFI>0.60 = sistemik risk · rejimler: Hedge/Speculative/Ponzi → t* tekilliği

---

### DOĞRULUK TABLOSU
| Bileşen | Kanıt | Model | Not |
| :--- | :--- | :--- | :--- |
| Econ 12 katman | G (1104 satır okundu) | V | 44 modül |
| KE/ZTJ/IUY/SST | G (korpus okundu) | V | Kumpas=ZTJ-1 |
| IDIS 100/(1+KE) | G (Daron v2.1) | V | 18A'dan ayrı |
| FFI>0.60 | G (Econ L5) | V | 2008 öncesi |

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
