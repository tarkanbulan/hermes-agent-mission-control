# 🚨 T2SAIM 29 ÜLKE — KONTROL + KALİBRASYON + GÖZLEM (Spark/Antigravity orkestrasyonu)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar:** Kaptan Tarco
**Kaynak:** Spark (kalibrasyon + veri kontrol + gözlem mimarisi) + Antigravity (kod yazdırma)

---

## 1. VERİ BÜTÜNSEL KONTROL (Spark yöntemi → Antigravity yazdırdı)
```
1) Bütünlük: 29 ülke FX/CPI/faiz/rezerv VAR/YOK tablo
2) Tarih kapsamı: FRED start vs kriz yılları → test edilemezler
3) Aykırı: Dondurulmuş (Roll_Std12=0) · Atlama (Z>4) · Süreksiz (30g+/7g+)
4) Çapraz kur: TRY/EUR≈TRY/USD×USD/EUR, fark>%0.5 → FX ölçek hatası
5) Test edilebilir kriz: Σ I[FRED_start ≤ kriz]
Çıktı: outputs/VERI_KONTROL_29.md
```

## 2. ÜLKEYE ÖZGÜ KALİBRASYON (Spark → Antigravity uygulayacak)
```
σ_c = σ_base(1+α·RegimeVar_c)·(R_ref/R_c)   (US ~1.45, TR 1.25)
3 tipoloji W_c:
  Finans hub (US/UK/JP/CH): [0.25, 0.50, 0.25]
  Emtia/maden (SA/AU/BR):   [0.20, 0.30, 0.50]
  Fragile/sosyo (TR/ZA):    [0.40, 0.35, 0.25]
Amnesia λ + tevekkül ülkeye göre · sum W_c = 1
Her ülke tek tek koş → X/ana kriz
```

## 3. GÖZLEM KATMANI (Spark mimarisi)
```
UCI_i (0-100) · bulaşma M_ij × UCI → SpillIn_j · Ω_Küresel = Σ α_i·UCI_i×(1+γ·GraphDensity)
Günlük: UCI<45🟢 45-65🟡 65-80🟠 >80🔴 · UCI>80+M>0.60 → T-τ erken uyarı
29 düğüm: 23 ülke + 6 Hariseldon panel (TARCO/Struct.Decay/Acemoğlu/Gullini/Index/Bellek)
```

## 4. AJAN ZİNCİRİ (kod yazdırma — ben değil agent'lar)
| Aşama | Ajan | Görev |
| :--- | :--- | :--- |
| Veri + kalibrasyon tasarımı | Spark | σ_c, W_c, kontrol yöntemi |
| Her ülkeyi tek tek koş + kodla | Antigravity | 29 motor + kalibrasyon + veri kontrol |
| PR/rutin | Jules | modüller + dokümantasyon |

*Veritas Per Se — Komutan Picard 🖖*
