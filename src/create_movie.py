import cv2
import numpy as np

from Variables import *

# 動画と背景画像の読込
path = f'{MATERIALS}/{FILENAME}'
video = cv2.VideoCapture(path)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
back = cv2.imread(f'{MATERIALS}/back.jpg')
back = cv2.resize(back, (width, height))
print("動画読み込み")

# 動画の総フレーム数を取得
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print("フレーム数読み込み")

# 書き出し用のwriteクラスを作成
fps = video.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(f'{OUT_DIR}/{OUT_FILE}', fourcc, fps, (width, height), 1)
print("ライタークラス作成")

# 音声トラック書き出し
# clip_input = mpe.VideoFileClip(path)
# clip_input.audio.write_audiofile("outputs/audio.mp3")
# print("音声トラック読み込み")

def create_frame(input_frame):
    # コントラスト調整
    contrast_image = cv2.convertScaleAbs(input_frame, alpha=contrast_adjustment_value, beta=0)

    # クロマキー処理と二値化
    hsv_chroma_key_color = cv2.cvtColor(chroma_key_color, cv2.COLOR_BGR2HSV)
    lower_green = np.array([hsv_chroma_key_color[0][0][0] - chroma_key_threshold, 50, 50])
    upper_green = np.array([hsv_chroma_key_color[0][0][0] + chroma_key_threshold, 255, 255])
    hsv_image = cv2.cvtColor(contrast_image, cv2.COLOR_BGR2HSV)
    chroma_key_image = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_image = cv2.bitwise_not(chroma_key_image)

    # ノイズ除去
    transparent_image = cv2.cvtColor(input_frame, cv2.COLOR_BGR2BGRA) # RGBA形式に変換
    transparent_image[:, :, 3] = mask_image # アルファチャンネルにマスク画像を設定
    
    # 背景画像に重ねる
    foreground = transparent_image[:, :, :3]
    alpha = transparent_image[:, :, 3:] / 255.0
    background = back.copy()

    output_frame = cv2.convertScaleAbs(background * (1 - alpha) + foreground * alpha)

    return output_frame

for i in range(frame_count):
    success, movie_frame = video.read()

    if not success:
        print("failed reading")
        break
    
    chroma_frame = create_frame(movie_frame)

    # 画像を動画へ書き出し
    writer.write(chroma_frame)

# 読み込んだ動画と書き出し先の動画を開放
video.release()
writer.release()

# 音声トラックを動画に追加
# clip = mpe.VideoFileClip("outputs/chroma.mp4").subclip()
# clip.write_videofile("outputs/result.mp4", audio="outputs/audio.mp3")

print("finish!")
