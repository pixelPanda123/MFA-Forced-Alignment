#!/bin/bash
# Setup script for MFA Forced Alignment Assignment

set -e

echo "Setting up MFA Forced Alignment environment..."

# Create conda environment
echo "Creating conda environment 'mfa_env'..."
conda create -n mfa_env python=3.10 -y

# Activate environment and install MFA
echo "Installing Montreal Forced Aligner..."
conda activate mfa_env
conda install -c conda-forge montreal-forced-aligner -y

# Download models
echo "Downloading english_us_arpa dictionary..."
mfa model download dictionary english_us_arpa

echo "Downloading english_mfa acoustic model..."
mfa model download acoustic english_mfa

# Create directory structure
echo "Creating directory structure..."
mkdir -p data/audio data/transcripts
mkdir -p outputs/TextGrids outputs/logs
mkdir -p scripts models report/figures

echo "Setup complete!"
echo "To activate the environment, run: conda activate mfa_env"

