# 🖥️ DONANIM — Limitler ve Börek Mimarisi

> Kaynak: Kaptan donanım limitleri dokümanı (2026-08-24).

## Profil
- AMD Ryzen 7 · 16 GB RAM · 4 GB VRAM (RX 580)

## Prensip: Börek (Katmanlı)
1. Taban: NumPy/Polars/DuckDB mmap → vektörel tarama
2. İç harç: Ryzen 7 çok çekirdek → aday eleme (multiprocessing)
3. Üst: 3B-7B Q4_K_M (Vulkan/DirectML) → finalist 3-5 hisse

## Ayarlar
- `POLARS_MAX_THREADS=8`, `OMP_NUM_THREADS=8`
- `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_MAX_LOADED_MODELS=1`
- llama: `-ngl 20 -c 2048 --threads 8`
- RAM tavanı 10-12 GB, Parquet + lazy scan, explicit GC.
