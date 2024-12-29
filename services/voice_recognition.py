import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {command}")
            return command
        except sr.UnknownValueError:
            print("Não entendi. Pode repetir?")
        except sr.RequestError:
            print("Erro ao acessar o serviço de reconhecimento de voz.")
    return None
