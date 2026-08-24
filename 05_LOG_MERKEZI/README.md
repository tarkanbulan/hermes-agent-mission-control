# 🪵 MISSION CONTROL LOG SİSTEMİ — HER ŞEYİ LOGLA

> **Kaptan emri (24 Ağustos 2026):** "Bu sisteme her şeyin loglanmasını sağlayan eklentiler koy. Amaç hataları bulmak."
>
> **Prensip:** Loglanmayan işlem YOKTUR. Hata bulmanın tek yolu, olan her şeyin izlenebilir olmasıdır.

---

## 🎯 NEDEN

- **Hata bulmak:** Her işlem, çağrı, dosya, hata izlenebilir olursa bir arıza anında kök neden (root cause) bulunur.
- **Denetlenebilirlik:** "Kim, ne zaman, ne yaptı?" her zaman cevaplanabilir.
- **Context koruma:** Loglar oturum handoff'larının temelini oluşturur.

---

## 📁 LOG DİZİN YAPISI

```
05_LOG_MERKEZI/                        ← TÜM LOGLARIN TEK MERKEZİ
├── MASTER_LOG.md                      ← Tüm ajanların kronolojik ana günlüğü (append-only)
├── HATA_LOGU.md                       ← Hatalar (hata tespit edilince KESİN kayıt)
├── OTOMATIK/                          ← Script/cron tarafından otomatik yazılanlar
│   ├── ajan_aktivite.jsonl            ← Her ajanın her işlemi (JSON lines)
│   └── hata_kayitlari.jsonl           ← Otomatik hata logları
├── ARAC_CAĞRILARI.md                  ← Ajanın her araç/tool çağrısı (terminal, dosya, web)
└── KARAR_LOGU.md                      ← Kararlar + gerekçe (ADR ile bağlantılı)
```

---

## 🧩 LOGLAMA EKLENTİLERİ (Ajanlara Enjekte Edilecek Kurallar)

Her ajan, başına şu loglama davranışını takınır:

### EKLENTİ-1: MASTER_LOG (ana kronolojik kayıt)
Her önemli işlem sonunda `MASTER_LOG.md`'ye EKLE:
```markdown
| 2026-08-24 10:20 | picard | SİSTEM: Mission Control log dizini kuruldu | ✅ | kurulduğu kanıt (ls) |
```

### EKLENTİ-2: HATA_LOGU (hataları yakala)
Bir hata/istisna oluşursa ASLA gizle — `HATA_LOGU.md`'ye kaydet:
```markdown
## [HATA] 2026-08-24 10:22 — picard
- **Belirti:** Python module not found
- **Hata Mesajı:** `ModuleNotFoundError: No module named 'x'`
- **Bağlam:** Misyon kontrol scripti çalıştırılırken
- **Çözüm:** pip install veya sys.path düzeltildi
- **Durum:** ✅ ÇÖZÜLDÜ / 🔴 AÇIK
```

### EKLENTİ-3: ARAC_CAĞRILARI (araç izleme)
Ajan her `terminal`/`read_file`/`patch`/`web` çağrısında kanıt satırı bırakır:
```markdown
| 2026-08-24 10:25 | picard | terminal | "python veriyi_calistir.py" | exit=0 |
```

### EKLENTİ-4: Hata bulma (Pattern Recognition)
`HATA_LOGU.md`'de aynı hata 2+ kez geçiyorsa:
- → Kök neden analizi başlat
- → `HATA_COZUM` havuzuna kalıcı çözüm ekle (2_HATA_VE_COZUM_HAVUZU)
- → Ajanın aynı hatayı tekrarlaması engellenir

---

## ✅ HER AJAN İÇİN ZORUNLU LOGLAMA RUTİNİ

| Adım | Nereye | Ne zaman |
| :--- | :--- | :--- |
| 1 | `ARAC_CAĞRILARI.md` | Her terminal/dosya/web çağrısı |
| 2 | `MASTER_LOG.md` | Her tamamlanan işlem |
| 3 | `HATA_LOGU.md` | Her hata/istisna |
| 4 | `KARAR_LOGU.md` | Her karar/gerekçe |
| 5 | Otomatik (cron) | Gece rüya + otomatik hata taraması |

---

## 🤖 OTOMATİK HATA BULMA (Cron ile)

1. **Sağlık kontrolü:** Cron, periyodik olarak `HATA_LOGU` + `MASTER_LOG`'u tarar
2. **Aynı hata tekrarı → alarm:** 2+ tekrar tespit edilirse "kök neden" uyarısı
3. **Aktivite boşluğu → alarm:** Bir ajan uzun süre log yazmıyorsa (takıldı mı?) uyarı
4. **Rapor:** Haftalık `05_COMPRESSION/hata_ozeti.md`

---

## 📌 Mission Control ile Bağlantı

| Log Sistemi | İlgili Misyon Kontrol |
| :--- | :--- |
| MASTER_LOG | `02_HAFIZA/CONTEXT_SNAPSHOTS` (handoff'lar bundan türer) |
| HATA_LOGU | `02_HAFIZA/HATA_VE_COZUM_HAVUZU` (çözüm kalıcılaşır) |
| ARAC_CAĞRILARI | `01_GOREV_MERKEZI/DOGRULAMA_VE_TEST` (kanıt) |
| KARAR_LOGU | `00_STRATEJI/ADR` (mimari kararlar) |

---

*Veritas Per Se — Mission Control Log Sistemi, 24 Ağustos 2026*
