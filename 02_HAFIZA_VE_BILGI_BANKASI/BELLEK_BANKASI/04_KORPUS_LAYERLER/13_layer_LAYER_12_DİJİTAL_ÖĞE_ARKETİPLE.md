# LAYER 12: DİJİTAL ÖĞE ARKETİPLERİ, İNANÇ REJİMİ & CİNSİYET TAHAKKÜMÜ (BRP & GV)

## 12A: MİMARİ — DİJİTAL ÖĞE NEDİR?

### 12A.1 Tanım

Dijital Öğe (DO), hedef ülke/bölge toplumunun antropolojik, sosyolojik, psikiyatrik ve psikanalitik verilerine dayanarak oluşturulan parametreli insan modeli ajanıdır. Bu ajanlar öğrenen modellerdir: simülasyon boyunca kendi parametrelerini günceller, çevresel sinyallere tepki verir ve diğer ajanlarla etkileşime girer.

```
Dijital Öğe = f(
  Antropolojik_prior,      ← Kültürel şema, kolektif bellek, kimlik yapısı
  Sosyolojik_ağ,           ← Sınıf konumu, cemaat bağı, ağ merkezi
  Psikiyatrik_profil,      ← Temel kaygı, savunma mekanizmaları
  Psikanalitik_katman,     ← İdoktrinizasyon, süperego yapısı, bağlanma biçimi
  CBC_parametreleri,       ← MBP/ICF/NRG/SDP/EBP/CCP bağlamı
  BRP_katmanı,             ← İnanç rejimi baskısı katsayıları
  GV_kanalı,               ← Toplumsal cinsiyet normu baskısı
  WVS_arketip              ← TRA/CRT/ANX/RES temel davranış şeması
)
```

### 12A.2 Simülasyon Mantığı

```
Her zaman adımı t'de:

1. ÇEVRE GÜNCELLEME:
   CBC_t, SRI_t, EFMI_t → dışsal bağlam vektörü

2. AJAN ALGILAMA:
   DO_i.perceive(CBC_t, medya_t, ağ_sinyalleri_t)
   → bireysel algı = ajan_prior × (1 − BRP_kapanma) + çevre_sinyal × BRP_kapanma

3. İNANÇ GÜNCELLEMESİ (Bayesian + Ising):
   belief_i(t+1) = Bayesian_update(belief_i(t), yeni_kanıt, BRP_ağırlığı)
   uyum_i(t+1) = Ising_step(s_i, komşular, h_i_efektif)

4. DAVRANIŞSAL ÇIKTI:
   exit_prob_i = f(EBP_bağlam, ekonomik_stres, ajan_resilience)
   voice_prob_i = f(SDP_bağlam, CRT_oranı, epistemic_closure)
   loyalty_prob_i = 1 − exit_prob_i − voice_prob_i

5. ÖĞRENME GÜNCELLEMESİ (RL):
   R_i(t) = ödül_sinyali (ekonomik çıktı, sosyal onay, güvenlik)
   Q_parametreleri_güncelle → sonraki t için davranış eğrisi güncellenir

6. MAKRO AGGREGASYON:
   Toplam_tepki(t) = Σ_i [DO_i.davranış × DO_i.arketip_payı]
   → SRI_psy_tahmini, protest_potential, emigration_signal
```

---

## 12B: CBC PARAMETRELERİ × DİJİTAL ÖĞE BAĞLANTISI

Her CBC bileşeni Dijital Öğe'nin dışsal bağlamını belirler:

```
CBC-01 MBP → DO ekonomik stres girdisi:
  Yüksek MBP → ANX arketip exit_prob artar
              → TRA arketip "ekonomik tevekkül" uyum büyür
              → CRT arketip sistematik itiraz arar

CBC-02 ICF → DO kurumsal güven girişi:
  Yüksek ICF → tüm arketipler authority_deference günceller (negatif)
              → CRT için: voice_prob artar
              → TRA için: inanç-yetki transferi (dini/lidere)

CBC-03 NRG → DO bilgi kalitesi filtresi:
  Yüksek NRG → TRA arketip resmi anlatıyı kabul oranı yüksek kalır
              → ANX arketip belirsizlik altında anlatıya sığınır
              → CRT arketip bağımsız kaynak arama davranışı artar

CBC-04 SDP → DO sosyal baskı tepkisi:
  Yüksek SDP → konformite baskısı; DO_i.uyum şiddetlenir
              → Milgram etkisi: otorite + sosyal baskı → itaat amplifikasyonu
              → BRP ile etkileşim: yüksek BRP → SDP amplifikasyonu

CBC-05 EBP → DO kaçış davranışı:
  Yüksek EBP → tüm arketipler exit_prob baskısı alır
              → RES arketip kaçış vs. adaptasyon hesabı yapar
              → CRT arketip yüksek EBP'de emigrasyon seçer

CBC-06 CCP → DO bulaşma hassasiyeti:
  Yüksek CCP → ANX arketip sürü davranışına geçer
              → Deffuant ε düşer (kutuplaşma artar)
              → TRA arketip cemaat içi konsolidasyon
```

---

## 12C: BRP — İNANÇ REJİMİ BASINCI (F1-F10 TAM DETAY)

> **⛔ Etik Bayrak:** Kullanılacak şey: "TR 2021-2023 döneminde belief_regime_rigidity yüksek"  
> Kullanılmayacak şey: "şu kişi/şu grup şu dine ait olduğu için risklidir"  
> Analiz birimi: ülke, dönem, rejim yapısı — asla birey veya cemaat.

```
BRP_t = 0.18 × F1 + 0.12 × F2 + 0.12 × F3 + 0.12 × F4 + 0.11 × F5
      + 0.10 × F6 + 0.10 × F7 + 0.08 × F8 + 0.07 × F9
```

### F1: belief_regime_rigidity (ağırlık 0.18)

```
Tanım: İnanç sisteminin kendi içinde sorgulamaya ne kadar kapalı olduğu
Ölçüm: Heterodoks dini yorumların kovuşturulma oranı + inanç değişimi ceza riski
Proxy: USCIRF raporları; Freedom House din özgürlüğü skoru; V-Dem
Türkiye 2023: F1 ≈ 0.55
DO etkisi: Artan F1 → TRA arketip epistemic_closure artar; CRT arketip baskılanır
```

### F2: doctrinal_centralization (ağırlık 0.12)

```
Tanım: Dini yorumun tek otorite (devlet kurumu) üzerinden yürütülmesi
Ölçüm: Diyanet İşleri'nin kapsam ve bütçe büyümesi + alternatif dini yapı yasallığı
Proxy: Diyanet bütçesi/GSYİH + cami yoğunluğu / mezhep çeşitliliği endeksi
Türkiye: F2 ≈ 0.70 (Diyanet monopolü yüksek)
```

### F3: authority_sanctification (ağırlık 0.12)

```
Tanım: Siyasi otorite ile dini meşruiyetin birbirine kayması
Ölçüm: Dini lider → siyasi destek beyanları frekansı
       + Devlet söyleminde "İslami/ulusal kader" referansları
Proxy: NLP → hutbe/resmi söylem analizi; EFMI S_t bileşeni
DO etkisi: Yüksek F3 → TRA arketip "lider=kutsal emanet" çerçevesi
```

### F4: dissent_cost (ağırlık 0.12)

```
Tanım: İnanç/yorum farklılığı için sosyal/ekonomik/hukuki bedel
Ölçüm: Blasphemy yasası uygulamaları + sosyal baskı raporları
Proxy: RSF basın özgürlüğü + V-Dem freedom_of_expression
DO etkisi: Yüksek F4 → CRT arketip voice_prob azalır; ANX'nin panik skoru artar
```

### F5: epistemic_closure (ağırlık 0.11)

```
Tanım: Alternatif bilgi kaynaklarına sistemik erişim engeli
Ölçüm: İnternet engelleme (NetBlocks Turkey endeksi) + VPN kullanım oranı
       + Bağımsız medya kısıtlama sayısı
Proxy: Freedom on the Net; RSF; V-Dem
DO Bilgi Filtresi:
  DO_i.info_kalitesi = 1 − epistemic_closure × (1 − arketip_bağımsız_arama)
Türkiye 2023: F5 ≈ 0.65
```

### F6: ritual_morality_substitution (ağırlık 0.10)

```
Tanım: Etik yargının somut çıktılar yerine ritüel uyuma (ibadet biçimi) göre yapılması
Ölçüm: "Dini davranış = ahlaki değer" anlatı yoğunluğu (NLP)
Proxy: WVS V105 × WVS V45 (dini pratik × hukuk eşitsizliği tolere etme)
DO etkisi: Yüksek F6 → TRA arketip EFMI farkındalığı düşük kalır
```

### F7: female_exclusion_pressure (ağırlık 0.10)

```
Tanım: Dini/ahlaki çerçevede kadın karar alma özerkliğinin kısıtlanması
Ölçüm: WEF GGI + kadın parlamenter/kabineteki oran + özel alana çekilme baskısı
Proxy: WEF GGR; CEVRI/kadın hakları endeksleri
DO etkisi: Yüksek F7 → kadın arketip ajanların exit_prob artışı;
           GV_kanalıyla doğrudan bağlantı (GV4 female_bodily_autonomy_suppression)
```

### F8: outgroup_hostility_load (ağırlık 0.08)

```
Tanım: Dini/milli kimliğin dışgrup (Batı, Hristiyan, Yahudi, ateist) düşmanlığıyla
       desteklenmesi
Ölçüm: Medyada düşman-kimlik söylemi frekansı (NLP); Coxall T-03 şablon match skoru
Proxy: WVS V39 (dışgrup güvensizlik) + scapegoat_index
DO etkisi: Yüksek F8 → Deffuant ε düşer (kutuplaşma); Coxall Scapegoating aktif
```

### F9: sectarian_fragmentation_risk (ağırlık 0.07)

```
Tanım: Mezhep/cemaat ayrışmasının sosyal kırılma yaratan çatışma potansiyeli
Ölçüm: Cemaat çatışması olayları + sektarian kutuplaşma endeksi
Proxy: ACLED sektarian şiddet verisi; V-Dem social_cleavages
DO etkisi: Yüksek F9 → Ajan arası cemaat grupları oluşur; Deffuant alt-küme dinamiği
```

### F10: salvation_over_rules_bias (ağırlık — BRP gövdesi dışında; SDP'ye eklenti)

```
Tanım: Kurallar/hukuk yerine kişisel kurtuluş/ahiret beklentisinin tercih edilmesi
Ölçüm: WVS kurumsal hukuk güveni vs. dini otorite güveni farkı
Proxy: WVS V114 (parlamento güveni) vs. V145 (dini lider etkisi)
DO etkisi: Yüksek F10 → TRA arketip hukuk yoluna başvurmaz → ICF erozyon hızlanır
```

---

## 12D: GV KANALI — TOPLUMSAL CİNSİYET ŞİDDETİ KATMANI

> **⛔ Etik Bayrak:** Bu katman insan hakları ve toplumsal adalet ihlallerini tespit amacıyla
> tasarlanmıştır. Hiçbir şekilde mağdurları tanımlamak ya da hedeflemek için kullanılamaz.
> "HOW NOT WHO" ilkesi burada özellikle kritiktir.

### 12D.1 GV1-GV7 Özellikleri

```
GV1: femicide_rate_pressure
  Tanım: Kadın cinayetinin sistematik toplumsal baskı ve normalleşme bağlamı
  Ölçüm: Femisid oranı / intihar sınıflandırma anomalisi / basın haberi baskılama
  Proxy: UN Women istatistikleri; Kadın Cinayetlerini Durduracağız veritabanı
  DO etkisi: Yüksek GV1 → ANX kadın arketipler exit_prob maksimum
             → SDP + Hoffer H boyutu amplifikasyonu

GV2: honor_norm_justification_load
  Tanım: "Namus" söylemiyle şiddetin sosyal meşrulaştırılması
  Ölçüm: Mahkeme kararlarında töre/namus savunması kullanım oranı
         + medyada sempati-söylemi NLP analizi
  Proxy: Toplumsal Cinsiyet Eşitliği izleme raporları (CEDAW UPR)
  DO etkisi: Yüksek GV2 → F3 (authority_sanctification) ile birleşince
             toplumsal onaylama döngüsü → SDP amplifikasyonu

GV3: religious_moral_legitimation_score
  Tanım: Dini argümanla cinsiyet şiddetinin meşrulaştırılması
  Ölçüm: Dini yetkililerden gelen normalize edici söylem frekansı (NLP)
  Proxy: BRP F6 (ritual_morality_substitution) ile yüksek korelasyon
  DO etkisi: Yüksek GV3 → TRA arketip GV olaylarına müdahale etmez

GV4: female_bodily_autonomy_suppression
  Tanım: Bedene yönelik yasal/sosyal/dini kontrol mekanizmaları
  Ölçüm: Kürtaj kısıtlaması endeksi + evlilik yaşı yasal alt sınırı
         + kıyafet zorunluluğu endikatorleri
  Proxy: WEF GGR; F7 (female_exclusion_pressure) ile bağlantılı
  DO etkisi: Kadın arketip ajanların autonomy_score azalır → exit_prob artar
             veya içe kapanma (loyalty by suppression)

GV5: sexual_slavery_atrocity_signal
  Tanım: Örgütlü cinsel şiddet/kölelik örüntülerinin varlık sinyali
  Ölçüm: İnsan ticareti raporları (IOM/ILO); organized crime × seksüel şiddet verisi
  Proxy: UNODC trafficking in persons report; Veritas Ajan 01 → UNVERIFIED bayrağı gerekir
  DO etkisi: Aşırı yüksek GV5 → sistem düzeyinde normalleşme riski → Hoffer H boyutu

GV6: impunity_underclassification_score
  Tanım: GV olaylarının cezasız kalması / cinayet olarak değil "intihar" vs. kayıt sapması
  Ölçüm: Adli tıp kurumu istatistikleri vs. NGO belgeleme karşılaştırması
  Proxy: GREVIO (Türkiye değerlendirmesi); COE izleme raporları
  DO etkisi: Yüksek GV6 → NRG'ye (Anlatı-Gerçeklik Sapması) eklenti
             → CBC-03 aktif olma eşiği düşer

GV7: border_escape_safe_haven_risk
  Tanım: GV'den kaçmak isteyen bireylerin sığınak bulamaması
  Ölçüm: Sığınmaevi kapasite endeksi + sınır geçiş erişim kısıtı
  Proxy: GREVIO; UNHCR sığınmacı profil verisi
  DO etkisi: Yüksek GV7 → ANX ve RES kadın arketip exit_prob yüksek ama
             exit_capacity düşük → psikolojik çıkmaz → SRI_psy artışı
```

### 12D.2 GV Bileşik İndeks

```
GV_composite = 0.20 × GV1 + 0.18 × GV2 + 0.15 × GV3 + 0.15 × GV4
             + 0.12 × GV5 + 0.12 × GV6 + 0.08 × GV7

GV Alarm Eşiği: GV_composite > 0.60 → Hoffer H boyutu = yüksek
                GV_composite > 0.70 → SDP_t += 0.08 (doğrudan eklenti)

Türkiye 2023 tahmini: GV_composite ≈ 0.62
```

### 12D.3 BRP × GV Çapraz Etkileşim

```
BRP_t yüksek VE GV_composite yüksek → SDP amplifikasyonu maksimum:
  SDP_amplified = SDP_t × (1 + 0.30 × BRP_t × GV_composite)

BRP_t yüksek VE GV6 yüksek (cezasızlık) → NRG artar:
  NRG_t += 0.05 × GV6 × (1 − ICF_score)
```

---

## 12E: BEŞ DİJİTAL ÖĞE ARKETİPİ

### 12E.1 Arketip 1 — GELENEKSELci/İTAAT EDEN (TRA)

```
WVS Payı: %38 (Türkiye 2018 WVS Dalga 7 uyumlu)

ANTROPOLOJİK KALİBRASYON:
  Kimlik yapısı:     Kolektif kimlik > bireysel kimlik
  Değerler skalası:  Aile > cemaat > ulusal kimlik > bireysel hak
  Kültürel bellek:   Osmanlı mirasına pozitif atıf; Batı modernleşmesine çelişkili
  Hofstede:          Yüksek güç mesafesi (PDI=66) + düşük bireysellik (IDV=37)

SOSYOLOJİK KALİBRASYON:
  Ağ konumu:         Cemaat/mahalle merkezli; homofil ağ (yüksek BRP ortamı)
  Sınıf:             Düşük-orta gelir; tarımsal köken veya ilk kuşak kentli
  Eğitim:            Ortalama 8-10 yıl; imam hatip veya mesleki
  Siyasi katılım:    Düşük - orta; oy kullanır ama kritik takip etmez

PSİKİYATRİK PROFİL:
  Temel kaygı:       Statü kaybı, cemaatten dışlanma, sosyal onaysızlık
  Savunma mekan.:    Rasyonalizasyon + inkar (yüksek NRG ortamında)
  Stres tepkisi:     Gruba yaklaşma, otoriteye biat artışı
  psychological_strain (psychosocial_panel): 0.42 (orta; baskı altında artar)

PSİKANALİTİK/İNDOKTRİNASYON KATMANI:
  Süperego yapısı:   Dini-otoriter çerçeveli; "doğru-yanlış" kesin sınır
  Bağlanma biçimi:   Kaygılı-saplantılı (cemaatle; otoriteyle)
  Indoktrinasyon:    Erken yaşta dini eğitim + aile-cemaat pekiştirmesi
  BRP uyumu:         0.90 (yüksek F3 authority_sanctification + F6 uyumu)

PARAMETRE TABLOSU:
  conformity_pressure:          0.85
  critical_thinking_strain:     0.18 (düşük eleştirel)
  authority_dependence:         0.82
  uncertainty_avoidance:        0.80 (UAI yüksek)
  psychological_strain_base:    0.42
  propaganda_susceptibility:    0.72
  crisis_resilience:            0.55 (cemaat desteğiyle orta)
  reform_latency_years:         5.2 (davranış değişimi yavaş)
  BRP_alignment:                0.90
  EFMI_awareness:               0.15

KRİZ DÖNEMLERINDE DAVRANIŞSAL ÇIKTI:
  Yüksek MBP (ekonomik stres):  → uyum artar ("Allah büyük")
  Yüksek NRG (söylem-gerçeklik makası): → resmi anlatı tercih edilir
  Yüksek SDP (sosyal baskı):    → konformite maksimum
  Yüksek EBP:                   → göç son seçenek; önce cemaat dayanışması
  exit_prob (yüksek stres):     0.12
  voice_prob (yüksek stres):    0.08
  loyalty_prob (yüksek stres):  0.80
```

### 12E.2 Arketip 2 — ELEŞTİREL DÜŞÜNEN (CRT)

```
WVS Payı: %22

ANTROPOLOJİK KALİBRASYON:
  Kimlik yapısı:     Bireysel kimlik ön planda; çoğulcu kimlik mümkün
  Değerler:          Özgürlük, bilgi erişimi, kurumsal hesap verebilirlik
  Kültürel bellek:   Erken Cumhuriyet reformlarına pozitif; modernleşme projesine yatırım
  Hofstede:          Düşük güç mesafesi eğilimi; yüksek bireysellik (alt-grup)

SOSYOLOJİK KALİBRASYON:
  Ağ:               Heterojen; bağımsız medya, sivil toplum, meslek örgütleri
  Sınıf:            Orta-üst orta; yüksek eğitimli
  Eğitim:           14+ yıl; üniversite (çoğunlukla büyük şehir)
  Siyasi katılım:   Yüksek; eleştirel medya takibi

PSİKİYATRİK PROFİL:
  Temel kaygı:       Kurumsal yozlaşma, özgürlük kaybı, kriz sonrası ülke geleceği
  Savunma mekan.:    Entelektüelleştirme + eylem (sivil katılım, haber üretimi)
  Stres tepkisi:     Kriz dönemlerinde örgütlenme veya emigrasyon
  psychological_strain (psychosocial_panel): 0.35 (daha az; ama moral tükenme riski)

PSİKANALİTİK KATMAN:
  Süperego:          Hukuki-etik çerçeve; rasyonalist
  Bağlanma:          Güvenli-özerk veya kaçınmacı (kurumsal güvensizlik nedeniyle)
  Indoktrinasyon:    Düşük BRP; laik/rasyonalist çevre pekiştirmesi
  BRP uyumu:         0.20

PARAMETRE TABLOSU:
  conformity_pressure:          0.25
  critical_thinking_strain:     0.82
  authority_dependence:         0.22
  uncertainty_avoidance:        0.30 (belirsizliğe toleranslı)
  psychological_strain_base:    0.35
  propaganda_susceptibility:    0.18
  crisis_resilience:            0.75
  reform_latency_years:         1.5 (hızlı adaptasyon)
  EFMI_awareness:               0.85
  BRP_alignment:                0.20

KRİZ DÖNEMLERINDE:
  Yüksek NRG:    → bağımsız kaynak arama maksimum; T-02 tespiti
  Yüksek SDP:    → voice_prob artar; protesto/sivil eylem veya emigrasyon
  Yüksek EBP:    → emigrasyon "beyin göçü" kanalı aktivasyonu
  exit_prob (yüksek stres): 0.40 (emigrasyon; en yüksek arketip)
  voice_prob:   0.45
  loyalty_prob: 0.15
```

### 12E.3 Arketip 3 — KAYGILI/KIRILGAN (ANX)

```
WVS Payı: %20

ANTROPOLOJİK KALİBRASYON:
  Kimlik yapısı:     Belirsiz; kimlik istikrarsız, dışsal onay bağımlı
  Değerler:          Güvenlik, istikrar, ekonomik koruma
  Kültürel bellek:   Kriz dönemlerinden travmatik iz; "1994 krizi sarsıntısı" kuşakları

SOSYOLOJİK KALİBRASYON:
  Ağ:               Zayıf; kırılgan sosyal ağlar; destek sistemi yetersiz
  Sınıf:            Alt-orta; ekonomik güvencesizlik yüksek
  İstihdam:         Kayıt dışı veya geçici; ekonomik şoka açık

PSİKİYATRİK PROFİL:
  Tanı profili proxy: Yaygın kaygı bozukluğu örüntüsü (DSM-5 referanslı, TOPLUMSAL düzey)
  Temel kaygı:       Varlık güvencesi, ekonomik çöküş, aile güvenliği
  Savunma mekan.:    Panik → gruba katılım → hızlı görüş değişimi
  Stres tepkisi:     Sürü davranışı; ani karar değişimi; yüksek manipülasyon hassasiyeti
  psychological_strain (psychosocial_panel): 0.78 (en yüksek)
  crisis_resilience: 0.25 (en düşük)

PSİKANALİTİK KATMAN:
  Süperego:          Zayıf iç tutarlılık; değerler duruma göre kayar
  Bağlanma biçimi:   Kaygılı-saplantılı veya dezorganize
  Indoktrinasyon:    Yüksek risk; hem BRP hem anti-BRP mesajlara açık
  BRP uyumu:         0.55 (değişken; kriz stresinde BRP'ye yaklaşır)

PARAMETRE TABLOSU:
  conformity_pressure:          0.72
  critical_thinking_strain:     0.28
  authority_dependence:         0.65 (kriz döneminde artar)
  uncertainty_avoidance:        0.88 (en yüksek)
  psychological_strain_base:    0.78
  propaganda_susceptibility:    0.75 (en yüksek)
  crisis_resilience:            0.25
  reform_latency_years:         3.8

KRİZ DÖNEMINDE:
  "Swing agent" role: ANX arketip kritik; kriz döneminde TRA veya CRT'ye
  yaklaşma (Coxall: Swing Agent Reassurance mekanizması)
  exit_prob:    0.25 (kaçmak ister ama exit_capacity düşük)
  voice_prob:   0.12
  loyalty_prob: 0.63 (pasif biat; kayıtsız)
```

### 12E.4 Arketip 4 — DAYANIKLI/PRAGMATİST (RES)

```
WVS Payı: %20

ANTROPOLOJİK KALİBRASYON:
  Kimlik:       Pragmatik; hem geleneksel hem modern öğeler; hibrid
  Değerler:     Pratik çözüm, ekonomik başarı, aile güvencesi
  Kültürel bellek: Adaptasyon kapasitesi yüksek; "her krizden çıktık" motivasyonu

SOSYOLOJİK KALİBRASYON:
  Ağ:           Çeşitli; hem BRP hemde laik ağlarda ilişki
  Sınıf:        Orta; küçük işletmeci, serbest meslek
  İstihdam:     Özel sektör; kendi kendine yeterli veya mikro girişimci

PSİKİYATRİK PROFİL:
  Temel kaygı:  Orta; odak ekonomik fırsatlar ve aile güvencesi
  Savunma:      Akıl yürütme + pratik eylem; korku değil hesap
  Stres:        Kriz döneminde yeni fırsat arar (arbitraj zihniyeti)
  psychological_strain (psychosocial_panel): 0.30 (en düşük)

PSİKANALİTİK KATMAN:
  Süperego:     Pragmatik-etik; sonuca göre; sabit değil
  Bağlanma:     Güvenli-özerk
  BRP uyumu:    0.45 (araçsal; gerektiğinde BRP söylemini kullanır)
  EFMI_awareness: 0.60 (makasın farkında; adapte eder)

PARAMETRE TABLOSU:
  conformity_pressure:      0.40
  crisis_resilience:        0.90 (en yüksek)
  authority_dependence:     0.38
  propaganda_susceptibility: 0.35
  adaptasyon_hızı:           0.85

KRİZ DÖNEMINDE:
  exit_prob:    0.30 (alternatif piyasa/ülke araması)
  voice_prob:   0.25 (sistem içi müzakere)
  loyalty_prob: 0.45 (pragmatik biat; fırsat gidince biat da gider)
```

### 12E.5 Arketip 5 — MARJİNAL/DIŞLANAN (MAR) [Opsiyonel Beşinci Öğe]

```
WVS Payı: ~%5-10 (yapısal dışlanma nedeniyle WVS altında temsil edilebilir)

Tanım: Ekonomik, etnik, mezhepsel veya cinsiyet temelli yapısal dışlanmayı yaşayan
       segment. GV kanalı ve BRP F7+F8+F9 ile en doğrudan bağlantılı.

PARAMETRE TABLOSU:
  conformity_pressure:      0.30 (dışlanmışlık uyumu zorlaştırır)
  crisis_resilience:        0.20 (en düşük; destek ağı yok)
  authority_dependence:     0.20 (otorite güvene değmez)
  propaganda_susceptibility: 0.50 (hem resmi hem karşı-söyleme açık)
  exit_prob:    0.55 (en yüksek; fırsatı olan kaçar)
  voice_prob:   0.10 (ses çıkarmanın bedeli yüksek)
  loyalty_prob: 0.35

CBC Bağlantısı:
  GV_composite > 0.65 → MAR arketip boyutu büyür
  BRP F7+F8+F9 yüksek → MAR'ın exit_capacity azalır (kaçmak ister ama kanallar kapalı)

⛔ Etik Bayrak: MAR arketipi hiçbir zaman etnik/dini/cinsiyet kimliğiyle
etiketlenmez. Yalnızca yapısal dışlanma örüntüsü olarak tanımlanır.
```

---

## 12F: ÖĞRENEN MODEL MATEMATİĞİ

### 12F.1 Bayesian İnanç Güncelleme

```
Her t adımında ajan i'nin inanç vektörü:

belief_i(t+1) = α × likelihood(kanıt_t | belief_i(t)) × belief_i(t)
              + (1 − α) × BRP_prior_i

Burada:
  α = BRP_kapanma_ağırlığı (yüksek F5 epistemic_closure → düşük α → prior baskın)
  likelihood = yeni bilginin inanç ile uyumu
  BRP_prior_i = arketipin BRP uyumuyla şekillenmiş a priori

Basitleştirilmiş form (sayısal implementasyon):
  belief_i(t+1) = belief_i(t) + η_B × (kanıt_t − belief_i(t)) × (1 − F5_i)

  η_B: öğrenme hızı (TRA için 0.05; CRT için 0.25; ANX için 0.15; RES için 0.20)
  F5_i: bireysel epistemic_closure (F5 feature'dan türetilir)
```

### 12F.2 Dinamik Arketip Pay Evrimi

```
Arketip payları sabit değildir; toplumsal baskıya göre kayar:

φ_TRA(t+1) = φ_TRA(t) × exp(+λ_TRA × SDP_t × BRP_t)
φ_CRT(t+1) = φ_CRT(t) × exp(−λ_CRT × SDP_t) × exp(+λ_emigr × EBP_t)
φ_ANX(t+1) = φ_ANX(t) × exp(+λ_ANX × δ_economic_shock)
φ_RES(t+1) = φ_RES(t) [nispeten stabil; dışsal şoktan az etkilenir]

Normalleştirme:
  φ_TRA + φ_CRT + φ_ANX + φ_RES = 1.0 (her t'de)

Türkiye 2022 kriz simülasyonu (başlangıç: WVS 2018 payları):
  φ_TRA: 0.38 → 0.44 (+6% konsolidasyon)
  φ_CRT: 0.22 → 0.16 (−6% emigrasyon/susturulma)
  φ_ANX: 0.20 → 0.24 (+4% ekonomik şok)
  φ_RES: 0.20 → 0.16 (−4% adaptasyon sınırı aşıldı)
```

### 12F.3 Pekiştirmeli Öğrenme (Q-Learning) Davranış Katmanı

```
Her ajan i, EBP/SDP ortamında davranış seçer:
  Eylemler: A = {exit, voice, loyalty, adapt}

Q_i(s, a) ← Q_i(s, a) + η_Q × [R(s,a) + γ × max_{a'} Q_i(s', a') − Q_i(s,a)]

Ödül fonksiyonu R(s, a):
  R(exit):    ekonomik_güvenlik × (1 − exit_cost)
  R(voice):   (1 − SDP_t) × sosyal_onay_kazanım
  R(loyalty): ekonomik_teşvik_t + BRP_t × sosyal_güvenlik
  R(adapt):   RES_ağırlıklı; Δ_ekonomik_fırsat

Parametreler:
  η_Q = 0.10 (öğrenme hızı; sabit)
  γ = 0.90 (gelecek indirim faktörü; uzun vadeli düşünen)
  Episod: 12 aylık simülasyon adımı
```

### 12F.4 Ağ Etkileşim Matrisi

```
N ajan × N ajan ağırlık matrisi W:
  W_ij = 0 eğer i ve j aynı Deffuant hoşgörü ε içinde değilse
  W_ij > 0 eğer |opinion_i − opinion_j| < ε

Güncelleme:
  W_ij her simülasyon adımında yeniden hesaplanır (adaptif ağ)
  Arketip aynı → W_ij yüksek (cemaat içi echo chamber)
  Arketip farklı → W_ij düşük (kutuplaşma; Deffuant ε = 0.18 Türkiye)

Makro çıktı:
  ağ_kutuplaşma = 1 − ortalama_W_cross_arketip
  Türkiye 2022 simülasyonu: ağ_kutuplaşma ≈ 0.78 (çok yüksek)
```

---

## 12G: SİMÜLASYON MİMARİSİ

### 12G.1 Simülasyon Genel Akışı

```
BAŞLANGIÇ (t=0):
  1. Ülke/dönem seç (örn: Türkiye 2021-2024)
  2. CBC vektörünü başlat (MBP, ICF, NRG, SDP, EBP, CCP) → tarihsel değerler
  3. 5 arketip payını WVS'ten başlat
  4. BRP_t = F1-F9 ağırlıklı sum → başlangıç BRP
  5. GV_composite başlat
  6. N ajan oluştur (örn: N=10000); arketip = başlangıç paylarına göre örnekle
  7. Her ajan: parametreler = arketip tablosundan ± Gaussian gürültü (σ=0.05)

HER t ADIMI:
  1. Dışsal güncelleme: CBC_t yeni değerleri (EVDS/BDDK/WJP veri akışı)
  2. BRP_t ve GV_composite güncelle (mevcut veriyle)
  3. Her ajan: perceive → belief_update (Bayesian) → action_select (Q-learning)
  4. Ajan çiftleri: Deffuant güven difüzyonu
  5. Ising uyum: toplumsal konformite güncellemesi
  6. RPE hesapla: ekonomik beklenti vs. gerçekleşen
  7. Arketip pay evrimi: φ dinamik güncelleme
  8. Makro aggregasyon: SRI_psy_sim, protest_potential, emigration_signal

ÇIKTI (her t):
  - SRI_psy_simulated(t)
  - Aggregate exit_prob, voice_prob, loyalty_prob
  - Ağ kutuplaşma endeksi
  - Tevekkül kırılma olasılığı
  - CRISIS_HAZARD katkısı (SDP güncelleme için)
```

### 12G.2 Simülasyon Doğrulama Kriterleri

```
Simülasyon çıktısı kabul edilebilir IF:
  1. SRI_psy_simulated, BTF walk-forward SRI_psy ile ±0.10 band içinde
  2. Arketip pay evrimi WVS trend verisiyle uyumlu (1990-2018 dalgaları)
  3. 2018 ve 2022 kriz dönemlerinde tevekkül_kırıldı = 1 tespit edilmeli
  4. CRT arketip emigrasyon sinyali 2020+ için artan eğilim göstermeli
     (pasaport başvuruları gerçek verisiyle kıyasla)

Kalibrasyon:
  Hata fonksiyonu: RMSE(SRI_psy_sim, SRI_psy_BTF) < 0.08
  Optimize edilecek: η_B, ağırlık matrisi W başlangıç değerleri, φ_λ parametreleri
```

### 12G.3 Simülasyon Çıktı Formatı

```
Çıktı dosyası: do_simulation_output_YYYYMMDD.json

{
  "ülke": "TR",
  "dönem": "2021-01 → 2024-12",
  "arketip_paylari_son": { "TRA": 0.44, "CRT": 0.16, "ANX": 0.24, "RES": 0.16, "MAR": 0.00 },
  "SRI_psy_sim": [serisi],
  "tevekkül_kırılma_tarihleri": ["2021-11", "2022-06"],
  "protest_potential_peak": { "tarih": "2023-05", "değer": 0.62 },
  "emigration_signal": [serisi],
  "ağ_kutuplaşma_son": 0.78,
  "L6_sim_kilit": ["2021-10", "2022-01", "2022-09", "2023-04"],
  "epistemik_not": "Tüm DO çıktıları ülke düzeyi tahmindir; birey atfı içermez"
}
```

---

## 12H: VERİ PANEL REFERANSLARı

Aşağıdaki panel verileri Dijital Öğe kalibrasyonu için kullanılmaktadır. Veriler uygun kaynaklardan toplanacaktır (bkz. Türkiye Toplumsal Kalibrasyon Protokolü):

| Panel Dosyası | Kapsam | DO Bağlantısı |
|--------------|--------|--------------|
| `psychosocial_profile_panel.csv` | conformity_pressure, critical_thinking_strain, authority_dependence, uncertainty_avoidance, psychological_strain, polarization_load, propaganda_susceptibility, crisis_resilience, reform_latency_years, psy_soc_frag_score | Tüm 5 DO arketip temel parametreleri |
| `behavioral_action_funnel_panel.csv` | exit/voice/loyalty davranış oranları | Q-learning ödül fonksiyonu kalibrasyonu |
| `monthly_macro_regime_panel.csv` | Rejim durumu etiketleri (CBC-07 durum) | Bayesian prior + BTF backtest |
| `media_policy_bias_panel.csv` | NLP söylem analizi çıktıları | NRG + S_t hesabı |
| `institutional_commitment_protocol.csv` | Taahhüt değişkenleri | ICF katmanı |
| `daily_blind_flight_snapshot.csv` | Anlık kör uçuş verileri | Gerçek zamanlı CBC tetikleyicisi |
| `weekly_banking_reserve_panel.csv` | M2/NIR haftalık | MBP ve SRI_fin |
| `company_financials_ghost_revenue_panel.csv` | Hayalet şirket ağ verisi | L2 topoloji + T2SAIM Fraud Gate |
| `REQUIRED_SERIES_MASTER_MANIFEST.csv` | Tüm EVDS seri kodları | Veri altyapısı referansı |
| `TR_1994_FINANCING_CHAIN_MONTHLY.csv` | 1994 kriz zinciri | BTF backtest kalibrasyonu |
| `TR_WORLD_BANK_MACRO_SERIES_1990_2024.csv` | WB makro seri seti | CBC-01 ve CBC-06 girdileri |

**Kalibrasyon Veri Kaynakları (Türkiye Toplumsal Kalibrasyon Protokolü'nden):**

```
WVS Dalga 2-7 (1990-2018):    → Arketip pay kalibrasyonu + prior
Inglehart-Welzel Kültürel Harita: → Temel kültürel prior ekseni
Pew Din ve Kamusal Hayat:     → BRP F1-F3 proxy
Sabancı Üniversitesi Dindarlık Raporu: → Türkiye özgül dini veri
OECD PISA (2022):             → Bilişsel kapasite proxy (epistemic_closure)
TÜİK Eğitim İstatistikleri:  → Sosyolojik kalibrasyon
World Bank WGI:               → ICF + IDIS
WJP Rule of Law Index:        → ICF + Yargı_İstiklal
TI CPI:                       → B_t (EFMI davranış skoru)
World Bank Kadın İşgücü:      → GV4 female_bodily_autonomy
WEF Gender Gap Report:        → GV kanal kalibrasyonu
TCMB Finansal İstikrar Raporu: → MBP + SRI_fin
BDDK Ana Göstergeler:         → MBP + EBP (DTH oranı)
```

---

## 12I: ETİK ÇERÇEVE — DİJİTAL ÖĞELER İÇİN ÖZEL KISITLAMALAR

```
DO-ETİK-01: Bireysel hedefleme yasağı
  Dijital Öğeler hiçbir gerçek kişiyi veya tanımlanabilir küçük grubu modelleme
  veya hedefleme amacıyla kullanılamaz. Çıktılar yalnızca ülke/dönem düzeyindedir.

DO-ETİK-02: Manipülasyon aracı yasağı
  DO simülasyonları yalnızca analitik/tahmin amaçlıdır.
  Bir topluluk veya arketip grubunu manipüle etmek için kullanılamaz.
  Coxall manipülasyon mekanizmaları TESPIT amaçlıdır; UYGULAMA amaçlı değildir.

DO-ETİK-03: Nüfus yönlendirme yasağı
  Simülasyon çıktıları oy yönlendirme, kalabalık mobilizasyonu veya siyasi kampanya
  optimizasyonu için kullanılamaz.

DO-ETİK-04: Kimlik etiketi yasağı
  Arketip isimleri (TRA, CRT, ANX, RES, MAR) hiçbir zaman etnik, dini veya siyasi
  kimlik etiketiyle eşleştirilmez. Yapısal örüntü tanımlaması yapılır; kimlik atfı olmaz.

DO-ETİK-05: Özerk karar yasağı
  DO simülasyonu çıktıları karar tetikleyicisi değil, analitik girdidir.
  "Karar = Tarco" ilkesi burada da geçerlidir. Hiçbir algoritma kendi başına
  eylem kararı almaz veya önermez.

DO-ETİK-06: McCoy Protokolü
  "Spock yorumlar, McCoy insanı hatırlatır."
  DO çıktısına bakıldığında "bu sayıların arkasında insan var" refleksi
  her analizin başına yazılır.

Denetim kaydı: Her DO simülasyonu çıktısı şu bilgileri içerir:
  - Analiz düzeyi: [ülke/dönem]
  - Bireysel atıf: YOK
  - Manipülasyon niyeti: YOK
  - Kaptan onayı: [imza + tarih]
```

---

# EK A: VERİ TOPLANACAK SERİLER VE KAYNAKLAR

> Aşağıdaki seriler uygun kaynaklardan toplanacaktır. Bu liste veri toplama rehberi
> olup içerik bu korpusa dahil edilmemiştir.

| Seri | Kaynak | Katman |
|------|--------|--------|
| M2 haftalık | EVDS: TP.HPBITABLO1.11 | MBP/SRI_fin |
| NIR haftalık | EVDS: TP.AB.N06 | MBP/SRI_fin |
| İç kredi | EVDS: TP.HPBITABLO6.19 | MBP |
| CDS 5Y | Bloomberg/Refinitiv | MBP |
| WGI 6 boyut | World Bank data360 | ICF/IDIS |
| WJP RoL | worldjusticeproject.org | ICF |
| TI CPI | transparency.org | EFMI B_t |
| V-Dem (12 değişken) | v-dem.net | ICF/NRG/SDP |
| WVS Türkiye Dalga 2-7 | worldvaluessurvey.org | DO arketip |
| WEF GGR | weforum.org | GV4/F7 |
| TÜİK eğitim | veriportali.tuik.gov.tr | DO kalibrasyon |
| BDDK ana göstergeler | bddk.org.tr | EBP/MBP |
| TCMB FİR | tcmb.gov.tr | MBP |
| RSF basın özgürlüğü | rsf.org | F4/F5/NRG |
| GREVIO Türkiye | coe.int | GV1-GV7 |
| ACLED Türkiye | acleddata.com | SDP/GV1 |
| UNHCR sığınma | unhcr.org | GV7/EBP |
| EVDS Eurobond takvimleri | tcmb.gov.tr | CBC-06 CCP |

---

# EK B: CANON HİYERARŞİSİ VE ONAY PROTOKOLÜ

```
CANON HİYERARŞİSİ (değişmez):
  1. Kaptan Tarkan Bulan (nihai karar mercii)
  2. T2SAIM v09.6 Mühürlü Çekirdek
  3. Master Unified Corpus v1.1 (bu doküman)
  4. Motor Mühürlü Versiyonlar
  5. Aday Sürümler
  6. Arşiv

EPİSTEMİK MARKALAR (tüm korpus için geçerli):
  ✅  Doğrulandı — Veriyle teyit edildi
  🔴 THE TEST — Metodoloji geçerliliği test altında
  ⚠️  Varsayıldı — Makul çıkarım; tek kaynaklı
  ❌  Geçersiz — Çürütüldü; kullanılmaz
  ⛔  Etik Bayrak — Yanlış kullanım potansiyeli; dikkat gerekir

SON GÜNCELLEME: 2026-06-12
DURUM: AKTIF YAZIM — KAPTAN ONAYI BEKLENİYOR
```

---

*T2SAIM Master Unified Corpus v1.1 — Tüm haklar saklıdır.*  
*Ticari sır — Yayılmaması gereken dahili doküman.*  
*Kaptan Tarkan Bulan (Tarco) — Şirket: [T2SAIM Technologies]*

---

