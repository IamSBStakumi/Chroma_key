import moviepy.editor as mpe
from Variables import *

path = f'{MATERIALS}/{FILENAME}'
video = mpe.VideoFileClip(path)

masked_video = mpe.vfx.mask_color(video, color=COLOR, thr=THR, s=S)

out_path = f'{OUT_DIR}/{OUT_FILE}'
output = masked_video.write_videofile(
    out_path,
    codec="libx264",
    audio_codec="aac",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True
)