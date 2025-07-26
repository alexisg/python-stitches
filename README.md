# Media Slideshow Creator

A Python script that automatically creates slideshow videos from a collection of images and videos, with proper aspect ratio preservation and crossfade effects.

## Features

- **Mixed Media Support**: Handles both images and videos in the same slideshow
- **Aspect Ratio Preservation**: Automatically resizes media to fit the target resolution without distortion
- **Smart Centering**: Centers all media on a black background, supporting both portrait and landscape orientations
- **Configurable Duration**: Set custom display duration for images
- **Crossfade Effects**: Smooth transitions between clips with configurable duration
- **High Quality Output**: Produces 1920x1080 MP4 videos with H.264 encoding

## Prerequisites

### Installing pyenv (Python Version Manager)

**macOS (using Homebrew):**
```bash
brew install pyenv
```

**Linux:**
```bash
curl https://pyenv.run | bash
```

**Windows:**
```bash
# Install pyenv-win via pip
pip install pyenv-win
```

### Setting up pyenv

Add pyenv to your shell configuration:

**For bash/zsh (add to `~/.bashrc` or `~/.zshrc`):**
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

**For Windows (add to PowerShell profile):**
```powershell
# Add pyenv-win to PATH
$env:PYENV_ROOT = "$env:USERPROFILE\.pyenv"
$env:PATH = "$env:PYENV_ROOT\bin;$env:PATH"
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd stitches
   ```

2. **Install Python version** (optional - pyenv recommended):
   ```bash
   # Install Python 3.13.0 or higher (3.13.5 recommended)
   pyenv install 3.13.5
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv stitch-env
   ```

4. **Activate the virtual environment**:
   ```bash
   # On macOS/Linux:
   source stitch-env/bin/activate
   
   # On Windows:
   stitch-env\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Auto-Activation Setup (Optional but Recommended)

To automatically activate the virtual environment when you enter the project directory:

### Using pyenv-virtualenv (Recommended)

1. **Install pyenv-virtualenv**:
   ```bash
   # macOS
   brew install pyenv-virtualenv
   
   # Linux
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   ```

2. **Add to your shell configuration** (`~/.bashrc` or `~/.zshrc`):
   ```bash
   eval "$(pyenv virtualenv-init -)"
   ```

3. **Create a virtual environment with pyenv**:
   ```bash
   pyenv virtualenv 3.13.5 stitches-env
   ```

4. **Set local virtual environment**:
   ```bash
   pyenv local stitches-env
   ```

Now the virtual environment will automatically activate when you enter the project directory!

### Alternative: Using direnv

1. **Install direnv**:
   ```bash
   # macOS
   brew install direnv
   
   # Linux
   sudo apt install direnv  # Ubuntu/Debian
   ```

2. **Add to your shell configuration**:
   ```bash
   eval "$(direnv hook bash)"  # or zsh
   ```

3. **Create `.envrc` file in project root**:
   ```bash
   echo "source stitch-env/bin/activate" > .envrc
   direnv allow
   ```

## Usage

1. **Prepare your media files**:
   - Place all your images and videos in the `media/` folder
   - Supported formats:
     - Images: `.jpg`, `.jpeg`, `.png`, `.webp`
     - Videos: `.mp4`, `.mov`, `.avi`, `.mkv`

2. **Run the script**:
   ```bash
   python stitch_media.py
   ```

3. **Find your output**:
   - The slideshow will be saved as `output_video.mp4` in the project directory

## Configuration

Edit the configuration section in `stitch_media.py` to customize your slideshow:

```python
# --- CONFIGURATION ---
FOLDER_PATH = "./media"   # Change to your media folder
IMAGE_DURATION = 15       # Seconds to display each image
FADE_DURATION = 1.0       # Crossfade duration (currently disabled)
CROSSFADE_ENABLED = True  # Enable/disable crossfades between clips
CROSSFADE_DURATION = 3.0  # Crossfade duration in seconds
OUTPUT_FILE = "output_video.mp4"
RESOLUTION = (1920, 1080) # Target resolution
# ----------------------
```

### Configuration Options

- **FOLDER_PATH**: Directory containing your media files
- **IMAGE_DURATION**: How long to display each image (videos play at full length)
- **CROSSFADE_ENABLED**: Enable or disable crossfade effects between clips (default: True)
- **CROSSFADE_DURATION**: Duration of crossfade effects in seconds (default: 3.0)
- **OUTPUT_FILE**: Name of the output video file
- **RESOLUTION**: Target resolution for the slideshow (width, height)

## How It Works

1. **Media Processing**: The script scans the specified folder for supported media files
2. **Aspect Ratio Preservation**: Each media file is resized to fit within the target resolution while maintaining its original aspect ratio
3. **Centering**: Media is centered on a black background, ensuring no distortion regardless of orientation
4. **Concatenation**: All processed clips are combined into a single video
5. **Output**: The final slideshow is rendered as an MP4 file

## File Structure

```
stitches/
├── stitch_media.py      # Main script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore rules
├── media/              # Place your media files here
├── bak/                # Backup folder (ignored by git)
├── compressed/         # Compressed media (ignored by git)
└── output_video.mp4    # Generated slideshow (ignored by git)
```

## Troubleshooting

### Common Issues

1. **"No module named 'moviepy'"**: Make sure you've activated the virtual environment and installed requirements:
   ```bash
   source stitch-env/bin/activate  # or use auto-activation
   pip install -r requirements.txt
   ```

2. **pyenv not found**: Ensure pyenv is properly installed and configured in your shell:
   ```bash
   pyenv --version
   ```

3. **Python version issues**: Check your Python version:
   ```bash
   python --version
   pyenv version
   ```

4. **Large file sizes**: The script processes media at full quality. Consider compressing your source files if output size is a concern.

5. **Slow processing**: Video processing can be resource-intensive. The script processes files sequentially for memory efficiency.

### Performance Tips

- Use compressed video formats (H.264) for faster processing
- Consider reducing image resolution if processing speed is important
- Ensure sufficient disk space for the output video
- Use pyenv-virtualenv for better environment management

## Dependencies

- **Python**: 3.13+ (managed by pyenv)
- **MoviePy**: Video editing and processing
- **NumPy**: Numerical operations
- **Pillow**: Image processing

## Development

### Setting up for development

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**:
   ```bash
   python stitch_media.py
   ```
5. **Commit and push**:
   ```bash
   git add .
   git commit -m "Add your feature description"
   git push origin feature/your-feature-name
   ```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## Version History

- **v1.0**: Initial release with basic slideshow functionality
- **v2.0**: Updated for MoviePy v2.x compatibility with improved aspect ratio handling
- **v2.1**: Added pyenv support and auto-activation instructions 