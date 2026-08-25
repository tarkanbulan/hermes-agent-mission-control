# 🎭 SIMÜLASYON CORPUS — 5'Lİ GRUPLAR · KRİZ KULLANIM KLAVUZU (72 simülasyon)

**Üretici:** Komutan Picard · **Tarih:** 25.08.2026 · **Kaynak:** `00_Simulation Corpus` (72 .py)
**Kapsam:** Her grup → ekonomik/finansal/toplumsal kriz ÖNCE-görme + SONRASI olay tespiti + anlam + veri + nereden bulunur.
**Not:** Veri kaynağı = hangi FRED/hangi CSV/hangi API; "nerede" = projede/dış.

---

## GRUP 1 — Ising Polarizasyon + Jump Diffusion (kutuplaşma + finansal sıçrama)
| Sim | Kriz öncesi | Kriz sonrası | Anlam | Veri | Nerede |
|:---:|:---|:---|:---|:---|:---|
| run_all | tüm sim koş | — | orkestratör | — | corpus kök |
| sim_ising_polarization | **kutuplaşma faz geçişi** → toplumsal kırılma öncüsü | rejim kilitlenme sonrası | iki kutupluluk eşiği | polarization/trust | panel/EVDS |
| sim_ising_v20j | aynı (versiyon) | — | kalibre | polarization | panel |
| sim08_jump_diffusion | **finansal sıçrama frekansı λ** artışı → kriz öncesi | şok yayılımı sonrası | λ_jump = kırılganlık | döviz/fiyat seri | FRED FX |
| sim_deffuant | **fikir ayrışması** (echo chamber) → toplumsal parçalanma | kutuplaşma kalıcılığı | ε ne kadar kapanır | görüş dağılımı | panel/anket |

## GRUP 2 — Galam + Hegselmann (oy çoğunluk + fikir birleşme)
| sim_friedkin_johnsen | **inkarcı/bağımlı ajanlar** → hızlı fikir kilidi | uzlaşmazlık bölgesi | atalet | inanç matrisi | panel |
| sim_galam | **çoğunluk sıçraması** → ani rejim değişimi öncüsü | çoğunluk pivot | kritik çoğunluk fraksiyonu | oy/eylem oranı | anket/seçim |
| sim_galam_v20j | kalibre | — | — | — | — |
| sim15_hk | **fikir yakınsama hızı** → toplumsal ortak akıl | homojenleşme | tolerans | görüş aralığı | panel |

## GRUP 3 — Percolation + SEIZ (bulaşma + dezenformasyon)
| sim_percolation | **ağ iletim eşiği p_c** → kriz sıçrayacak mı | kaskad sonrası | perkolasyon eşiği | ağ bağlantı | sosyal ağ |
| sim_percolation_v20j | kalibre | — | — | — | — |
| sim14_seiz | **dezenformasyon/söylem bulaşması** → toplumsal panik öncüsü | salgın sonrası direnç | SEIZ kanalları | haber/medya | GDELT/gazete |
| sim_minority_game | **kalabalık akılcılığı** → piyasa tersliği öncüsü | kaynak yanlısı | uyum-karşıtlık | ajan strateji | simulasyon |

## GRUP 4 — Sandpile + Kinetic Wealth + SOC (kritiklik + zenginlik)
| sim07_sandpile | **kritik el / kum tepesi → çığ beklenir** | çığ sonrası dinginlik | SOC eşiği | artış hızı | FRED toplam değer |
| sim_kinetic_gini | **Gini yükselişi → toplumsal gerginlik öncüsü** | servet dağılımı sonrası | Gini eşiği | gelir/dağılım | WB Gini |
| sim_soc_power_law | **üstel kuyruk** → büyük kriz olasılığı | güç-yasası kırılma | ölçek değişmezlik | uç olaylar | veri uzun seri |
| sim_soc_power_law_v20j | kalibre | — | — | — | — |

## GRUP 5 — Amigdala Jump + Bank Run + IK (amigdala + banka panik + istifa)
| sim_jump_diff_amigdala | **A_load deformasyonu → finansal kırılganlık** | panik şoku | A_load×drift | A_load/PFC | nöro modül |
| sim_bank_run_percolation | **banka hücum eşiği → mevduat kaçışı öncüsü** | banka iflası sonrası | kritik çekilme fraksiyonu | mevduat/rezerv | FRED rezerv |
| sim_quiet_quitting | **toplu istifa/sessiz ayrılma → emek çöküşü** | işgücü erozyonu | kopuş eşiği | istifa/işsizlik | istatistik/çalışma |

## GRUP 6 — Hoarding + Echo Chamber (stokçuluk + medya yankı)
| sim_hoarding_sir | **stokçuluk salgını → kıtlık/panik** | tüketim çöküşü | SIR panik | perakende stok | envanter/karaborsa |
| sim_marketing_echo | **pazarlama yankı → fiyat şişirme** | marka erozyonu | echo gücü | reklam/duyarlılık | medya |

## GRUP 7 — Urban Jump + Social Media SEIZ (kentsel + sosyal medya)
| sim_urban_jump_diff | **gayrimenkul sıçraması → konut krizi öncüsü** | emlak çöküşü | λ_jump emlak | konut fiyat | FRED/emlak |
| sim_seiz_disinfo | **dezenformasyon yayılımı → toplumsal kutuplaşma** | bilgi kirliliği sonrası | S/E/I/Z oran | sosyal medya | GDELT/API |

## GRUP 8 — Hypergame + Structural Balance (memetik + dengeler)
| sim_hypergame | **asimetrik oyun / şaşırtma → algı krizi** | strateji kayması | bilgi asimetrisi | algı oyuncuları | istihbarat |
| sim_harary_balance | **ağ dengesi → ittifak/kutuplaşma** | denge-yok fazı | dengeli üçgenler | ilişki ağı | diplomasi |

## GRUP 9 — Fikir Liderliği + Uzamsal + Bayesyen Hoax + SEIZ
| sim_fj_stubborn | **inatçı liderler → fikir dominasyonu** | çoğunluk inanç | atalet/bit | inanç+lider | panel |
| sim25_uzamsal | **uzamsal baskılama → bölgesel kaynaşma** | bölgesel ayrışma | coğrafi etki | bölge verisi | harita/bölge |
| sim20_mit_hoax | **bayesyen söylenti → güven çöküşü** | inanç yıkımı | posterior kayma | söylenti/kanıt | GDELT |

## GRUP 10 — SIRMIS SDE + Europe + Global (makro sistemik)
| sim22_sirmis_sde | **stoastik kriz dinamiği → rejim değişimi** | kararlılık | SDE drift/vol | makro seri | FRED |
| sim_europe_macro | **AB makro bulaşma → üye krizi** | üye yayılım | τ matrisi | AB ülke seri | ECB/FRED |
| sim_global_systemic | **küresel sistemik → dünya krizi öncüsü** | global yayılım | Ω_Küresel | 29 ülke UCI | ülke paket |

## GRUP 11-12 — MUHASEBE FRAUD (M1-M16) — örgütsel adli kriz
| M1 FraudSim | **fraud imzası → bilanço çöküşü öncüsü** | iflas sonrası | fraktal imza | muhasebe veri | yevmiye/ledger |
| M2 Benford MAD | **doğallık sapması → manipülasyon** | uydurma tespit | MAD | fatura/tutar | defter |
| M3 Gini/Zipf | **yoğunlaşma → tek risk** | tersi | Gini | tedarik/firma | ihale |
| M6 Percoll/Cashflow | **nakit sıkışma kaskadı** | zincir iflas | eşik | nakit akışı | ledger |
| M10 SOC Avalanche | **fraktal stok çığı** | kritik | çığ | stok | ledger |
| M16 Jump Diff | **fraud fiyat sıçraması** | çöküş | λ | marj | ledger |

## GRUP 13-15 — Türkiye/UK/USA + Picard Fraud Sim (ülke odaklı)
| turkey_81_province | **il bazlı kriz dağılımı → bölgesel öncü** | TR bölge | 81 il | il verisi | TÜİK/il |
| aberdeen_south | **UK yerel simülasyon** | UK bölge | — | UK bölge | ONS |
| makerfield/uk_election | **UK seçim simülasyonu** | oy dağılımı | — | anket | ONS |
| uk/usa_market_amygdala | **UK/USA piyasa amigdala** | panik | A_load | borsa | FRED |
| fraudsim/spaces/swarm | **Picard fraud sim (yeni)** | — | — | ledger | PICARD_SIM |

---
*Veritas Per Se — Komutan Picard · 72 simülasyon, 15 grup. Her grup kriz önce/sonrası + veri. Deep Search'e yüklenecek temel.*
