#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image
from pytesseract import pytesseract

def see_it(path_to_image):
    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img).strip()
    values = text.split(",")
    if len(values) < 2:
        raise RuntimeError(f"Could not identify list of values from text: {values}")
    print(" ".join(values))

def main():
    see_it(sys.argv[1])

if __name__ == "__main__":
    main()
