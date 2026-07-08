# Skenario Behavioral: 8 Pertanyaan Profil Risiko

> **"Risk composure — how an investor has actually behaved during past losses — is more predictive of future behavior than their stated risk preference."**
> — Grable & Hubble, CFA Institute Research Foundation (2020)

---

## Mengapa Behavioral Scenarios?

Sebagian besar risk profiler tradisional hanya menanyakan: *"Seberapa besar risiko yang kamu inginkan?"* — ini menghasilkan jawaban yang **bias** karena:

1. **Overconfidence** — investor cenderung melebihi toleransi risiko sebenarnya
2. **Social desirability** — menjawab "agresif" karena terlihat keren
3. **Anchoring** — terpengaruh angka yang disebutkan sebelumnya
4. **Recency bias** — terpengaruh kondisi pasar terkini

Framework CFA Institute menggunakan **8 komponen Behavioral Loss Tolerance** yang mengukur perilaku riil, bukan niat. Aplikasi ini mengimplementasikan 8 skenario berdasarkan komponen-komponen tersebut.

---

## Kategori 1: Risk Composure (Ketahanan Emosional)

### Skenario 1: Reaksi terhadap Penurunan Portofolio

**Pertanyaan:**
> "Bayangkan investasi kamu senilai Rp 100 juta turun menjadi Rp 70 juta dalam waktu 2 minggu (turun 30%). Apa yang paling mungkin kamu lakukan?"

**Pilihan jawaban:**
- A. Langsung jual semua — saya tidak mau rugi lebih dalam
- B. Jual sebagian untuk mengurangi risiko
- C. Tidak melakukan apa-apa — tunggu dan lihat
- D. Tambah investasi — ini kesempatan beli murah

**Mengapa ditanyakan:**
Skenario ini mengukur **risk composure** — reaksi emosional riil terhadap kerugian besar. CFA Institute menekankan bahwa ini adalah prediktor paling kuat untuk perilaku masa depan.

**Apa yang diukur:**
- Kemampuan menahan panic selling
- Orientasi jangka panjang vs jangka pendek
- Emotional regulation saat investasi rugi

**Sumber:**
> CFA Institute IRP Factor 3, Component 1: Risk Tolerance
> CFA Institute IRP Factor 3, Component 2: Risk Composure
> Hubble, Grable & Dannhauser (2020): *"Past behavior during market downturns is the single best predictor of future behavior."*

---

### Skenario 2: Pengalaman Kerugian Masa Lalu

**Pertanyaan:**
> "Pernahkah kamu mengalami kerugian investasi lebih dari 20%? Jika ya, apa yang kamu lakukan?"

**Pilihan jawaban:**
- A. Belum pernah mengalami kerugian signifikan
- B. Pernah, dan saya langsung jual semua
- C. Pernah, dan saya jual sebagian
- D. Pernah, dan saya pertahankan semua posisi
- E. Pernah, dan saya tambah posisi (average down)

**Mengapa ditanyakan:**
Pengalaman kerugian masa lalu membentuk "scar tissue" yang memengaruhi reaksi di masa depan. Investor yang pernah mengalami crash dan berhasil melewatinya cenderung lebih tenang di crash berikutnya.

**Apa yang diukur:**
- Pengalaman riil dengan kerugian
- Pola coping behavior
- Resiliensi investasi

**Sumber:**
> CFA Institute IRP Factor 3, Component 6: Investing Experience ("scar tissue" concept)
> Grable & Lytton (1999): *"Prior investment experience, particularly negative experience, significantly influences risk tolerance."*

---

### Skenario 3: Durasi Tahan Kerugian

**Pertanyaan:**
> "Berapa lama kamu bisa melihat portofolio kamu merah (rugi) tanpa melakukan apa-apa?"

**Pilihan jawaban:**
- A. Beberapa hari — saya cek portofolio setiap hari
- B. Beberapa minggu — tapi mulai tidak nyaman
- C. Beberapa bulan — saya bisa tunggu
- D. Tahunan — saya investasi jangka panjang

**Mengapa ditanyakan:**
Durasi seseorang bisa "menahan" kerugian tanpa bertindak adalah indikator kuat dari behavioral loss tolerance. Investor yang hanya bisa tahan beberapa hari akan cenderung panic selling.

**Apa yang diukur:**
- Time horizon emosional (bukan time horizon finansial)
- Frekuensi monitoring (over-monitoring → over-trading)
- Kemampuan "duduk diam" selama drawdown

**Sumber:**
> CFA Institute IRP Factor 3, Component 2: Risk Composure
> Barber & Odean (2000): *"Trading is hazardous to your wealth"* — investor yang sering monitor cenderung over-trade

---

## Kategori 2: Risk Preference (Preferensi Risiko)

### Skenario 4: Preferensi Portofolio

**Pertanyaan:**
> "Dari pilihan portofolio berikut, mana yang paling membuat kamu nyaman?"

**Pilihan jawaban:**
- A. Portofolio yang paling buruk: -5%, paling baik: +10% (ekspektasi: +5%)
- B. Portofolio yang paling buruk: -15%, paling baik: +25% (ekspektasi: +8%)
- C. Portofolio yang paling buruk: -30%, paling baik: +45% (ekspektasi: +12%)
- D. Portofolio yang paling buruk: -50%, paling baik: +70% (ekspektasi: +15%)

**Mengapa ditanyakan:**
Ini adalah **classic risk preference elicitation** — mengukur trade-off antara potensi gain dan potensi loss. Berbeda dari skenario 1 yang mengukur reaksi, skenario ini mengukur *preferensi* proaktif.

**Apa yang diukur:**
- Risk-return trade-off preference
- Variasi toleransi terhadap volatility
- Orientasi terhadap downside vs upside

**Sumber:**
> CFA Institute IRP Factor 3, Component 3: Risk Preference
> Merrill Edge risk preference methodology
> Grable & Lytton (1999): Risk Tolerance Scale

---

### Skenario 5: Guaranteed vs Uncertain Outcome (Tes Expected Utility)

**Pertanyaan:**
> "Kamu diberi dua pilihan:
> - **Pilihan A:** Terima Rp 50 juta PASTI
> - **Pilihan B:** Lempar koin — kalau menang dapat Rp 120 juta, kalau kalah dapat Rp 0
>
> Nilai expected dari Pilihan B = Rp 60 juta (lebih tinggi dari A). Pilih mana?"

**Pilihan jawaban:**
- A. Pilih A — Rp 50 juta pasti lebih baik
- B. Pilih B — expected value lebih tinggi, worth the risk

**Mengapa ditanyakan:**
Ini adalah **tes expected utility klasik** yang berasal dari riset Kahneman & Tversky (1979). Sebagian besar orang memilih A meskipun B secara matematis lebih menguntungkan — ini menunjukkan **loss aversion**.

**Apa yang diukur:**
- Aversion terhadap ketidakpastian
- Deviasi dari expected utility theory
- Sensitivity terhadap worst-case scenario

**Sumber:**
> Kahneman & Tversky (1979) — Prospect Theory
> CFA Institute IRP Factor 3, Component 3: Risk Preference
> Classic expected utility test dalam behavioral economics

---

## Kategori 3: Risk Perception (Persepsi Pasar)

### Skenario 6: Persepsi terhadap Pasar Saham

**Pertanyaan:**
> "Menurut kamu, pasar saham Indonesia (IHSG) dalam 12 bulan ke depan akan..."

**Pilihan jawaban:**
- A. Naik signifikan (>10%)
- B. Naik sedikit (3-10%)
- C. Sideways (-3% sampai +3%)
- D. Turun sedikit (-3% sampai -10%)
- E. Turun signifikan (> -10%)

**Mengapa ditanyakan:**
Risk perception — bagaimana investor melihat kondisi pasar — memengaruhi keputusan investasi secara langsung. Investor yang pesimis cenderung lebih konservatif dari yang seharusnya.

**Apa yang diukur:**
- Optimisme/pesimisme terhadap pasar
- Pengaruh media dan noise terhadap persepsi
- Anchoring pada kondisi pasar terkini (recency bias)

**Sumber:**
> CFA Institute IRP Factor 3, Component 4: Risk Perception
> *"Investors' perception of market conditions is often anchored to recent performance, leading to pro-cyclical behavior."*

---

## Kategori 4: Financial Knowledge (Pengetahuan Finansial)

### Skenario 7: Tes Literasi Keuangan

**Pertanyaan:**
> "Pilih jawaban yang benar: Jika kamu memiliki obligasi pemerintah (ORI) dengan kupon 6% per tahun, dan suku bunga Bank Indonesia naik dari 5% menjadi 7%, maka harga obligasi kamu di pasar sekunder akan..."

**Pilihan jawaban:**
- A. Naik
- B. Turun
- C. Tetap sama
- D. Tidak tahu

**Mengapa ditanyakan:**
Financial knowledge adalah komponen kunci dari risk profiling karena investor yang **tidak paham** produk investasinya lebih cenderung membuat keputusan berdasarkan emosi. Baker et al. menunjukkan bahwa literasi keuangan yang rendah berkorelasi dengan overconfidence — semakin tidak tahu, semakin yakin.

**Apa yang diukur:**
- Pemahaman konsep dasar investasi (inverse relationship bond price-interest rate)
- Literasi finansial fungsional
- Kesiapan untuk berinvestasi di produk yang lebih kompleks

**Sumber:**
> CFA Institute IRP Factor 3, Component 5: Financial Knowledge
> Baker, H. Kent et al. — financial literacy research (609 citations)
> Hasanah, Wiryono & Koesrindartoto (2024) — financial literacy questions in robo-advisor

---

## Kategori 5: Investing Experience (Pengalaman Investasi)

### Skenario 8: Pengalaman Investasi

**Pertanyaan:**
> "Produk investasi apa saja yang pernah kamu miliki? (Pilih semua yang berlaku)"

**Pilihan jawaban:**
- [ ] Tabungan / Deposito
- [ ] Reksa Dana (Pasar Uang / Pendapatan Tetap)
- [ ] Reksa Dana (Saham / Campuran)
- [ ] Obligasi Pemerintah (ORI / SBR / Sukuk)
- [ ] Sahham individu (IDX)
- [ ] Emas / Logam Mulia
- [ ] Cryptocurrency
- [ ] Properti (investasi, bukan tempat tinggal utama)
- [ ] Forex / Komoditas
- [ ] Belum pernah investasi sama sekali

**Mengapa ditanyakan:**
CFA Institute menjelaskan konsep **"scar tissue"** — pengalaman investasi membentuk respons emotional di masa depan. Investor yang pernah rugi di saham akan punya "scar tissue" yang membuatnya lebih berhati-hati (atau terlalu takut) di investasi berikutnya.

**Apa yang diukur:**
- Breadth of investment experience
- Kompleksitas produk yang pernah digunakan
- Kesiapan untuk produk investasi yang lebih sophisticated
- Scar tissue dari pengalaman negatif

**Sumber:**
> CFA Institute IRP Factor 3, Component 6: Investing Experience
> *"Investors who have experienced market crashes develop 'scar tissue' — either healthy caution or debilitating fear, depending on how the experience was processed."*

---

## Matriks Skenario vs Komponen CFA IRP

| Skenario | Komponen CFA IRP | Dimensi | Bobot Relatif |
|----------|-------------------|---------|---------------|
| 1. Reaksi penurunan | F3-C1: Risk Tolerance | Behavioral | ⭐⭐⭐⭐⭐ |
| 2. Pengalaman kerugian | F3-C2: Risk Composure | Behavioral | ⭐⭐⭐⭐ |
| 3. Durasi tahan rugi | F3-C2: Risk Composure | Behavioral | ⭐⭐⭐⭐ |
| 4. Preferensi portofolio | F3-C3: Risk Preference | Behavioral | ⭐⭐⭐ |
| 5. Guaranteed vs uncertain | F3-C3: Risk Preference | Behavioral | ⭐⭐⭐ |
| 6. Persepsi pasar | F3-C4: Risk Perception | Behavioral | ⭐⭐ |
| 7. Literasi keuangan | F3-C5: Financial Knowledge | Behavioral | ⭐⭐⭐ |
| 8. Pengalaman investasi | F3-C6: Investing Experience | Behavioral | ⭐⭐⭐ |

> **Catatan:** Skenario 1 (reaksi terhadap penurunan) diberikan bobot tertinggi karena paling predictive terhadap perilaku riil.

---

## Referensi

Lihat [08_references.md](./08_references.md) untuk daftar referensi lengkap.

---

*Dokumen ini merupakan bagian dari dokumentasi teknis Risk Profiler App.*
*Terakhir diperbarui: Juli 2026*
