# TTS Audio Mixer v3.0

## Features
- Organized folder structure for input/output files
- Batch processing from JSON configuration files
- Command-line interface for single-file generation
- Automatic audio mixing with background sounds
- Support for 100+ languages via Google TTS
- Bundled with FFmpeg (no installation required)
- Modern Python codebase with type hints and error handling

## Installation
1. Download and extract TTS-Audio-Mixer-v3.0.zip
2. Edit `input/config.json` with your text
3. Run `TTS-Audio-Mixer.exe`
4. Find your audio files in the `output/` folder

## System Requirements
- Windows 7 or later

## Folder Structure
- `TTS-Audio-Mixer.exe` - Main application
- `input/` - Put your config.json and sound files here
  - `config.json` - Configuration file
  - `breach_alarm_994.wav` - Sample background sound
- `output/` - Generated mixed audio files
- `dependencies/` - Contains ffmpeg.exe

## Changes in v3.0
- Reorganized folder structure (input/, output/, dependencies/)
- Improved user experience - clearer file organization
- Background sounds automatically resolved from input/ folder
- Better documentation with clear folder structure

## Changes in v2.0
- JSON-based batch configuration
- Modular code architecture
- Improved error messages
- Professional documentation

