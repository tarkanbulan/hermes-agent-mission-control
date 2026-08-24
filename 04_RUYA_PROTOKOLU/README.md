# 💭 RÜYA PROTOKOLÜ — Boştaki Ajanların Kolektif İstihbarat Üretimi

> **Kaptan emri (24 Ağustos 2026):** "Çalışan HERKES'i bir süre boştayken RÜYA görmesini sağla."
>
> **Prensip:** Ajanın aktif görevi yoksa boş bekleyeceği yerde, var olan bilgilerden (OKF/külliyat) yeni kavram sentezleri (KARBON) üretir. Bu, sentetik keşif = "rüya"dır; GDPO ile filtrelenir; KG ≥ 0.65 ise mühürlenir (SEALED).

---

## 🎯 NEDEN

İnsan beyni uyurken (boştayken) günün deneyimlerini konsolide edip yeni bağlar kurar. Ajanlar da boştayken aynısını yapmalı: **durup beklemek yerine, okuduklarından yeni sentezler üretmek.** Böylece sabah masada filtrelenmiş öngörü "rüyası" olur.

---

## 🔄 RÜYA DÖNGÜSÜ (boştaki ajan için)

```
1. AKTİF GÖREV YOK MU? → Rüya protokolüne geç (AGENTS.md kuralı)
2. KAYNAK SEÇ: OKF/külliyattan bir TEZ dokümanı oku
3. BİSOCIATION: TEZ'i ilgisiz bir konu/ANTİTEZ ile çaprazla
4. KARBON ÜRET: 5N1K + Köprü Hipotezi + KG skoru
5. GDPO FİLTRE: halüsinasyon/abartıyı ele (r_truth, r_amygdala)
6. KG ≥ 0.65 → SEALED → KARBON_HAVUZU'na kaydet
7. LOGLA: 05_LOG/MASTER_LOG + KARBON_HAVUZU
```

---

## 🧩 KARBON ŞABLONU (her rüya çıktısı)

```markdown
## KARBON-{NO}: {Başlık}

| 5N1K | Açıklama |
|:-----|:----------|
| **Ne?** | ... |
| **Nerede?** | ... |
| **Hadi canım?** | ✅ / ❌ |

**Bisociation:** {TEZ kaynağı} × {ANTİTEZ/konu}
**Köprü Hipotezi:** {iki kaynak nasıl yeni bağ kurar}
**KG Hesaplama:** I=…, A=…, O=… → **KG=… → SEALED**
```

---

## 🏆 KG (Knowledge Gain) FORMÜLÜ

KG = I (İlgi) × A (Anlamlılık) × O (Özgünlük)
- **KG ≥ 0.65 → SEALED** (mühürlü, geçerli rüya)
- **KG ≥ 0.80 → SEALED 🏆** (yüksek değer)
- **KG ≥ 0.90 → ABSOLUTE** (nadir, köşe taşı)

Referans: `PICARD_DREAM_CARBON_v4_10_KARBON.md` (10 karbon; en yüksek KG=0.90 R-Calculus × TEZ/ANTİTEZ).

---

## 🕒 ZAMANLAMA & ORKESTRASYON

| Yöntem | Açıklama |
| :--- | :--- |
| **Cron (önerilen)** | Ajan boşsa ve gece → rüya görevi otomatik başlar |
| **Manuel** | Kaptan "rüya gör" derse ajan hemen başlar |
| **Otomatik (boşluk)** | AGENTS.md kuralı: aktif görev yoksa rüyaya geç |

**Çıktı:** `04_RUYA_PROTOKOLU/KARBON_HAVUZU/<tarih>_<ajan>_karbon.md`

---

## 🔗 BAĞLANTILAR

- GDPO filtresi → `0000_A_Karargah/scripts/t2saim_gdpo_multi_reward_engine.py`
- Karbon referansı → `CARBON_ENGINE` v4.0 (bisociation)
- OKF kaynakları → `02_HAFIZA_VE_BILGI_BANKASI/OKF_BILGI_BANKASI.md`

---

*Veritas Per Se — Rüya Protokolü, 24 Ağustos 2026*
