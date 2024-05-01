import moviepy.editor as mpe

# 動画素材の置き場
MATERIALS = 'materials'
FILENAME = 'cow.mp4'

# 出力するフォルダ/ファイル名を指定
OUT_DIR = 'outputs'
OUT_FILE = 'test.mp4'

path = f'{MATERIALS}/{FILENAME}'
video = mpe.VideoFileClip(path)

# COLOR: マスクする色 THR: しきい値 S: 距離
COLOR = [0,255,0]
THR = 20
S = 3
masked_video = mpe.vfx.mask_color(video, color=COLOR, thr=THR, s=S)

out_path = f'{OUT_DIR}/{OUT_FILE}'
output = masked_video.write_videofile(
    out_path,
    codec="libx264",
    audio_codec="aac",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True
)