import os
import pickle
import numpy as np
from windowing import make_windows
from imaging import to_gaf, to_rp, to_cwt

# Sampling rates and parameters
FS_ECG = 700
FS_PPG = 64
WINDOW_SECONDS = 10
OVERLAP = 0.5

def load_subject_data(subject_path):
    """Step 7: Load any WESAD subject safely"""
    if not os.path.exists(subject_path):
        raise FileNotFoundError(f"Subject file not found: {subject_path}")
        
    with open(subject_path, 'rb') as f:
        data = pickle.load(f, encoding='latin1')
    return data

def process_and_save_all(data_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    subjects = [s for s in os.listdir(data_dir) if s.startswith('S')]
    
    for sub in sorted(subjects):
        pkl_path = os.path.join(data_dir, sub, f"{sub}.pkl")
        if not os.path.exists(pkl_path):
            continue
            
        print(f"🔄 Processing {sub}...")
        data = load_subject_data(pkl_path)
        
        # Extract ECG signal
        ecg_signal = data['signal']['chest']['ECG'].flatten()
        
        # Calculate window parameters
        window_size = int(WINDOW_SECONDS * FS_ECG)
        step_size = int(window_size * (1 - OVERLAP))
        
        windows = make_windows(ecg_signal, window_size, step_size)
        gaf_imgs = [to_gaf(w) for w in windows]
        
        output_file = os.path.join(output_dir, f"{sub}_processed.pkl")
        with open(output_file, 'wb') as f:
            pickle.dump({'gaf': gaf_imgs}, f)
        print(f"✅ Saved {sub} to {output_file}")

if __name__ == "__main__":
    process_and_save_all("wesad_data/WESAD", "processed_data")

def extract_signals(data):
    """Step 8: Safely extract signals from a loaded WESAD subject"""
    if data is None:
        return None, None
        
    try:
        ecg = data['signal']['chest']['ECG'].flatten()
    except KeyError:
        print("⚠️ ECG signal missing in chest data")
        ecg = None
        
    try:
        ppg = data['signal']['wrist']['BVP'].flatten()
    except KeyError:
        print("⚠️ PPG (BVP) signal missing in wrist data")
        ppg = None
        
    return ecg, ppg

def process_single_subject(subject_id, data_dir='wesad_data/WESAD', output_dir='processed_data'):
    """Step 9: Full per-subject processing function"""
    data = load_wesad_subject(subject_id, data_dir)
    if data is None:
        return False
        
    ecg, ppg = extract_signals(data)
    if ecg is None:
        return False
        
    window_size = int(10 * 700)  # 10s window at 700Hz
    step_size = int(window_size * 0.5)
    
    windows = make_windows(ecg, window_size, step_size)
    gaf_imgs = [to_gaf(w) for w in windows]
    
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{subject_id}_processed.pkl")
    with open(out_path, 'wb') as f:
        pickle.dump({'gaf': gaf_imgs}, f)
        
    print(f"✅ Finished {subject_id}: {len(gaf_imgs)} windows saved to {out_path}")
    return True


def process_all_subjects(subject_ids, data_dir='wesad_data/WESAD'):
    results = {}
    for sid in subject_ids:
        print(f"Processing {sid}...")
        r = process_subject_full(sid, data_dir) if 'process_subject_full' in globals() else None
        if r is not None:
            results[sid] = r
            print(f" -> success, {len(r['ecg_windows'])} windows")
        else:
            print(" -> skipped")
    return results
