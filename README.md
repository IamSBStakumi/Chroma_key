# Chroma_key

<img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">

## Requirement

- Docker version 26.1.0
- Docker Compose version v2.26.1

## Usage

```bash
git clone https://github.com/IamSBStakumi/Chroma_key.git
cd Chroma_key
docker compose up -d --build
docker container exec -it <Container Name> bash
```

Save the video you wish to edit in `materials` before running the program.

Then edit `src/Variables.py` as you like.

```bash
python src/movie.py
```

