# -*- coding: utf-8 -*-
"""
Picard_Mem_V1 — external plugin (hermes-example-plugins biçimi)

Amac: Bellek Bankası'na görsel erişim + sıkıştırma-öncesi OKF arşivleme
      + OpenViking(1933) RAG baglantisi. Context kaybini onler.
Kaynak: hermes-agent-mission-control musteri bellek bankasi.
"""

import os, json, glob
from pathlib import Path

# Bellek Bankası kökü (Mission Control SSOT)
BELLEK_BANKASI = r"E:\T2SAIM_NEXUS_MIRROR\jules_repos\hermes-mission-control\02_HAFIZA_VE_BILGI_BANKASI\BELLEK_BANKASI"
# OKF külliyatı
OKF_KOK = r"E:\T2SAIM_NEXUS_MIRROR\00_CENTRAL_DATA\okf_exports"


def _list_md(directory):
    """Dizin altındaki .md dosyalarını (yol + boyut) listele."""
    out = []
    if not os.path.isdir(directory):
        return out
    for f in sorted(glob.glob(os.path.join(directory, "**", "*.md"), recursive=True)):
        out.append({
            "path": f,
            "name": os.path.basename(f),
            "rel": os.path.relpath(f, directory),
            "size": os.path.getsize(f),
        })
    return out


def _read_md(path):
    """Markdown dosyasını güvenli oku (en fazla 50KB)."""
    if not os.path.isfile(path):
        return {"path": path, "error": "dosya yok"}
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            content = f.read(50000)
        return {"path": path, "content": content, "length": len(content)}
    except Exception as e:
        return {"path": path, "error": str(e)}


# ==== Hermes plugin SDK yüzeyi ====

def register(server, ctx):
    """Hermes plugin SDK: register edilen rota + slash komutu."""

    # --- Dashboard API rotaları ---
    @server.api_route("/api/picard-mem/index")
    def _api_index(_req, _res):
        """Bellek Bankası kategorilerini + dosya listesini döndür."""
        kategoriler = {}
        for d in sorted(os.listdir(BELLENK_BANKASI)) if os.path.isdir(BELLEK_BANKASI) else []:
            path = os.path.join(BELLEK_BANKASI, d)
            if os.path.isdir(path):
                kategoriler[d] = _list_md(path)
        return json.dumps({"kok": BELLEK_BANKASI, "kategoriler": kategoriler})

    @server.api_route("/api/picard-mem/oku")
    def _api_oku(req, _res):
        """Belirli bir Bellek Bankası / OKF markdown dosyasını oku."""
        path = req.query.get("yol", "")
        if not path:
            return json.dumps({"error": "yol parametresi gerekli"})
        full = os.path.join(BELLEK_BANKASI, path) if not os.path.isabs(path) else path
        if not os.path.abspath(full).startswith(os.path.abspath(BELLEK_BANKASI)):
            return json.dumps({"error": "Bellek Bankası dışı erişim yasak"})
        return json.dumps(_read_md(full))

    @server.api_route("/api/picard-mem/okf")
    def _api_okf(_req, _res):
        """OKF külliyatı üst klasörlerini listele (RAG kaynağı)."""
        return json.dumps({"kategoriler": _list_md(OKF_KOK)})

    @server.api_route("/api/picard-mem/openviking")
    def _api_ov(_req, _res):
        """OpenViking(1933) sağlık + indeks durumu."""
        import urllib.request
        try:
            with urllib.request.urlopen("http://127.0.0.1:1933/health", timeout=3) as r:
                return json.dumps({"health": r.status})
        except Exception as e:
            return json.dumps({"health": "kapali", "hata": str(e)})

    # --- Slash komutu: /mem <kategori> ---
    @ctx.on_command("mem")
    def _cmd_mem(args, _ctx):
        """Kullanım: /mem index | <kategori> | oku:<yol>"""
        arg = (args or "index").strip()
        if arg == "index":
            cats = sorted(os.listdir(BELLEK_BANKASI)) if os.path.isdir(BELLEK_BANKASI) else []
            return "Bellek Bankası kategorileri:\n" + "\n".join("• " + c for c in cats)
        if arg.startswith("oku:"):
            p = arg[4:]
            return str(_read_md(os.path.join(BELLEK_BANKASI, p)))
        # kategori listele
        p = os.path.join(BELLEK_BANKASI, arg)
        if os.path.isdir(p):
            files = _list_md(p)
            return f"{arg} dosyaları (n={len(files)}):\n" + "\n".join(f"• {f['rel']}" for f in files)
        return f"'{arg}' Bellek Bankası'nda bulunamadı. /mem index dene."


def process_departing_prompt(prompt, extra):
    """Sıkıştırma-öncesi arşivleme: oturum sonu bu çağrılırsa önemli bağlamı OKF'ye yazar."""
    # Amaç: context sıkıştırılırken kaybolacak bağlamı FILESYSTEM'e mühürlemek.
    # (Hermes 'departing prompt' kancası plugin'e promptu verir; burada özet yazılır.)
    import datetime
    hedef = os.path.join(BELLEK_BANKASI, "06_OTURUM", "sıkıştırma_kaydi.md")
    os.makedirs(os.path.dirname(hedef), exist_ok=True)
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    with open(hedef, "a", encoding="utf-8") as f:
        f.write(f"\n## [{ts}] sıkıştırma öncesi bağlam özeti\n{prompt[:2000]}\n")
    return prompt  # orijinali değiştirmeden geri ver

# import json (üstte tanımlı değilse)
import json
