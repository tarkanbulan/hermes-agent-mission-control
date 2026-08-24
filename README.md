# 🎛️ HERMES AGENT — MISSION CONTROL

**T2SAIM Görev Kontrol ve Profesyonel Proje Yönetim Merkezi**

> Bu, T2SAIM'in **tek makine kontrol yeridir.** Tüm ajanların pencereleri buradan açılır, yapılacak işler burada takip edilir, yapılanların kayıtları buraya düşer, hafıza (RAG + OKF bilgi bankası) ve bilgi arşivi burada yaşar. Profesyonel proje yönetimi merkezidir.

---

## 🧠 SİSTEM MİMARİSİ (3 Katmanlı Beyin + Görev Merkezi)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     MISSION CONTROL (bu merkez)                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [HAVUZ — Kayıt Deposu]        [OKF — Bilgi Bankası]               │
│  📁 02_KAYIT_HAVUZU             📁 03_OKF_BILGI_BANKASI             │
│  • Ne YAPTIK? sorusunun cevabı  • NE BİLİYORUZ? sorusunun cevabı   │
│  • İşlem logları, kararlar      • Doğrulanmış külliyat             │
│  • Emirler, üretimler           • Kriz kronolojileri, formüller    │
│                                                                     │
│        ┌──────────────────────────────────────────┐                │
│        │  [RAG — Ortak Sorgulanabilir Hafıza]     │                │
│        │  📁 04_RAG_ORTAK_HAFIZA                  │                │
│        │  • Havuz + OKF → vektörleştirilmiş       │                │
│        │  • NASIL BULURUZ? sorusunun cevabı      │                │
│        └──────────────────────────────────────────┘                │
│                                                                     │
│  [GÖREV MERKEZİ]             [KARAR & RAPOR]                       │
│  📁 01_GOREV_LISTESI          📁 05_KARARLAR · 06_RAPORLAR          │
│  • Yapılacak işler (backlog)  • Kararlar + gerekçeler              │
│  • Aktif / bekleyen / bitti   • Üretilen raporlar                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🏛️ 7 SİSTEMLİ KARARGAH HAFIZASIYLA İLİŞKİ

> **Bu merkez, karargahtaki mevcut 7-sistem hafızadan BAĞIMSIZ değildir; onun PROJE ODAKLI yüzeyidir.**

Karargahın büyük sistemi (KB DB, state.db, kontekst kütüphanesi, kara kutu logları) **aynen durur.** Mission Control, **odaklı tek proje için** dar, self-contained bir çalışma alanı sunar:

| Buradaki Katman | Karargah Karşılığı | Farkı |
| :--- | :--- | :--- |
| `02_KAYIT_HAVUZU` | Kara kutu logları + KB DB | Proje özelinde, okunabilir Markdown |
| `03_OKF_BILGI_BANKASI` | OKF külliyatı (`00_CENTRAL_DATA`) | Projeye gerekli doğrulanmış özetler |
| `04_RAG_ORTAK_HAFIZA` | NotebookLM/OpenViking | Bu projenin dokümanlarını vektörleştirir |
| `01_GOREV_LISTESI` | Seneca emir defteri | Profesyonel proje yönetimi |

**Hedef:** Tüm ajanlar (picard, shadow, cyberknife...) bu merkeze yazar/okur; böylece proje tek pencereden yönetilir.

---

## 📁 KLASÖR REHBERİ

| Klasör | İçerik | Ajan Görevi |
| :--- | :--- | :--- |
| `01_GOREV_LISTESI/` | Yapılacak işler: aktif, bekleyen, tamamlanan | Görev başında güncelle |
| `02_KAYIT_HAVUZU/` | Yapılanların logu (havuz) | Her işi buraya kaydet |
| `03_OKF_BILGI_BANKASI/` | Doğrulanmış külliyat (kriz, formül, PDF özeti) | Referans için oku |
| `04_RAG_ORTAK_HAFIZA/` | Vektörleştirilmiş ortak arama (kurulum + indeks) | Sorgula |
| `05_KARARLAR/` | Kararlar + gerekçeler | Karar verilince kaydet |
| `06_RAPORLAR/` | Üretilen raporlar | Rapor buraya |
| `07_PERSONA/` | Ajan profilleri (her ajanın SOUL özeti) | Kendi profilini tut |
| `99_ARHIV/` | Eski/pasif dosyalar | Taşı | 

---

## ⚙️ NASIL ÇALIŞIR

### HER AJAN (oturum başında) — ZORUNLU RUTİN
1. `AGENTS.md` oku (kurallar)
2. `01_GOREV_LISTESI/AKTIF_GOREVLER.md` oku → görevini bul
3. Göreve başla
4. İş bitince → `02_KAYIT_HAVUZU/HAVUZ.md`'ye ne yaptığını KAYDET
5. Görevi `TAMAMLANAN.md`'ye taşı
6. Gerekirse `05_KARARLAR/` ve `06_RAPORLAR/` güncelle

### KRİTİK KURAL
> **"Kayıt yoksa iş yapılmamıştır." (R-017)** — Her işlem havuza işlenmeden kapalı sayılmaz.

---

## 🧠 RAG / OKF / HAVUZ NASIL BAĞLANIR

1. **Havuz** (`02_`) → herkesin ürettiği veriler Markdown olarak kaydedilir
2. **OKF** (`03_`) → doğrulanmış bilgiler (kriz kronolojileri, formüller) buraya
3. **RAG** (`04_`) → `02_` + `03_` içeriği vektörleştirilip **ortak sorgulanabilir** hale gelir (NotebookLM MCP / OpenViking)

Böylece: *"Bu projede X ne zaman yapıldı?"* (havuz) ve *"Bu krizi nasıl tespit ederiz?"* (OKF+RAG) tek yerden cevaplanır.

---

## 🚀 BAŞLANGIÇ

Bu şablon boş repo üzerine kuruldu. Sıradaki adımlar (mission control'ün kendi görev listesine işlenecek):
- [ ] 10_GOREV_LISTESI'ne proje görevleri ekle (kriz tespit sistemi)
- [ ] 03_OKF → kriz külliyatı özetlerini kopyala
- [ ] 04_RAG → kurulum + ilk indeksleme
- [ ] 02_HAVUZ → oturum rutini başlat

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026*
