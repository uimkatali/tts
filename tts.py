from gtts import gTTS
import subprocess
import os
import shutil
import sys

text = "Alarma afi turnicheti"
lang = 'ro'
filename = "alarma_afi_turnicheti.mp3"
background_filename = "breach_alarm_994.wav"
background_volume = 0.3

tts = gTTS(text=text, lang=lang)
tts.save(filename)
print(f"Generated TTS: {filename}")

output_filename = "mixed_" + filename

def find_ffmpeg():
    ffmpeg_cmd = shutil.which("ffmpeg")
    if ffmpeg_cmd:
        return ffmpeg_cmd
    
    if sys.platform == "win32":
        import glob
        user_home = os.path.expanduser("~")
        paths = [
            os.path.join(user_home, "AppData", "Local", "Microsoft", "WinGet", "Packages", "Gyan.FFmpeg*", "**", "bin", "ffmpeg.exe"),
            "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe",
            "C:\\ffmpeg\\bin\\ffmpeg.exe",
        ]
        for pattern in paths:
            found = glob.glob(pattern, recursive=True)
            if found:
                return found[0]
    
    return None

ffmpeg_path = find_ffmpeg()

if not ffmpeg_path:
    print("ERROR: ffmpeg not found! Please install ffmpeg:")
    print("   Windows: winget install --id=Gyan.FFmpeg -e")
    print("   Linux: sudo apt-get install ffmpeg")
    print("   macOS: brew install ffmpeg")
    sys.exit(1)

ffmpeg_cmd = [
    ffmpeg_path,
    "-y",
    "-i", filename,
    "-i", background_filename,
    "-filter_complex",
    f"[1:a]volume={background_volume}[bg];[0:a][bg]amix=inputs=2:duration=shortest:dropout_transition=0",
    "-c:a", "libmp3lame",
    "-q:a", "2",
    output_filename
]

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, check=True, cwd=script_dir)
    print(f"SUCCESS: Mixed audio saved: {output_filename}")
except subprocess.CalledProcessError as e:
    print(f"ERROR: Error mixing audio: {e.stderr}")
    sys.exit(1)
