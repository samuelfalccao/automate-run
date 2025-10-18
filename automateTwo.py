from automate_run_Utils_Two import *

os.system('cls')

while True:
    whats_message = input("\n\tEnter the name of the contact or group: ")
    os.system('cls')
    print("\n\tSend the message to", whats_message, "!")
    message_text = input("\n\t\t")
    os.system('cls')
    print(f"\n\tDo you want to convert '{message_text}' to audio?")
    print("\n\t| 0: Yes | 1: No |")
    audio_run = wait_for_0_or_1()
    os.system('cls')

    if audio_run == '0':
        try:
            audio_file = convert_text_to_audio(message_text)
            print("\n\tMessage converted to audio successfully!")
        except Exception as e:
            print(f"\n\tError converting message to audio: {e}")
    else:
        print("\n\tAudio conversion canceled.")
        os.system('cls')
    
    # Abrindo o navegador
    subprocess.Popen([r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
    wait(5)
    human_like_move(658, 444)
    wait(3)
    pa.click(658, 444)
    wait(10)
    pa.hotkey("ctrl", "t")
    wait(3)
    human_like_typing("https://web.whatsapp.com/")
    wait(3)
    pa.press("Enter")
    wait(60)


    # Copiar e colar o nome do contato/grupo
    with auto_wait(5) as pa:
        human_like_move(212, 164)
        pa.click(197, 167)
        #pp.copy(whats_message)
        #pa.hotkey("ctrl", "v")
        human_like_typing(whats_message)
        pa.press("Enter")

    if audio_run == '0':
        with auto_wait(7) as pa:
            human_like_move(514, 697)
            pa.click(514, 697)
            human_like_move(525, 386)
            pa.click(525, 386)
            human_like_move(84, 181)
            pa.doubleClick(84, 181)
            pa.hotkey("ctrl", "f")
            pp.copy(audio_file)
            pa.hotkey("ctrl", "v")
            pa.press("Enter")
            human_like_move(200, 125)
            pa.doubleClick(200, 125)
            pa.press("Enter")
            human_like_move(635, 696)
            pa.click(635, 696)
            human_like_typing("Audiozinho para você!")
            pa.press("Enter")
    else:
        # Copiar e colar a mensagem
        with auto_wait(5) as pa:
            #pp.copy(message_text)
            #pa.hotkey("ctrl", "v")
            human_like_typing(message_text)
            pa.press("Enter")
    
    print("\n\tTask Successfully Completed!")
    print("\n\tWould you like to send another message?")
    print("\n\t| 0: Yes | 1: No |")
    prog = wait_for_0_or_1()
    
    if prog == '1':
        print("\n\tThank you for using the program!")
        break
