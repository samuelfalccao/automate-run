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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import filedialog
from PIL import Image



pygame.mixer.init()



def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        
        if e.name == '0':
            print("\n\n\tYou chose yes!")
            pa.press("Enter")
            
        elif e.name == '1':
            print("\n\n\tYou chose no!")
            pa.press("Enter")
            
        elif e.name.lower() == 'esc':
            print("\n\n\tProgram closed.")
            keyboard.unhook_all()

keyboard.hook(on_key_event)

def convert_text_to_audio(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'audio.mp3')
    engine.runAndWait()
    
    # Faz o download do arquivo de áudio
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/path/to/your/download/folder",  # Altere o caminho para a pasta de download desejada
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    service = Service('/path/to/chromedriver')  # Altere o caminho para o seu chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get('file://' + 'audio.mp3')  # Abre o arquivo local no navegador
    time.sleep(5)  # Dá tempo para o download começar
    driver.find_element(By.XPATH, "//a[contains(.,'audio.mp3')]").click()  # Clica no link de download
    time.sleep(5)  # Espera o download terminar
    driver.quit()  # Fecha o navegador após o download

def open_image(image):
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        # Faz alguma coisa com a imagem, como exibir
        image.show()

def wait(seconds):
    time.sleep(seconds)

@contextmanager
def auto_wait(seconds, **module_aliases):
    class Wrapper:
        def __init__(self, module):
            self.module = module
        
        def __getattr__(self, attr):
            original_attr = getattr(self.module, attr)

            if callable(original_attr):  # Se for uma função/método
                def wrapped_function(*args, **kwargs):
                    result = original_attr(*args, **kwargs)  # Chama a função original
                    time.sleep(seconds)  # Aguarda automaticamente
                    return result
                return wrapped_function
            return original_attr  # Se for variável, retorna direto
    
    wrapped_modules = {alias: Wrapper(module) for alias, module in module_aliases.items()}  
    yield wrapped_modules  # Retorna os módulos modificados

def human_like_move(x, y, duration=2):
    start_x, start_y = pa.position()  # Posição inicial do mouse
    steps = int(duration * 50)  # Número de pequenos passos no movimento

    for i in range(steps):
        new_x = start_x + (x - start_x) * (i / steps) + random.uniform(-1, 1)
        new_y = start_y + (y - start_y) * (i / steps) + random.uniform(-1, 1)
        pa.moveTo(new_x, new_y, duration=0.02)  # Pequenos movimentos rápidos
        time.sleep(0.01)

def human_like_typing(text):
    for char in text:
        pa.write(char)
        time.sleep(random.uniform(0.05, 0.2))  # Variação no tempo entre as teclas



while True:
    whats_message = input("\n\tEnter the name of the contact or group: ")
    print("\n\tSend the message to", whats_message, "!")
    message_text = input("\n\t\t")
    print(f"\n\tDo you want to convert '{message_text}' to audio?")
    audio_run = input("\n\t| 0: Yes | 1: No | : ")

    if audio_run.lower() == '0':
        try:
            convert_text_to_audio(message_text)
            print("\n\tMessage converted to audio successfully!")
        
        except Exception as e:
            print(f"\n\tError converting message to audio: {e}")
            
    elif audio_run.lower() == '1':
        print("\n\tAudio conversion canceled.")
     
    print("\n\tDo you want to send any image to", whats_message, "?")
    image_run = input("\n\t| 0: Yes | 1: No | : ")
    
    if image_run.lower() == '0':
        open_image()
        
    elif image_run.lower() == '1':
        # Opening the Browser
        with auto_wait(5, pa=pa) as mods:
            wait(5)
            chrome_path = os.path.join(os.getenv("PROGRAMFILES(X86)", "C:\\Program Files (x86)"), "Google", "Chrome", "Application", "chrome.exe")
            subprocess.Popen([chrome_path])
            human_like_move(658, 444)
            pa.click(658, 444)
            pa.hotkey("ctrl", "t")
            human_like_typing("https://web.whatsapp.com/")
            pa.press("Enter")
            human_like_move(212, 164)
            pa.click(197, 167)

        # Copy and paste the contact/group name
        with auto_wait(5, pa=pa, pp=pp) as mods:
            pa = mods["pa"]  # PyAutoGUI com auto-wait
            pp = mods["pp"]  # Pyperclip com auto-wait
            pp.copy(whats_message)
            pa.hotkey("ctrl", "v")
            pa.press("Enter")

    if audio_run.lower() == '0':
        with auto_wait(5, pa=pa) as mods:
            pa = mods["pa"]  # PyAutoGUI com auto-wait
            pa.moveTo(468, 828)
            pa.click(467, 828)
            pa.click(511, 570)
            pa.click(239, 164)
            pa.press("Enter")
            pa.write("Audiozinho para você!")
            pa.press("Enter")
        
    elif  audio_run.lower() == '1':
        # Copy and paste the message text
        with auto_wait(5, pa=pa, pp=pp) as mods:
            pa = mods["pa"]  # PyAutoGUI com auto-wait
            pp = mods["pp"]  # Pyperclip com auto-wait
            pp.copy(message_text)
            pa.hotkey("ctrl", "v")
            pa.press("Enter")
        
    print("\n\tTask Successfully Completed!")
    prog = input("\n\tWould you like to send another message? \n\t| 0: Yes | 1: No | : ")
    print("\n\t-----------------------------------------")
    if prog.lower() == '1':
        print("\n\tThank you for using the program!")
        break
