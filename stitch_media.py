import sys
import os
from moviepy import (
    ImageClip,
    VideoFileClip,
    concatenate_videoclips
)
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy import ColorClip
from moviepy.video.fx import CrossFadeIn, CrossFadeOut

# Check Python version
if sys.version_info < (3, 13, 0):
    print(f"Error: Python 3.13.0 or higher is required. You are using Python {sys.version}")
    print("Please upgrade your Python version or use pyenv to install Python 3.13+")
    sys.exit(1)

# --- CONFIGURATION ---
FOLDER_PATH = "./media"   # Change to your media folder
IMAGE_DURATION = 15       # Seconds
FADE_DURATION = 1.0       # Crossfade duration
CROSSFADE_ENABLED = True  # Enable/disable crossfades between clips
CROSSFADE_DURATION = 3.0  # Crossfade duration in seconds
OUTPUT_FILE = "output_video.mp4"
RESOLUTION = (1920, 1080) # Desired resolution (optional)
# ----------------------

def is_image(file):
    return file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))

def is_video(file):
    return file.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))



def get_media_clips(folder):
    media_files = sorted(os.listdir(folder))
    clips = []

    for file in media_files:
        full_path = os.path.join(folder, file)

        if is_image(file):
            clip = ImageClip(full_path, duration=IMAGE_DURATION)
        elif is_video(file):
            clip = VideoFileClip(full_path)
        else:
            continue

        # Resize while preserving aspect ratio
        target_width, target_height = RESOLUTION
        clip_width, clip_height = clip.size
        scale = min(target_width / clip_width, target_height / clip_height)
        new_width = int(clip_width * scale)
        new_height = int(clip_height * scale)
        clip = clip.resized((new_width, new_height))

        # Center the clip on a black background
        background = ColorClip(size=RESOLUTION, color=(0, 0, 0), duration=clip.duration)
        x_center = (target_width - new_width) // 2
        y_center = (target_height - new_height) // 2
        composite = CompositeVideoClip([background, clip.with_position((x_center, y_center))])
        composite = composite.with_duration(clip.duration)
        clips.append(composite)

    return clips

def concatenate_clips(clips):
    if not clips:
        return None
    
    if not CROSSFADE_ENABLED or len(clips) <= 1:
        return concatenate_videoclips(clips)
    
    # Apply crossfade effects to clips
    processed_clips = []
    
    for i, clip in enumerate(clips):
        current_clip = clip
        
        # Calculate crossfade duration (don't exceed half the clip duration)
        crossfade_duration = min(CROSSFADE_DURATION, current_clip.duration / 2)
        
        if i == 0:
            # First clip: only fade out at the end
            if crossfade_duration > 0 and len(clips) > 1:
                current_clip = current_clip.with_effects([CrossFadeOut(crossfade_duration)])
        elif i == len(clips) - 1:
            # Last clip: only fade in at the beginning
            if crossfade_duration > 0:
                current_clip = current_clip.with_effects([CrossFadeIn(crossfade_duration)])
        else:
            # Middle clips: fade in at beginning and fade out at end
            if crossfade_duration > 0:
                current_clip = current_clip.with_effects([
                    CrossFadeIn(crossfade_duration),
                    CrossFadeOut(crossfade_duration)
                ])
        
        processed_clips.append(current_clip)
    
    print(f"Applying crossfade with duration: {crossfade_duration} seconds")
    
    # Use concatenate_videoclips with method="compose" and negative padding for overlaps
    return concatenate_videoclips(processed_clips, method="compose", padding=-crossfade_duration)

if __name__ == "__main__":
    print("Processing media...")
    if CROSSFADE_ENABLED:
        print(f"Crossfade enabled: {CROSSFADE_DURATION} seconds")
    else:
        print("Crossfade disabled")
    
    clips = get_media_clips(FOLDER_PATH)
    final_clip = concatenate_clips(clips)

    if final_clip:
        print(f"Writing final video to {OUTPUT_FILE}...")
        final_clip.write_videofile(OUTPUT_FILE, fps=30, codec="libx264", audio_codec="aac")
        print("Done!")
    else:
        print("No media files found.")