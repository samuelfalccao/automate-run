import time
import subprocess
import pyautogui as pa

mensagem = ("Hello World!")

def wait(seconds):
    time.sleep(seconds)

subprocess.Popen("C:\Program Files\Sublime Text 3\sublime_text.exe")
wait(10)
pa.write(mensagem)
