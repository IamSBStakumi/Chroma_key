# 動画素材の置き場
MATERIALS = 'materials'
FILENAME = 'First.mp4'

# 出力するフォルダ/ファイル名を指定
OUT_DIR = 'outputs'
OUT_FILE = 'test.mp4'

# 透明度の計算式：d**s / (thr**s + d**s) (d: COLORとの距離、色差)
# d>>thr の場合は 1、d<<thr の場合は 0に近づく
# COLOR: マスクする色
# THR: しきい値
# S: 
COLOR = [63,94,72]
THR = 0
S = 1
