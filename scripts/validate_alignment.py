#!/usr/bin/env python3
"""
Script to validate and analyze MFA alignment outputs.
"""

import os
import sys
from pathlib import Path
from praatio import textgrid

def analyze_textgrid(textgrid_path):
    """Analyze a TextGrid file and return statistics."""
    try:
        tg = textgrid.openTextgrid(textgrid_path, includeEmptyIntervals=False)
        
        # Get word tier
        word_tier = tg.getTier('words')
        phone_tier = tg.getTier('phones')
        
        stats = {
            'file': Path(textgrid_path).name,
            'duration': tg.maxTimestamp,
            'num_words': 0,
            'num_phones': 0,
            'num_unknown_words': 0,
            'num_silence_words': 0,
            'num_silence_phones': 0,
            'words': [],
            'phones': []
        }
        
        if word_tier:
            entries = word_tier.entryList if hasattr(word_tier, 'entryList') else word_tier.entries
            stats['num_words'] = len(entries)
            for entry in entries:
                word = entry.label.strip() if hasattr(entry, 'label') else entry[2].strip()
                start = entry.start if hasattr(entry, 'start') else entry[0]
                end = entry.end if hasattr(entry, 'end') else entry[1]
                if word == '<unk>':
                    stats['num_unknown_words'] += 1
                elif word == '':
                    stats['num_silence_words'] += 1
                else:
                    stats['words'].append({
                        'text': word,
                        'start': start,
                        'end': end,
                        'duration': end - start
                    })
        
        if phone_tier:
            entries = phone_tier.entryList if hasattr(phone_tier, 'entryList') else phone_tier.entries
            stats['num_phones'] = len(entries)
            for entry in entries:
                phone = entry.label.strip() if hasattr(entry, 'label') else entry[2].strip()
                start = entry.start if hasattr(entry, 'start') else entry[0]
                end = entry.end if hasattr(entry, 'end') else entry[1]
                if phone == '' or phone == 'sp':
                    stats['num_silence_phones'] += 1
                else:
                    stats['phones'].append({
                        'text': phone,
                        'start': start,
                        'end': end,
                        'duration': end - start
                    })
        
        return stats
    except Exception as e:
        print(f"Error analyzing {textgrid_path}: {e}", file=sys.stderr)
        return None

def main():
    """Main function to analyze all TextGrid files."""
    output_dir = Path("outputs/TextGrids")
    
    if not output_dir.exists():
        print(f"Error: {output_dir} does not exist!")
        sys.exit(1)
    
    textgrid_files = list(output_dir.glob("*.TextGrid"))
    
    if not textgrid_files:
        print(f"No TextGrid files found in {output_dir}")
        sys.exit(1)
    
    print(f"Analyzing {len(textgrid_files)} TextGrid files...\n")
    print("=" * 80)
    
    all_stats = []
    for tg_file in sorted(textgrid_files):
        stats = analyze_textgrid(tg_file)
        if stats:
            all_stats.append(stats)
            
            # Print summary
            print(f"\nFile: {stats['file']}")
            print(f"  Duration: {stats['duration']:.3f} seconds")
            print(f"  Words: {stats['num_words']} (Unknown: {stats['num_unknown_words']}, Silence: {stats['num_silence_words']})")
            print(f"  Phones: {stats['num_phones']} (Silence: {stats['num_silence_phones']})")
            
            if stats['words']:
                print(f"  First 5 words:")
                for word in stats['words'][:5]:
                    print(f"    '{word['text']}': {word['start']:.3f}-{word['end']:.3f}s ({word['duration']:.3f}s)")
    
    # Overall statistics
    print("\n" + "=" * 80)
    print("\nOverall Statistics:")
    print(f"  Total files: {len(all_stats)}")
    print(f"  Total duration: {sum(s['duration'] for s in all_stats):.3f} seconds")
    print(f"  Total words: {sum(s['num_words'] for s in all_stats)}")
    print(f"  Total unknown words: {sum(s['num_unknown_words'] for s in all_stats)}")
    print(f"  Total phones: {sum(s['num_phones'] for s in all_stats)}")
    
    if all_stats:
        avg_duration = sum(s['duration'] for s in all_stats) / len(all_stats)
        avg_words = sum(s['num_words'] for s in all_stats) / len(all_stats)
        avg_phones = sum(s['num_phones'] for s in all_stats) / len(all_stats)
        print(f"  Average duration: {avg_duration:.3f} seconds")
        print(f"  Average words per file: {avg_words:.1f}")
        print(f"  Average phones per file: {avg_phones:.1f}")

if __name__ == "__main__":
    main()

