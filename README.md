# tfl-sort
TfL sorting algorithm

The TfL sorting algorithm is inspired by Transport for London.

1. See it

Save the list of objects as an image (JPG, GIF, PNG etc). Provide it as input to an image-to-text model.

2. Say it

Pass the text as input to a text-to-speech model.

3. Sorted

A third, speech-to-text model parses the output and sorts it.

## Install

```
sudo apt update && sudo apt install -y python3-pil tesseract-ocr libtesseract-devffmpeg
pip install pytesseract pillow SpeechRecognition pydub
```

## Run

```
python run.py input.jpg
```