#!/usr/bin/env python3

import sys
import argparse
import subprocess
import shutil
from pathlib import Path

class MetadataRemover:
    def __init__(self):
        self.supported_extensions = {'.mp3', '.flac', '.ogg', '.m4a', '.aac', '.wav', '.wma'}
        
    def check_ffmpeg(self):
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         stdout=subprocess.DEVNULL, 
                         stderr=subprocess.DEVNULL, 
                         check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def is_audio_file(self, file_path):
        return Path(file_path).suffix.lower() in self.supported_extensions
    
    def remove_metadata_from_file(self, file_path, create_backup=False):
        file_path = Path(file_path)
        
        if not file_path.exists():
            print(f"❌ Error: File '{file_path}' not found")
            return False
            
        if not self.is_audio_file(file_path):
            print(f"⚠️  Skipping: '{file_path}' (unsupported format)")
            return False
        
        print(f"🔧 Processing: {file_path}")
        
        if create_backup:
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            try:
                shutil.copy2(file_path, backup_path)
                print(f"💾 Backup created: {backup_path}")
            except Exception as e:
                print(f"❌ Error creating backup: {e}")
                return False
        
        temp_path = file_path.with_suffix('.temp' + file_path.suffix)
        
        cmd = [
            'ffmpeg', '-i', str(file_path),
            '-map', '0:a',
            '-c', 'copy',
            '-map_metadata', '-1',
            '-fflags', '+bitexact',
            str(temp_path),
            '-y'
        ]
        
        try:
            subprocess.run(cmd, 
                           capture_output=True, 
                           text=True, 
                           check=True)
            
            shutil.move(temp_path, file_path)
            print(f"✅ Metadata removed from: {file_path}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error processing '{file_path}': {e.stderr}")
            if temp_path.exists():
                temp_path.unlink()
            return False
        except Exception as e:
            print(f"❌ Unexpected error while processing '{file_path}': {e}")
            if temp_path.exists():
                temp_path.unlink()
            return False
    
    def process_directory(self, directory_path, recursive=False, create_backup=False):
        directory_path = Path(directory_path)
        
        if not directory_path.is_dir():
            print(f"❌ Error: '{directory_path}' is not a directory")
            return False
        
        print(f"📁 Processing directory: {directory_path}")
        print(f"🔄 Mode: {'recursive' if recursive else 'current directory only'}")
        
        if recursive:
            files = directory_path.rglob('*')
        else:
            files = directory_path.iterdir()
        
        audio_files = [f for f in files if f.is_file() and self.is_audio_file(f)]
        
        if not audio_files:
            print("⚠️  No audio files found")
            return True
        
        print(f"🎵 Audio files found: {len(audio_files)}")
        
        success_count = 0
        for file_path in audio_files:
            if self.remove_metadata_from_file(file_path, create_backup):
                success_count += 1
        
        print(f"📊 Successfully processed: {success_count}/{len(audio_files)}")
        return True
    
    def run(self):
        parser = argparse.ArgumentParser(
            description='Removes metadata from audio files using ffmpeg.',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Usage examples:
  %(prog)s song.mp3                    # Remove metadata from a single file
  %(prog)s -r /path/to/music/          # Process an entire directory recursively
  %(prog)s -b -r /path/to/music/       # Process recursively with backups

Supported formats: MP3, FLAC, OGG, M4A, AAC, WAV, WMA
            '''
        )
        
        parser.add_argument('target', 
                          help='The file or directory to process')
        parser.add_argument('-r', '--recursive', 
                          action='store_true',
                          help='Process all files in the directory recursively')
        parser.add_argument('-b', '--backup', 
                          action='store_true',
                          help='Create backups of the original files (.backup extension)')
        
        args = parser.parse_args()
        
        if not self.check_ffmpeg():
            print("❌ Error: ffmpeg is not installed. Please install it:")
            print("   Ubuntu/Debian: sudo apt install ffmpeg")
            print("   CentOS/RHEL: sudo yum install ffmpeg")
            print("   Arch: sudo pacman -S ffmpeg")
            print("   macOS: brew install ffmpeg")
            print("   Windows: download from https://ffmpeg.org/download.html")
            sys.exit(1)
        
        target_path = Path(args.target)
        
        if not target_path.exists():
            print(f"❌ Error: '{target_path}' does not exist")
            sys.exit(1)
        
        try:
            if target_path.is_file():
                success = self.remove_metadata_from_file(target_path, args.backup)
                sys.exit(0 if success else 1)
            elif target_path.is_dir():
                success = self.process_directory(target_path, args.recursive, args.backup)
                sys.exit(0 if success else 1)
            else:
                print(f"❌ Error: '{target_path}' is not a file or a directory")
                sys.exit(1)
                
        except KeyboardInterrupt:
            print("\n⚠️  Operation interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            sys.exit(1)
        
        print("🎉 Done!")

if __name__ == '__main__':
    remover = MetadataRemover()
    remover.run()