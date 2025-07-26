# Media Slideshow Creator

A Python script that creates slideshow videos from images and videos with smooth crossfade transitions and proper aspect ratio preservation.

## Features

- **Mixed Media Support**: Handles both images and videos
- **Aspect Ratio Preservation**: No distortion for portrait/landscape media
- **Crossfade Effects**: Smooth transitions between clips
- **Smart Centering**: Centers media on black background
- **High Quality Output**: 1920x1080 MP4 videos with H.264 encoding

## Prerequisites

### Install pyenv (Python Version Manager)

**macOS:**
```bash
brew install pyenv pyenv-virtualenv
```

**Linux:**
```bash
curl https://pyenv.run | bash
```

**Add to your shell configuration** (`~/.bashrc` or `~/.zshrc`):
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Restart your shell after adding these lines.

## Installation

1. **Clone and enter the repository:**
   ```bash
   git clone <your-repo-url>
   cd stitches
   ```

2. **Install Python and create virtual environment:**
   ```bash
   pyenv install 3.13.5
   pyenv virtualenv 3.13.5 stitches-env
   pyenv local stitches-env
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

The virtual environment will now activate automatically when you enter the project directory.

## Usage

1. **Add your media files** to the `media/` folder
   - Supported: `.jpg`, `.jpeg`, `.png`, `.webp`, `.mp4`, `.mov`, `.avi`, `.mkv`

2. **Run the script:**
   ```bash
   python stitch_media.py
   ```

3. **Find your slideshow:** `output_video.mp4`

## Configuration

Edit the settings in `stitch_media.py`:

```python
# --- CONFIGURATION ---
FOLDER_PATH = "./media"           # Media folder location
IMAGE_DURATION = 15               # Seconds per image
CROSSFADE_ENABLED = True          # Enable crossfade transitions
CROSSFADE_DURATION = 3.0          # Crossfade duration in seconds
OUTPUT_FILE = "output_video.mp4"  # Output filename
RESOLUTION = (1920, 1080)         # Video resolution
# ----------------------
```

## How It Works

1. **Scans** the media folder for supported files
2. **Resizes** each file to fit the target resolution (preserving aspect ratio)
3. **Centers** media on a black background
4. **Applies** crossfade transitions between clips
5. **Outputs** a single MP4 slideshow

## Troubleshooting

**"No module named 'moviepy'":**
```bash
# Make sure you're in the project directory (virtual environment should auto-activate)
pip install -r requirements.txt
```

**pyenv not found:**
```bash
# Check installation
pyenv --version
# If not found, reinstall pyenv and restart your shell
```

**Python version issues:**
```bash
# Check current version
python --version
pyenv version
# Should show Python 3.13.5 and stitches-env
```

## Dependencies

- **Python**: 3.13+ (managed by pyenv)
- **MoviePy**: Video editing and processing
- **NumPy**: Numerical operations
- **Pillow**: Image processing

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and test: `python stitch_media.py`
4. Commit and push: `git commit -m "Add feature" && git push origin feature/your-feature`
5. Create a pull request 