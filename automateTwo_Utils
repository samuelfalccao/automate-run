import pygame
import keyboard
import pyautogui as pa
import pyperclip as pp
import pyttsx3
import time
from contextlib import contextmanager
import subprocess
import random
import os

pygame.mixer.init()

def wait_for_0_or_1():
    while True:
        event = keyboard.read_event(suppress=True)  # 'suppress=True' evita que a tecla apareça no terminal
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '0':
                print("\n\n\tYou chose yes!")
                return '0'
            elif event.name == '1':
                print("\n\n\tYou chose no!")
                return '1'
            elif event.name.lower() == 'esc':
                print("\n\n\tProgram closed.")
                keyboard.unhook_all()
                exit()

def convert_text_to_audio(text):
    engine = pyttsx3.init()
    filename = f"audio_{int(time.time())}.mp3"
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename

def wait(seconds):
    time.sleep(seconds)

@contextmanager
def auto_wait(seconds):
    class Wrapper:
        def __getattr__(self, attr):
            def wrapper(*args, **kwargs):
                result = getattr(pa, attr)(*args, **kwargs)
                time.sleep(seconds)
                return result
            return wrapper
    yield Wrapper()

def human_like_move(x, y, duration=1):
    start_x, start_y = pa.position()
    steps = max(1, int(duration * 30))
    
    for i in range(steps):
        new_x = start_x + (x - start_x) * (i / steps) + random.uniform(-1, 1)
        new_y = start_y + (y - start_y) * (i / steps) + random.uniform(-1, 1)
        pa.moveTo(new_x, new_y, duration=0.02)
        time.sleep(0.01)

def human_like_typing(text):
    typing_sound = pygame.mixer.Sound("typing_soundOne.wav")

    for char in text:
        typing_sound.play() # Tocar o som a cada caractere digitado
        pa.write(char)
        time.sleep(random.uniform(0.05, 0.2))
        typing_sound.stop()
