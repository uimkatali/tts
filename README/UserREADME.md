# TTS Audio Mixer - User Guide

A simple application that converts text to speech and mixes it with background sounds (like alarms).

## Quick Start

### Step 1: Extract Files

Extract all files from the ZIP to a folder:


### Step 2: Edit Your Text

Open `input/config.json` with Notepad and edit the text you want to convert to speech.

**Example:**
```json
{
  "audio_jobs": [
    {
      "text": "Alarma afi parter",
      "language": "ro",
      "output_filename": "alarma_parter.mp3",
      "background_sound": "breach_alarm_994.wav",
      "background_volume": 0.3
    }
  ]
}
```

**What each field means:**
- `text` - The words to speak
- `language` - Language code (`ro` for Romanian, `en` for English, `es` for Spanish, etc.)
- `output_filename` - Name of the file to create
- `background_sound` - Sound file to mix with speech (optional)
- `background_volume` - How loud the background is (0.1 = quiet, 0.5 = medium, 1.0 = full volume)

### Step 3: Run the Application

Double-click `TTS-Audio-Mixer.exe` in the main folder

The application will:
1. Read your config from the `input/` folder
2. Generate speech from your text and save to `output/TTS/`
3. Mix it with background sounds from the `input/` folder
4. Save the final mixed files in the `output/MIXED/` folder

## Creating Multiple Audio Files

You can create many files at once by adding more jobs to config.json:

```json
{
  "audio_jobs": [
    {
      "text": "Alarma afi parter",
      "language": "ro",
      "output_filename": "alarma_parter.mp3",
      "background_sound": "breach_alarm_994.wav",
      "background_volume": 0.3
    },
    {
      "text": "Alarma afi etajul 1",
      "language": "ro",
      "output_filename": "alarma_etaj1.mp3",
      "background_sound": "breach_alarm_994.wav",
      "background_volume": 0.3
    },
    {
      "text": "Emergency floor 2",
      "language": "en",
      "output_filename": "emergency_floor2.mp3",
      "background_sound": "breach_alarm_994.wav",
      "background_volume": 0.5
    }
  ]
}
```

Just add a comma after each job and copy the pattern!

## Quick Reference

### Supported Languages

Common language codes:
- `ro` - Romanian
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese

### Volume Settings

- `0.1` - Very quiet background
- `0.3` - Recommended (default)
- `0.5` - Medium background
- `1.0` - Full volume background

### Creating Speech Without Background Sound

Remove the `background_sound` and `background_volume` lines:

```json
{
  "text": "Simple announcement",
  "language": "en",
  "output_filename": "announcement.mp3"
}
```

## Advanced: Command Line Usage

You can also run the application from the command line for one-off files:

```bash
TTS-Audio-Mixer.exe --text "Your text here" --output myfile.mp3 --lang en
```

**With background sound:**
```bash
TTS-Audio-Mixer.exe --text "Alert message" --output alert.mp3 --background alarm.wav --volume 0.3 --lang ro
```

## Folder Structure

- `TTS-Audio-Mixer.exe` - The application (double-click to run)
- `input/` - Put your config.json and background sound files here
- `output/` - Generated audio files
  - `TTS/` - TTS-only audio files (speech without background)
  - `MIXED/` - Final mixed audio files (speech + background sound)
- `dependencies/` - Contains ffmpeg.exe (don't modify)
- `dist/` and `build/` - Build artifacts (can be ignored/deleted)

## Tips

1. **Keep it simple** - Short, clear messages work best
2. **Test first** - Create one file to test before making many
3. **Backup config.json** - Save a copy before making big changes
4. **Use meaningful filenames** - Name files so you know what they contain
5. **Place background sounds in input/** - Any .wav or .mp3 files should go in the input folder
6. **Find your files**:
   - TTS-only files: `output/TTS/`
   - Mixed files (with background): `output/MIXED/`

## Version

Version 3.0.0 - Bundled with ffmpeg for easy deployment