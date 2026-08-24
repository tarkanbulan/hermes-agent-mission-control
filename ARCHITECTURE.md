# 🧠 ARCHITECTURE.md — Sistem Haritası (4 Katmanlı Beyin)

> Mission Control, "Kaptan ve Ajanları için Deterministik Komuta Merkezi" olarak 3 + log + rüya katmanında çalışır.

## Katmanlar

```
┌────────────────────────────────────────────────────────────────┐
│  STRATEJİ (00)  → NEDEN yapıyoruz?  (ADR, Mental Models)       │
├────────────────────────────────────────────────────────────────┤
│  GÖREV (01)     → NE yapıyoruz?     (İş Akış Motoru)          │
├────────────────────────────────────────────────────────────────┤
│  HAFIZA (02)    → NE biliyoruz?     (OKF + Hata/Çözüm)         │
├────────────────────────────────────────────────────────────────┤
│  LOG (05)       → NE OLDU?          (Her şeyin izi, hata bul)  │
├────────────────────────────────────────────────────────────────┤
│  RÜYA (04)      → NE KEŞFEDEBİLİRİZ? (Boşta karbon sentezi)    │
└────────────────────────────────────────────────────────────────┘
```

## Veri Akışı (SSOT — Single Source of Truth)

1. **Kaptan/Orkestratör** → `01_GOREV_MERKEZI`'ne atomik görev yazar → `03_PROMPTLAR` şablonuyla ajanlara dağıtır.
2. **Uygulayıcı Ajan** → görevi tamamlar → çıktıyı doğrular → `01_DOGRULAMA_VE_TEST`'e bırakır → `05_LOG/MASTER_LOG`'a kaydeder.
3. **Karar** → `00_STRATEJI/ADR` + `05_KARAR_LOGU`'na gerekçeyle yazılır.
4. **Öğrenme** → hatalar `05_HATA_LOGU` → kalıcı çözüm `02_HATA_VE_COZUM_HAVUZU`'na.
5. **Oturum sonu** → `02_CONTEXT_SNAPSHOTS`'a handoff → ertesi gün sıfır kayıp devam.
6. **Boşta** → ajan `04_RUYA_PROTOKOLU` ile karbon sentezi üretir.

## Dörtlü Hibrit Düğüm (Sync)

Yerel (Antigravity/Hermes CLI) ⇄ GitHub (Jules) ⇄ Google Drive (Hub) ⇄ Gemini (RAG) — tek SSOT reposu.

*Detay: `00_STRATEJI_VE_KARARLAR/MULTI_AGENT_TOPOLOGY.md`*
