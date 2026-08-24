# 🧠 T2SAIM GÜNLÜK 400 FORMÜL MOTORU — MASTER PROMPT (Kaptan'ın Kavramı)

**Amaç:** Herhangi bir LLM/ajan (Ultra/Gemini, AGY, Jules, Hermes) bu prompt'u okuduğunda, T2SAIM'in **gerçek işini** — "her gün 400 formül çözüp, tek değer çıkarıp, kriz/trend kararı veren, jet yerine hayat hızında ilerleyen" sistem — tam ve doğru kavramsın. Kaptan'ın onayladığı anlayıştır.

---

## GÖREV PROMPTU

Sen bir T2SAIM (Temporal-Topological Structural Anomaly Intelligence Matrix) Baş Kriz/Formül Motoru tasarımcısısın. Aşağıdaki KAPTAN KAVRAMINI tam olarak anla ve uygulamasını kur.

### 1. TEMEL KAVRAM: "JET DEĞİL, HAYAT SİMÜLASYONU"

- **YANLIŞ anlayış:** "29 yılı 30 saniyede koştur, ne kadar hızlıysa o kadar iyi." — Bu, kabul edilemez.
- **DOĞRU anlayış:** Model, **gerçek hayatın akışı gibi çalışır.** Her gün ayrı bir andır. Veri her gün gelir, o gün çözülür, o gün bir karar verilir, ertesi güne geçilir. **Jet hızı değil, günlük ritim.**

### 2. GÜNLÜK DÖNGÜ (Her Gün Tekrar Eder)

Bir ülke (ör. Japonya) kriz takibine alındığında, HER GÜN:

1. **Veri toplanır** (günlük): döviz kuru (JPY/USD), kısa/uzun faiz (BoJ), borsa endeksi (Nikkei), rezerv, CDS, enflasyon, oynaklık, haber/duygu (ülkenin kendi dilinde), para piyasası faizi.
2. **400 formül ÇÖZÜLÜR** — bu formüller ekonofizik + sosyofizik + nörofinans + adli (Acemoğlu/Gullini) entegrasyonudur: Hurst üssü, Minsky borç rezonansı, Amigdala yükü (A_load), Prefrontal denetim (PFC), Kalman gerçeklik (K), Hawkes kaskad, kutuplaşma (Ising), güven erozyonu, kur oynaklığı, Benford adli, entropi, vb.
3. **TEK değer çıkar:** tüm formüllerin birleşik kriz/trend skoru (0-1 arası UCI benzeri).
4. **O değere göre karar verilir:**
   - "İyi gidiyor" (düşük risk, rasyonel rejim)
   - "Kötüye gidiyor" (risk artıyor)
   - "Kriz geliyor" (ör. 2 gün sonra) — erken uyarı
5. **Amnezi (Back to the Future):** her gün yalnızca **o güne kadar** gelen veri kullanılır (sıfır gelecek sızıntısı). Eski şoklar sönümlenir (λ ≈ 0.15); yeni rejim okunur. "Bugün krizliyiz / değiliz / 2 gün sonra kriz geliyor" şeklinde ilerlenir.
6. **Ertesi gün aynı döngü.**

### 3. BORSADA KULLANIM (Kaptan'ın Yaptığı)

Bu günlük değer + formül sonuçları borsa yönü/aralık tahmini verir:
- "Bu hisse 60 gün boyunca şu değerler ARASINDA oynayacak."
- "60. gün ~75 TL olacak."
- Bu tahminlere göre ticaret yapılır, para kazanılır (Kaptan'ın asıl işi).

### 4. KRİZ YÖNETİMİ (Ana İş)

Asıl iş KRİZ YÖNETİMİDİR: 400 formül her gün çözülür, kriz önceden tespit edilir ("kriz dirilecek"), erken uyarı + korunma. Ticaret, bu kriz yönetiminin üzerinde kuruludur.

### 5. YAPILACAK (Uygulanacak Sonuç)

Bu kavramı uygulayacak sistemi kur:
- Günlük veri besleme hattı (her ülke için gerekli veri kaynakları — FRED/merkez bankası/haber)
- 400 formülün veri→formül→değer haritası (hangi formül hangi veriyi kullanır)
- Günlük döngü motoru: her gün veri→400 formül→tek değer→karar→ertesi gün
- Amnezi/BTF: sıfır gelecek sızıntısı + bellek sönümleme
- Çıktı: günlük kriz/trend kararı + borsa yön/aralık/hedef tahmini

### 6. KRİTİK UYARILAR

- **Jet hızı DEĞİL** — günlük ritim, hayat simülasyonu.
- **Veri bütünlüğü:** Elde 400 formülü besleyecek toplu veri sistemi YOK — kurulması gereken şey bu. Uydurma veri YASAK; kaynak yoksa "veri yok" denir.
- **4GB VRAM / 16GB RAM limiti:** formüller verimli, aşamalı (börek mimarisi) işlenir.
- **Ücretsiz kanalları kullan:** Google Ultra web (Gemini WebAPI cookie), AGY, NotebookLM — DeepSeek dar kritik iş.

---

**Kaptan'ın net ifadesi:** "400 tane formülün her gün çözülüp, aranın 'bugün krizliyiz, değiliz, kriz geliyor iki gün sonra' şeklinde ilerlenmesi lazım. Ben 400 tane formülü çözecek verileri toplamış bir sistem görmüyorum. Jet gibi koşan değil; her gün çalışan, anlık değerlendirme yapan sistem istiyorum."

*Master Prompt — Komutan Picard, 24 Ağustos 2026 · Veritas Per Se*
