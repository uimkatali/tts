# Build Instructions for TTS Audio Mixer

This guide explains how to create a distributable .exe from the Python source code.

## Prerequisites

1. Python 3.8+ installed
2. All dependencies installed:
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

3. Download ffmpeg.exe:
   - Visit: https://www.gyan.dev/ffmpeg/builds/
   - Download "ffmpeg-release-essentials.zip"
   - Extract `ffmpeg.exe` from the `bin` folder

## Building the Executable

### Option 1: Single .exe File (Slower startup, fully portable)

```bash
pyinstaller --onefile --console --name "TTS-Audio-Mixer" tts.py
```

**Result:** Single .exe in `dist/TTS-Audio-Mixer.exe` (~10-15 MB)

### Option 2: Folder with Dependencies (Faster startup)

```bash
pyinstaller --onedir --console --name "TTS-Audio-Mixer" tts.py
```

**Result:** Folder in `dist/TTS-Audio-Mixer/` with .exe and libraries

### Option 3: Custom Build (Recommended)

```bash
pyinstaller --onefile --console --name "TTS-Audio-Mixer" --icon=app_icon.ico tts.py
```

Add `--icon=app_icon.ico` if you have a custom icon.

## Creating Distribution Package

After building, create the distribution folder structure:

```bash
# Create distribution folder
mkdir TTS-Audio-Mixer-Distribution
cd TTS-Audio-Mixer-Distribution

# Copy the executable
copy ..\dist\TTS-Audio-Mixer.exe .

# Copy ffmpeg (download separately)
copy path\to\ffmpeg.exe .

# Copy config and example files
copy ..\config.json .
copy ..\breach_alarm_994.wav .

# Copy user documentation
copy ..\UserREADME.md README.txt

# Create examples folder
mkdir examples
copy ..\config.json examples\config_example.json
```

## Final Distribution Structure

```
TTS-Audio-Mixer-v2.0/
├── TTS-Audio-Mixer.exe          (~10-15 MB)
├── ffmpeg.exe                   (~70-120 MB)
├── config.json
├── breach_alarm_994.wav
├── README.txt (copy of UserREADME.md)
└── examples/
    └── config_example.json
```

## Creating ZIP for Distribution

```bash
# Compress the entire folder
powershell Compress-Archive -Path TTS-Audio-Mixer-Distribution -DestinationPath TTS-Audio-Mixer-v2.0.zip
```

## Testing the Build

1. Copy the distribution folder to a different location
2. Run `TTS-Audio-Mixer.exe`
3. Verify it finds ffmpeg.exe
4. Test generating audio files
5. Test with different config.json settings

## Troubleshooting Build Issues

### "Module not found" errors
```bash
# Install missing dependencies
pip install gtts
```

### Large .exe size
- Normal for Python executables with dependencies
- Expected size: 10-15 MB for app + 70-120 MB for ffmpeg
- Use `--onedir` instead of `--onefile` if size is critical

### Missing imports in frozen app
Add hidden imports to PyInstaller:
```bash
pyinstaller --onefile --hidden-import=gtts --hidden-import=json tts.py
```

### ffmpeg not found in .exe
- Make sure ffmpeg.exe is in the same folder as the .exe
- The code checks the exe directory first (using `sys.executable`)

## Advanced: Custom Build Script

Create `build.py` for automated builds:

```python
import os
import shutil
import subprocess

# Clean previous builds
if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists('build'):
    shutil.rmtree('build')

# Build executable
subprocess.run([
    'pyinstaller',
    '--onefile',
    '--console',
    '--name', 'TTS-Audio-Mixer',
    'tts.py'
])

# Create distribution folder
dist_folder = 'TTS-Audio-Mixer-Distribution'
os.makedirs(dist_folder, exist_ok=True)

# Copy files
shutil.copy('dist/TTS-Audio-Mixer.exe', dist_folder)
shutil.copy('config.json', dist_folder)
shutil.copy('UserREADME.md', f'{dist_folder}/README.txt')

print(f"Build complete! Distribution in {dist_folder}/")
print("Don't forget to add ffmpeg.exe manually!")
```

Run with: `python build.py`

## Version Management

Update version in:
1. UserREADME.md
2. DevREADME.md
3. tts.py (add `__version__ = "2.0.0"` at the top)

## Distribution Checklist

Before releasing:
- [ ] Test on clean Windows machine
- [ ] Verify all audio formats work
- [ ] Check error messages are user-friendly
- [ ] Ensure ffmpeg.exe is included
- [ ] Test config.json with various settings
- [ ] Verify UserREADME.md is clear
- [ ] Test command-line arguments
- [ ] Check file sizes are reasonable
- [ ] Scan with antivirus (false positives common with PyInstaller)

## Notes

- PyInstaller creates large executables (normal behavior)
- First run may be slow (unpacking to temp folder)
- Some antivirus software flags PyInstaller executables (false positive)
- ffmpeg.exe must be distributed separately (licensing reasons)
- Users need no Python installation to run the .exe

