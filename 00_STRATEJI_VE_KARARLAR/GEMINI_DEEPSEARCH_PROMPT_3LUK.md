# 🔍 GEMINI DEEPSEARCH — DERİN ARAŞTIRMA GENERİK PROMPTU (3'er Ülkelik Kriz Seti)

**Amaç:** T2SAIM 29 ülkelik erken uyarı sistemi için, ekonomik/mali/finansal krizleri 3'er ülkelik gruplara bölüp derin araştırma. Bu prompt **generik** — her ülke grubu için aynı, sadece `{ÜLKE1}, {ÜLKE2}, {ÜLKE3}` değişir.

---

## NEDEN ARAŞTIRIYORUZ (bağlam)
T2SAIM, küresel finansal krizleri **salgın hastalık gibi** (bulaşıcı) modelliyor. Krizler ülkeden ülkeye iletim ağları (ticaret, finans, emtia, nöro-davranışsal) üzerinden yayılıyor. Her ülkenin **ekonomik/mali/finansal krizlerini** doğru kaynaklarla topluyoruz ki:
- Erken uyarı sistemi her ülkenin **kriz öncesi sinyal desenini** öğrensin (kalibrasyon)
- Hangi ülkenin krizi hangi ülkeyi kaç gün sonra etkilediğini (iletim/contagion) ölçelim
- 29 ülkenin tamamını **eş zamanlı** değerlendirebilelim (hastalık yayılım modeli gibi)

## NE ARAŞTIRIYORUZ
**Ülkeler:** `{ÜLKE1}`, `{ÜLKE2}`, `{ÜLKE3}`

Her ülke için (1973-2026, 50 yıl):

### A. EKONOMİK KRİZLER (makro-finansal)
1. Her kriz: **tarih (başlangıç-zirve-bitiş)**, tetikleyici, mekanizma, **sayısal etki** (GSYH daralması %, devalüasyon %, enflasyon zirve %, işsizlik %, borsa çöküşü %, rezerv erimesi $, CDS bps)
2. Kriz öncesi **öncü sinyaller** (ne zaman görünmeye başladı — aylar önce)
3. İletim: bu ülke krizi **hangi ülkelere** yayıldı, ne kadar sürede (gün/hafta/ay)

### B. MALİ / FİNANSAL KRİZLER
- Bankacılık krizleri, borç krizleri (egemen/özel), döviz krizleri, borsa çöküşleri, enflasyon/para krizleri
- Her kriz tipi için: banka iflasları, NPL, LDR, döviz rezervi, CDS, sermaye kaçışı

### C. SİYASAL KRİZLER (ekonomiye bulaşan)
- Rejim değişimi, istikrarsızlık, ekonomiyi vuran siyasi şoklar (seçim, darbe, ambargo, protesto)

## ÇIKTI FORMATI (her ülke için)
```
## {ÜLKE} KRİZ LİSTESİ
| Kriz | Yıl | Tip | Tetikleyici | Sayısal etki | Öncü sinyal | Φ-katman | Kaynak |

Kalibrasyon amaçlı ≥3 ana kriz + siyasal olanlar. Kaynak: resmi istatistik/IMF/WB/merkez bankası.

## BULAŞMA ({ÜLKE1}-{ÜLKE2}-{ÜLKE3})
Hangi ülke krizi → hangi ülkeye → kaç gün/hafta sonra → iletim kanalı
```

## KURALLAR (kesin)
- **KAYNAKSIZ SAYI UYDURMA.** Bulunamayan değer → "VERİ YOK" + neden
- Resmi kaynak (IMF/WB/merkez bankası/ulusal istatistik) birincil
- Belirsiz rakam ≈ işaretli
- Türkçe çıktı
- Her ülke için 3-8 kriz (ekonomik + mali + siyasal)

---

## ÜLKE GRUPLARI (3'er, DeepSearch çağrısı başına 1 grup)
1. `ABD, Çin, Almanya`
2. `İngiltere, Japonya, Fransa`
3. `Rusya, Brezilya, Meksika`
4. `Suudi, Hindistan, Avustralya`
5. `İtalya, Hollanda, Türkiye`
6. `Tayvan, G.Kore, İsviçre`
7. `Şili, Kongo, Endonezya`
8. `G.Afrika, Kazakistan, Singapur`
9. `Kanada, İspanya, Hong Kong`
10. `Katar, BAE, [tamamlayıcı germani?]`

*Veritas Per Se — Komutan Picard · 24 Ağustos 2026*
