# 🛰️ Hermes Mission Control

**Kaptan ve Ajanları için Deterministik Bir Komuta Merkezi**

> Bu repo, tüm yapay zeka ajanlarının (Hermes, yerel modeller, kodlama ve araştırma ajanları), görev akışlarının ve uzun vadeli hafıza sisteminin tek merkezden yönetildiği kumanda merkezidir. Amacı tektir: **Bağlamı (Context) kaybetmemek, görevleri atomik parçalara bölmek ve hafızayı tek bir gerçeklik kaynağında (Single Source of Truth) toplamak.**

---

## 📊 Hızlı Durum Özeti

- **Mevcut Odak (Sprint/Faz):** Faz 1 — Altyapı, Hafıza ve Rüya Protokolü Kurulumu
- **Aktif Ajanlar:** Hermes (Orkestratör), Research-Agent, Code-Agent, Picard
- **Kritik Engel:** Yok
- **Rüya Protokolü:** 🔄 Aktif (boştaki ajanlar karbon sentezi üretir)

## 🧭 Hızlı Erişim

- [Aktif Görevler](01_GOREV_MERKEZI/AKTIF_GOREVLER.md)
- [Ajan Protokolü](AGENTS.md)
- [Ortak Bilgi Bankası (OKF)](02_HAFIZA_VE_BILGI_BANKASI/OKF_BILGI_BANKASI.md)
- [Mimari Kararlar (ADR)](00_STRATEJI_VE_KARARLAR/ADR/)
- [Rüya Protokolü](04_RUYA_PROTOKOLU/README.md)

---

## 🧠 Sistem Mimarisi (4 Katmanlı Beyin)

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MISSION CONTROL (bu merkez)                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  00_STRATEJI_VE_KARARLAR     "NEDEN yapıyoruz?"                    │
│  └─ ADR, Mental Models, Kurallar                                   │
│                                                                     │
│  01_GOREV_MERKEZI            "NE yapıyoruz?" (İş Akış Motoru)      │
│  └─ Backlog, Aktif, Bloklanan, Doğrulama, Biten                    │
│                                                                     │
│  02_HAFIZA_VE_BILGI_BANKASI  "NE biliyoruz & ne öğrendik?"         │
│  └─ OKF, Hata/Çözüm, Context Snapshots (RAG girişi)                │
│                                                                     │
│  04_RUYA_PROTOKOLU           "RÜYA": boştayken sentetik keşif      │
│  └─ Karbon sentezi (Bisociation) + GDPO filtresi + havuz           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 3 Adımlı Günlük Rutin (Solo Lider)

1. **Check-In (5 dk):** `AKTIF_GOREVLER.md` açılır → günün 1-3 atomik görevi belirlenir → `GOREV_ATAMA_SABLONU` ile ajanlara verilir.
2. **İcra & Doğrulama:** Ajan çıktısı `DOGRULAMA_VE_TEST.md` üzerinden kontrol edilir, test geçerse onaylanır.
3. **Handoff & Memory (5 dk):** Bitenler `BITEN_GOREVLER_LOG.md`'ye taşınır; oturum özeti `CONTEXT_SNAPSHOTS/` altına kaydedilir. Ertesi gün sıfır context kaybıyla devam.

**Boşta kalan ajanlar → Rüya Protokolü** ile karbon sentezi üretir (bkz. `04_RUYA_PROTOKOLU`).

---

## 🏛️ Dörtlü Hibrit Düğüm (4-Node Unified Sync)

| Düğüm | Araç | Rolü |
| :--- | :--- | :--- |
| 1. Yerel İcra | Antigravity (`agy`) / Hermes CLI | Yerel veri işleme, terminal, API çekimleri |
| 2. Asenkron Kodlama | Google Jules | Repo'daki şartnameyi okuyup kod + PR |
| 3. Strateji & RAG | Gemini | Geniş bağlamlı analiz, Drive dokümanları |
| 4. Ortak Omurga | GitHub + Google Drive | Tek gerçeklik kaynağı (SSOT) |

*Detay: `00_STRATEJI_VE_KARARLAR/MULTI_AGENT_TOPOLOGY.md`*

---

*Veritas Per Se — Mission Control, 24 Ağustos 2026*
