# 🧯 HATA VE ÇÖZÜM HAVUZU — Lessons Learned

> Yaşanan hatalar ve KALICI çözümleri. Aynı hatayı 2+ kez görmek → kök neden + buraya ekle.

| # | Hata (Belirti) | Kök Neden | Kalıcı Çözüm | İlk Görülme | Durum |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H-001 | FRED CSV parse hatası "could not convert to float: '.'" | FRED eksik veriyi '.' ile işaretler | `_read_fred` '.' ve bozuk satırı atlar | 2026-08-24 | ✅ Kalıcı |
| H-002 | `ModuleNotFoundError: No module named 'x'` | sys.path/PYTHONPATH karışması | PYTHONPATH temizle + doğru venv | 2026-08-24 | ✅ Kalıcı |
| H-003 | state.db şişkinliği (2.5GB) → session görünmüyor | eski session ağırlığı | son 2 hafta temizlik + RAG arşivi | 2026-08-24 | 🔄 Çözüm kuruldu |
