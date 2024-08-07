import numpy as np

# 動画素材の置き場
MATERIALS = 'materials'
FILENAME = 'Sample.mp4'

# 出力するフォルダ/ファイル名を指定
OUT_DIR = 'outputs'
OUT_FILE = 'output.mp4'

# パラメータ設定
contrast_adjustment_value = 1.5  # コントラスト調整値
chroma_key_color = np.uint8([[[0, 255, 0]]])  # クロマキー処理の指定色（緑色）
chroma_key_threshold = 20  # クロマキー処理の閾値
noise_removal_iterations = 50  # ノイズ除去の繰り返し回数

