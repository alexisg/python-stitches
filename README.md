# Media Slideshow Creator

A Python script that automatically creates slideshow videos from a collection of images and videos, with proper aspect ratio preservation and crossfade effects.

## Features

- **Mixed Media Support**: Handles both images and videos in the same slideshow
- **Aspect Ratio Preservation**: Automatically resizes media to fit the target resolution without distortion
- **Smart Centering**: Centers all media on a black background, supporting both portrait and landscape orientations
- **Configurable Duration**: Set custom display duration for images
- **High Quality Output**: Produces 1920x1080 MP4 videos with H.264 encoding

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd stitches
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv stitch-env
   source stitch-env/bin/activate  # On Windows: stitch-env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
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
OUTPUT_FILE = "output_video.mp4"
RESOLUTION = (1920, 1080) # Target resolution
# ----------------------
```

### Configuration Options

- **FOLDER_PATH**: Directory containing your media files
- **IMAGE_DURATION**: How long to display each image (videos play at full length)
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

1. **"No module named 'moviepy'"**: Make sure you've installed the requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. **Large file sizes**: The script processes media at full quality. Consider compressing your source files if output size is a concern.

3. **Slow processing**: Video processing can be resource-intensive. The script processes files sequentially for memory efficiency.

### Performance Tips

- Use compressed video formats (H.264) for faster processing
- Consider reducing image resolution if processing speed is important
- Ensure sufficient disk space for the output video

## Dependencies

- **MoviePy**: Video editing and processing
- **NumPy**: Numerical operations
- **Pillow**: Image processing

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## Version History

- **v1.0**: Initial release with basic slideshow functionality
- **v2.0**: Updated for MoviePy v2.x compatibility with improved aspect ratio handling 