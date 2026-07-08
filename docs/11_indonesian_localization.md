# 🇮🇩 Indonesian Market Localization

> Mengadaptasi Risk Profiler dari framework global ke konteks Indonesia: budaya, instrumen, dan skenario pasar lokal.

---

## Daftar Isi

1. [Mengapa Lokalisasi Penting](#mengapa-lokalisasi-penting)
2. [Dasar Akademis](#dasar-akademis)
3. [Perubahan Utama](#perubahan-utama)
4. [Scenario Localization](#scenario-localization)
5. [Product Mapping](#product-mapping)
6. [Cultural Considerations](#cultural-considerations)
7. [Inflasi & Asumsi Ekonomi](#inflasi--asumsi-ekonomi)
8. [Before vs After](#before-vs-after)
9. [Referensi](#referensi)

---

## Mengapa Lokalisasi Penting

Risk Profiler yang dibangun untuk konteks Barat (AS/Eropa) **tidak langsung applicable** untuk investor Indonesia karena:

1. **Instrumen berbeda** — Indonesia punya ORI, SBR, Reksa Dana, yang tidak ada di AS
2. **Budaya keuangan berbeda** — keluarga besar, gotong royong, keputusan finansial kolektif
3. **Konteks pasar berbeda** — IHSG bukan S&P 500, Rupiah bukan Dollar
4. **Tingkat literasi berbeda** — mayoritas masih dalam tahap awal literasi investasi
5. **Skenario referensi berbeda** — crash IHSG Maret 2020 bukan crash Wall Street

---

## Dasar Akademis

### Hofstede — Individualism Index

| Negara | IDV Score | Interpretasi |
|---|---|---|
| **Indonesia** | **14** | **Sangat kolektivis** — skor terendah di antara negara besar |
| Amerika Serikat | 91 | Sangat individualis |
| Jepang | 46 | Moderate |
| Malaysia | 26 | Kolektivis |

**Implikasi untuk Risk Profiling:**
- Keputusan investasi sering **bukan keputusan individual**
- Keluarga besar memiliki **pengaruh signifikan** terhadap alokasi aset
- Konsep "uang keluarga" vs "uang pribadi" mempengaruhi risk perception
- **Social proof** (tetangga/keluarga investasi apa) sangat berpengaruh

> Sumber: Hofstede Insights — Country Comparison Indonesia

### ResearchGate (Januari 2026) — "Cultural Influences on Risk Tolerance and Portfolio Creation"

Studi terhadap mahasiswa Indonesia menemukan:

- **Faktor budaya** signifikan mempengaruhi risk tolerance (p < 0.05)
- Mahasiswa Indonesia cenderung **lebih konservatif** dari rekan AS pada risk tolerance test yang sama
- **Keluarga** adalah sumber utama referensi investasi (>60% responden)
- **Agama** juga mempengaruhi preferensi instrumen (Syariah compliance)

### Asia Pacific Journal (2026) — Cultural Norms & Risk Tolerance

Temuan utama:
- **Norma budaya** lebih kuat mempengaruhi risk tolerance daripada pendapatan
- Investor di Asia Tenggara (termasuk Indonesia) menunjukkan **herding behavior** yang lebih tinggi
- **Financial socialization** dimulai dari keluarga, bukan institusi pendidikan

---

## Perubahan Utama

### 7 Area Lokalisasi

| # | Area | Versi Global | Versi Indonesia |
|---|---|---|---|
| 1 | **Benchmark pasar** | S&P 500, NASDAQ | **IHSG (Indeks Harga Saham Gabungan)** |
| 2 | **Mata uang** | USD, EUR | **Rupiah (Rp)** |
| 3 | **Bursa saham** | NYSE, LSE | **BEI (Bursa Efek Indonesia)** |
| 4 | **Instrumen** | Mutual Fund, ETF, 401k | **Reksa Dana, ORI/SBR, Emas, Saham IDX** |
| 5 | **Faktor budaya** | Individual decision-making | **Keluarga, gotong royong, komunal** |
| 6 | **Asumsi inflasi** | 2-3% (US/EU) | **4% (Indonesia)** |
| 7 | **Skenario crash** | 2008 GFC (US) | **IHSG crash Maret 2020 (COVID)** |

---

## Scenario Localization

### Skenario 1: Market Crash

**Versi Global:**
> "Bayangkan Anda punya investasi $100.000 di S&P 500. Dalam satu bulan, turun jadi $70.000 (-30%). Apa yang Anda lakukan?"

**Versi Indonesia:**
> "Bayangkan Anda punya investasi Rp 150.000.000 di saham-saham IHSG. Dalam satu bulan (Maret 2020), nilainya turun jadi Rp 100.500.000 (-33%). IHSG turun dari 5.900 ke 3.937. Apa yang Anda lakukan?"

| Aspek | Global | Indonesia |
|---|---|---|
| Index | S&P 500 | IHSG |
| Aset awal | $100.000 | Rp 150.000.000 |
| Penurunan | -30% | -33% (IHSG Maret 2020) |
| Aset akhir | $70.000 | Rp 100.500.000 |
| Referensi waktu | 2008 GFC | Maret 2020 COVID |

### Skenario 2: Reksa Dana Performance

**Versi Global:**
> "Your mutual fund returned 8% last year. S&P 500 returned 15%. How do you feel?"

**Versi Indonesia:**
> "Reksa Dana Saham Anda return 8% tahun lalu. IHSG naik 15% (selevel 7.000). Apa yang Anda rasakan?"

### Skenario 3: Obligasi Pemerintah

**Versi Global:**
> "US Treasury bonds offer 4.5% yield."

**Versi Indonesia:**
> "Obligasi Negara Ritel (ORI024) menawarkan kupon 6.25% per tahun, dibayar bulanan."

### Skenario 4: Dana Darurat

**Versi Global:**
> "You need 3-6 months of expenses as emergency fund."

**Versi Indonesia:**
> "Idealnya, dana darurat = 6-12x pengeluaran bulanan (karena jaring pengaman sosial lebih terbatas). Simpan di RDPU atau Deposito."

### Skenario 5: Kerugian Besar

**Versi Global:**
> "If your portfolio lost 40%, what would you do?"

**Versi Indonesia:**
> "Jika portofolio Anda (yang berisi saham BBCA, BBRI, dan Reksa Dana) turun 40% — dari Rp 500 juta jadi Rp 300 juta — apa yang Anda lakukan?"

---

## Product Mapping

### Instrumen Global → Indonesia

| Instrumen Global | Equivalent Indonesia | Tipe |
|---|---|---|
| S&P 500 Index Fund | **Reksa Dana Indeks IHSG** | Equity |
| US Treasury Bonds | **Obligasi Negara (ORI/SBR/ST)** | Fixed Income |
| 401(k) | **DPLK (Dana Pensiun Lembaga Keuangan)** | Retirement |
| Money Market Fund | **RDPU (Reksa Dana Pasar Uang)** | Cash Equivalent |
| Corporate Bonds | **Obligasi Korporasi (OCC) / RDPT** | Fixed Income |
| REITs | **DIRE (Dana Investasi Real Estate)** | Alternatives |
| Gold ETF | **Emas Antam / Pegadaian / ETF Emas** | Commodities |
| Roth IRA | **Tidak ada equivalent langsung** | — |
| High-Yield Savings | **Deposito Berjangka** | Cash |

### Lengkap: Instrumen Indonesia yang Digunakan

#### 🏦 Konservatif
| Instrumen | Risiko | Likuiditas | Return Historis |
|---|---|---|---|
| Deposito Berjangka | Sangat Rendah | Sedang (terikat tenor) | 3-5% |
| RDPU | Sangat Rendah | Tinggi (T+1) | 4-6% |
| SBR (Savings Bond Ritel) | Rendah | Rendah (terikat) | 5-7% |
| ORI (Obligasi Ritel Indonesia) | Rendah | Sedang (bisa dijual) | 5.5-7% |
| Emas (Antam) | Rendah-Sedang | Sedang | 5-8% |

#### ⚖️ Moderate
| Instrumen | Risiko | Likuiditas | Return Historis |
|---|---|---|---|
| Reksa Dana Pendapatan Tetap | Rendah-Sedang | Tinggi (T+2) | 6-9% |
| Reksa Dana Campuran | Sedang | Tinggi (T+2) | 8-12% |
| Saham IDX Blue Chip | Sedang-Tinggi | Tinggi (T+2) | 8-15% |
| P2P Lending (Modalku, Investree) | Sedang-Tinggi | Rendah | 10-18% |

#### 🚀 Agresif
| Instrumen | Risiko | Likuiditas | Return Historis |
|---|---|---|---|
| Reksa Dana Saham | Tinggi | Tinggi (T+2) | 10-18% |
| Saham IDX Individual | Tinggi | Tinggi (T+2) | -20% to +50%+ |
| Saham IDX Small/Mid Cap | Sangat Tinggi | Sedang | -30% to +100%+ |
| Bitcoin | Sangat Tinggi | Tinggi | -70% to +300%+ |
| Altcoin / DeFi | Ekstrem | Tinggi | -90% to +1000%+ |

---

## Cultural Considerations

### 1. 🏠 Kewajiban Finansial Keluarga

**Konteks:** Di Indonesia, gaji tidak hanya untuk diri sendiri. Banyak yang mengirim uang ke orang tua, membantu saudara, atau menanggung biaya keluarga besar.

**Dampak pada Risk Profiling:**
- Risk Capacity lebih rendah karena ada komitmen rutin ke keluarga
- Dana darurat perlu **lebih besar** (6-12x pengeluaran, bukan 3-6x)
- Alokasi ke instrumen likuid lebih tinggi

**Adaptasi:**
```yaml
input_tambahan:
  kiriman_keluarga: 1500000    # per bulan
  tanggungan_orang_tua: true
  tanggungan_saudara: 1
  dana_pendidikan_adik: 500000  # per bulan
```

### 2. 👨‍👩‍👧‍👦 Keputusan Keuangan Komunal

**Konteks:** Berdasarkan Hofstede IDV score = 14, keputusan investasi sering melibatkan:
- Pasangan (suami/istri)
- Orang tua
- Saudara kandung
- Bahkan tetangga/rekan (social proof)

**Dampak pada Risk Profiling:**
- Risk Tolerance yang terukur mungkin **bukan preferensi sebenarnya** — bisa jadi lebih konservatif karena pengaruh keluarga
- Perlu pertanyaan tambahan: *"Siapa yang Anda libatkan dalam keputusan investasi?"*
- Risk profile bisa berubah jika ada perubahan dinamika keluarga

**Adaptasi:**
```yaml
pertanyaan_tambahan:
  - "Siapa yang biasanya Anda ajak diskusi sebelum investasi?"
    options:
      - "Sendiri" → individual decision
      - "Pasangan" → couple decision
      - "Orang tua" → family-influenced
      - "Keluarga besar / teman" → highly communal
```

### 3. 🕌 Preferensi Syariah

**Konteks:** Mayoritas Muslim Indonesia membutuhkan opsi investasi Syariah.

**Adaptasi:**
- Tambah filter: **Syariah / Konvensional / Tidak peduli**
- Mapping ke instrumen Syariah:

| Konvensional | Syariah Equivalent |
|---|---|
| Deposito | Deposito/iB Mudharabah |
| RDPU | RDPU Syariah |
| Reksa Dana Campuran | Reksa Dana Campuran Syariah |
| Saham (semua) | Saham dari Daftar Efek Syariah (DES) |
| Obligasi Korporasi | Sukuk Korporasi |
| ORI / SBR | Sukuk Ritel / Sukuk Tabungan |

### 4. 📱 Literasi Digital & Fintech

**Konteks:** Indonesia pasar fintech yang berkembang pesat (GoPay, OVO, Tokopedia, Bibit, Stockbit).

**Adaptasi:**
- Asumsi user familiar dengan **mobile-first** interface
- Referensi ke platform yang dikenal: **Bibit, Stockbit, Ajaib, Bareksa**
- Link ke fitur auto-invest yang populer di Indonesia

### 5. 💰 Gaji & Proporsi Investasi

**Konteks:** UMR Jakarta 2026 ~Rp 5.300.000. Banyak yang merasa "tidak punya cukup uang untuk investasi."

**Adaptasi:**
- Minimum investasi yang realistis: **Rp 100.000** (via Reksa Dana)
- Nada komunikasi: **inklusif**, tidak eksklusif untuk high-net-worth
- Tunjukkan bahwa investasi bisa dimulai dari nominal kecil

---

## Inflasi & Asumsi Ekonomi

### Parameter Ekonomi Indonesia

| Parameter | Nilai | Sumber |
|---|---|---|
| **Inflasi tahunan** | 4.0% | Bank Indonesia target |
| **BI Rate / 7-Day RR** | 5.75 – 6.25% | Bank Indonesia |
| **IHSG historical return (10yr avg)** | ~8-10% nominal | BEI data |
| **Rupiah depreciation vs USD** | ~3-5% per tahun | Historical average |
| **GDP growth** | ~5% | BPS |
| **Growth rate populasi muda** | Tinggi (median umur 30) | BPS |

### Mengapa 4% Inflasi?

Berbeda dari AS (target 2%) atau Eropa (target 2%), Indonesia secara historis memiliki inflasi yang lebih tinggi:

```
Tahun     Inflasi (YoY)
2020      1.68%  (COVID, anomali)
2021      1.87%  (recovery)
2022      5.51%  (global inflation)
2023      2.61%
2024      ~3.0%
2025      ~3.5%
Target BI  3.0 ± 1%
─────────────────────
Asumsi:   4.0% (conservative estimate)
```

> 📌 **Mengapa bukan 3%?** Kita menggunakan 4% sebagai asumsi **conservative** karena:
> 1. Memberikan buffer untuk tahun inflasi tinggi (seperti 2022)
> 2. Lebih aman untuk perencanaan jangka panjang
> 3. Menghindari over-optimistic projection

---

## Before vs After

### Contoh: Risk Profile Question

#### ❌ Sebelum Lokalisasi (Generic/US)

> **Q1:** "If you had $10,000 invested and it lost $2,000 in a month, you would:"
> - A) Sell everything
> - B) Sell half
> - C) Hold
> - D) Buy more

> **Q2:** "Your investment time horizon for this money is:"
> - A) < 1 year
> - B) 1-3 years
> - C) 3-5 years
> - D) 5-10 years
> - E) > 10 years

> **Q3:** "The chart below shows the range of returns for 4 hypothetical portfolios over a 1-year period. Which portfolio would you prefer?"

#### ✅ Sesudah Lokalisasi (Indonesia)

> **Q1:** "Jika Anda punya investasi Rp 15.000.000 dan nilainya turun Rp 3.000.000 dalam sebulan (karena IHSG koreksi), Anda akan:"
> - A) Jual semua, pindahkan ke Deposito
> - B) Jual sebagian, pindahkan ke RDPU
> - C) Tahan (hold), tunggu recovery
> - D) Tambah beli (average down) saham yang sama
> - E) Tambah beli, dan pindahkan dana dari instrumen lain ke saham

> **Q2:** "Untuk investasi ini, jangka waktu Anda adalah:"
> - A) < 1 tahun (misal: dana nikah yang sudah dekat)
> - B) 1-3 tahun (misal: DP rumah)
> - C) 3-5 tahun (misal: dana pendidikan anak)
> - D) 5-10 tahun (misal: dana pendidikan tinggi anak)
> - E) > 10 tahun (misal: dana pensiun)

> **Q3:** "Grafik berikut menunjukkan range return 4 portofolio hipotetis dalam 1 tahun. Mana yang Anda pilih?
> *(Masing-masing menggunakan benchmark IHSG, bukan S&P 500)*"

### Contoh: Scenario Descriptions

| Skenario | Before (Global) | After (Indonesia) |
|---|---|---|
| Market benchmark | "S&P 500 returned 25%" | "IHSG naik 15% ke level 7.800" |
| Amount format | "$50,000" | "Rp 750.000.000" |
| Crisis reference | "2008 Financial Crisis" | "IHSG crash Maret 2020 (5.900 → 3.937)" |
| Savings instrument | "High-yield savings account" | "Deposito Berjangka 6 bulan di Bank BCA" |
| Bond reference | "US Treasury 10Y at 4.5%" | "ORI024 kupon 6.25% per tahun" |
| Stock exchange | "NYSE/NASDAQ" | "BEI (Bursa Efek Indonesia)" |
| Investment platform | "Vanguard, Fidelity" | "Bibit, Stockbit, Ajaib, Bareksa" |
| Retirement | "401(k) with employer match" | "DPLK dari perusahaan" |
| Gold | "Gold ETF (GLD)" | "Emas Antam 1 gram = Rp 1.500.000" |
| Tax | "Capital gains tax 15-20%" | "PPh final 0.1% atas penjualan saham" |

### Contoh: Response Display

#### ❌ Before
```
Your Risk Number: 58 (Moderate)
Expected Return: 7.5%
Suggested Allocation:
  - 55% US Equities
  - 30% US Bonds
  - 10% International
  - 5% Cash
```

#### ✅ After
```
Risk Number Anda: 58 (Moderat)
Expected Return: 8.5%
Alokasi yang Disarankan:
  - 40% Saham IDX (BBCA, BBRI, TLKM)
  - 25% Reksa Dana Campuran
  - 20% Obligasi Pemerintah (ORI/SBR)
  - 10% Emas
  - 5% RDPU

Platform yang bisa digunakan:
  Bibit | Stockbit | Ajaib | Bareksa
```

---

## Referensi

| # | Sumber | Key Insight |
|---|---|---|
| 1 | **Hofstede Insights — Indonesia** | IDV score = 14 (sangat kolektivis); keputusan investasi bersifat komunal |
| 2 | **ResearchGate (Jan 2026)** — "Cultural influences on risk tolerance and portfolio creation" | Faktor budaya signifikan mempengaruhi risk tolerance mahasiswa Indonesia |
| 3 | **Asia Pacific Journal (2026)** — Cultural norms & risk tolerance | Norma budaya lebih kuat mempengaruhi risk tolerance daripada tingkat pendapatan |
| 4 | **Bank Indonesia** | Inflasi target 3±1%, BI Rate, kebijakan moneter |
| 5 | **BEI (Bursa Efek Indonesia)** | IHSG historical data, produk pasar modal |
| 6 | **OJK (Otoritas Jasa Keuangan)** | Regulasi investasi, perlindungan konsumen |

---

*Last updated: Juli 2026*
*Bagian dari Risk Profiler App — Indonesian Market Localization*
