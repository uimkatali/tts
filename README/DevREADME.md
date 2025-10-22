
## Project Structure

```
tts/
├── tts.py                    # Main application (source)
├── TTS-Audio-Mixer.exe       # Compiled executable (for distribution)
├── input/                    # User input files
│   ├── config.json          # Configuration file
│   └── *.wav, *.mp3         # Background sound files
├── output/                   # Generated mixed audio files
├── dependencies/             # External dependencies
│   └── ffmpeg.exe           # Audio processing binary
├── dist/                     # Build output (can be deleted)
├── build/                    # Build artifacts (can be deleted)
└── README/                   # Documentation
```

## Prerequisites

### 1. Install ffmpeg

**Windows:**
```bash
winget install --id=Gyan.FFmpeg -e
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

The application supports two modes of operation:

### Mode 1: Batch Processing (JSON Config)

Create or edit `input/config.json` with your audio jobs:

```json
{
  "audio_jobs": [
    {
      "text": "Alarma parter",
      "language": "ro",
      "output_filename": "alarma_parter.mp3",
      "background_sound": "breach_alarm_994.wav",
      "background_volume": 0.3
    },
    {
      "text": "Emergency alert floor 2",
      "language": "en",
      "output_filename": "alert_floor2.mp3",
      "background_sound": "alarm_sound.wav",
      "background_volume": 0.5
    }
  ],
  "default_settings": {
    "language": "ro",
    "background_volume": 0.3,
    "audio_quality": 2
  }
}
```

**Note:** Background sound paths are relative to the `input/` folder.

Run batch processing (uses default `input/config.json`):
```bash
python tts.py
```

Or specify a custom config file:
```bash
python tts.py --config path/to/custom_config.json
```

### Mode 2: Single File (Command Line)

Generate a single TTS file with background:
```bash
python tts.py --text "Alarma afi etajul 3" --output alarm3.mp3 --background input/breach_alarm_994.wav --volume 0.3 --lang ro
```

Generate TTS without background sound:
```bash
python tts.py --text "Hello world" --output hello.mp3 --lang en
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--config` | Path to JSON configuration file | `input/config.json` |
| `--text` | Text to convert to speech (single mode) | None |
| `--output` | Output filename (single mode) | None |
| `--background` | Background sound file path (relative to input/ for batch mode) | None |
| `--volume` | Background volume (0.0-1.0) | 0.3 |
| `--lang` | Language code (ro, en, fr, es, etc.) | ro |

## Configuration File Format

Each audio job in `config.json` supports:

- `text` (required): Text to convert to speech
- `output_filename` (required): Name of the output MP3 file
- `language` (optional): Language code (default: 'ro')
- `background_sound` (optional): Path to background audio file (relative to `input/` folder)
- `background_volume` (optional): Volume of background (0.0-1.0, default: 0.3)

## Output Files

- **TTS only file**: `<output_filename>.mp3` (saved in root directory)
- **Mixed file**: `output/mixed_<output_filename>.mp3` (TTS + background, saved in output/ folder)

## Supported Languages

Common language codes:
- `ro` - Romanian
- `en` - English
- `fr` - French
- `es` - Spanish
- `de` - German
- `it` - Italian

See [gTTS documentation](https://gtts.readthedocs.io/) for full language list.

## Supported Audio Formats

Background sounds can be in any format supported by ffmpeg:
- MP3 (.mp3)
- WAV (.wav)
- OGG (.ogg)
- FLAC (.flac)
- AAC (.aac)

### Background sound too loud/quiet
- Adjust `background_volume` in config (0.0 = silent, 1.0 = original volume)
- Recommended range: 0.2 - 0.5

### Output audio quality issues
- Default quality is set to 2 (high quality)
- FFmpeg quality range: 0 (best) to 9 (worst)

## Advanced Usage

### Custom Audio Quality

Modify the `quality` parameter in the code (default: 2):
```python
mixer.mix_audio(..., quality=0)  # Best quality, larger file
```

### Working Directory

The script processes files in its own directory. All relative paths in config files are relative to the script location.

## Version

3.0.0 - Refactored with batch processing support
