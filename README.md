# Mixare Audio TTS cu Sunet de Fundal

Script Python pentru mixarea text-to-speech cu un sunet de fundal (de exemplu, alarmă).

## Instalare și Utilizare

### 1. Instalează ffmpeg

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

### 2. Instalează biblioteca Python

```bash
pip install gtts
```

### 3. Rulează scriptul

```bash
python tts.py
```

## Configurare

Deschide `tts.py` și modifică:

```python
text = "Alarma afi turnicheti"
lang = 'ro'
filename = "alarma_afi_turnicheti.mp3"
background_filename = "breach_alarm_994.wav"
background_volume = 0.3
```

- `text` - textul de rostit
- `lang` - limba (ro, en, fr, etc.)
- `filename` - numele fișierului TTS generat
- `background_filename` - fișierul cu sunetul de fundal
- `background_volume` - volumul fundal (0.3 = 30%, 0.5 = 50%, etc.)

## Ieșire

Scriptul creează două fișiere:
- `alarma_afi_turnicheti.mp3` - TTS generat
- `mixed_alarma_afi_turnicheti.mp3` - audio mixat final

## Compatibilitate

- Python 3.x (testat pe 3.14)
- Windows, Linux, macOS
- Formate suportate: .mp3, .wav, .ogg, .flac

