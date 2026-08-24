# -*- coding: utf-8 -*-
"""Buyuk korpusu 24 Layer bolumune kes."""
import os, re

src = r"E:\T2SAIM_NEXUS_MIRROR\Obsidian_Vaults\T2SAIM_Corpus\Books _Makale\T2SAIM_MASTER_UNIFIED_CORPUS_v2.0_V21_DATA.md"
out_dir = r"E:\T2SAIM_NEXUS_MIRROR\jules_repos\hermes-mission-control\02_HAFIZA_VE_BILGI_BANKASI\BELLEK_BANKASI\04_KORPUS_LAYERLER\\"
os.makedirs(out_dir, exist_ok=True)

with open(src, encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

marks = []
for i, l in enumerate(lines, 1):
    if re.match(r'^# LAYER', l.strip()):
        marks.append((i, l.strip()[:50]))

bolumler = []
for idx, (start, title) in enumerate(marks):
    end = marks[idx+1][0] if idx+1 < len(marks) else len(lines)+1
    bolumler.append((start, end, title))

for n, (start, end, title) in enumerate(bolumler):
    clean = re.sub(r'[^\w\s]', '', title).strip().replace(' ', '_')[:30]
    fname = f"{n+1:02d}_layer_{clean}.md"
    content = "".join(lines[start-1:end-1])
    with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{n+1:02d}. {start:>5}-{end:>5} ({end-start:>4} satir) {fname[:50]}")

print(f"\nToplam {len(bolumler)} bolum kestildi")
