#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import io
import sys

from PIL import Image
from pytesseract import pytesseract

from gtts import gTTS

import speech_recognition as sr
from pydub import AudioSegment
from contextlib import redirect_stdout


def see_it(path_to_image):
    '''See it'''
    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img).strip()
    values = text.split(",")
    return values

def say_it(values):
    '''Say it'''
    save_directory = "sound_out"
    for i, value in enumerate(values):
        save_path = f"{save_directory}/value_{i}.mp3"
        tts = gTTS(value, lang='en')
        tts.save(save_path)
    return save_directory

def recognize_google_without_output(audio_data):
    '''Prevent library from logging everything to stdout'''
    target = io.StringIO()
    with redirect_stdout(target):
        return sr.Recognizer().recognize_google(
            audio_data=audio_data,
            language="en-US",
            show_all=False,
            with_confidence=False
        )

def sorted(sound_directory):
    '''Sorted'''
    # find all wav files in directory, one level
    file_paths = glob.glob(f"{sound_directory}/*.mp3")

    values = []
    for p in file_paths:
        sound = AudioSegment.from_mp3(p)
        wav_path = f"{p}.wav"
        sound.export(wav_path, format="wav")
        audio = sr.AudioFile(wav_path)
        recogniser = sr.Recognizer()
        with audio as source:
            audio_text = recogniser.record(source)
            try:
                text = recognize_google_without_output(audio_data=audio_text)
                values.append(text)
            except sr.UnknownValueError as error:
                print(f"failed to parse text for file: {wav_path}, error: {error}")

    result = []
    for v in values:
        try:
            result.append(int(v))
        except ValueError:
            print(f"failed to convert value to int: {v}")

    #TODO: have an LLM do the sorting
    result.sort()
    return result

def main():
    print(sorted(say_it(see_it(sys.argv[1]))))

if __name__ == "__main__":
    main()
