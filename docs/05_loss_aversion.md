# Loss Aversion: Mengukur Koefisien Aversi Kerugian

> **"Losses loom larger than gains. The pain of losing Rp 1 juta is approximately 2 to 2.5 times greater than the pleasure of gaining Rp 1 juta."**
> — Kahneman, D. & Tversky, A. (1979), "Prospect Theory: An Analysis of Decision under Risk", Econometrica 47(2): 263-291

---

## Apa itu Loss Aversion?

Loss aversion adalah fenomena behavioral di mana **rasa sakit kehilangan** (loss) dirasakan **lebih kuat** daripada **rasa senang mendapatkan** (gain) dengan jumlah yang sama.

### Koefisien Loss Aversion (λ)

Kahneman & Tversky (1979) menemukan koefisien loss aversion **λ ≈ 2.0 - 2.5**, artinya:

```
Pain of losing Rp 1.000.000 ≈ 2.0-2.5 × Pleasure of gaining Rp 1.000.000
```

Ini berarti seseorang perlu **potensi gain Rp 2-2.5 juta** untuk mau menerima **risiko kerugian Rp 1 juta**.

### Fungsi Nilai S-Shape (Value Function)

```
         Gain
          │      ╱ (concave — diminishing sensitivity)
          │    ╱
          │  ╱
          │╱
──────────┼──────────── Outcome
         ╱│
       ╱  │
     ╱    │ (convex — increasing sensitivity)
   ╱      │
 Loss
```

Karakteristik fungsi nilai Prospect Theory:
- **Concave untuk gains** — semakin besar gain, semakin kurang puas per Rupiah tambahan
- **Convex untuk losses** — semakin besar loss, semakin sakit per Rupiah tambahan
- **Steeper di sisi loss** — inilah yang menyebabkan loss aversion

---

## Mengapa Loss Aversion Penting untuk Risk Profiling?

Loss aversion adalah **prediktor #1 dari panic selling behavior**. Investor dengan loss aversion tinggi akan:

1. **Menjual di harga terendah** — karena tidak tahan melihat kerugian
2. **Melewatkan recovery** — setelah jual, pasar naik, tapi sudah tidak punya posisi
3. **Mengalami regret** — menyesal jual di bawah, lalu tidak berani masuk lagi
4. **Underperform jangka panjang** — karena selalu beli tinggi (saat optimis) dan jual rendah (saat takut)

> **Temuan:** Investor dengan loss aversion tinggi (λ > 2.5) mengalami **underperformance 3-4% per tahun** dibandingkan investor dengan loss aversion normal, karena pattern beli-tinggi-jual-rendah.
> — Referensi: Behavioral finance literature (Odean, 1998; Barber & Odean, 2000)

---

## Metode Pengukuran: 3 Lottery-Style Scenarios

Pengukuran loss aversion menggunakan **3 skenario lotere** yang diadaptasi dari risk elicitation tasks dalam literatur akademik. Setiap skenario mengukur **trade-off antara gain pasti dan loss potensial**.

### Skenario 1: Gain Pasti vs Gamble (Low Stakes)

**Pertanyaan:**
> "Kamu diberi dua pilihan:
>
> **Pilihan A:** Terima **Rp 2.000.000** PASTI
>
> **Pilihan B:** Lempar koin:
> - Kalau menang: dapat **Rp 5.000.000**
> - Kalau kalah: dapat **Rp 0** (tidak dapat apa-apa, tidak rugi)
>
> Expected value Pilihan B = Rp 2.500.000 (lebih tinggi dari A). Pilih mana?"

**Pilihan jawaban:**
- A. Pilih A — Rp 2 juta pasti
- B. Pilih B — gamble dengan expected value lebih tinggi

**Yang diukur:**
- Risk aversion terhadap **pure gain gamble**
- Ini adalah baseline — TIDAK mengukur loss aversion secara langsung
- Digunakan sebagai **control** untuk skenario 2 dan 3

**Sumber:**
> Adapted from Kahneman & Tversky (1979) — certainty effect
> Classic risk elicitation task dalam behavioral economics

---

### Skenario 2: Mixed Gamble — Low Loss Aversion Test

**Pertanyaan:**
> "Kamu diberi dua pilihan:
>
> **Pilihan A:** Terima **Rp 1.500.000** PASTI
>
> **Pilihan B:** Lempar koin:
> - Kalau menang: dapat **Rp 4.000.000**
> - Kalau kalah: **kehilangan Rp 1.000.000**
>
> Expected value Pilihan B = Rp 1.500.000 (sama dengan A). Pilih mana?"

**Pilihan jawaban:**
- A. Pilih A — Rp 1.5 juta pasti
- B. Pilih B — gamble dengan EV sama

**Yang diukur:**
- Loss aversion dalam **mixed domain** (ada gain DAN loss)
- Jika memilih A meskipun EV sama → loss averse
- Jika memilih B → loss neutral atau loss seeking

**Sumber:**
> Kahneman & Tversky (1979): mixed gamble paradigm
> Tversky & Kahneman (1992): Cumulative Prospect Theory

---

### Skenario 3: Mixed Gamble — High Loss Aversion Test

**Pertanyaan:**
> "Kamu diberi dua pilihan:
>
> **Pilihan A:** Terima **Rp 500.000** PASTI
>
> **Pilihan B:** Lempar koin:
> - Kalau menang: dapat **Rp 5.000.000**
> - Kalau kalah: **kehilangan Rp 3.000.000**
>
> Expected value Pilihan B = Rp 1.000.000 (lebih tinggi dari A). Pilih mana?"

**Pilihan jawaban:**
- A. Pilih A — Rp 500 ribu pasti
- B. Pilih B — gamble dengan EV lebih tinggi, tapi downside besar

**Yang diukur:**
- Loss aversion dalam **high-stakes mixed gamble**
- Meskipun EV B lebih tinggi, potensi loss Rp 3 juta bisa terasa sangat berat
- Jika memilih A → **high loss aversion** (λ > 2.5)
- Jika memilih B → **moderate/low loss aversion** (λ < 2.0)

**Sumber:**
> Kahneman & Tversky (1979): "losses loom larger than gains"
> High-stakes risk elicitation tasks dalam experimental economics

---

## Kalkulasi Koefisien Loss Aversion (λ)

### Method

Koefisien loss aversion dihitung berdasarkan kombinasi jawaban dari ketiga skenario:

| Jawaban S1 | Jawaban S2 | Jawaban S3 | Interpretasi | λ Estimate |
|-----------|-----------|-----------|-------------|-----------|
| A (safe) | A (safe) | A (safe) | **Sangat loss averse** | λ > 3.0 |
| A (safe) | A (safe) | B (gamble) | **Loss averse** | λ ≈ 2.0-2.5 |
| A (safe) | B (gamble) | B (gamble) | **Moderate loss aversion** | λ ≈ 1.5-2.0 |
| B (gamble) | B (gamble) | B (gamble) | **Loss neutral** | λ ≈ 1.0 |
| B (gamble) | B (gamble) | A (safe) | **Unusual pattern** — check consistency |

### Mapping ke Risk Profile Impact

| λ Estimate | Loss Aversion Level | Impact pada Risk Profile |
|-----------|--------------------|-----------------------|
| λ > 3.0 | Sangat Tinggi | **Turunkan** risk tolerance 2 level |
| λ 2.5 - 3.0 | Tinggi | **Turunkan** risk tolerance 1 level |
| λ 2.0 - 2.5 | Normal | **Tidak ada adjustment** |
| λ 1.5 - 2.0 | Rendah | Bisa sedikit **naikkan** risk tolerance |
| λ < 1.5 | Sangat Rendah | **Flag**: mungkin risk-seeking behavior |

---

## Integrasi dengan Behavioral Scenarios

Loss aversion score dari modul ini **dikombinasikan** dengan Risk Composure (Skenario 1-3) untuk menghasilkan final Behavioral Loss Tolerance:

```
behavioral_loss_tolerance = weighted_average(
    risk_composure_score   (skenario 1-3)  × 50%,
    loss_aversion_score    (skenario LA)   × 30%,
    risk_preference_score  (skenario 4-5)  × 20%
)
```

**Mengapa loss aversion mendapat bobot 30%?**
Karena loss aversion adalah prediktor terkuat untuk panic selling — perilaku yang paling merusak bagi return jangka panjang.

---

## Studi Pendukung

### Walasek & Stewart (2014)
- Menemukan bahwa loss aversion adalah **property of experimental design**, bukan trait yang tetap
- Implikasi: skenario yang berbeda bisa menghasilkan skor berbeda → penting untuk menggunakan **multiple scenarios**
- Itulah mengapa kita menggunakan **3 skenario**, bukan 1

### De Baets (2012) — Loss Aversion Questionnaire (LAQ)
- Mengembangkan kuesioner spesifik untuk mengukur loss aversion
- Menemukan bahwa loss aversion bervariasi berdasarkan domain (finansial vs non-finansial)
- Aplikasi ini fokus pada **domain finansial** dengan Rupiah amounts

---

## Referensi

Lihat [08_references.md](./08_references.md) untuk daftar referensi lengkap.

---

*Dokumen ini merupakan bagian dari dokumentasi teknis Risk Profiler App.*
*Terakhir diperbarui: Juli 2026*
