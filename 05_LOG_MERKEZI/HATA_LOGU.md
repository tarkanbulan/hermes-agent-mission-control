# 🪵 HATA LOGU — T2SAIM KRİZ MOTORU VERİ BÜTÜNLÜĞÜ (L-024)

**Tarih:** 24 Ağustos 2026 · **Ajan:** Picard · **Belirti:** doğrulama hatası

## HATA: TR USD/TRY serisi güncel DEĞİL (FRED DEXTHUS 1981'de durmuş)

**Belirti:** `t2saim_daily_23_ulke_kopru.py` TR için fx=20.66 üretti (1981 kuru), güncel kur ~33 beklentisi yerine.

**Kök neden:** FRED `DEXTHUS` (USD/TRY) serisi **1981'de sonlanmış** — FRED bu seriyi güncellemiyor. Hem `TR/data/FRED/DEXTHUS.csv` hem merkez `FRED_DATA/DEXTHUS.csv` 1981 kuru ile bitiyor. Türkiye döviz kurunun güncel değeri için **farklı kaynak** gerekli (TCMB EVDS, api_canli.py, veya TradingEconomics).

**Etki:** 23 ülke köprü motoru TR için yanlış (eski) kur kullanıyor → A_load/fx kaynaklı formüller bozulur → Φ skor yanıltıcı olabilir.

**Çözüm (önerilen):**
- TR için güncel FX kaynağı: `fetch_latest_usdtry.py` (Hariseldon'da var) veya TCMB EVDS
- 23 ülke için **her serinin güncellik kontrolü** — son tarih > 1 yıl öncesineyse "ESKİ SERİ" işaretle

## GENEL: 23 ÜLKE VERİ BÜTÜNLÜĞÜ

| Ülke | FX serisi | Güncel mi? | Not |
| :--- | :--- | :---: | :--- |
| TR | DEXTHUS | ❌ 1981 | TCMB/EVDS gerekli |
| US | DTWEXBGS | ✅ | dolar endeksi güncel |
| UK | DEXUSUK | ✅ | |
| JP | DEXJPUS | ✅ | 159.2 doğrulandı |
| DE | DEXUSEU | ✅ | |
| HK | DEXHKUS | ✅ | |
| CN | DEXCHUS | ✅ | |
| BR | DEXBZUS | ✅ | 5.24 doğrulandı |
| CL | CCUSMA02CLM618N | ✅ | 931 doğrulandı |
| KZ | PURANUSDM | ✅ | uranyum |
| RU | DCOILWTICO | ✅ | petrol proxy |
| CD | (boş) | ❌ | FRED'te kobalt yok — Cobalt Institute |

**Durum:** 🔄 Kısmi — TR ve CD için güncel kaynak bekleniyor; diğerleri köprüde çalışıyor.

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
