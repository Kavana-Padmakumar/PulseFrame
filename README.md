\# PhysioShift — Physiological Dataset Verification



This repository contains the initial data verification workflow for multi-modal physiological datasets (ECG, PPG, and accelerometer signals).



All verification code, signal shape checks, sampling rate inspections, and metadata extractions are implemented in \[`notebooks/00\_dataset\_verification.ipynb`](./notebooks/00\_dataset\_verification.ipynb).



\---



\## 1. Summary of Open Datasets Verified



| Dataset | Primary Format | Access / Loader Method | Sampling Rate ($f\_s$) | Key Channels / Signals | Verification Status |

| :--- | :--- | :--- | :--- | :--- | :---: |

| \*\*PTB-XL\*\* | PhysioNet WFDB (`.hea` / `.dat`) | `wfdb.rdrecord()` | 100 Hz / 500 Hz | 12-lead ECG (I, II, III, aVR, aVL, aVF, V1–V6) | ✅ \*\*Verified\*\* |

| \*\*MIT-BIH Arrhythmia\*\* | PhysioNet WFDB (`.hea` / `.dat` / `.atr`) | `wfdb.rdrecord()`, `wfdb.rdann()` | 360 Hz | Modified Lead II (MLII), V1 / V2 / V4 / V5 | ✅ \*\*Verified\*\* |

| \*\*WESAD\*\* | UCI Pickle (`.pkl`) | `pickle.load(f, encoding='latin1')` | 700 Hz (Chest) / 64 Hz (Wrist) | ECG, EDA, EMG, Temp (Chest) / BVP/PPG, EDA, TEMP (Wrist) | ✅ \*\*Verified\*\* |

| \*\*PPG-DaLiA\*\* | UCI Pickle (`.pkl`) | `pickle.load(f, encoding='latin1')` | 700 Hz (Chest) / 64 Hz (Wrist) | ECG, ACC (Chest) / BVP/PPG, ACC, TEMP (Wrist) | ✅ \*\*Verified\*\* |

| \*\*Multi-site PPG\*\* | Tabular / Binary (`.csv` / `.pkl` / `.hdf5`) | `pandas.read\_csv()` / `pickle.load()` | Variable (Site-dependent) | Multi-site PPG (Earlobe, Finger, Toe) | ✅ \*\*Verified\*\* |



\---



\## 2. Technical Breakdown \& Data Specifications



\### 2.1 PTB-XL (PhysioNet WFDB Format)

\* \*\*Overview:\*\* A large 12-lead ECG dataset containing 21,837 clinical ECG records from 18,885 patients.

\* \*\*Storage Standard:\*\* Standard WFDB format consisting of paired plain-text header files (`.hea`) and binary signal files (`.dat`).

\* \*\*Loading Mechanism:\*\*

&#x20; ```python

&#x20; import wfdb

&#x20; record = wfdb.rdrecord('data/ptb-xl/records100/00000/00001\_lr')

&#x20; signal = record.p\_signal  # Shape: (1000, 12) at 100 Hz

