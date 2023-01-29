#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import sys

from PIL import Image
from pytesseract import pytesseract

from gtts import gTTS

def see_it(path_to_image):
    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img).strip()
    values = text.split(",")
    if len(values) < 2:
        raise RuntimeError(f"Could not identify list of values from text: {values}")
    return values

def say_it(values):
    save_directory = "sound_out"
    for i in range(len(values)):
        value = values[i]
        save_path = f"{save_directory}/value_{i}.mp3"
        tts = gTTS(value, lang='en', slow=True)
        tts.save(save_path)
    return save_directory

def main():
    say_it(see_it(sys.argv[1]))

if __name__ == "__main__":
    main()
