import uinput


def get_key_code(char):
    key_name = f"KEY_{char.upper()}"
    return getattr(uinput, key_name, None)

def type_char(device, char):
    key = get_key_code(char)
    if not key:
        return

    if char.isupper():
        device.emit(uinput.KEY_LEFTSHIFT, 1)
        device.emit_click(key)
        device.emit(uinput.KEY_LEFTSHIFT, 0)
    else:
        device.emit_click(key)

 
 
def build_device(actions):
    
    chars = set(actions.values())
    # Construir lista de códigos necesarios
    uinput_keys = [uinput.KEY_LEFTSHIFT]  # por si hay mayúsculas
    for char in chars:
        key_code = get_key_code(char)
        if key_code:
            uinput_keys.append(key_code)
        else:
            print(f"Advertencia: tecla '{char}' no reconocida por uinput")
    # Crear el dispositivo con las teclas necesarias
    device = uinput.Device(uinput_keys)  
    return device