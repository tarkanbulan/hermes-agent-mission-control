# AGENTS.md — Mission Control Çalışma Kuralları

**Bu dosya, T2SAIM Mission Control'e erişen TÜM hermès ajanları (picard, shadow, cyberknife, james...) için bağlayıcı talimattır.**

---

## 1. HER O TURUM BAŞINDA

1. `README.md` oku (sistem mimarisi)
2. `01_GOREV_LISTESI/AKTIF_GOREVLER.md` oku → sana ait aktif görevleri bul
3. Mevcut görevin varsa durumunu anla; yoksa `BEKLEMEDE_ISLER.md`deki sıradaki işi al
4. Çalışma bitince aşağıdaki zorunlu kayıt rutinini uygula

## 2. ZORUNLU KAYIT RUTİNİ (R-017: "Kayıt yoksa iş yapılmamıştır")

Her görev/tur bitiminde:

```
1. Yaptığın işi 02_KAYIT_HAVUZU/HAVUZ.md dosyasına EKLE:
   | Tarih | Ajan | İş | Sonuç | Kanıt(yol) |
2. Görevi 01_/AKTIF → 01_/TAMAMLANAN'a TAŞI
3. Karar verildiyse 05_KARARLAR/KARAR.md'ye ekle (gerekçe + tarih)
4. Rapor üretildiyse 06_RAPORLAR/ altına kaydet
```

## 3. HAVUZ → OKF → RAG AKIŞI

- **ÜRETİM:** Yeni doğrulanmış bilgi üretirsen → `03_OKF_BILGI_BANKASI/` kopyala
- **TOPLAMA:** OKF + havuz içeriği zamanla `04_RAG` ile vektörleştirilir → ortak sorgulanabilir
- **SORGULAMA:** "Bu projede X ne zaman/bu kriz nasıl" → RAG + havuzu ara, tahmin etme

## 4. DİSİPLİN

- **Uydurma yasak:** Kayıt/OKF'e ispatsız sayı/olay yazma — kaynak göster
- **Veri bütünlüğü:** Havuzdaki kayıt değiştirilemez (immutable); yeni kayıt EKLE
- **Profesyonellik:** Yapılanların kaydı, kararların gerekçesi, görevlerin durumu her zaman güncel

## 5. PERSONA

- `07_PERSONA/<ajan_adı>.md` → her ajan kendi SOUL/profil özetini tutar (kim, neye sorumlu, uzmanlık)

---

*Veritas Per Se — Mission Control, 24 Ağustos 2026*
