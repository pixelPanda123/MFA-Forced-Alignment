# MFA Forced Alignment Assignment Report

## Executive Summary

This report summarizes the implementation and results of forced alignment using Montreal Forced Aligner (MFA) on a dataset of 6 audio files with corresponding transcripts.

## Methodology

### Tools and Models Used

- **Montreal Forced Aligner (MFA)**: Version 3.3.8
- **Dictionary**: `english_us_arpa` (pronunciation dictionary)
- **Acoustic Model**: `english_mfa` (pre-trained acoustic model)
- **Environment**: Conda environment with Python 3.10

### Dataset

- **Total Files**: 6 audio files
- **Total Duration**: 97.163 seconds
- **File Types**:
  - 3 long-form news segments (F2BJRLP1-3)
  - 3 short utterances (ISLE_SESS0131_BLOCKD02_01-03)

## Results

### Alignment Statistics

| File | Duration (s) | Words | Phones | Status |
|------|-------------|-------|--------|--------|
| F2BJRLP1 | 25.309 | 71 | 71 | ✅ Aligned |
| F2BJRLP2 | 28.647 | 73 | 73 | ✅ Aligned |
| F2BJRLP3 | 30.707 | 82 | 82 | ✅ Aligned |
| ISLE_SESS0131_BLOCKD02_01_sprt1 | 4.125 | 5 | 5 | ✅ Aligned |
| ISLE_SESS0131_BLOCKD02_02_sprt1 | 3.875 | 5 | 5 | ✅ Aligned |
| ISLE_SESS0131_BLOCKD02_03_sprt1 | 4.500 | 5 | 5 | ✅ Aligned |

**Overall Statistics:**
- Total duration: 97.163 seconds
- Total words: 241
- Total phones: 241
- Average duration: 16.194 seconds per file
- Average words per file: 40.2

### Key Observations

1. **Alignment Success**: All 6 files were successfully aligned with timing information for both word and phoneme boundaries.

2. **Unknown Words**: Many words were marked as `<unk>` (unknown), indicating:
   - Words not found in the `english_us_arpa` dictionary
   - Proper nouns (e.g., "Dukakis", "Hennessy", "Massachusetts")
   - Abbreviations (e.g., "S.J.C.")
   - Numbers or special formatting

3. **Alignment Quality**: 
   - TextGrid files were successfully generated for all files
   - Both word and phone tiers are present in all outputs
   - Timing boundaries are available for all segments

4. **Warnings**: 
   - MFA reported 208,649 pronunciations were ignored due to phones not present in the acoustic model
   - This is expected when using a general-purpose dictionary/model combination

## Visualizations

Alignment visualizations have been generated for all 6 files and are available in `report/figures/`. Each visualization shows:
- Word-level alignment timeline
- Phoneme-level alignment timeline
- Timing boundaries for each segment

## Technical Implementation

### Setup Process

1. **Environment Setup**: Created conda environment `mfa_env` with Python 3.10
2. **MFA Installation**: Installed MFA via conda-forge channel
3. **Model Download**: Downloaded `english_us_arpa` dictionary and `english_mfa` acoustic model
4. **Data Preparation**: Organized audio and transcript files into MFA-required format
5. **Alignment Execution**: Ran forced alignment on all 6 files

### Scripts Created

1. **`scripts/prepare_data.py`**: Prepares and formats transcripts for MFA
2. **`scripts/validate_alignment.py`**: Validates and analyzes alignment quality
3. **`scripts/visualize.py`**: Creates visualizations of alignment results
4. **`run_alignment.sh`**: Automated script to run alignment

## Output Files

All TextGrid files are located in `outputs/TextGrids/`:
- 6 TextGrid files (one per audio file)
- `alignment_analysis.csv` (quality metrics)

## Recommendations for Improvement

1. **Custom Dictionary**: Create a custom dictionary including proper nouns and abbreviations from the transcripts
2. **G2P Model**: Use a Grapheme-to-Phoneme model to generate pronunciations for unknown words
3. **Transcript Cleaning**: Pre-process transcripts to expand abbreviations and normalize text
4. **Model Adaptation**: Consider training a custom acoustic model adapted to the specific dataset

## Conclusion

The forced alignment process was successfully completed for all 6 audio files. While many words were marked as unknown due to the general-purpose dictionary, the alignment provides useful timing information for both word and phoneme boundaries. The TextGrid outputs can be used for further phonetic analysis, speech recognition training, or linguistic research.

## Files and Resources

- **GitHub Repository**: https://github.com/pixelPanda123/Assignment_IIIT_internship
- **MFA Documentation**: https://montreal-forced-aligner.readthedocs.io/
- **Output Location**: `outputs/TextGrids/`
- **Visualizations**: `report/figures/`

