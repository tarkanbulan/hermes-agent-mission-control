# 🧪 CAPSULE COMPRESSION — Context Kalitesi Değerlendirmesi

> **Motor:** NousResearch/hermes-compression-eval (offline probe-based evaluation harness for Hermes ContextCompressor).
> **Kullanım:** Mission Control'ün context kaybı sorununu ÖLÇER — "state.db 2.5GB, eski session görünmüyor" probleminin kalite boyutu.

## Neden Gerekli
- Hermes `context_compressor.py` bir oturum tavanına ulaşınca ne haysiyetle sıkıştıracağına karar verir.
- Şimdiye dek "test suite yeşil" ile "kötü özet" arasında ölçüm yoktu.
- Bu harness o sinyali verir: compressor prompt'unu değiştir → eval çalıştır → 6 boyut skorunu baseline ile karşılaştır.

## 6 Değerlendirme Boyutu
accuracy · context_awareness · artifact_trail · completeness · continuity · instruction_following (0-5)

## Kurulum
```bash
git clone https://github.com/NousResearch/hermes-compression-eval.git
pip install -r requirements.txt  # openai, fire
# hermes-agent checkout'u HERMES_AGENT_ROOT veya ~/.hermes/hermes-agent
```

## Kullanım (baseline + tweak karşılaştırma)
```bash
python3 run_eval.py --compressor-model=... --judge-model=... --runs=3 --label=baseline
# compressor prompt'u düzenle:
python3 run_eval.py ... --label=my-tweak --compare-to=results/baseline
```

## Mission Control Bağlantısı
- `05_LOG/HATA_LOGU`'daki context kaybı hataları → compression-eval ile ölçülür
- Sonuç `05_COMPRESSION/ozet.md`'ye yazılır
- Budget notu: LLM-graded, ~30 probe çifti — CI'de değil, manuel değerlendirme

## Durum
📌 **TASLAK** — kurulum bekliyor (hermes-agent checkout + provider kredisi). Mission Control tamamlanınca bu entegre edilecek.
