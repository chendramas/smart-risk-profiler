# Smart Risk Profiler

Profil risiko investasi berdasarkan framework CFA Institute Investment Risk Profile (IRP).

## Features

- **Risk Number 1-99** — skala kontinu ala Nitrogen/Riskalyze
- **Behavioral Analysis** — 5 komponen: composure, preference, perception, knowledge, experience
- **Financial Health Check** — dana darurat, rasio utang, tanggungan, net worth, kepemilikan rumah
- **Loss Aversion Test** — berdasarkan Kahneman & Tversky Prospect Theory
- **Overconfidence Detection** — consistency checks antar skenario
- **Goal-Based Risk Need** — kalkulator return yang dibutuhkan per tujuan finansial
- **Traffic Light Reconciliation** — Green/Yellow/Red berdasarkan CFA IRP
- **Dark/Light Mode** — full theme support
- **IDX/IHSG/Rupiah** — localized untuk pasar Indonesia

## Run

```bash
./run.sh
```

Atau manual:

```bash
source venv/bin/activate
streamlit run app.py
```

## Stack

- Python, Streamlit, Plotly
- CFA Institute IRP framework

## Docs

Lihat folder `docs/` untuk penjelasan lengkap setiap modul beserta referensi akademik.
