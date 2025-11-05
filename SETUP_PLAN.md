# MFA Forced Alignment Setup Plan

## 1. Folder Structure

```
Assignment/
├── README.md                    # Main documentation
├── requirements.txt            # Python dependencies
├── setup.sh                    # Setup script
├── run_alignment.sh            # Alignment execution script
├── venv/                       # Python virtual environment
├── data/                       # Organized data for MFA
│   ├── audio/                  # Audio files (wav format)
│   │   ├── F2BJRLP1.wav
│   │   ├── F2BJRLP2.wav
│   │   ├── F2BJRLP3.wav
│   │   ├── ISLE_SESS0131_BLOCKD02_01_sprt1.wav
│   │   ├── ISLE_SESS0131_BLOCKD02_02_sprt1.wav
│   │   └── ISLE_SESS0131_BLOCKD02_03_sprt1.wav
│   └── transcripts/            # Text transcripts (one per audio file)
│       ├── F2BJRLP1.txt        # MFA requires .txt extension
│       ├── F2BJRLP2.txt
│       ├── F2BJRLP3.txt
│       ├── ISLE_SESS0131_BLOCKD02_01_sprt1.txt
│       ├── ISLE_SESS0131_BLOCKD02_02_sprt1.txt
│       └── ISLE_SESS0131_BLOCKD02_03_sprt1.txt
├── outputs/                     # MFA outputs
│   ├── TextGrids/              # Generated TextGrid files
│   └── logs/                   # MFA execution logs
├── scripts/                     # Utility scripts
│   ├── prepare_data.py         # Script to organize data
│   ├── validate_alignment.py   # Script to check alignment quality
│   └── visualize.py            # Script to create visualizations
├── models/                      # MFA models and dictionaries (downloaded)
│   ├── english_us_arpa/        # Pronunciation dictionary
│   └── english_mfa/            # Acoustic model
└── report/                      # Report materials
    ├── alignment_analysis.md
    └── figures/                 # Visualizations
```

## 2. How Forced Alignment Works (Simple Terms)

**The Problem:**
- You have audio of someone speaking
- You have the transcript (what they said)
- But you don't know WHEN each word was spoken in the audio

**The Solution (Forced Alignment):**
Think of it like subtitles, but more precise:
1. **Input**: Audio file + Text transcript
2. **Process**: The aligner uses a pronunciation dictionary to break words into phonemes (sounds), then matches those sounds to the audio waveform
3. **Output**: A TextGrid file that tells you:
   - Word "HELLO" starts at 0.00 seconds, ends at 0.45 seconds
   - Phoneme "HH" starts at 0.00, ends at 0.10
   - Phoneme "AH" starts at 0.10, ends at 0.25
   - etc.

**Analogy:**
It's like a music player that shows you exactly which lyrics are being sung at each moment. The aligner "forces" the known transcript to match the audio, finding where each word and sound occurs.

## 3. What MFA Does Internally (End-to-End)

### Step-by-Step Process:

1. **Data Preparation**:
   - Validates audio files (sample rate, format)
   - Validates transcripts (encoding, format)
   - Pairs audio files with their transcripts

2. **Dictionary Lookup/Generation**:
   - Uses pronunciation dictionary (e.g., `english_us_arpa`) to convert words to phonemes
   - Example: "HELLO" → "HH AH L OW"
   - If word not in dictionary, uses G2P (Grapheme-to-Phoneme) model to generate pronunciation

3. **Acoustic Model Loading**:
   - Loads pre-trained acoustic model (e.g., `english_mfa`)
   - This model knows how English sounds should look in audio signals

4. **Feature Extraction**:
   - Converts audio waveform to acoustic features (MFCCs, Mel-spectrograms)
   - These features represent the audio in a way the model can understand

5. **Alignment Algorithm**:
   - Uses Viterbi algorithm (Hidden Markov Model approach)
   - Creates a sequence of phonemes that best matches the audio features
   - Constrains the search to only sequences that match the transcript

6. **Boundary Detection**:
   - Determines exact start/end times for each phoneme
   - Aggregates phoneme boundaries to get word boundaries
   - Handles silence, pauses, and coarticulation

7. **Output Generation**:
   - Creates TextGrid files with:
     - Word tier: Word boundaries
     - Phone tier: Phoneme boundaries
   - Validates alignment quality

8. **Post-processing**:
   - Cleans up boundaries
   - Handles edge cases (silence, overlapping sounds)
   - Generates alignment statistics

## 4. Clean Environment Setup

### Steps:
1. Remove existing venv (if needed)
2. Create fresh virtual environment
3. Activate venv
4. Install Montreal Forced Aligner
5. Download `english_us_arpa` dictionary
6. Download `english_mfa` acoustic model
7. Verify installation

