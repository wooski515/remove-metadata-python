Audio Metadata Remover 🧹

A simple yet powerful Python script to remove all metadata from your audio files using FFmpeg. This tool helps you clean up your music library for privacy, consistency, or to fix corrupted tags.

The script directly copies the audio stream without re-encoding, so there is no loss in audio quality.

Features

Removes All Metadata: Strips tags, cover art, lyrics, and any other embedded information.

Batch Processing: Process a single file or an entire directory of audio files.

Recursive Mode: Optionally process all subdirectories within a given folder.

Safe Backups: Create a backup of the original file before removing metadata.

No Quality Loss: Directly copies the audio stream without re-encoding.

Cross-Platform: Works on Windows, macOS, and Linux.

Why Use This Script?

Privacy: Remove personal information that might be stored in audio tags.

Consistency: Create a clean, uniform library where all files are free of unwanted data.

Fixing Errors: Resolve issues with players that struggle to read corrupted metadata.

Requirements

Python 3.6+

FFmpeg: The script relies on FFmpeg to process the files. You must install it and ensure it's available in your system's PATH.

Windows: Download from ffmpeg.org and add the bin folder to your PATH.

macOS (using Homebrew): brew install ffmpeg

Linux (Debian/Ubuntu): sudo apt update && sudo apt install ffmpeg

Installation

Clone the repository:

code
Bash
download
content_copy
expand_less

git clone https://github.com/your-username/your-repository-name.git

Navigate to the project directory:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
cd your-repository-name

Alternatively, you can just download the metadata_remover.py script directly.

Usage

The script is run from the command line. The basic syntax is:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python metadata_remover.py <target> [options]

<target>: The path to the audio file or directory you want to process.

[options]: Optional flags to change the script's behavior.

Examples
1. Remove metadata from a single file
code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python metadata_remover.py "/path/to/your/song.mp3"
2. Process all audio files in a directory

This will process files only in the specified directory, not subfolders.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python metadata_remover.py "/path/to/your/music_folder/"
3. Process a directory recursively (including all subfolders)

Use the -r or --recursive flag.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python metadata_remover.py -r "/path/to/your/music_library/"
4. Process a directory and create backups

Use the -b or --backup flag. A copy of each original file will be saved with a .backup extension (e.g., song.mp3.backup).

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python metadata_remover.py -b "/path/to/your/music_folder/"

You can combine flags:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python metadata_remover.py -r -b "/path/to/your/entire_music_library/"
Supported Formats

The script supports the following audio formats:
MP3, FLAC, OGG, M4A, AAC, WAV, WMA

How It Works

The script uses ffmpeg to create a new, clean version of each audio file. It does this by copying the audio stream (-c copy) while simultaneously removing all metadata streams (-map_metadata -1). This process is fast and does not affect audio quality. The original file is then replaced by the new, clean file.

License

This project is licensed under the MIT License. See the LICENSE file for details.
