# 🤖 Ajan Protokolü ve Çalışma İlkeleri

> Bunu, Mission Control'e erişen TÜM ajanlar (Hermes/orkestratör, Picard, shadow, araştırma, kodlama) okur ve uyar.

---

## 1. Altın Kurallar

1. **İzin Sınırları:** Size atanmamış dosyalara dokunmayın. Her görev, `01_GOREV_MERKEZI` içindeki bir kartla başlar.
2. **Doğrulama Önce Gelir:** Test edilmemiş veya çıktısı doğrulanmamış hiçbir görevi `DOGRULAMA_VE_TEST.md` aşamasından geçirmeden "bitti" saymayın.
3. **Kayıt Tutma (R-017):** Yaptığınız her kritik değişikliği ve mimari kararı ilgili log havuzuna yazın. *"Kayıt yoksa iş yapılmamıştır."*
4. **Context Koruma:** Oturum sonunda mutlaka `02_HAFIZA_VE_BILGI_BANKASI/CONTEXT_SNAPSHOTS/` altına `HANDOFF_SABLONU` formatında özet bırakın.
5. **Uydurma Yasak:** OKF'ye / havuza ispatsız sayı veya olay yazmayın — kaynak gösterin.
6. **Boşta Kalınca Rüya:** Aktif göreviniz yoksa boş oturmayın → `04_RUYA_PROTOKOLU`'ne geçin ve karbon sentezi üretin.

---

## 2. Ajan Rolleri

| Rol | Sorumlu | Görev |
| :--- | :--- | :--- |
| **Kaptan** (İnsan) | Tarco | Nihai onay, strateji, hedef koyma |
| **Orkestratör** (Hermes) | Hermes | Görevleri atomik parçala, alt ajanlara dağıt, durum takip |
| **Uygulayıcı Ajanlar** | Picard, shadow... | Tek atomik görevi tamamla, doğrula, teslim et |

---

## 3. İletişim Kuralları

- **Ajan → Kaptan:** `01_GOREV_MERKEZI`'ne görev durumu + `05 (rapor)` klasörüne çıktı. Yüzeysel "oldu" demek yasak — kanıt (dosya yolu, test çıktısı) sun.
- **Ajan → Ajan:** Bot-to-bot mesajlaşma (bot chat) veya `03_PROMPTLAR_VE_TALIMATLAR` üzerinden formal handoff.
- **Kararlar:** Bir teknik/yön kararı verilince `00_STRATEJI_VE_KARARLAR/ADR/` altına ADR kaydı aç (gerekçe + seçenekler + sonuç).

---

## 4. Rüya Protokolü (Boştayken)

> Ajan aktif görevde DEĞİLSE:
1. `04_RUYA_PROTOKOLU/README.md` oku
2. OKF/külliyat tan bir TEZ kaynağı seç
3. Bisociation kur (TEZ × ilgisiz ANTİTEZ/konu)
4. Yeni karbon hipotezi üret → `04_RUYA_PROTOKOLU/KARBON_HAVUZU/` kaydet
5. GDPO ile skorla → KG ≥ 0.65 ise **SEALED** işaretle

*Tüm ajanlar aynı protokole uyar — böylece boştayken kolektif istihbarat üretilir.*

---

*Veritas Per Se — Mission Control, 24 Ağustos 2026*
