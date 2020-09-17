# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-alpine

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# psycopg2とpillowのインストールの準備
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg\
    && apk add postgresql-dev
    
# pipのアプデ
RUN pip install --upgrade pip 

# ホストのrequirements.txtをコンテナの作業ディレクトリにコピー
COPY ./requirements.txt /usr/src/app/requirements.txt

# entrypoint.shをコピー
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# requirements.txtからパッケージをインストールしてDjango環境を構築
RUN pip install -r requirements.txt

# ホストのカレントディレクトリ（現在はappディレクトリ）を作業ディレクトリにコピー
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

WORKDIR /usr/src/app/sns_project