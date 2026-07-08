# 🎯 Goal-Based Risk Need Calculator

> *"The return required to achieve investment goals."* — CFA Institute IRP Framework

---

## Daftar Isi

1. [Konsep Dasar](#konsep-dasar)
2. [Framework Akademis](#framework-akademis)
3. [Input & Alur Kerja](#input--alur-kerja)
4. [Perhitungan TVM](#perhitungan-tvm)
5. [Kategorisasi Risk Need](#kategorisasi-risk-need)
6. [Red Light Condition](#red-light-condition)
7. [Scoring Methodology](#scoring-methodology)
8. [Contoh Perhitungan](#contoh-perhitungan)
9. [Referensi](#referensi)

---

## Konsep Dasar

**Goal-Based Risk Need Calculator** menghitung **return minimum yang dibutuhkan** agar pengguna bisa mencapai setiap tujuan finansialnya. Ini bukan soal "mau ambil risiko berapa" — tapi seberapa besar return yang **harus** dikejar supaya goal-nya tercapai.

Setiap tujuan finansial diperlakukan **secara terpisah** (per-goal risk profiling), sesuai pendekatan goal-based investing dari Betterment.

### Mengapa Per-Goal?

| Pendekatan Lama | Pendekatan Goal-Based |
|---|---|
| Satu profil risiko untuk semua uang | Setiap goal punya profil risiko sendiri |
| Tidak jelas tujuan investasi | Tujuan spesifik: rumah, pensiun, nikah |
| Risiko dikira berdasarkan "perasaan" | Risiko dikira berdasarkan **kebutuhan return** |

---

## Framework Akademis

### CFA Institute IRP — Factor 1: Risk Need

CFA Institute Investment Risk Profiling (IRP) menetapkan bahwa Risk Need adalah faktor pertama dari tiga faktor utama:

1. **Risk Need** — return yang dibutuhkan untuk mencapai tujuan ← *ini yang dihitung*
2. **Risk Capacity** — kemampuan finansial untuk menanggung kerugian
3. **Risk Tolerance** — kenyamanan psikologis terhadap risiko

> ⚠️ **Aturan Kritis CFA:** Ketika Risk Need **melebihi** Risk Capacity, ini adalah kondisi **RED LIGHT** — artinya goal tersebut harus di-*adjust* (dikurangi targetnya, diperpanjang timeline-nya, atau ditambah kontribusinya).

### Betterment — Goal-Based Investing

Betterment menerapkan prinsip: **setiap goal mendapat alokasi aset yang berbeda** berdasarkan timeline dan targetnya.

- 🏠 Rumah (3 tahun) → lebih konservatif
- 👴 Pensiun (25 tahun) → lebih agresif
- 🎓 Pendidikan anak (15 tahun) → moderate

### Oxford Risk / FinaMetrica — Risk Required vs Risk Capacity

| Konsep | Definisi |
|---|---|
| **Risk Required** | Return minimum untuk mencapai goal (inilah yang kita hitung) |
| **Risk Capacity** | Kemampuan keuangan menanggung loss (dari questionnaire) |
| **Risk Tolerance** | Kenyamanan psikologis (dari questionnaire) |

> ✅ Investasi yang sehat: Risk Required **≤** Risk Capacity
> ❌ Investasi berbahaya: Risk Required **>** Risk Capacity

---

## Input & Alur Kerja

### Data yang Diinput Per Goal

```yaml
goal:
  nama: "Beli Rumah"          # Nama tujuan
  tipe: RUMAH                  # Tipe: RUMAH | PENSIUN | NIKAH | PENDIDIKAN | DANA_DARURAT | LAINNYA
  target_amount: 500_000_000   # Target dalam Rupiah
  timeline_years: 5            # Jangka waktu dalam tahun
  current_savings: 50_000_000  # Uang yang sudah ada (Rupiah)
  monthly_contribution: 5_000_000  # Setoran bulanan (Rupiah)
```

### Tipe Goal yang Didukung

| Tipe | Emoji | Deskripsi | Contoh Target |
|---|---|---|---|
| `RUMAH` | 🏠 | DP atau beli rumah | Rp 200.000.000 – Rp 2.000.000.000 |
| `PENSIUN` | 👴 | Dana pensiun | Rp 2.000.000.000 – Rp 20.000.000.000 |
| `NIKAH` | 💍 | Biaya pernikahan | Rp 100.000.000 – Rp 500.000.000 |
| `PENDIDIKAN` | 🎓 | Biaya pendidikan anak | Rp 500.000.000 – Rp 3.000.000.000 |
| `DANA_DARURAT` | 🛡️ | Dana darurat (6-12x pengeluaran) | Rp 30.000.000 – Rp 200.000.000 |
| `LAINNYA` | 📌 | Custom goal | Bebas |

### Alur Kerja

```
┌─────────────────────┐
│  User Input Goals   │
│  (Rupiah, timeline) │
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  Adjust for Inflasi │
│  (4% per tahun)     │
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  Hitung Required    │
│  Return per Goal    │
│  (TVM Formula)      │
└────────┬────────────┘
         ▼
┌─────────────────────────────┐
│  Kategorisasi Risk Need     │
│  RENDAH / SEDANG / TINGGI   │
└────────┬────────────────────┘
         ▼
┌─────────────────────────────────┐
│  Cross-check: Risk Need vs      │
│  Risk Capacity                  │
│  ✅ GREEN / 🔴 RED LIGHT        │
└─────────────────────────────────┘
```

---

## Perhitungan TVM

### Mengapa TVM?

Time Value of Money (TVM) adalah konsep bahwa uang hari ini bernilai lebih dari uang yang sama di masa depan, karena potensi pertumbuhan (return). Kita gunakan TVM untuk menghitung **real return** yang dibutuhkan.

### Formula

#### Step 1: Hitung Future Value yang Dibutuhkan (Inflation-Adjusted)

```
Future Value = Target Amount × (1 + inflation_rate)^timeline_years
```

Dengan asumsi inflasi Indonesia **4% per tahun**:

```
FV = Target × (1.04)^n
```

**Contoh:** Target Rp 500 juta dalam 5 tahun
```
FV = 500.000.000 × (1.04)^5
FV = 500.000.000 × 1.2167
FV = Rp 608.326.451
```

#### Step 2: Hitung Required Annual Return

Formula TVM dengan regular contributions (annuity):

```
FV = PV × (1 + r)^n + PMT × [((1 + r)^n - 1) / r]
```

Dimana:
- `FV` = Future Value target (inflation-adjusted)
- `PV` = Present Value (current savings)
- `PMT` = Monthly contribution × 12 (annual contribution)
- `r` = Required annual return (yang dicari)
- `n` = Timeline dalam tahun

Karena tidak bisa diselesaikan secara analitik (closed-form), kita gunakan **numerical iteration** (Newton-Raphson) untuk mencari nilai `r`.

#### Step 3: Konversi ke Real Return

```
Real Return = Nominal Return - Inflation Rate
```

Atau lebih tepatnya:

```
Real Return = ((1 + nominal_return) / (1 + inflation_rate)) - 1
```

> 📌 **Yang dikategorisasi adalah Real Return**, bukan nominal.

---

## Kategorisasi Risk Need

### Tiga Kategori Risk Need

| Kategori | Real Return | Interpretasi | Warna |
|---|---|---|---|
| **RENDAH** | < 5% | Goal bisa dicapai dengan instrumen konservatif | 🟢 Hijau |
| **SEDANG** | 5% – 10% | Butuh alokasi moderate (campuran obligasi & saham) | 🟡 Kuning |
| **TINGGI** | > 10% | Harus agresif — perlu ekuitas atau alternatif | 🔴 Merah |

### Mapping ke Instrumen Indonesia

| Kategori | Instrumen yang Cocok |
|---|---|
| **RENDAH** | Deposito, RDPU (Reksa Dana Pasar Uang), Obligasi Pemerintah (ORI/SBR) |
| **SEDANG** | Reksa Dana Campuran, Obligasi Korporasi, Emas, P2P Lending |
| **TINGGI** | Saham IDX, Reksa Dana Saham, Crypto, Startup Equity |

---

## Red Light Condition

### Apa Itu Red Light?

Ketika **Risk Need > Risk Capacity**, sistem menampilkan peringatan **RED LIGHT**. Ini sesuai dengan framework CFA Institute IRP yang menyatakan bahwa investor seharusnya tidak diarahkan ke portofolio yang lebih agresif dari kemampuannya.

```
┌──────────────────────────────────────────────┐
│  🔴 RED LIGHT ALERT                          │
│                                              │
│  Goal: Beli Rumah                            │
│  Required Return: 12.5% (TINGGI)            │
│  Your Risk Capacity: SEDANG (max 8%)        │
│                                              │
│  ⚠️  Goal ini TIDAK BISA dicapai dengan     │
│     profil risiko Anda saat ini.            │
│                                              │
│  💡 Rekomendasi:                             │
│  1. Tambah setoran bulanan                   │
│  2. Perpanjang timeline                      │
│  3. Kurangi target amount                    │
│  4. Tingkatkan current savings               │
└──────────────────────────────────────────────┘
```

### Resolusi Red Light

| Opsi | Formula Baru | Efek |
|---|---|---|
| **Tambah setoran** | Naikkan PMT | Risk Need turun |
| **Perpanjang timeline** | Naikkan n | Risk Need turun (compound effect) |
| **Kurangi target** | Turunkan FV | Risk Need turun |
| **Tambah modal** | Naikkan PV | Risk Need turun |

Sistem akan **menghitung ulang** dan menunjukkan berapa perubahan yang dibutuhkan untuk mencapai kondisi GREEN.

---

## Scoring Methodology

### Weighted Risk Need Score

Jika user memiliki **multiple goals**, skor keseluruhan dihitung dengan **weighted average** berdasarkan prioritas dan proporsi target amount:

```
Overall Risk Need Score = Σ (Weight_i × Risk Need Score_i)
```

Dimana:
```
Weight_i = Target Amount_i / Total All Targets
```

### Contoh:

| Goal | Target | Real Return | Kategori |
|---|---|---|---|
| Rumah | Rp 500.000.000 | 8.2% | SEDANG |
| Pensiun | Rp 5.000.000.000 | 6.5% | SEDANG |
| Nikah | Rp 200.000.000 | 11.3% | TINGGI |

```
Total = Rp 5.700.000.000

Weight Rumah   = 500/5700  = 0.088
Weight Pensiun = 5000/5700 = 0.877
Weight Nikah   = 200/5700  = 0.035

Overall = (0.088 × 8.2) + (0.877 × 6.5) + (0.035 × 11.3)
        = 0.72 + 5.70 + 0.40
        = 6.82% → SEDANG
```

---

## Contoh Perhitungan

### Kasus: Beli Rumah

**Input:**
```
Target:         Rp 500.000.000
Timeline:       5 tahun
Current Saving: Rp 50.000.000
Monthly:        Rp 5.000.000 (= Rp 60.000.000/tahun)
Inflasi:        4%
```

**Step 1: Inflation-Adjusted Target**
```
FV = 500.000.000 × (1.04)^5
FV = 500.000.000 × 1.21665
FV = Rp 608.326.451
```

**Step 2: Hitung Required Return (numerical)**
```
608.326.451 = 50.000.000 × (1+r)^5 + 60.000.000 × [((1+r)^5 - 1) / r]

Solving numerically:
r ≈ 7.1% (nominal)
```

**Step 3: Real Return**
```
Real Return = ((1.071) / (1.04)) - 1
Real Return = 0.0298 = 2.98%
```

**Result:**
```
┌────────────────────────────────┐
│  🏠 Goal: Beli Rumah          │
│                                │
│  Nominal Return:  7.1%         │
│  Real Return:     3.0%         │
│  Kategori:        🟢 RENDAH   │
│  Status:          ✅ GREEN     │
│                                │
│  💡 Bisa dicapai dengan        │
│     instrumen konservatif!     │
└────────────────────────────────┘
```

### Format Rupiah

Semua angka Rupiah diformat dengan:
- **Pemisah ribuan**: titik (`.`)
- **Desimal**: koma (`,`)
- **Prefix**: `Rp`
- **Contoh**: `Rp 608.326.451`

```
Format:  Rp {amount:,.0f}     → Rp 608.326.451
```

> Mengikuti standar **Bahasa Indonesia** (berbeda dari English yang pakai comma).

---

## Referensi

| # | Sumber | Key Insight |
|---|---|---|
| 1 | **CFA Institute — Investment Risk Profiling (IRP)** | Risk Need = return yang dibutuhkan; Factor 1 dari 3 |
| 2 | **Betterment — Goal-Based Investing** | Setiap goal punya risk profile terpisah |
| 3 | **Oxford Risk / FinaMetrica** | Risk Required vs Risk Capacity reconciliation |
| 4 | **Bank Indonesia — Inflasi** | Asumsi inflasi 4% per tahun |

---

*Last updated: Juli 2026*
*Bagian dari Risk Profiler App — Goal-Based Risk Need Calculator*
