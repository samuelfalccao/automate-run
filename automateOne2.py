import pyautogui as pa
import pyperclip as pp
import time
import keyboard
import pyttsx3
import pygame


pygame.mixer.init()


def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == '0':
            print("\n\n\tVocê escolheu Sim")
            pa.press("Enter")
        elif e.name == '1':
            print("\n\n\tVocê escolheu Não")
            pa.press("Enter")
        elif e.name.lower() == 'esc':
            print("\n\n\tPrograma encerrado.")
            keyboard.unhook_all()

keyboard.hook(on_key_event)

def convert_text_to_audio(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'audio.mp3')
    engine.runAndWait()

def wait(seconds):
    time.sleep(seconds)


while True:
    whats_message = input("\n\tInsira o nome do contato/grupo: ")
    print("\n\tEnvie a mensagem para", whats_message, "!")
    message_text = input("\n\t\t")
    print(f"\n\tDeseja converter '{message_text}' em áudio?")
    audio_run = int(input("\n\t| 0: Sim | 1: Não | : "))

    if audio_run.lower() == '0':
        try:
            convert_text_to_audio(message_text)
            print("\n\tMensagem convertida em áudio com sucesso!")
        except Exception as e:
            print(f"\n\tErro ao converter em áudio: {e}")
            
    elif audio_run.lower() == '1':
        print("\n\tConversão de áudio cancelada.")
     
    # Abrindo o Navegador
    wait(8)
    pa.hotkey("win", "s")
    wait(8)
    pa.write("Google Chrome", interval=0.3)
    wait(8)
    pa.press("Enter")
    wait(8)
    pa.hotkey("ctrl", "t")
    wait(8)
    pa.write("https://web.whatsapp.com/")
    wait(8)
    pa.press("Enter")
    wait(10)
    pa.moveTo(212, 164, duration=2)
    wait(10)
    pa.click(197, 167)
    wait(10)

    # Copiar e colar o nome do contato/grupo
    pp.copy(whats_message)
    wait(3)
    pa.hotkey("ctrl", "v")
    wait(2)
    pa.press("Enter")
    wait(5)

    if audio_run.lower() == '0':
        pa.moveTo(468, 828)
        wait(2)
        pa.click(467, 828)
        wait(2)
        pa.click(511, 570)
        wait(2)
        pa.click(385, 46)
        wait(2)
        pa.press("Delete")
        wait(3)
        endCami = (r"C:\Users\PHTABULEIRO\Videos\Samuel\3. Programming\1. Python\2. Codes\2. cd_automate\automate_three")
        pp.copy(endCami)
        wait(2)
        pa.hotkey("ctrl", "v")
        wait(2)
        pa.press("Enter")
        wait(3)
        pa.click(237, 157)
        wait(4)
        pa.press("Enter")
        wait(3)
        pa.write(str("Audiozinho para voce!"))
        wait(3)
        pa.press("Enter")
        
    elif  audio_run.lower() == '1':
        # Copiar e colar o texto da mensagem
        pp.copy(message_text)
        wait(2)
        pa.hotkey("ctrl", "v")
        wait(2)
        pa.press("Enter")
        
    print("\n\tTarefa Finalizada Com Sucesso!")
    prog = int(input("\n\tDeseja enviar alguma outra mensagem? \n\t| 0: Sim | 1: Não | : "))
    print("\n\t-----------------------------------------")
    if prog.lower() == '1':
        print("\n\tObrigado por usar o programa!")
        break
