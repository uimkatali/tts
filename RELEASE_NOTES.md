# TTS Audio Mixer v2.0

## Features
- Batch processing from JSON configuration files
- Command-line interface for single-file generation
- Automatic audio mixing with background sounds
- Support for 100+ languages via Google TTS
- Bundled with FFmpeg (no installation required)
- Modern Python codebase with type hints and error handling

## Installation
1. Download and extract TTS-Audio-Mixer-v2.0.zip
2. Run TTS-Audio-Mixer.exe

## Usage

### Batch Mode
```
TTS-Audio-Mixer.exe
```

### Single File Mode
```
TTS-Audio-Mixer.exe --text "Your text" --output file.mp3 --lang en
```

### With Background Sound
```
TTS-Audio-Mixer.exe --text "Alert" --output alarm.mp3 --background sound.wav --volume 0.3 --lang ro
```

## System Requirements
- Windows 7 or later

## Files Included
- TTS-Audio-Mixer.exe
- ffmpeg.exe
- config.json
- breach_alarm_994.wav

## Changes in v2.0
- JSON-based batch configuration
- Modular code architecture
- Improved error messages
- Professional documentation

