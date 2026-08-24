// Picard_Mem_V1 — Dashboard tab ön yüzü (minimal)
// Bellek Bankası'nı Hermes Dashboard'da görsel gösterir.
// API: /api/picard-mem/index, /api/picard-mem/oku?yol=..., /api/picard-mem/openviking

window.picardMem = {
  async loadIndex() {
    try {
      const r = await fetch('/api/picard-mem/index');
      return await r.json();
    } catch (e) { return { error: String(e) }; }
  },
  async loadOpenviking() {
    try {
      const r = await fetch('/api/picard-mem/openviking');
      return await r.json();
    } catch (e) { return { health: 'kapali', hata: String(e) }; }
  },
  render(container) {
    container.innerHTML = '<div style="padding:16px;font-family:monospace">Picard Mem yükleniyor…</div>';
    Promise.all([this.loadIndex(), this.loadOpenviking()]).then(([idx, ov]) => {
      if (idx.error) { container.innerHTML = '<pre style="color:red">' + idx.error + '</pre>'; return; }
      let html = '<div style="padding:16px;font-family:system-ui">';
      html += '<h2>🧠 Picard Bellek Bankası</h2>';
      html += '<div>OpenViking: ' + (ov.health === 200 ? '<b style="color:green">açık</b>' : '<b style="color:red">' + (ov.health || 'kapalı') + '</b>') + '</div>';
      html += '<div>' + idx.kok + '</div><hr>';
      for (const [kat, dosyalar] of Object.entries(idx.kategoriler || {})) {
        html += '<h3>' + kat + '</h3><ul>';
        for (const f of dosyalar) {
          html += '<li><code>' + f.rel + '</code> (' + f.size + 'B)</li>';
        }
        html += '</ul>';
      }
      html += '</div>';
      container.innerHTML = html;
    });
  }
};
