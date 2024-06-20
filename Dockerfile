# FROM python:3.11.9-slim-bullseye as builder

# 必要なパッケージ
# RUN apt-get update -q
# RUN apt-get -y upgrade --no-install-recommends
# RUN apt-get -y install libopencv-dev

# pipのアップグレードとpoetryのインストール
# RUN pip install --upgrade pip && \
#     pip install poetry && \
    # 仮想環境を作らないよう設定
#     poetry config virtualenvs.create false

# FROM python:3.11.9-slim-bullseye as dev
# タイムゾーンを日本に設定
# ENV TZ Asia/Tokyo

# COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# COPY --from=builder /usr/local/bin /usr/local/bin

# WORKDIR /workspace/app

# EXPOSE 8888

FROM python:3.11.9-slim

# pipのアップグレード
RUN pip install --upgrade pip

# パッケージのアップグレード、インストール
RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev

# poetryのインストール、設定
RUN pip install poetry
RUN poetry config virtualenvs.create false

# コンテナの作業ディレクトリを作成
RUN mkdir -p /workspace/app
WORKDIR /workspace/app

EXPOSE 8888
