# Text-to-Speech Audio Mixer

A Python application for generating text-to-speech audio and mixing it with background sounds. Supports both single-file and batch processing modes.

## Features

- Generate TTS audio in multiple languages using Google Text-to-Speech
- Mix TTS with background sounds (alarms, music, etc.)
- Batch processing from JSON configuration
- Command-line interface for single files
- Cross-platform support (Windows, Linux, macOS)
- Automatic ffmpeg detection

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

Create or edit `config.json` with your audio jobs:

```json
{
  "audio_jobs": [
    {
      "text": "Alarma afi parter",
      "language": "ro",
      "output_filename": "alarma_afi_parter.mp3",
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

Run batch processing:
```bash
python tts.py
```

Or specify a custom config file:
```bash
python tts.py --config my_custom_config.json
```

### Mode 2: Single File (Command Line)

Generate a single TTS file with background:
```bash
python tts.py --text "Alarma afi etajul 3" --output alarm3.mp3 --background breach_alarm_994.wav --volume 0.3 --lang ro
```

Generate TTS without background sound:
```bash
python tts.py --text "Hello world" --output hello.mp3 --lang en
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--config` | Path to JSON configuration file | `config.json` |
| `--text` | Text to convert to speech (single mode) | None |
| `--output` | Output filename (single mode) | None |
| `--background` | Background sound file path | None |
| `--volume` | Background volume (0.0-1.0) | 0.3 |
| `--lang` | Language code (ro, en, fr, es, etc.) | ro |

## Configuration File Format

Each audio job in `config.json` supports:

- `text` (required): Text to convert to speech
- `output_filename` (required): Name of the output MP3 file
- `language` (optional): Language code (default: 'ro')
- `background_sound` (optional): Path to background audio file
- `background_volume` (optional): Volume of background (0.0-1.0, default: 0.3)

## Output Files

- **Without background**: `<output_filename>.mp3` (TTS only)
- **With background**: Both `<output_filename>.mp3` (TTS) and `mixed_<output_filename>.mp3` (final mix)

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

## Examples

### Example 1: Emergency Alerts for Multiple Floors

```json
{
  "audio_jobs": [
    {
      "text": "Alarma afi parter",
      "output_filename": "alarm_ground.mp3",
      "background_sound": "siren.wav",
      "background_volume": 0.4
    },
    {
      "text": "Alarma afi etajul 1",
      "output_filename": "alarm_floor1.mp3",
      "background_sound": "siren.wav",
      "background_volume": 0.4
    }
  ]
}
```

### Example 2: Multi-Language Announcements

```json
{
  "audio_jobs": [
    {
      "text": "Emergency evacuation required",
      "language": "en",
      "output_filename": "evacuation_en.mp3"
    },
    {
      "text": "Evacuare de urgență necesară",
      "language": "ro",
      "output_filename": "evacuation_ro.mp3"
    }
  ]
}
```

### Example 3: Command Line Quick Generation

```bash
# English announcement with alarm
python tts.py --text "Fire alarm activated" --output fire_alert.mp3 --background alarm.wav --lang en

# Simple Romanian TTS
python tts.py --text "Bine ați venit" --output welcome.mp3 --lang ro
```

## Troubleshooting

### ffmpeg not found
- Ensure ffmpeg is installed and in your system PATH
- On Windows, the script automatically searches common installation locations
- Manual installation: Download from [ffmpeg.org](https://ffmpeg.org/)

### Module not found: gtts
```bash
pip install gtts
```

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

## Technical Details

- TTS Engine: Google Text-to-Speech (gTTS)
- Audio Mixing: FFmpeg with amix filter
- Output Format: MP3 (libmp3lame codec)
- Default Quality: VBR level 2 (high quality)

## License

Free to use and modify.

## Version

2.0.0 - Refactored with batch processing support
