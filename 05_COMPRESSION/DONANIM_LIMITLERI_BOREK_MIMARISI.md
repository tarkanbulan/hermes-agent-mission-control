# 🖥️ DONANIM LİMİTLERİ & BÖREK (Katmanlı) MİMARİSİ

> **Profil:** AMD Ryzen 7 · 16 GB RAM · 4 GB VRAM (RX 580)
> **Amaç:** Büyük veri setleri ve çok ajanlı simülasyonları kilitlemeden çalıştırmak.
> **Prensip:** İş yükünü "katmanlı yufka ve harç" (pipelined chunking & tiering) bölmek.

---

## 1. 🥟 BÖREK MİMARİSİ (3 Katman)

```
┌────────────────────────────────────────────────────────────────────┐
│ 1. TABAN KATMANI (16GB RAM & Ryzen 7): Vektörel Hızlı Tarama     │
│    NumPy / Polars / DuckDB → bellek eşlemeli (mmap) toplu filtre  │
├────────────────────────────────────────────────────────────────────┤
│ 2. İÇ HARÇ (Ryzen 7 Çok Çekirdek): Aday Eleme & Heuristic Süzgeç │
│    Multiprocessing → 50 hisseden 45'ini milisaniyede ele          │
├────────────────────────────────────────────────────────────────────┤
│ 3. ÜST KATMAN (4GB VRAM / Hafif Model): Niteliksel Karar & Sentez │
│    Sadece finalist 3-5 hisse → 3B-7B Q4_K_M (Vulkan/DirectML/CPU) │
└────────────────────────────────────────────────────────────────────┘
```

## 2. Kaynak Yönetimi Prensipleri

| Kaynak | Strateji |
| :--- | :--- |
| **Ryzen 7 (CPU)** | Ağır matematik (RSI, volatilite, korelasyon) + veri yükleme → multiprocessing/Polars paralel |
| **16 GB RAM** | 29 yıllık veriyi tek seferde bellekten geçirme → DuckDB/Polars **lazy scanning** (`scan_parquet`) · RAM tavanı **10-12 GB** |
| **4 GB VRAM** | 3B/7B model Q4_K_M · `n-gpu-layers` ~18-22 GPU'ya, kalan CPU'ya |

## 3. Ortam Değişkenleri (Windows)

```powershell
# Polars/OpenMP thread'lerini fiziksel çekirdeğe sabitle
$env:POLARS_MAX_THREADS = "8"
$env:OMP_NUM_THREADS = "8"

# Ollama/llama.cpp paralel sınırı (RAM taşmasını önle)
$env:OLLAMA_NUM_PARALLEL = "1"
$env:OLLAMA_MAX_LOADED_MODELS = "1"
```

## 4. Yerel LLM (llama.cpp, 4GB VRAM)

```bash
# Vulkan backend, model katmanlarının ~20'si GPU'da, kalanı CPU'da
llama-cli -m ./models/qwen2.5-3b-instruct-q4_k_m.gguf -ngl 20 -c 2048 --threads 8
```

## 5. KOD ŞABLONU (lazy + chunk + finalist)

```python
import gc, numpy as np, polars as pl
from concurrent.futures import ProcessPoolExecutor

def stream_market_data(file_path, chunk_days=250):
    lazy_df = pl.scan_parquet(file_path)
    dates = lazy_df.select("date").unique().collect().to_series().sort()
    for i in range(0, len(dates), chunk_days):
        chunk = lazy_df.filter(pl.col("date").is_in(dates[i:i+chunk_days])).collect()
        yield chunk
        del chunk; gc.collect()

def fast_vector_filter(df_chunk):
    return (df_chunk.filter((pl.col("rsi_14")<35)&(pl.col("volume_ratio")>1.2))
            .select("ticker").unique().to_series().to_list())

def evaluate_finalists(candidates, current_date):
    # Yalnızca 3-5 hisse için yerel 3B model / kural çağrılır
    return [{"ticker": t, "date": current_date, "decision": "EVALUATED"}
            for t in candidates]

def run_pipeline(data_path):
    for batch in stream_market_data(data_path, chunk_days=60):
        cands = fast_vector_filter(batch)
        if cands:
            results = evaluate_finalists(cands, str(batch["date"][-1]))
            # sonucu diske append (RAM'de tutma)
```

## 6. Özet Kontrol Listesi

1. **Parquet/Arrow** → CSV yerine, I/O + RAM %70 azalır
2. **Lazy processing** → `scan_parquet` ile sadece gerekli sütunlar
3. **Explicit GC** → her chunk sonunda `del` + `gc.collect()`
4. **VRAM sınırı** → 4GB kartta context ≤ 2048-4096 token

---

**Mission Control Bağlantısı:** Bu, T2SAIM kriz ve çoklu-ajan motorlarının yerel donanımda çalışma şemasıdır. `country_sensor.py` ve `ubtf_walkforward.py` bu prensibe göre lazy/chunk çalışmalıdır.

*Veritas Per Se — Donanım Limiti Doktrini, 24 Ağustos 2026*
