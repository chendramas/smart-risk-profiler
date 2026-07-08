# Smart Risk Profiler

https://smart-risk-profiler.streamlit.app

Alat profiling risiko investasi untuk advisor dan investor retail. Input data diri, jawab skenario behavioral, dapatkan profil risiko lengkap dengan rekomendasi alokasi aset.

## Apa yang didapat user

- **Risk Number 1-99** — skor kontinu yang langsung bisa dipahami, bukan cuma label konservatif/moderat/agresif
- **Rekomendasi alokasi aset** — persentase per instrumen (RDPU, obligasi, saham, emas, crypto) sesuai profil
- **Behavioral breakdown** — radar chart 5 komponen: ketahanan emosional, preferensi risiko, persepsi pasar, pengetahuan finansial, pengalaman investasi
- **Capacity vs Tolerance** — apakah user mampu secara finansial atau hanya berani secara psikologis
- **Financial health score** — skor kesehatan finansial dari 5 pertanyaan objektif
- **Loss aversion coefficient** — berapa x lebih sakit loss dibanding gain (Kahneman)
- **Goal-based analysis** — return yang dibutuhkan per tujuan finansial (rumah, nikah, pensiun, dll)
- **Traffic light reconciliation** — apakah semua faktor sejalan atau ada kontradiksi
- **Export** — download hasil sebagai .txt atau kartu .png

## Untuk siapa

- **Financial advisor** — tool profiling klien sebelum rekomendasi investasi
- **Investor retail** — self-assessment sebelum mulai investasi
- **Edukasi** — belajar risk tolerance dan behavioral finance

## Framework

Semua pertanyaan dan scoring berdasarkan:
- CFA Institute Investment Risk Profile (IRP)
- Kahneman & Tversky Prospect Theory
- Hasanah, Wiryono & Koesrindartoto (2024) — ITB
- Wealthfront Portfolio Methodology
- Grable & Lytton (1999) Risk Tolerance Scale
- Nitrogen/Riskalyze Risk Number methodology

## Run lokal

```bash
./run.sh
```

Atau:

```bash
source venv/bin/activate
streamlit run app.py
```

## Stack

Python, Streamlit, Plotly

## Docs

Folder `docs/` berisi penjelasan lengkap setiap modul beserta referensi akademik.
