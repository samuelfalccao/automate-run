import pyautogui as pa
import pyperclip as pp
import time
import tkinter as tk

def main_program():
    # Coloque todo o seu código aqui
    print("\n\tOlá! Seja Bem-Vindo!\n")
    whatsMensage = input("\tInsira o nome do contato/grupo: ")
    print("\n\tEnvie a mensagem para", whatsMensage, "!")
    mensageText = input("\n\t")

    def wait(seconds):
        time.sleep(seconds)

    wait(2)
    pa.hotkey("win", "s")
    wait(2)
    pa.write("Google Chrome")
    wait(2)
    pa.press("Enter")
    wait(2)
    pa.hotkey("ctrl", "t")
    wait(2)
    pa.write("https://web.whatsapp.com/")
    wait(2)
    pa.press("Enter")
    wait(8)
    pa.moveTo(212, 164)
    wait(2)
    pa.click(197, 167)
    wait(2)

    # Copiar e colar o nome do contato/grupo
    pp.copy(whatsMensage)
    wait(2)
    pa.hotkey("ctrl", "v")
    wait(2)
    pa.press("Enter")

    # Copiar e colar o texto da mensagem
    pp.copy(mensageText)
    wait(2)
    pa.hotkey("ctrl", "v")
    wait(2)
    pa.press("Enter")
    
    pass

def create_gui():
    root = tk.Tk()
    root.configure(bg="blue")

    # Criando um widget Text
    text_widget = tk.Text(root, bg="blue", fg="white", font=("Arial", 12))
    text_widget.pack(expand=True, fill="both")

    # Conteúdo do código
    code_content = """ ... """

    # Inserindo o conteúdo do código no widget Text
    text_widget.insert(tk.END, code_content)

    root.mainloop()

# Chamar a função de criação da interface gráfica
create_gui()
