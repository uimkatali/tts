"""
Text-to-Speech Audio Mixer
Generates TTS audio and mixes it with background sounds using ffmpeg.
"""
import json
import logging
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List
import argparse

from gtts import gTTS


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Output folder for final mixed audio files
OUTPUT_FOLDER = "output"


@dataclass
class AudioJob:
    """Configuration for a single TTS audio mixing job."""
    text: str
    output_filename: str
    language: str = 'ro'
    background_sound: Optional[str] = None
    background_volume: float = 0.3
    
    @classmethod
    def from_dict(cls, data: dict) -> 'AudioJob':
        """Create AudioJob from dictionary."""
        return cls(**data)


class TTSMixer:
    """Handles text-to-speech generation and audio mixing."""
    
    def __init__(self, ffmpeg_path: Optional[str] = None):
        """Initialize TTSMixer with optional ffmpeg path."""
        self.ffmpeg_path = ffmpeg_path or self._find_ffmpeg()
        if not self.ffmpeg_path:
            raise RuntimeError(
                "ffmpeg.exe not found!\n"
                "Please ensure ffmpeg.exe is in the same folder as this application.\n"
                "Download from: https://www.gyan.dev/ffmpeg/builds/"
            )
    
    @staticmethod
    def _find_ffmpeg() -> Optional[str]:
        """Locate ffmpeg executable. Checks bundled version first, then system."""
        
        # Check if running as PyInstaller executable
        if getattr(sys, 'frozen', False):
            exe_dir = os.path.dirname(sys.executable)
            bundled_ffmpeg = os.path.join(exe_dir, "ffmpeg.exe")
            if os.path.exists(bundled_ffmpeg):
                logger.info(f"Using bundled ffmpeg: {bundled_ffmpeg}")
                return bundled_ffmpeg
        
        # Check same directory as script (development/distribution folder)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_ffmpeg = os.path.join(script_dir, "ffmpeg.exe")
        if os.path.exists(local_ffmpeg):
            logger.info(f"Using local ffmpeg: {local_ffmpeg}")
            return local_ffmpeg
        
        # Fallback: Check system PATH
        ffmpeg_cmd = shutil.which("ffmpeg")
        if ffmpeg_cmd:
            logger.info(f"Using system ffmpeg: {ffmpeg_cmd}")
            return ffmpeg_cmd
        
        return None
    
    def generate_tts(self, text: str, lang: str, output_file: str) -> Path:
        """Generate TTS audio file from text."""
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(output_file)
            logger.info(f"Generated TTS: {output_file}")
            return Path(output_file)
        except Exception as e:
            logger.error(f"Failed to generate TTS: {e}")
            raise
    
    def mix_audio(
        self, 
        tts_file: str, 
        background_file: str,
        output_file: str,
        background_volume: float = 0.3,
        quality: int = 2
    ) -> Path:
        """Mix TTS audio with background sound using ffmpeg."""
        
        if not Path(tts_file).exists():
            raise FileNotFoundError(f"TTS file not found: {tts_file}")
        if not Path(background_file).exists():
            raise FileNotFoundError(f"Background file not found: {background_file}")
        
        ffmpeg_cmd = [
            self.ffmpeg_path,
            "-y",
            "-i", tts_file,
            "-i", background_file,
            "-filter_complex",
            f"[1:a]volume={background_volume}[bg];[0:a][bg]amix=inputs=2:duration=shortest:dropout_transition=0",
            "-c:a", "libmp3lame",
            "-q:a", str(quality),
            output_file
        ]
        
        try:
            # Determine working directory (handles both .py and .exe)
            if getattr(sys, 'frozen', False):
                # Running as compiled .exe
                work_dir = os.path.dirname(sys.executable)
            else:
                # Running as .py script
                work_dir = os.path.dirname(os.path.abspath(__file__))
            
            result = subprocess.run(
                ffmpeg_cmd, 
                capture_output=True, 
                text=True, 
                check=True, 
                cwd=work_dir
            )
            logger.info(f"Mixed audio saved: {output_file}")
            return Path(output_file)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error mixing audio: {e.stderr}")
            raise
    
    def process_job(self, job: AudioJob) -> tuple[Path, Optional[Path]]:
        """Process a single audio job."""
        logger.info(f"Processing: {job.text[:50]}...")
        
        tts_file = self.generate_tts(job.text, job.language, job.output_filename)
        
        if job.background_sound:
            # Create output folder if it doesn't exist
            output_folder = Path(OUTPUT_FOLDER)
            output_folder.mkdir(exist_ok=True)
            
            # Save mixed file in the output folder
            mixed_filename = output_folder / f"mixed_{job.output_filename}"
            mixed_file = self.mix_audio(
                str(tts_file),
                job.background_sound,
                str(mixed_filename),
                job.background_volume
            )
            return tts_file, mixed_file
        
        return tts_file, None
    
    def process_batch(self, jobs: List[AudioJob]) -> None:
        """Process multiple audio jobs."""
        logger.info(f"Processing {len(jobs)} audio jobs...")
        
        for i, job in enumerate(jobs, 1):
            try:
                logger.info(f"Job {i}/{len(jobs)}")
                self.process_job(job)
            except Exception as e:
                logger.error(f"Failed to process job {i}: {e}")
                continue
        
        logger.info("Batch processing complete!")


def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_file}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate TTS audio and mix with background sounds'
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config.json',
        help='Path to JSON configuration file'
    )
    parser.add_argument(
        '--text',
        type=str,
        help='Text to convert to speech (single job mode)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output filename (single job mode)'
    )
    parser.add_argument(
        '--background',
        type=str,
        help='Background sound file (optional)'
    )
    parser.add_argument(
        '--volume',
        type=float,
        default=0.3,
        help='Background volume (0.0-1.0)'
    )
    parser.add_argument(
        '--lang',
        type=str,
        default='ro',
        help='Language code (ro, en, etc.)'
    )
    
    args = parser.parse_args()
    
    try:
        mixer = TTSMixer()
        
        if args.text and args.output:
            job = AudioJob(
                text=args.text,
                output_filename=args.output,
                language=args.lang,
                background_sound=args.background,
                background_volume=args.volume
            )
            mixer.process_job(job)
        else:
            config = load_config(args.config)
            jobs = [AudioJob.from_dict(job) for job in config.get('audio_jobs', [])]
            
            if not jobs:
                logger.warning("No jobs found in configuration")
                return
            
            mixer.process_batch(jobs)
    
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
