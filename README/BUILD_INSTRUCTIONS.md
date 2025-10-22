# Build Instructions for TTS Audio Mixer

This guide explains how to create a distributable .exe from the Python source code.

## Prerequisites

1. **Python 3.8+ installed**
2. **All dependencies installed:**
   ```powershell
   pip install -r requirements.txt
   pip install pyinstaller
   ```

3. **Download ffmpeg.exe:**
   - Visit: https://www.gyan.dev/ffmpeg/builds/
   - Download "ffmpeg-release-essentials.zip"
   - Extract `ffmpeg.exe` from the `bin` folder
   - Place it in the `dependencies` folder

## Quick Build Guide (Recommended)

### Step-by-Step Build Process

```powershell
# 1. Build the executable 
pyinstaller --onefile --console --name "TTS-Audio-Mixer" tts.py

# 2. Copy new .exe to main folder
Copy-Item dist\TTS-Audio-Mixer.exe . -Force

# 3. Test the new .exe
.\TTS-Audio-Mixer.exe
```

### Cleanup After Build (Optional)

```powershell
# Remove temporary build files (keeps the .exe in root)
Remove-Item -Recurse -Force build, dist
Remove-Item TTS-Audio-Mixer.spec
```

**Note:** The executable is copied to the root directory for easy access. The `dist/` and `build/` folders are just build artifacts.

### Option 3: With Custom Icon

```powershell
pyinstaller --onefile --console --name "TTS-Audio-Mixer" --icon=app_icon.ico tts.py
```

**Note:** Only if you have a custom `app_icon.ico` file.

## Testing the Build

1. Copy the distribution folder to a different location
2. Ensure required folders exist:
   - `dependencies/` with `ffmpeg.exe`
   - `input/` with `config.json` and background sound files
   - `output/` folder (will be created automatically with TTS/ and MIXED/ subfolders)
3. Run `TTS-Audio-Mixer.exe`
4. Verify it finds ffmpeg.exe in the dependencies folder
5. Verify it reads config from the input folder
6. Test generating audio files
7. Check that files are saved:
   - TTS files in `output/TTS/`
   - Mixed files in `output/MIXED/`
8. Test with different settings in `input/config.json`
