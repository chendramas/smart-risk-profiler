# Deteksi Overconfidence: Metodologi dan Implementasi

> **"Overconfidence is the most common and most costly bias in investing. It causes investors to overestimate their knowledge, underestimate risks, and trade too frequently."**
> — Kahneman, D. & Riepe, M. (1998), "Aspects of Investor Behavior"

---

## Apa itu Overconfidence dalam Konteks Investasi?

Overconfidence adalah kecenderungan investor untuk **melebihi kemampuan sebenarnya** — baik dalam pengetahuan, kemampuan prediksi, maupun toleransi terhadap risiko.

Dalam konteks risk profiling, overconfidence berbahaya karena:
- Investor **mengklaim** bisa tahan penurunan 30%, padahal sebenarnya akan panic selling di 10%
- Skor risk tolerance **terinflate** 15-25% dari kondisi sebenarnya
- Portofolio yang dialokasikan menjadi **terlalu agresif** untuk profil risiko riil investor

> **Temuan Wealthfront:** *"Risk tolerance questionnaires consistently overstate actual risk tolerance by 15-25% due to overconfidence bias. Our methodology applies consistency checks to deflate these scores."*
> — Wealthfront Classic Portfolio Investment Methodology White Paper

---

## Mengapa Overconfidence Terjadi?

### 1. Illusion of Knowledge (Kahneman & Riepe, 1998)

Investor yang membaca berita keuangan atau punya pengalaman investasi **seadanya** merasa lebih tahu dari yang sebenarnya. Semakin banyak informasi (bahkan noise), semakin confident — padahal akurasi tidak naik.

> *"The illusion of knowledge — the feeling that one understands the world — is reinforced by the amount of information one has, even when that information is irrelevant."*
> — Kahneman, D. & Riepe, M. (1998)

### 2. Financial Literacy Paradox (Baker et al.)

Baker, H. Kent (dengan 609 citations pada riset financial literacy) menunjukkan **paradox menarik**:
- Investor dengan literasi keuangan **sedang** = paling overconfident
- Investor dengan literasi keuangan **tinggi** = lebih realistis (mereka tahu apa yang tidak mereka tahu)
- Investor dengan literasi keuangan **rendah** = tidak overconfident karena tidak tahu harus confident

### 3. Dunning-Kruger Effect dalam Investasi

Investor pemula yang baru belajar tentang saham sering mengalami Dunning-Kruger — merasa sudah paham padahal baru di permukaan. Ini menyebabkan mereka:
- Mengambil risiko berlebihan
- Tidak diversifikasi
- Mengabaikan risk management

---

## Metode Deteksi: Consistency Checks

### Prinsip Dasar

Overconfidence dideteksi dengan cara **cross-check jawaban** dari pertanyaan-pertanyaan yang secara logika harus konsisten. Jika ada inkonsistensi, kemungkinan besar jawaban yang lebih *agresif* adalah hasil overconfidence.

### Rule: Ketika Inkonsisten, Weight Jawaban yang LEBIH KONSERVATIF

```
IF answer_A (agresif) INCONSISTENT with answer_B (agresif):
    final_score = weight(MORE_CONSERVATIVE_answer)
    
REASON: The conservative answer is more likely to reflect true behavior under stress
```

---

## Consistency Check Pairs yang Diimplementasikan

### Check Pair 1: Composure vs Loss Tolerance

| Pertanyaan A (Skenario 1) | Pertanyaan B (Skenario 3) |
|---------------------------|--------------------------|
| "Tahan penurunan 30%" | "Tidak tahan rugi lebih dari beberapa hari" |

**Inkonsistensi:** Jika seseorang mengklaim tahan penurunan 30% (agresif) tetapi hanya bisa "menahan" kerugian beberapa hari (konservatif), maka ada ketidakcocokan.

**Aksi:** Weight jawaban yang lebih konservatif — "beberapa hari" → skor composure diturunkan.

**Analogi:** "Mau bilang tahan 30% drop, tapi kalau lihat portofolio merah 3 hari langsung jual" → yang benar adalah behavior 3 hari, bukan klaim tahan 30%.

---

### Check Pair 2: Risk Preference vs Financial Knowledge

| Pertanyaan A (Skenario 4/5) | Pertanyaan B (Skenario 7) |
|----------------------------|--------------------------|
| Pilih portofolio paling agresif | Tidak tahu jawaban literasi keuangan |

**Inkonsistensi:** Investor yang memilih portofolio sangat agresif tetapi tidak paham konsep dasar investasi (misalnya tidak tahu hubungan suku bunga dan harga obligasi) kemungkinan besar **overconfident**.

**Aksi:** Turunkan skor risk preference karena investor tidak benar-benar memahami risiko yang diambil.

**Analogi:** "Mau main F1 tapi tidak tahu cara kerja rem" → penurunan skor agresivitas.

---

### Check Pair 3: Experience vs Composure Claim

| Pertanyaan A (Skenario 8) | Pertanyaan B (Skenario 1) |
|---------------------------|--------------------------|
| "Belum pernah investasi" | "Tahan penurunan 30% dan tambah posisi" |

**Inkonsistensi:** Investor tanpa pengalaman yang mengklaim tahan penurunan besar kemungkinan besar **mengira** dia tahan, padahal belum pernah mengalaminya.

**Aksi:** Weight skor berdasarkan pengalaman — kurangi skor agresivitas karena tidak ada "scar tissue" yang membuktikan klaim.

**Analogi:** "Bilang tahan roller coaster tapi belum pernah naik" → sementara anggap skor moderat.

---

### Check Pair 4: Perception vs Preference

| Pertanyaan A (Skenario 6) | Pertanyaan B (Skenario 4) |
|---------------------------|--------------------------|
| "Pasar akan turun signifikan" | Pilih portofolio paling agresif |

**Inkonsistensi:** Investor yang pesimis terhadap pasar tetapi memilih portofolio agresif menunjukkan ketidakselarasan antara persepsi dan tindakan.

**Aksi:** Pertanyakan motivasi — mungkin ada framing effect atau social desirability bias.

---

### Check Pair 5: Duration Tolerance vs Emotional Reaction

| Pertanyaan A (Skenario 3) | Pertanyaan B (Skenario 1) |
|---------------------------|--------------------------|
| "Bisa tahan bertahun-tahun" | "Langsung jual semua kalau turun" |

**Inkonsistensi:** Mengklaim bisa tahan lama tetapi reaksi pertama adalah jual semua.

**Aksi:** Weight jawaban Skenario 1 (behavioral reaction) lebih tinggi dari Skenario 3 (stated preference), karena behavioral lebih predictive.

---

## Skor Overconfidence

### Kalkulasi Overconfidence Score

```
overconfidence_score = count(inconsistent_pairs) / total_pairs

IF overconfidence_score > 0.5:
    adjustment = -25%  (maximum deflation)
ELIF overconfidence_score > 0.3:
    adjustment = -15%  (moderate deflation)
ELIF overconfidence_score > 0.1:
    adjustment = -10%  (light deflation)
ELSE:
    adjustment = 0%    (consistent answers, no adjustment)
```

### Contoh Kasus

**Investor X:**
- Skenario 1: "Tahan 30% drop, tambah posisi" → Agresif (skor: 9/10)
- Skenario 3: "Hanya tahan beberapa hari" → Konservatif (skor: 3/10)
- Skenario 7: "Tidak tahu jawaban" → Low knowledge (skor: 2/10)
- Skenario 8: "Belum pernah investasi" → No experience (skor: 1/10)

**Consistency checks:**
- Check 1 (Composure vs Duration): INCONSISTEN ❌
- Check 2 (Preference vs Knowledge): INCONSISTEN ❌
- Check 3 (Experience vs Composure): INCONSISTEN ❌

**Overconfidence score:** 3/3 = 100% → Adjustment: **-25%**

**Hasil:**
- Skor asli: 9/10 → Disesuaikan: 6.75/10
- Profil berubah dari "Agresif" menjadi "Moderat-Agresif"

---

## Implementasi dalam Aplikasi

### Flow Diagram

```
┌─────────────────────────┐
│   User menjawab 8       │
│   skenario behavioral   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Hitung raw scores     │
│   untuk setiap skenario │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Jalankan 5 consistency│
│   check pairs           │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Hitung overconfidence │
│   score (0-100%)        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Apply adjustment      │
│   (-0% to -25%)         │
│   ke risk tolerance     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Final behavioral      │
│   loss tolerance score  │
└─────────────────────────┘
```

---

## Referensi

Lihat [08_references.md](./08_references.md) untuk daftar referensi lengkap.

---

*Dokumen ini merupakan bagian dari dokumentasi teknis Risk Profiler App.*
*Terakhir diperbarui: Juli 2026*
