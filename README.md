# Audio Metadata Remover 🎵

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)

A simple yet powerful cross-platform Python script to completely remove all metadata (tags) from audio files using **FFmpeg**.

The script operates without re-encoding, ensuring that the original audio quality is preserved.

### ✨ Key Features

*   **Complete Metadata Removal**: Strips all tags (ID3, Vorbis comments, etc.) from your audio files.
*   **Lossless Operation**: Does not re-encode the audio, preserving 100% of the original quality (`-c copy`).
*   **Batch Processing**: Process single files or entire directories at once.
*   **Recursive Mode**: Optionally scan and process all subdirectories within a given path.
*   **Safe Backups**: Create a `.backup` copy of each original file before processing for peace of mind.
*   **Cross-Platform**: Works flawlessly on Windows, macOS, and Linux.
*   **Wide Format Support**: Handles most common audio formats out of the box.

### ⚙️ Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.6+**
2.  **FFmpeg**: The script depends on FFmpeg being installed and accessible in your system's PATH.

    *   **On Ubuntu/Debian:**
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    *   **On CentOS/RHEL:**
        ```bash
        sudo yum install ffmpeg
        ```
    *   **On Arch Linux:**
        ```bash
        sudo pacman -S ffmpeg
        ```
    *   **On macOS (using [Homebrew](https://brew.sh/)):**
        ```bash
        brew install ffmpeg
        ```
    *   **On Windows:**
        Download the latest build from the [official FFmpeg website](https://ffmpeg.org/download.html), extract it, and add the `bin` directory to your system's `PATH` environment variable.

### 🚀 Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  (Optional, for Linux/macOS) Make the script executable for easier use:
    ```bash
    chmod +x metadata_remover.py
    ```
    *Assuming the script is named `metadata_remover.py`.*

### 🔧 Usage

The script is run from the command line, targeting either a single file or a directory.

**General Syntax:**
```bash
# On Windows
python metadata_remover.py [options] <target_path>

# On Linux/macOS (if executable)
./metadata_remover.py [options] <target_path>
```

#### **Arguments & Options**

*   `target`: **(Required)** The path to the audio file or directory you want to process.
*   `-r`, `--recursive`: Process files in the target directory and all its subdirectories.
*   `-b`, `--backup`: Create a backup of each original file (with a `.backup` extension) before removing metadata.

#### **Usage Examples**

1.  **Remove metadata from a single file:**
    ```bash
    python metadata_remover.py "path/to/my song.mp3"
    ```

2.  **Process all audio files in a specific directory (non-recursive):**
    ```bash
    python metadata_remover.py "path/to/music_folder/"
    ```

3.  **Process an entire directory and all its subdirectories:**
    ```bash
    python metadata_remover.py -r "path/to/my_music_library/"
    ```

4.  **Process recursively and create backups for all original files:**
    ```bash
    python metadata_remover.py -r -b "/path/to/another/folder"
    ```

### 🎧 Supported Formats

The script can process the following audio file types:

*   `.mp3`
*   `.flac`
*   `.ogg`
*   `.m4a`
*   `.aac`
*   `.wav`
*   `.wma`

### 💡 How It Works

The script leverages the power of FFmpeg by using a `subprocess` call to execute the following command on each audio file:

```bash
ffmpeg -i "input.mp3" -map 0:a -c copy -map_metadata -1 -fflags +bitexact "output.mp3"
```

*   `-i "input.mp3"`: Specifies the input file.
*   `-map 0:a`: Selects **only the audio streams** from the input file, ignoring any video or other data streams.
*   `-c copy`: This is the most important flag. It instructs FFmpeg to **copy** the audio stream without re-encoding it. This is fast and preserves 100% of the original audio quality.
*   `-map_metadata -1`: This flag is the core of the script's function, telling FFmpeg to **remove all metadata** streams from the output file.
*   `-fflags +bitexact`: An additional flag to ensure the output is bit-for-bit identical where possible, contributing to a clean, unaltered audio stream.

The script handles file operations safely by first creating a temporary output file and then replacing the original only upon successful completion.
