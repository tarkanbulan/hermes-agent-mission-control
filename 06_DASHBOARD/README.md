# Mission Control Dashboard

Bu dizin, T2SAIM Mission Control projesinin Kaptan için tasarlanmış görsel arayüzünü (Faz 1) barındırır.

## Özellikler

- **Görev Merkezi:** Markdown tabanlı görevleri listeler.
- **Canlı Log:** Log dosyalarını sürekli okur ve görüntüler. Olası hataları kırmızı renkte vurgular.
- **Ekip Köprüleri:** Tıklanabilir butonlarla markdown raporlarını çeşitli arka plan sistemlerine (G-Drive, ADR, Arka plan komutları) yönlendirir.

## Çalıştırma

Dashboard uygulamasını çalıştırmak için harici bir bağımlılığa (pip paketi) ihtiyaç yoktur.

```bash
python 06_DASHBOARD/server.py
```

Ardından web tarayıcınızda [http://127.0.0.1:8080](http://127.0.0.1:8080) adresine gidin.

## Dosyalar

- `index.html`: Kumanda masası arayüzü.
- `server.py`: Markdown dosyalarını API olarak sunan ve statik dosyaları servis eden yerel HTTP sunucusu.
- `dagit_ekip.py`: Ekip köprü butonlarının arka ucunu işleyen Python betiği.
