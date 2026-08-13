<<<<<<< Updated upstream
# PulseFrame — Project Progress Log

## Project Initialization & Environment Setup
* **Repository Architecture**: Configured a clean, modular repository structure (`src/`, `notebooks/`, `wesad_data/`, `ppg_dalia_data/`) to isolate source modules, experimental notebooks, and raw signal inputs.
* **Environment Configuration**: Defined core dependencies (`torch`, `numpy`, `scipy`, `pyts`, `wfdb`, `matplotlib`) in `requirements.txt`.
* **Version Control Hygiene**: Configured `.gitignore` rules to prevent tracked commits of raw dataset files, cached artifacts, and system binaries.

---

## Signal Ingestion & Preprocessing Pipeline
* **WESAD Ingestion**: Built a dedicated data loader for WESAD pickle (`.pkl`) files to extract raw chest ECG and wrist PPG signals alongside aligned ground-truth affect/stress annotations.
* **Signal Segmentation**: Implemented continuous signal windowing into fixed-length segments to construct uniform time-series matrices suitable for feature extraction.
* **PPG-DaLiA Ingestion**: Extended data ingestion capability using a `wfdb`-based loader to parse real-world PPG and accelerometer signals.

---

## 2D Multimodal Image Transformations
* **Gramian Angular Field (GAF)**: Developed 2D temporal encoding using Gramian Angular Difference/Summation Fields to capture quasi-periodic time-series dynamics.
* **Recurrence Plot (RP)**: Implemented phase-space trajectory reconstruction to generate Recurrence Plots that characterize signal stationarity and non-linear patterns.
* **Continuous Wavelet Transform (CWT)**: Applied CWT using Mexican Hat (Ricker) wavelets to construct multi-scale time-frequency scalogram representations.
* **Sanity Checks & Verification**: Executed visual inspection notebooks (`notebooks/`) to verify transformation matrix shapes, scaling, and quality across converted signal windows.

---

## Pipeline Modularization & Leakage Prevention
* **Modular Source Code (`prepare_dataset.py`)**: Refactored signal extraction, windowing, and 2D transformation routines into a unified, reusable processing script (`src/prepare_dataset.py`).
* **Cross-Dataset Compatibility**: Confirmed that signal windowing and 2D transformation pipelines run unmodified across both lab-controlled (WESAD) and ambulatory (PPG-DaLiA) datasets.
* **Leakage-Safe Subject Tagging**: Implemented explicit subject ID metadata tagging across all output tensors to support Leave-One-Subject-Out (LOSO) cross-validation and prevent data leakage during train/test splits.
* **Data Quality Analysis**: Identified and documented structural noise differences, observing significantly higher real-world motion artifacts in PPG-DaLiA signals compared to WESAD baseline conditions.
=======
WEEK 1 COMPLETE (Aug 11-15): Environment set up, WESAD + PPG-DaLiA loaded, windowing function built, GAF/RP/CWT imaging pipeline implemented and verified across 3 subjects (S2, S3, S4). No blockers. Ready for Week 2: dataset engineering.
## PART 5 - Batch Processing Summary
- Total subjects detected: 1
- Successfully processed: 0
- Processed list: []

Extended pipeline to PPG-DaLiA (separate loader, wfdb-based). Confirmed same windowing/imaging code works unmodified across both datasets. Added subject-ID tagging to prevent data leakage in future train/test splits. Noted: PPG-DaLiA signals are visibly noisier (real-world activity vs WESAD's lab conditions), as expected.
>>>>>>> Stashed changes
