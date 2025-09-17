# Audio Metadata Remover 🧹

A simple yet powerful Python script to remove all metadata from your audio files using FFmpeg. This tool helps you clean up your music library for privacy, consistency, or to fix corrupted tags.

The script directly copies the audio stream without re-encoding, so **there is no loss in audio quality**.

## Features

-   **Removes All Metadata:** Strips tags, cover art, lyrics, and any other embedded information.
-   **Batch Processing:** Process a single file or an entire directory of audio files.
-   **Recursive Mode:** Optionally process all subdirectories within a given folder.
-   **Safe Backups:** Create a backup of the original file before removing metadata.
-   **No Quality Loss:** Directly copies the audio stream without re-encoding.
-   **Cross-Platform:** Works on Windows, macOS, and Linux.

## Why Use This Script?

-   **Privacy:** Remove personal information that might be stored in audio tags.
-   **Consistency:** Create a clean, uniform library where all files are free of unwanted data.
-   **Fixing Errors:** Resolve issues with players that struggle to read corrupted metadata.

## Requirements

1.  **Python 3.6+**
2.  **FFmpeg:** The script relies on FFmpeg to process the files. You must install it and ensure it's available in your system's PATH.

    -   **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` folder to your PATH.
    -   **macOS (using Homebrew):** `brew install ffmpeg`
    -   **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install ffmpeg`

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd your-repository-name
    ```

Alternatively, you can just download the `metadata_remover.py` script directly.

## Usage

The script is run from the command line. The basic syntax is:

```bash
python metadata_remover.py <target> [options]

