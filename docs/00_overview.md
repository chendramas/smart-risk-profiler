# Smart Risk Profiler — Dokumentasi Metodologi

Folder ini berisi dokumentasi lengkap untuk setiap indikator dan pertanyaan
yang digunakan dalam Smart Risk Profiler. Setiap file mencantumkan:
- **Sumber akademik/industri** (dengan sitasi)
- **Alasan penggunaan** (kenapa pertanyaan ini penting)
- **Cara scoring** (bagaimana jawaban diproses)
- **Relevansi untuk Indonesia** (jika ada)

Tujuan: agar setiap desisi bisa dipertanggungjawabkan saat presentasi ke client
atau ditanya reviewer tentang fondasi riset di balik aplikasi.

## Daftar File

| File | Topik |
|------|-------|
| `01_framework.md` | Framework utama: CFA Institute 3-Factor IRP |
| `02_behavioral_scenarios.md` | 8 skenario behavioral (Risk Composure, Preference, dll) |
| `03_overconfidence_detection.md` | Deteksi overconfidence via inkonsistensi jawaban |
| `04_financial_health.md` | Modul kesehatan finansial (dana darurat, utang, tanggungan) |
| `05_loss_aversion.md` | Pengukuran loss aversion (lottery-style) |
| `06_scoring_methodology.md` | Metodologi scoring: min(capacity, tolerance) |
| `07_indonesian_context.md` | Konteks Indonesia: budaya, produk, IDX |
| `08_references.md` | Daftar lengkap referensi akademik & industri |

## Framework Summary

```
┌─────────────────────────────────────────────────┐
│           CFA Institute 3-Factor IRP            │
├─────────────────────────────────────────────────┤
│ Factor 1: Risk Need (Goal-Based)                │
│   → Usia, Horizon Investasi                     │
│                                                 │
│ Factor 2: Risk-Taking Ability (Capacity)        │
│   → Penghasilan, Net Worth, Dana Darurat,       │
│     Utang, Tanggungan, Asuransi                 │
│                                                 │
│ Factor 3: Behavioral Loss Tolerance             │
│   → 5 dimensi (8 skenario)                      │
│   → Overconfidence Detection                    │
│   → Loss Aversion Measurement                   │
├─────────────────────────────────────────────────┤
│ Reconciliation: min(Capacity, Tolerance)        │
│ + Traffic Light: Green / Yellow / Red           │
└─────────────────────────────────────────────────┘
```
