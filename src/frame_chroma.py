import os

import cv2
import moviepy.editor as mpe
import numpy as np
from PIL import Image

from Variables import *

path = f'{MATERIALS}/{FILENAME}'
video = cv2.VideoCapture(path)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
background = mpe.ImageClip(f'{MATERIALS}/back.jpg').resize((width, height))

for i in range(1): # 1フレーム分を処理
    success, frame = video.read()

    if not success:
        print(i, "failed")
        continue

    # HSV変換
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2値化する
    bin_img = ~cv2.inRange(hsv_frame, (62, 100, 0), (79, 255, 255))
    
    # 輪郭抽出
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 面積が最大の輪郭を取得する
    contour = max(contours, key=lambda x: cv2.contourArea(x))

    # マスク画像を作成
    mask = np.zeros_like(bin_img)
    cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
    
    # 合成
    dst = np.where(mask[:height, :width, np.newaxis] == 0, background, frame)
    out = 'chroma_frame{}.png'.format(str(i).zfill(3))

    print(dst)

    out_img = Image.fromarray(dst)

    out_img.save("outputs/f_img.png")
    # cv2.imwrite(os.path.join("outputs", out), Image(dst))

    # https://pystyle.info/opencv-mask-image/