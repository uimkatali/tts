# TTS Audio Mixer - User Guide

A simple application that converts text to speech and mixes it with background sounds (like alarms).

## Quick Start

### Step 1: Extract Files

Extract all files from the ZIP to a folder:

```
TTS-Audio-Mixer/
├── TTS-Audio-Mixer.exe      ← The application
├── ffmpeg.exe               ← Required audio processor
├── config.json              ← Your text configurations
├── breach_alarm_994.wav     ← Background sound (alarm)
└── UserREADME.md           ← This file
```

### Step 2: Edit Your Text

Open `config.json` with Notepad and edit the text you want to convert to speech.

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

Double-click `TTS-Audio-Mixer.exe`

The application will:
1. Read your config.json
2. Generate speech from your text
3. Mix it with background sounds
4. Save the files in the same folder

### Step 4: Find Your Files

After running, you'll have:
- `alarma_parter.mp3` - Speech only
- `mixed_alarma_parter.mp3` - Speech with background sound

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

## Troubleshooting

### "ffmpeg.exe not found"
- Make sure `ffmpeg.exe` is in the same folder as `TTS-Audio-Mixer.exe`
- Don't move or delete `ffmpeg.exe`

### "Config file not found"
- Make sure `config.json` is in the same folder
- Check that the file is named exactly `config.json` (not `config.json.txt`)

### No audio files created
- Check the application window for error messages
- Make sure your text is not empty
- Verify the config.json format (use a JSON validator online)

### Background sound too loud/quiet
- Adjust `background_volume` in config.json
- Try values between 0.2 and 0.5 for best results

### Text not pronounced correctly
- Google Text-to-Speech might not pronounce some words correctly
- Try adding spaces or hyphens to improve pronunciation
- Some special characters might not work

## Tips

1. **Keep it simple** - Short, clear messages work best
2. **Test first** - Create one file to test before making many
3. **Backup config.json** - Save a copy before making big changes
4. **Use meaningful filenames** - Name files so you know what they contain
5. **Check the output** - Always listen to generated files before using them

## Need Help?

Common tasks:

**Task: Create 10 alarm messages**
1. Open config.json
2. Copy one audio job block
3. Paste it 9 more times (add commas between blocks)
4. Change the text and filename for each
5. Save and run

**Task: Change the language**
1. Open config.json
2. Change `"language": "ro"` to `"language": "en"` (or your language)
3. Save and run

**Task: Make background quieter**
1. Open config.json
2. Change `"background_volume": 0.3` to a lower number like `0.2` or `0.1`
3. Save and run

**Task: Remove background sound**
1. Open config.json
2. Delete the `"background_sound"` and `"background_volume"` lines
3. Save and run

## File Formats

**Input:**
- config.json (text configuration)
- .wav, .mp3, .ogg files (for background sounds)

**Output:**
- .mp3 files (speech audio)

## Requirements

All required files are included:
- TTS-Audio-Mixer.exe (the application)
- ffmpeg.exe (audio processing)

No installation needed! Just extract and run.

## Version

Version 2.0 - Bundled with ffmpeg for easy deployment

