# Chroma_key_Movie_Creator

<img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">

## Requirement

- Ubuntu 22.04.4

or

- Windows 11

## Usage

### 1. Download

```bash
git clone https://github.com/IamSBStakumi/Chroma_key_Movie_Creator.git
cd Chroma_key_Movie_Creator
```

### 2. Create .venv

```bash
poetry install
```

### 3. Create Movie

Save the video you wish to edit in `materials` directory before running the program.
Also, save the picture you wish to use as the background.

Then, edit `src/Variables.py` as you like.

```bash
poetry run python src/create_movie.py
```
