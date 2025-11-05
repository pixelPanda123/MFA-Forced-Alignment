#!/usr/bin/env python3
"""
Script to visualize alignment results from TextGrid files.
"""

import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from praatio import textgrid

def visualize_alignment(textgrid_path, output_dir):
    """Create visualization for a single TextGrid file."""
    try:
        tg = textgrid.openTextgrid(textgrid_path, includeEmptyIntervals=False)
        
        # Get tiers
        word_tier = tg.getTier('words')
        phone_tier = tg.getTier('phones')
        
        # Extract data
        words = []
        phones = []
        
        if word_tier:
            entries = word_tier.entryList if hasattr(word_tier, 'entryList') else word_tier.entries
            for entry in entries:
                word = entry.label.strip() if hasattr(entry, 'label') else entry[2].strip()
                start = entry.start if hasattr(entry, 'start') else entry[0]
                end = entry.end if hasattr(entry, 'end') else entry[1]
                if word and word != '<unk>':
                    words.append((start, end, word))
        
        if phone_tier:
            entries = phone_tier.entryList if hasattr(phone_tier, 'entryList') else phone_tier.entries
            for entry in entries:
                phone = entry.label.strip() if hasattr(entry, 'label') else entry[2].strip()
                start = entry.start if hasattr(entry, 'start') else entry[0]
                end = entry.end if hasattr(entry, 'end') else entry[1]
                if phone and phone not in ['', 'sp']:
                    phones.append((start, end, phone))
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        fig.suptitle(f'Alignment Visualization: {Path(textgrid_path).stem}', fontsize=14, fontweight='bold')
        
        # Plot words
        if words:
            y_pos = 0
            for start, end, word in words:
                ax1.barh(y_pos, end - start, left=start, height=0.8, alpha=0.7, color='steelblue')
                mid = (start + end) / 2
                ax1.text(mid, y_pos, word, ha='center', va='center', fontsize=8)
                y_pos += 1
            
            ax1.set_xlim(0, max(end for _, end, _ in words))
            ax1.set_ylim(-0.5, len(words) - 0.5)
            ax1.set_xlabel('Time (seconds)')
            ax1.set_ylabel('Words')
            ax1.set_title('Word Alignment')
            ax1.grid(True, alpha=0.3)
        
        # Plot phones
        if phones:
            y_pos = 0
            for start, end, phone in phones:
                ax2.barh(y_pos, end - start, left=start, height=0.8, alpha=0.7, color='coral')
                mid = (start + end) / 2
                ax2.text(mid, y_pos, phone, ha='center', va='center', fontsize=6)
                y_pos += 1
            
            ax2.set_xlim(0, max(end for _, end, _ in phones))
            ax2.set_ylim(-0.5, len(phones) - 0.5)
            ax2.set_xlabel('Time (seconds)')
            ax2.set_ylabel('Phones')
            ax2.set_title('Phoneme Alignment')
            ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save figure
        output_path = Path(output_dir) / f"{Path(textgrid_path).stem}_alignment.png"
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Created visualization: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error visualizing {textgrid_path}: {e}", file=sys.stderr)
        return None

def main():
    """Main function to create visualizations for all TextGrid files."""
    textgrid_dir = Path("outputs/TextGrids")
    output_dir = Path("report/figures")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    textgrid_files = list(textgrid_dir.glob("*.TextGrid"))
    
    if not textgrid_files:
        print(f"No TextGrid files found in {textgrid_dir}")
        sys.exit(1)
    
    print(f"Creating visualizations for {len(textgrid_files)} TextGrid files...\n")
    
    created = []
    for tg_file in sorted(textgrid_files):
        result = visualize_alignment(tg_file, output_dir)
        if result:
            created.append(result)
    
    print(f"\nCreated {len(created)} visualizations in {output_dir}")

if __name__ == "__main__":
    main()

