import moviepy.editor as mpe
import cv2
from Variables import *

path = f'{MATERIALS}/{FILENAME}'
video = mpe.VideoFileClip(path)
background = mpe.ImageClip(f'{MATERIALS}/back.png').resize(video.size)

chroma_video = video.fx(mpe.vfx.mask_color, color=COLOR, thr=THR, s=S)

final_video = mpe.CompositeVideoClip([
    background.set_duration(video.duration),
    chroma_video.set_duration(video.duration)
])

out_path = f'{OUT_DIR}/{OUT_FILE}'
output = final_video.write_videofile(
    out_path,
    codec="libx264",
    audio_codec="aac",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    frame = 30
)