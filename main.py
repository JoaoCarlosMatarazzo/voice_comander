from services.voice_recognition import listen_command
from services.voice_feedback import speak
from utils.command_processor import process_command

def main():
    speak("Boas vindas ao sistema de automação por voz.")
    while True:
        speak("Diga um comando.")
        command = listen_command()
        if command:
            response = process_command(command)
            speak(response)
        if "sair" in command.lower():
            speak("Encerrando o sistema. Até logo!")
            break

if __name__ == "__main__":
    main()
