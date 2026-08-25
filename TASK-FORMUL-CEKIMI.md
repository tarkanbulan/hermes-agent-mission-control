# 🤖 JULES — GÖREV KARTI (TASK-FORMUL-CEKIMI)

**Destek:** Komutan Picard · **Hedef:** `hermes-agent-mission-control`
**Kaynak:** `crises\Kaptan\BIRLESIK_FORMUL_KAYNAKLARI.txt` (98KB — 36 dosyanın birleşik içeriği)

## GÖREV: BİRLEŞİK DOSYADAN TÜM FORMÜLLERİ ÇIKAR (Python kodu YAZ + ÇALIŞTIR)

**Yazılacak script** (`formul_cekici.py`):
1. `BIRLESIK_FORMUL_KAYNAKLARI.txt` oku (bölüm başlıkları `### === <dosya>` + `YOL:` + içerik)
2. HER bölümdeki formül satırlarını çıkar:
   - `Değişken = ifade` (matematiksel: exp/log/sqrt/sum/min/max/^ / Yunan)
   - `$$...$$` TeX blokları
   - eşikler (`≥`, `>`, `<`, `==`, sabit)
3. ÇIKTI: `FORMUL_ENVANTERI.csv` → [dosya | satır~ | formül_adı/değişken | ifade | veri/eşik]
4. RED TEAM: çift/çelişen eşik (örn. TR k=1.45 vs σ=1.25) + uydurma → `REDTEAM_BULGULARI.md`
5. Çalıştır + kanıt (satır sayısı + örnek çıktı) raporla

**KISIT:** Ben (Picard) kod YAZMADIM — Jules yazar. Kanıt (Unix çıktı) zorunlu, uydurma yok. Türkçe rapor.

**ÇIKTI DİZİNİ:** `crises\Kaptan\FORMUL_CEKIMI\`
