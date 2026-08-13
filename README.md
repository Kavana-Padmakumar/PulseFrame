
# PulseFrame

PulseFrame is an end-to-end framework for processing physiological time-series signals (ECG/PPG) into 2D imaging representations (Gramian Angular Field, Recurrence Plot, Continuous Wavelet Transform) for downstream deep learning models.

## 🚀 Key Features

- **Multi-Dataset Support**: Unified ingestion pipeline for both **WESAD** (lab-controlled) and **PPG-DaLiA** (real-world activity) datasets.
- **Leakage-Safe Subject Tagging**: Built-in subject ID tagging to prevent data leakage during train/validation/test splits.
- **Multimodal 2D Transformations**:
  - **GAF**: Gramian Angular Field
  - **RP**: Recurrence Plot
  - **CWT**: Continuous Wavelet Transform (Ricker/Mexican Hat)
- **Modular Design**: Reusable source scripts located in `src/` for clean dataset preparation.

---

## 📁 Repository Structure

```text
PulseFrame/
├── notebooks/            # Verification and exploratory notebooks
├── ppg_dalia_data/       # Ingested PPG-DaLiA dataset files (wfdb-based)
├── src/                  # Core modular source code for processing & transformation
│   └── prepare_dataset.py # Subject extraction, windowing, and imaging pipeline
├── wesad_data/           # Ingested WESAD dataset files (.pkl)
├── .gitignore            # Git exclusion rules
├── progress.md           # Log of daily progress and milestones
├── README.md             # Project overview and documentation
└── requirements.txt      # Project dependencies
