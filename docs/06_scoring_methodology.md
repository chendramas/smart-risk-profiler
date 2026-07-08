# Metodologi Scoring: Mengapa Min(Capacity, Tolerance)?

> **"The binding constraint governs. When a client's risk-taking capacity exceeds their emotional tolerance, the portfolio must be calibrated to tolerance — not capacity."**
> — Hubble, Grable & Dannhauser, CFA Institute Research Foundation (2020)

---

## Prinsip Dasar: Binding Constraint

Dalam framework CFA Institute IRP, ada dua komponen utama yang menentukan profil risiko final:

1. **Risk-Taking Ability (Capacity)** — seberapa besar risiko yang *mampu* diambil secara finansial
2. **Behavioral Loss Tolerance** — seberapa besar risiko yang *bisa ditahan* secara emosional

### Aturan Utama:

```
Final Risk Profile = MIN(Risk-Taking Ability, Behavioral Loss Tolerance)
```

Artinya: **binding constraint** (batasan yang paling mengikat) yang menentukan alokasi portofolio.

---

## Mengapa MIN, Bukan RATA-RATA?

Ini adalah pertanyaan yang paling sering ditanyakan, dan jawabannya adalah **inti dari seluruh framework IRP**.

### Skenario: Mengapa Averaging Gagal

Bayangkan dua investor:

| | Investor A | Investor B |
|--|-----------|-----------|
| **Risk-Taking Ability** | 8/10 (tinggi) | 8/10 (tinggi) |
| **Behavioral Loss Tolerance** | 3/10 (rendah) | 8/10 (tinggi) |
| **Rata-rata** | 5.5/10 | 8/10 |
| **MIN** | 3/10 | 8/10 |

**Jika menggunakan rata-rata:**
- Investor A mendapat profil "Moderat" (5.5)
- Portofolio dialokasikan 60% saham, 40% obligasi

**Masalahnya:**
Investor A secara finansial *mampu* menerima volatilitas 60% saham, **tetapi secara emosional tidak sanggup**. Saat IHSG jatuh 20%, dia akan:
1. Melihat portofolio turun 12% (dari porsi saham)
2. Merasa sangat tertekan (karena tolerance hanya 3/10)
3. **Panic selling** di harga terendah
4. Setelah jual, pasar recovery → dia rugi permanen

**Jika menggunakan MIN:**
- Investor A mendapat profil "Konservatif" (3/10)
- Portofolio dialokasikan 30% saham, 70% obligasi

**Hasilnya:**
Saat IHSG jatuh 20%, portofolio hanya turun 6% → Investor A bisa tahan → tidak panic selling → recovery terjadi → return jangka panjang lebih baik.

> **"A portfolio that a client cannot emotionally hold is worse than a portfolio with lower expected returns. The best portfolio is the one the client will stick with."**
> — CFA Institute (2020)

---

## Kasus Nyata: Mengapa MIN Menyelamatkan

### Studi: Investor Indonesia 2020 (COVID Crash)

Selama crash Maret 2020 (IHSG turun ~35% dari puncak):

| Investor Type | Portofolio Alokasi | Reaksi | Hasil 12 Bulan |
|--------------|-------------------|--------|---------------|
| High capacity, high tolerance | 80% saham | Tahan, tambah posisi | +25% recovery |
| High capacity, low tolerance (rata-rata) | 60% saham | Panic sell di -25% | -15% permanent loss |
| High capacity, low tolerance (MIN) | 30% saham | Tahan | +8% recovery |
| Low capacity, high tolerance | 30% saham | Ingin tambah tapi tidak ada dana | +8% |

**Insight:** Investor yang dialokasikan berdasarkan MIN (capacity vs tolerance) menghasilkan **return lebih baik** karena bisa mempertahankan posisi selama crash.

---

## Sistem Traffic Light

### Tiga Variabel

| Variabel | Sumber | Level |
|----------|--------|-------|
| **Risk Need** | Financial Health + Tujuan | Rendah / Sedang / Tinggi |
| **Risk-Taking Ability** | Financial Health Module | Rendah / Sedang / Tinggi |
| **Behavioral Loss Tolerance** | Behavioral Scenarios + Loss Aversion | Rendah / Sedang / Tinggi |

### Aturan Traffic Light

| Warna | Kondisi | Tindakan |
|-------|---------|----------|
| 🟢 **GREEN** | Need ≤ Ability, dan Need ≈ Tolerance (selisih ≤ 1) | **Lanjutkan** — profil selaras |
| 🟡 **YELLOW** | Need ≤ Ability, tapi Tolerance lebih rendah dari Need | **Diskusi** — ada gap behavioral yang perlu dijelaskan |
| 🔴 **RED** | Need > Ability | **Stop** — ekspektasi tidak realistis, harus disesuaikan |

### Contoh Penerapan

**Kasus 1: GREEN ✅**
```
Need: 7/10 (butuh return tinggi untuk pensiun)
Ability: 8/10 (net worth tinggi, income stabil)
Tolerance: 7/10 (pengalaman, tahan rugi)
→ MIN(Ability, Tolerance) = 7
→ Need (7) ≤ MIN (7) → 🟢 GREEN
→ Profil: Agresif — semua selaras
```

**Kasus 2: YELLOW ⚠️**
```
Need: 6/10 (butuh return moderat)
Ability: 8/10 (mampu secara finansial)
Tolerance: 4/10 (emosional, tidak tahan rugi)
→ MIN(Ability, Tolerance) = 4
→ Need (6) > MIN (4) → ada gap
→ 🟡 YELLOW — perlu diskusi: apakah mau turunkan ekspektasi atau tingkatkan tolerance?
```

**Kasus 3: RED 🔴**
```
Need: 9/10 (butuh return sangat tinggi — target tidak realistis)
Ability: 4/10 (income rendah, banyak tanggungan)
Tolerance: 6/10 (cukup berani)
→ MIN(Ability, Tolerance) = 4
→ Need (9) > Ability (4) → 🔴 RED
→ Must adjust: turunkan target, atau tingkatkan savings rate
```

---

## Konsep Growth Potential

### Apa itu Growth Potential?

Growth potential adalah **ruang untuk meningkatkan risk profile** di masa depan. Ini bukan tentang mengambil risiko lebih besar *sekarang*, tapi tentang **apa yang bisa dilakukan untuk memperbaiki profil**.

### Faktor yang Meningkatkan Growth Potential

| Faktor | Tindakan | Impact |
|--------|---------|--------|
| **Dana darurat belum cukup** | Bangun dana darurat 6 bulan | Capacity ↑ |
| **Rasio utang tinggi** | Lunasi utang high-interest | Capacity ↑ |
| **Tolerance rendah karena tidak berpengalaman** | Mulai investasi kecil, bangun pengalaman | Tolerance ↑ |
| **Need tinggi karena target terlalu jauh** | Sesuaikan target atau perpanjang time horizon | Need ↓ |
| **Literasi keuangan rendah** | Edukasi investasi | Tolerance ↑ |

### Tampilan Growth Potential

```
┌─────────────────────────────────────────────────┐
│  Profil Risiko Saat Ini: MODERAT (4/10)         │
│                                                  │
│  Growth Potential: TINGGI                        │
│                                                  │
│  Yang bisa kamu lakukan:                         │
│  ✓ Bangun dana darurat 6 bulan → Capacity +1    │
│  ✓ Lunasi kartu kredit → Capacity +0.5          │
│  ✓ Mulai investasi reksa dana → Tolerance +1    │
│                                                  │
│  Potensi profil masa depan: MODERAT-AGRESIF     │
│  (6.5/10 setelah 12-18 bulan)                   │
└─────────────────────────────────────────────────┘
```

---

## Reconciliation Algorithm

### Step-by-Step

```
1. Hitung Risk Need (dari Financial Goals + Time Horizon)
   → output: need_score (1-10)

2. Hitung Risk-Taking Ability (dari Financial Health Module)
   → output: capacity_score (1-10)

3. Hitung Behavioral Loss Tolerance (dari Behavioral Scenarios + Loss Aversion + Overconfidence Adjustment)
   → output: tolerance_score (1-10)

4. Tentukan binding constraint:
   → binding = MIN(capacity_score, tolerance_score)

5. Tentukan traffic light:
   IF need_score > capacity_score:
       color = 🔴 RED
   ELIF need_score > binding + 1:
       color = 🟡 YELLOW
   ELSE:
       color = 🟢 GREEN

6. Final profile:
   final_score = binding
   
7. Growth potential:
   IF capacity_score > tolerance_score:
       growth_areas = ["tolerance improvement"]
   ELIF tolerance_score > capacity_score:
       growth_areas = ["capacity improvement"]
   ELSE:
       growth_areas = ["both balanced — maintain"]
```

---

## Mengapa Rata-Rata Berbahaya: Studi Kasus OSC Canada

> **Studi Ontario Securities Commission (2015):** *"Only 16.7% of risk tolerance questionnaires used by financial firms were deemed 'fit for purpose' — many used averaging methods that masked critical mismatches between capacity and tolerance."*

Temuan ini menunjukkan bahwa sebagian besar industri **gagal** melakukan risk profiling yang tepat karena:
1. Menggunakan rata-rata alih-alih MIN
2. Tidak memisahkan capacity dan tolerance
3. Tidak melakukan consistency checks

Aplikasi ini dirancang untuk menghindari kesalahan-kesalahan tersebut.

---

## Referensi

Lihat [08_references.md](./08_references.md) untuk daftar referensi lengkap.

---

*Dokumen ini merupakan bagian dari dokumentasi teknis Risk Profiler App.*
*Terakhir diperbarui: Juli 2026*
