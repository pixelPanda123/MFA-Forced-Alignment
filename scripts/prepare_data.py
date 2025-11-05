#!/usr/bin/env python3
"""
Script to prepare transcripts for MFA alignment.
- Converts transcript files to lowercase .txt extension
- Cleans and formats transcripts for MFA
"""

import os
import re
from pathlib import Path

def clean_transcript(text):
    """Clean transcript text for MFA."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    # Remove empty lines
    text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    return text

def prepare_transcripts(source_dir, target_dir):
    """Copy and prepare transcript files."""
    source = Path(source_dir)
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    
    # Get all transcript files
    transcript_files = list(source.glob('*.TXT')) + list(source.glob('*.txt'))
    
    for transcript_file in transcript_files:
        # Read transcript
        with open(transcript_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean transcript
        cleaned = clean_transcript(content)
        
        # Create output filename (lowercase .txt)
        base_name = transcript_file.stem
        output_file = target / f"{base_name}.txt"
        
        # Write cleaned transcript
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        
        print(f"Prepared: {transcript_file.name} -> {output_file.name}")
    
    print(f"\nPrepared {len(transcript_files)} transcript files.")

if __name__ == "__main__":
    # Set paths
    source_dir = "/Users/pranavreddytalla/Desktop/Assignment/transcripts"
    target_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/transcripts"
    
    prepare_transcripts(source_dir, target_dir)

