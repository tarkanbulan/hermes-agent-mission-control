# 🧮 MODELLER — Kalibre Edilmiş Parametreler

> Kaynak: Hermes MEMORY.md (2026-08-24). T2SAIM model eşikleri.

## Amigdala / Nöro
- **κ_p = 2.00** İNSAN KALİBRE (Kaptan onaylı) — **5.0464 = ESKİ**.
- **θ_panic BÖLGESEL + DİNAMİK**: TR 0.50, Global 0.65, ABD 0.70 (mühürlü). Ülke bazlı 0.40-0.70.
- Dinamik: θ(t) = θ0 + α·Z(σ).
- **ECE ≤ 0.0124** hedefi.
- PFC lojistik: κ_p·(A_load − θ_panic)

## Kripto
- Model3 → **+%297.76 GERÇEK**. θ_kripto = 0.90.
- VERİ: 16_COIN pivot SAHTE → gerçek: `Kaptan_Tarco/Private/coins_csv`.

## ECE gerçek değerler (eski)
- ETH 0.0113 / BTC 0.0098 — T1 (0.07-0.23) kalibre DEĞİL.

## Finansal
- Merton λ = 4.21 doğru (PyMC 4.55 çapraz). μ/σ ×252 / ×√252.
- Reel kâr: volatilite-etiketli amigdala SAHTE; GERÇEK = psikososyal panel.
