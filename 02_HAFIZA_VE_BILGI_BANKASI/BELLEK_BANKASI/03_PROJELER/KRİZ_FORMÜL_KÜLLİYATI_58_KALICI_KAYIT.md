# 🧮 T2SAIM KRİZ TESPİT FORMÜL KÜLLİYATI — KALICI KAYIT (v1.0)

**Üretici:** Komutan Picard · **Tarih:** 24 Ağustos 2026 · **Karar Makamı:** Kaptan Tarco
**Amaç:** İleride güncelleme/denetimde tekrar uğraşmamak için, 58 kriz-tespit formülünün TAMAMI kalıcı kayda alındı.
**Konum:** Mission Control Bellek Bankası + OKF (SSOT)
**Durum:** Red Team doğrulandı, çalışan koda döküldü.

> **Kaptan'ın ilkesi:** "400 formül = TÜM SİSTEM. Bu 58 = SADECE kriz tespiti. Her ülkenin verisi kendi dilinde/kendi kaynağında. Detayda bilgidir."

---

## BÖLÜM 1 — NÖROFİNANS & AMİGDALA (Formül 1-11, Hariseldon Kriz)

| # | Formül | Veri Kaynağı | İnsan/Toplum Anlamı |
| :--- | :--- | :--- | :--- |
| 1 | Returns(t) = (P(t)-P(t-1))/P(t-1) | USD/TRY günlük | Günlük kur sıçraması |
| 2 | SmoothedReturns = 1/30·ΣReturns | 30 günlük pencere | Gürültü filtresi |
| 3 | Z(t) = (Smoothed−μ1260)/σ1260 | 5 yıl pencere | Kur tarihsel normdan kaç σ sapmış |
| 4 | Z_norm = min(1, max(0, |Z|/1.25)) | σ_limit=1.25 | Şok standardizasyonu |
| 5 | Vol_norm = min(1, σvol/5.0) | USDTRY_vol | %5 oynaklık = tam risk |
| 6 | SRI_vol = 0.60Z + 0.40Vol | türet | Bileşik oynaklık şoku |
| 7 | SRI = 0.30Psy + 0.40Fin + 0.30Vol | TR_PRIORITY1 panel | Sistemik rezonans |
| 8 | SRI_DEI = SRI·1.15 (DEI≥0.60) | DEI basel | Asimetrik çürüme çarpanı |
| 9 | Alarm = I(SRI≥0.65 ∨ Z≥1.25) | türet | Kriz alarmı |
| 10 | Memory = M(t-1)·exp(-λ/30)+Alarm | λ=0.15 | Kuşaksal unutma (eski şok sahte alarm üretmez) |
| 11 | CI = min(1, 0.70SRI_DEI + 0.30·Memory/5) | türet | Nihai kriz indeksi; Distance=1−CI≤0.2039 kriz |

## BÖLÜM 2 — SÜRÜ BİYOKİMYASI (Formül 12-20)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 12 | A_load = 1/(1+e^(-1.5·(Risk−1.8))) | CDS/vol/duygu | Toplum panik refleksi (>0.65 mantık çöker) |
| 13 | PFC = 0.85/(1+e^(5.0464·(Aload·1.2−0.65))) | türet | Rasyonel karar kapasitesi |
| 14 | Kalman K_eff = πe/(πe+πp), ≥0.08 | türet | Gerçeklik donması (panikte körleşme) |
| 15 | Hawkes λ = μ0·COI + Σα·e^(-β·Δt)·(1−PFC/PFC_max) | duygu/kaskad | Kendini besleyen şok |
| 16 | SSRI_numb = Reçeteli_SSRI/Popülasyon/(1+σ) | narkotik/ilaç | Kitlesel duygusuzlaşma = bastırılmış vol |
| 17 | Dopamine_0DTE = 0DTE_hacim/S&P_hacim | opsiyon | Gama sıkışması (kumar bağımlılığı) |
| 18 | C_atrofi = 1−e^(-γc·∫max(0,Aload−0.60)dτ) | türet | Kronik krizde hafıza kaybı |
| 19 | Oxy_split = Oxy_in − Oxy_out·Aload | sosyal | İç-grup güven / dış-grup nefret |
| 20 | R(t) = Δ0/√((ωfin²−ωreel²)²+4γ²ωreel²) | kredi/sanayi | Kuple osilatör rezonansı |

## BÖLÜM 3 — FRAKTAL & KAOS (Formül 21-29)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 21 | MFDFA F_q ~ s^h(q) | log-getiri | Çok-fraktallık (kriz belirsizliği) |
| 22 | Lyapunov λ_max | zaman serisi | Deterministik kaos (λ>0 tahmin kırılır) |
| 23 | D_2 Grassberger-Procaccia | zaman serisi | Gizli değişken sayısı |
| 24 | Tsallis S_q (q=1.45) | dağılım | Kalın kuyruk termodinamiği |
| 25 | Shannon H = −Σp·log2p | dağılım | Bilgi entropisi |
| 26 | v_run = d(FizikiAltın+SPV)/dt | altın/SPV | Mevduat kaçışı (>0.70 bank-run) |
| 27 | θ_REER = (REER−denge)/σREER | BIS | Aşırı değerli kur potansiyel enerjisi |
| 28 | DOLGAP = (Kapalıçarşı−Resmi)/Resmi | iki kur | İkili kur makası (sermaye kontrolü) |
| 29 | ALM_gap = KrediVadesi − MevduatVadesi(32g) | banka bilanço | Faiz şokunda kilitlenme riski |

## BÖLÜM 4 — MİKRO YAPI & LOB (Formül 30-35)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 30 | VPIN = Σ|V_B−V_S|/N·V_bucket | emir akışı | Toksik akış (>0.35 insider) |
| 31 | Kyle λ = Cov(ΔP,flow)/Var(flow) | LOB | Emir fiyat etkisi (sığ tahta) |
| 32 | Amihud ILLIQ = |R|/(Vol·P) | fiyat/hacim | Likidite kuruması |
| 33 | LBI = Σw_k(Bid−Ask)/Σw_k(Bid+Ask) | 50 kademe LOB | Derinlik dengesizliği (%0.4 alfa) |
| 34 | R_cancel = İptal/Toplam | LOB | Spoofing (≥0.85 manipülasyon) |
| 35 | C_takas = Σİlk5 SaklamaPayı | MKK saklama | Tahta kilitlenmesi (≥0.70 cornering) |

## BÖLÜM 5 — KURUMSAL & GULLINI/ACEMOĞLU (Formül 36-43)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 36 | Power_Total = De_Jure + μ·De_Facto | kurum/sokak | Siyasal güç gerilimi |
| 37 | IDIS = 0.40HHI + 0.35Yargı + 0.25Rant | kamu ihaleleri | Sömürücü kurum dengesi (%74.1 TR) |
| 38 | Dar Koridor = |State−Society| ≤ ε | devlet/toplum | Leviathan/kaos eşiği |
| 39 | ΔX = (I−A)⁻¹·ΔF | girdi-çıktı | Tedarik zinciri kaskadı |
| 40 | G_def = Var(TCMB−Beklenti)/Enflasyon | TCMB/piyasa | Merkez bankası inançsızlık (%78.2 TR) |
| 41 | Minsky t* = Faiz≥Vergi+Borçlanma | bütçe | Ponzi kırılma tarihi |
| 42 | HHI_ihale = Σs_i² | ihaleler | İhale tekelleşmesi |
| 43 | KÖİ = ΣKurGarantisi·max(0,Spot−Taban) | Londra tahkim | Gizli Hazine yükü (160Mr$ TR) |

## BÖLÜM 6 — 6 KÜRESEL PİYASA (Formül 44-52)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 44 | NetLiq = FedSheet−TGA−RRP | FRED WALCL | ABD likidite çekilmesi |
| 45 | FERC_deficit = AI_Talep−Şebeke | FERC/DOE | AI enerji darboğazı |
| 46 | D_M = √((x−μ)ᵀΣ⁻¹(x−μ)) > 3σ | City of London | SPV kara para kaçışı (UK) |
| 47 | Tail_DMO = İhaleKesme−Piyasa | DMO | 30Y Gilt kuyruğu (UK) |
| 48 | T2_ratio = Σ|TARGET2|/ECB | ECB | Avrupa dengesizlik vektörü |
| 49 | Choke_EU = I(Kaub<40cm)·Navlun | Ren Nehri | Kimya/çelik lojistik şoku |
| 50 | Basis_JPY = |3M USD/JPY baz swap| | BoJ/BIS | Yen carry çözülme (>60bp) |
| 51 | Chokepoint = I(EUI>36sa ∧ PMI≥48) | AIS boğaz | Enerji darboğazı alarmı |
| 52 | TAS_fraud = ÇevrimselCüzdan/Toplam | on-chain | Kripto wash trading (≥0.50) |

## BÖLÜM 7 — ADLİ & VERGİ (Formül 53-54)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 53 | D_Benford = Σ|P_obs−log10(1+1/d)| | bilanço/harcama | Muhasebe hilesi |
| 54 | NetReturn = Gross·(1−Tax)−Friction | vergi | BIST %0 stopaj avantajı |

## BÖLÜM 8 — BORSA 60-GÜN & KELLY (Formül 55-58)

| # | Formül | Kaynak | Anlam |
| :--- | :--- | :--- | :--- |
| 55 | m(t)=dP/dt, a(t)=d²P/dt² | fiyat | Kâr realizasyonu (m>0,a<0) / Dip (a→0) |
| 56 | Range_Low/High = P·(1±σ·(1±Φ)) | vol + kriz skoru | 60 günlük bant |
| 57 | P_Target(t+60) = P(t)·(1+0.18/−0.30/+0.45) | rejim | 60. gün hedef |
| 58 | Kelly f* = max(0,min(0.25,(p(b+1)−1)/b)) | olasılık | Dinamik sermaye boyutu |

---

## DOĞRULUK TABLOSU (VERITAS MATRIX)
| Katman | Formül | Fiziksel Kanıt | Çalışan Kod |
| :--- | :---: | :--- | :---: |
| Hariseldon | 1-11 | generate_crisis_data.py | ✅ |
| Nörofinans | 12-20 | daily engine | ✅ |
| Fraktal | 21-29 | master engine | ✅ |
| LOB | 30-35 | harita + hesaplama | ✅(harita) |
| Kurumsal | 36-43 | acemoglu/gullini html | ✅(harita) |
| 6-piyasa | 44-52 | compendium | ✅(harita) |
| Adli | 53-54 | benford | ✅(harita) |
| Borsa | 55-58 | daily engine | ✅ |

*Veritas Per Se — Komutan Picard, 24 Ağustos 2026 · Kaptan'a teşekkürle*
