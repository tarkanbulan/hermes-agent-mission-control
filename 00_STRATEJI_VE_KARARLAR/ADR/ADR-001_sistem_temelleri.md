# ADR-001: SİSTEM TEMELLERİ (Mission Control + Log + Rüya)

- **Tarih:** 2026-08-24
- **Durum:** Kabul Edildi
- **Verici:** Kaptan

## 1. Bağlam
Sistem büyük ve dağınık; context kaybı yaşanıyor (state.db 2.5GB), hata bulmak zor, boştaki ajanlar bekleşiyor.

## 2. Seçenekler
1. Dağınık klasörlere devam (context kaybı + hatalar izlenemez)
2. **Mission Control + Log sistemi + Rüya Protokolü (SSOT)**

## 3. Karar
Tek komuta merkezi kurulur: görev merkezi + hafıza + log (her şeyi izle) + rüya (boşta üretim).

## 4. Sonuç/Risk
Context kaybı azalır, hatalar izlenebilir, boştaki ajanlar üretir. Risk: disiplin gerektirir (ajanlar log yazmalı).
