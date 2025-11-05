#!/bin/bash
# Script to run MFA forced alignment

set -e

echo "Running MFA Forced Alignment..."
echo "================================"

# Activate conda environment
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate mfa_env

# Check if corpus directory exists
if [ ! -d "data/corpus" ]; then
    echo "Error: data/corpus directory not found!"
    echo "Please run prepare_data.py first to organize the data."
    exit 1
fi

# Check if outputs directory exists
mkdir -p outputs/TextGrids

# Run alignment
echo "Starting alignment..."
mfa align data/corpus english_us_arpa english_mfa outputs/TextGrids --clean

echo ""
echo "Alignment complete!"
echo "TextGrid files are in: outputs/TextGrids/"
echo ""
echo "To validate results, run:"
echo "  python scripts/validate_alignment.py"

