# LAYER 5: TARCOMAP — DURUM UZAYI & SİMÜLASYON

> **Kaynak:** `05_TARCOMAP_SNCX/03_TARCOMAP_DURUM_UZAYI_v2.md`  
> **Durum:** ⚠️ Assumed — Yapı doğrulandı; 10M MC simülasyon entegrasyonu bekliyor

## 5A: ENERJİ FONKSİYONU (Psikokültürel Terimli)

### 5A.1 Genişletilmiş Ising Enerji Modeli

$$E_{\text{total}}(k,t) = -\sum_i h_i s_i(k) - \frac{1}{2}\sum_{i \neq j} \tilde{J}_{ij} s_i(k) s_j(k) - \eta_\Psi \cdot \Psi(t) \cdot S_{\text{prob}}(k,t) - \eta_P \cdot P_{\text{pascal}}(t) \cdot \text{Exposure}(k,t)$$

| Terim | Fiziksel Anlam |
|-------|---------------|
| $-\sum h_i s_i$ | Aktörün KY alanına uyumu |
| $-\frac{1}{2}\sum \tilde{J}_{ij} s_i s_j$ | İttifak/çatışma uyumu |
| $-\eta_\Psi \cdot \Psi \cdot S_{\text{prob}}$ | Psikokültürel deformasyon terimi |
| $-\eta_P \cdot P_{\text{pascal}} \cdot \text{Exposure}$ | Pascal basınç terimi |

**Psikokültürel Terim:**
```
η_Ψ = 0.15 (başlangıç değeri, öğrenilebilir)
Ψ(t) = [PCCI(t), SMAI(t)]   (üst skorlar)
S_prob(k,t) = CoA k'nin toplum tarafından kabul olasılığı
```

### 5A.2 Enerji Manzarası Deformasyonu

```
PCCR yüksek → Otoriter CoA'lar daha düşük enerji
                (toplum boyun eğmeye hazır)
CRI düşük   → İşbirlikçi CoA'lar daha yüksek enerji
                (güven erozyonu iş birliğini engeller)
CEI yüksek  → Radikal CoA'lar daha düşük enerji
                (kriz penceresi açık, normal engeller kaldırılmış)
```

### 5A.3 CoA Olasılıkları

$$P_{KY}(k) \propto P_{\text{rat}}(k) \cdot \exp(-\lambda E_{\text{total}}(k))$$

- $P_{\text{rat}}(k)$: Rasyonel fayda temelli olasılık (LAMP çıktısı)
- $\lambda$: Enerji ağırlık katsayısı (sıcaklık parametresi)

### 5A.4 Aktör KY Alanları (Ψ Modülasyonlu)

```
h_i(t) = α_H · h_i^(H) + α_C · h_i^(C) + α_B · h_i^(B) + β_Ψ · Ψ_i(t)

Ψ_i(t): Aktörün temsil ettiği grubun zihin iklimi endeksi
Örnek:  Reform UK → FearLoad + EnemyImage + GMI
        Labour    → MSI + ReciprocityClimate + Trust
```

### 5A.5 Etkileşim Matrisi (Kutuplaşma Terimi)

$$\tilde{J}_{ij}(t) = \beta \cdot J_{ij} \cdot (1 + \gamma_J \cdot |\Psi_i - \Psi_j|), \quad \gamma_J = 0.10$$

$|\Psi_i - \Psi_j|$ büyükse → kutuplaşma → etkileşim güçlenir.

---

## 5B: STOKASTİK DİFERANSİYEL DENKLEM (SDE)

### 5B.1 Birleşik Sistem Denklemi

```
dZ(t)/dt = F(Z(t), θ) + Σ(Z(t)) · ξ(t)

dX/dt  = f_X(X, Ψ, O, P_pascal, ΔF, ΔAlign, θ_X) + Σ_X · ξ_X
dΨ/dt  = f_Ψ(Ψ, X, O, P_pascal, θ_Ψ)              + Σ_Ψ · ξ_Ψ
dO/dt  = f_O(O, G, θ_O)                            + Σ_O · ξ_O
dΛ/dt  = f_Λ(Λ, α, β, γ, X, Ψ, O, θ_Λ)           + Σ_Λ · ξ_Λ
```

**dΨ/dt bileşenleri:**
```
dΨ_base/dt     = f_Ψ_base(Ψ_base, X, O, N)
dΨ_cognitive/dt = f_Ψ_cognitive(Ψ_cog, Ψ_base, R, L)
dΨ_group/dt    = f_Ψ_group(Ψ_group, Ψ_base, R, O, N)
dΨ_moral/dt    = f_Ψ_moral(Ψ_moral, Ψ_base, I, S)
```

---

## 5C: 10M MONTE CARLO ÇERÇEVE

### 5C.1 Parametre Pertürbasyon Seti

```
phase_prevalence       = {rare, moderate}
network_heterogeneity  = {low, medium, high}
baseline_drift         = {0.00, 0.05, 0.10}
label_noise            = {0.00, 0.05, 0.10}
contrarian_fraction    = {0.00, 0.10, 0.25}
η_Ψ_perturbation       = ±0.05  (psikokültürel ağırlık)
N_runs ≥ 1,000,000
```

### 5C.2 Çıktı Dağılımı

Her simülasyon çalışmasında:
1. Enerji minimumları dağılımı → en olası CoA seti
2. Markov geçiş hızları → kriz olasılığı
3. Senaryo grupları (cluster) → K-means ile tipik yörüngeler
4. Robustluk testi → η_Ψ pertürbasyonuna duyarlılık

### 5C.3 Alternatif Gelecek Konileri (Cone of Plausibility)

```
Ufuk                    Senaryo Tipi
────────────────────────────────────────
0–2 yıl (taktik)        4 senaryo: +2σ / +1σ / -1σ / -2σ
2–5 yıl (operasyonel)   3 senaryo: iyimser / baz / kötümser
5+ yıl (stratejik)      2 senaryo: tutarlı yollar / dönüşüm noktaları
```

---

## 5D: MARKOV REJİM GEÇİŞLERİ

### 5D.1 Rejim Uzayı

```
S_t ∈ {0: Normal, 1: Stressed, 2: Critical, 3: Failure, 4: Recovery}
```

### 5D.2 Geçiş Sayım Matrisi

```
N = [[N_00, N_01, N_02, N_03, N_04],
     [N_10, N_11, N_12, N_13, N_14],
     ...
     [N_40, N_41, N_42, N_43, N_44]]

P_ij = N_ij / Σ_j N_ij   (satır toplamı = 1)
```

### 5D.3 Yutucı Durum Kontrolü

```
IF P_33 ≈ 1.0 → Failure yutucudur → Kurtarılamaz kriz
IF P_44 > 0.8 → Toparlanma kararlıdır
IF P_22 > 0.6 → Kritik durumda kalma riski yüksek
```

### 5D.4 Beklenen Kriz Süresi

$$E[\text{kriz\_süresi}] = \frac{1}{1 - P_{33}}$$

$$E[\text{toparlanma\_süresi}] = \frac{1}{1 - P_{44}}$$

### 5D.5 ASA_Markov

$$\text{ASA\_Markov} = P_{\text{gözlenen}} - P_{\text{beklenen}} \mid S_t, X_t, \Psi_t$$

Beklenen geçiş matrisinden anlamlı sapma → yapısal kırılma sinyali.

---

---

