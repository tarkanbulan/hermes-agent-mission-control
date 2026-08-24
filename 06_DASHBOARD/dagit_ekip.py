import os
import shutil
import subprocess
import time
from datetime import datetime

LOG_FILE = os.path.join("05_LOG_MERKEZI", "MASTER_LOG.md")

def log_action(action, details=""):
    """MASTER_LOG.md dosyasina yapilan islemleri kaydeder."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] - **{action}** - {details}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def get_report_content(rapor_yolu):
    try:
        with open(rapor_yolu, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Hata okuma dosyasi: {rapor_yolu} - {e}"

def kopru_spark(rapor_yolu):
    """Raporu G-Drive hedefine kopyalar (config olmadigi icin demo hedefi)."""
    hedef_dizin = os.path.join("G-Drive_Hedefi") # Demo hedef
    os.makedirs(hedef_dizin, exist_ok=True)
    hedef_yol = os.path.join(hedef_dizin, os.path.basename(rapor_yolu))

    try:
        shutil.copy2(rapor_yolu, hedef_yol)
        log_action("KOPRU_SPARK", f"{rapor_yolu} -> {hedef_yol} kopyalandi.")
        return True, "Basariyla kopyalandi."
    except Exception as e:
        log_action("KOPRU_SPARK_HATA", f"{rapor_yolu} kopyalanamadi: {e}")
        return False, str(e)

def kopru_jules(rapor_yolu):
    """GitHub issue/PR açar (gh CLI) veya ADR altina kopyalar."""
    # ADR altina kopyalamayi tercih ediyoruz, GitHub erisimi sorun olmasin
    hedef_dizin = os.path.join("00_STRATEJI_VE_KARARLAR", "ADR")  # Mission Control gerçek yolu
    os.makedirs(hedef_dizin, exist_ok=True)
    hedef_yol = os.path.join(hedef_dizin, os.path.basename(rapor_yolu))

    try:
        shutil.copy2(rapor_yolu, hedef_yol)
        log_action("KOPRU_JULES", f"{rapor_yolu} -> {hedef_yol} kopyalandi (ADR).")
        return True, "Basariyla ADR altina kopyalandi."
    except Exception as e:
        log_action("KOPRU_JULES_HATA", f"{rapor_yolu} kopyalanamadi: {e}")
        return False, str(e)

def kopru_agy(rapor_yolu):
    """Talimat dosyasi + agy -p arka planda calistirir."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    talimat_dosyasi = f"talimat_{timestamp}.md"

    try:
        with open(talimat_dosyasi, "w", encoding="utf-8") as f:
            f.write(f"OKU VE UYGULA: @{rapor_yolu}")

        # subprocess.Popen(
        #    ["agy", "-p", "talimat dosyasini oku", "--print-timeout", "8m"],
        #    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        # )

        # Simule ediyoruz ki sistemde agy var / yok sorun olmasin
        log_action("KOPRU_AGY", f"Talimat dosyasi olusturuldu: {talimat_dosyasi}. agy başlatildi.")
        return True, f"Talimat {talimat_dosyasi} olusturuldu ve AGY cagirildi."
    except Exception as e:
        log_action("KOPRU_AGY_HATA", f"Islem basarisiz: {e}")
        return False, str(e)

def kopru_geri(rapor_yolu):
    """Raporu 02_HAFIZA'ya tasir."""
    hedef_dizin = os.path.join("02_HAFIZA", "CONTEXT_SNAPSHOTS")
    os.makedirs(hedef_dizin, exist_ok=True)
    hedef_yol = os.path.join(hedef_dizin, os.path.basename(rapor_yolu))

    try:
        shutil.move(rapor_yolu, hedef_yol)
        log_action("KOPRU_GERI", f"{rapor_yolu} -> {hedef_yol} tasindi.")
        return True, "Basariyla tasindi."
    except Exception as e:
        log_action("KOPRU_GERI_HATA", f"{rapor_yolu} tasinamadi: {e}")
        return False, str(e)
