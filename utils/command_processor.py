from components.light_control import light_status, toggle_light
from components.temperature_control import get_temperature

def process_command(command):
    command = command.lower()
    if "luz" in command:
        if "ligar" in command:
            toggle_light("on")
            return "A luz está acesa."
        elif "desligar" in command:
            toggle_light("off")
            return "A luz está apagada."
        else:
            return f"A luz está {light_status()}."
    elif "temperatura" in command:
        temperature = get_temperature()
        return f"A temperatura agora está a {temperature} graus."
    else:
        return "Comando não reconhecido. Por favor, tente novamente."
