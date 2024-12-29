light_state = "apagada"

def toggle_light(state):
    global light_state
    light_state = "acesa" if state == "on" else "apagada"

def light_status():
    return light_state
