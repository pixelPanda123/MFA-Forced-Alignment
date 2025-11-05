# MFA Forced Alignment Assignment

## Setup Instructions

### 1. Environment Setup

This project uses **conda** for environment management (MFA requires kalpy which is better installed via conda).

```bash
# Activate the conda environment
conda activate mfa_env

# To deactivate when done
conda deactivate
```

### 2. Folder Structure

```
Assignment/
├── README.md                    # This file
├── SETUP_PLAN.md                # Detailed setup plan
├── data/                        # Organized data for MFA
│   ├── audio/                   # Audio files (wav format)
│   └── transcripts/             # Text transcripts (.txt format)
├── outputs/                     # MFA outputs
│   ├── TextGrids/              # Generated TextGrid files
│   └── logs/                   # MFA execution logs
├── scripts/                     # Utility scripts
├── models/                      # MFA models and dictionaries (downloaded automatically)
└── report/                      # Report materials
    └── figures/                 # Visualizations
```

### 3. Installed Components

- **Montreal Forced Aligner (MFA)**: v3.3.8
- **Dictionary**: `english_us_arpa` (pronunciation dictionary)
- **Acoustic Model**: `english_mfa` (pre-trained acoustic model)
- **Environment**: Conda environment `mfa_env` with Python 3.10

### 4. How Forced Alignment Works

**Simple Explanation:**
Forced alignment automatically matches audio recordings with their text transcripts at the word and phoneme level. If you know what was said (the transcript), forced alignment finds when each word and sound was spoken in the audio.

**Example:**
- **Audio**: Speaker says "Hello world"
- **Transcript**: "HELLO WORLD"
- **Dictionary**: HELLO → HH AH L OW, WORLD → W ER L D
- **Output**: TextGrid with timing:
  - Word "HELLO": 0.00 - 0.45 seconds
  - Phoneme "HH": 0.00 - 0.10 seconds
  - Phoneme "AH": 0.10 - 0.25 seconds
  - etc.

### 5. What MFA Does Internally (End-to-End)

1. **Data Preparation**: Validates audio and transcript files
2. **Dictionary Lookup**: Converts words to phonemes using pronunciation dictionary
3. **Acoustic Model Loading**: Loads pre-trained acoustic model
4. **Feature Extraction**: Converts audio to acoustic features (MFCCs, Mel-spectrograms)
5. **Alignment Algorithm**: Uses Viterbi algorithm (HMM) to match phoneme sequences to audio
6. **Boundary Detection**: Determines exact start/end times for phonemes and words
7. **Output Generation**: Creates TextGrid files with word and phone tiers
8. **Post-processing**: Cleans boundaries and handles edge cases

### 6. Running Alignment

```bash
# Activate environment
conda activate mfa_env

# Run alignment (example command - adjust paths as needed)
mfa align data/audio data/transcripts english_us_arpa english_mfa outputs/TextGrids
```

### 7. Data Preparation

Before running alignment, ensure:
- Audio files are in `.wav` format
- Transcripts are in `.txt` format
- Each audio file has a corresponding transcript with matching base filename
- Files are organized in the `data/audio/` and `data/transcripts/` directories

### 8. Alignment Results

✅ **Alignment Completed Successfully!**

- **6 files** processed
- **97.163 seconds** total audio
- **TextGrid files** generated in `outputs/TextGrids/`
- **Quality metrics** available in `outputs/TextGrids/alignment_analysis.csv`

See `ALIGNMENT_SUMMARY.md` for detailed results.

### 9. Next Steps

1. ✅ Organize audio files and transcripts - **DONE**
2. ✅ Run data preparation - **DONE**
3. ✅ Execute forced alignment - **DONE**
4. Inspect TextGrid outputs using Praat
5. Analyze alignment quality (see `scripts/validate_alignment.py`)
6. Generate report with visualizations

## References

- [MFA Documentation](https://montreal-forced-aligner.readthedocs.io/)
- GitHub Repository: https://github.com/pixelPanda123/Assignment_IIIT_internship

