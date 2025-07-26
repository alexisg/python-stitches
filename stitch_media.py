import os
from moviepy import (
    ImageClip,
    VideoFileClip,
    concatenate_videoclips
)
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy import ColorClip

# --- CONFIGURATION ---
FOLDER_PATH = "./media"   # Change to your media folder
IMAGE_DURATION = 15       # Seconds
FADE_DURATION = 1.0       # Crossfade duration
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
    return concatenate_videoclips(clips)

if __name__ == "__main__":
    print("Processing media...")
    clips = get_media_clips(FOLDER_PATH)
    final_clip = concatenate_clips(clips)

    if final_clip:
        print(f"Writing final video to {OUTPUT_FILE}...")
        final_clip.write_videofile(OUTPUT_FILE, fps=30, codec="libx264", audio_codec="aac")
        print("Done!")
    else:
        print("No media files found.")