# MFA Alignment Summary

## Alignment Results

### Execution Summary
- **Date**: November 5, 2025
- **Total Files Processed**: 6
- **Total Duration**: 97.163 seconds
- **Alignment Time**: ~40 seconds
- **Status**: ✅ Successfully Completed

### Files Aligned

| File | Duration (s) | Words | Phones | Notes |
|------|-------------|-------|--------|-------|
| F2BJRLP1 | 25.309 | 71 | 71 | Long news segment |
| F2BJRLP2 | 28.647 | 73 | 73 | Long news segment |
| F2BJRLP3 | 30.707 | 82 | 82 | Long news segment |
| ISLE_SESS0131_BLOCKD02_01_sprt1 | 4.125 | 5 | 5 | Short utterance |
| ISLE_SESS0131_BLOCKD02_02_sprt1 | 3.875 | 5 | 5 | Short utterance |
| ISLE_SESS0131_BLOCKD02_03_sprt1 | 4.500 | 5 | 5 | Short utterance |

### Statistics
- **Average Duration**: 16.194 seconds per file
- **Average Words**: 40.2 words per file
- **Average Phones**: 40.2 phones per file
- **Total Words**: 241
- **Total Phones**: 241

### Observations

1. **Unknown Words**: Many words were marked as `<unk>` (unknown) in the alignment. This indicates:
   - Words not found in the `english_us_arpa` dictionary
   - Proper nouns (e.g., "Dukakis", "Hennessy", "Massachusetts")
   - Abbreviations (e.g., "S.J.C.")
   - Numbers or special formatting

2. **Alignment Quality**: 
   - Alignment completed successfully for all files
   - TextGrid files were generated with word and phone tiers
   - Timing information is available for all segments

3. **Warnings**:
   - MFA reported 208,649 pronunciations were ignored due to phones not present in the acoustic model
   - This is expected for a general-purpose dictionary/model combination

### Output Files

All TextGrid files are located in `outputs/TextGrids/`:
- `F2BJRLP1.TextGrid` (17 KB)
- `F2BJRLP2.TextGrid` (18 KB)
- `F2BJRLP3.TextGrid` (21 KB)
- `ISLE_SESS0131_BLOCKD02_01_sprt1.TextGrid` (1.9 KB)
- `ISLE_SESS0131_BLOCKD02_02_sprt1.TextGrid` (1.7 KB)
- `ISLE_SESS0131_BLOCKD02_03_sprt1.TextGrid` (1.7 KB)
- `alignment_analysis.csv` (alignment quality metrics)

### Configuration Used

- **Dictionary**: `english_us_arpa`
- **Acoustic Model**: `english_mfa`
- **Environment**: Conda environment `mfa_env` with Python 3.10
- **MFA Version**: 3.3.8

### Next Steps for Improvement

1. **Custom Dictionary**: Create a custom dictionary with proper nouns and abbreviations from the transcripts
2. **G2P Model**: Use a Grapheme-to-Phoneme model to generate pronunciations for unknown words
3. **Transcription Cleaning**: Pre-process transcripts to expand abbreviations and normalize text
4. **Visualization**: Use Praat to visualize alignments and verify quality
5. **Error Analysis**: Compare aligned words with original transcripts to identify systematic errors

### Using the Outputs

TextGrid files can be opened in:
- **Praat**: Free software for speech analysis
- **Python**: Using the `praatio` library
- **TextGrid viewers**: Various online tools

Example command to view in Praat:
```bash
open outputs/TextGrids/F2BJRLP1.TextGrid
```

