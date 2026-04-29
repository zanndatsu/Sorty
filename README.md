# Sorty

An app that allows you to archive your SD card photos&videos smoothly.

## Features

- 📸 Archive photos from your SD card
- 🎥 Archive videos from your SD card
- 📁 Organize files smoothly into an archive folder
- 💻 Works on Windows, Mac, and Linux
- ⚡ No additional software required

## Download & Installation

### Option 1: Download Pre-Built Executable (Recommended for Windows)

1. Go to the [Releases](https://github.com/zanndatsu/Sorty/releases) page
2. Download `Sorty.exe` (Windows) or `Sorty` (Mac/Linux)
3. Double-click to run - **No installation needed!**

### Option 2: Run from Source (For Developers)

**Requirements:**
- Python 3.8 or higher

**Steps:**

1. Clone the repository:
   ```bash
   git clone https://github.com/zanndatsu/Sorty.git
   cd Sorty
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

## How to Use

1. **Launch** Sorty (double-click the .exe file on Windows)
2. **Click** "Select SD Card Folder" button
3. **Choose** your SD card or the folder containing photos/videos
4. **Click** "Archive Files" to organize your media
5. **Done!** Your files will be moved to an "Archived" folder

## Creating an Executable (For Windows Users)

If you want to create your own `.exe` file:

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Clone this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Build the executable:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```
5. Find `Sorty.exe` in the `dist/` folder

## System Requirements

- **Windows:** Windows 7 or later
- **Mac:** macOS 10.12 or later
- **Linux:** Any modern Linux distribution

## Supported File Types

- Photos: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- Videos: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`

## License

This project is open source and available under the MIT License.

## Support

Found a bug? Have a feature request? [Open an issue](https://github.com/zanndatsu/Sorty/issues)