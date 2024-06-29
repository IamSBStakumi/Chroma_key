import numpy as np

# 動画素材の置き場
MATERIALS = 'materials'
FILENAME = 'Sample.mp4'

# 出力するフォルダ/ファイル名を指定
OUT_DIR = 'outputs'
OUT_FILE = 'test.mp4'

# パラメータ設定
contrast_adjustment_value = 1.5  # コントラスト調整値
chroma_key_color = np.uint8([[[0, 255, 0]]])  # クロマキー処理の指定色（緑色）
chroma_key_threshold = 20  # クロマキー処理の閾値
noise_removal_iterations = 50  # ノイズ除去の繰り返し回数

# 透明度の計算式：d**s / (thr**s + d**s) (d: COLORとの距離、色差)
# d>>thr の場合は 1、d<<thr の場合は 0に近づく
# COLOR: マスクする色
# THR: しきい値
# S: 
COLOR = [63,94,72]
THR = 0
S = 1
