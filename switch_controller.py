import yaml
from gpiozero import Button
import subprocess
from signal import pause
from threading import Thread
import time

# Leer configuración desde config.yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Extraer tiempos
repeat_delay = config['delays']['repeat_delay']
hold_threshold = config['delays']['hold_threshold']

# Crear botones desde la configuración
buttons = {}
for name, info in config['buttons'].items():
    buttons[name] = Button(info['pin'])

# Crear lista de botones
buttons_list = list(buttons.values())

# Crear mapa de botones individuales
single_key_map = {buttons[name]: info['key'] for name, info in config['buttons'].items()}

# Crear mapas de combinaciones
def parse_combo(combo_str):
    names = combo_str.split('+')
    return tuple(sorted([buttons[name] for name in names], key=lambda b: id(b)))

combination_key_map = {parse_combo(k): v for k, v in config['combinations']['short'].items()}
hold_combination_key_map = {parse_combo(k): v for k, v in config['combinations']['long'].items()}

# Función para obtener botones pulsados
def get_pressed_keys():
    return [button for button in buttons_list if button.is_pressed]

# Función principal para gestionar pulsaciones
def hold_keys(button):
    start_time = time.time()
    combo_sent = False

    while button.is_pressed:
        pressed = get_pressed_keys()
        elapsed = time.time() - start_time

        if len(pressed) == 2:
            if not combo_sent:
                pressed_combo = tuple(sorted(pressed, key=lambda b: id(b)))

                if elapsed < hold_threshold:
                    combo_key = combination_key_map.get(pressed_combo)
                else:
                    combo_key = hold_combination_key_map.get(pressed_combo)

                if combo_key:
                    subprocess.run(['xdotool', 'key', combo_key])
                combo_sent = True
        elif len(pressed) == 1:
            key = single_key_map.get(pressed[0])
            if key:
                subprocess.run(['xdotool', 'key', key])
            time.sleep(repeat_delay)
        else:
            break

# Función para cuando un botón se pulsa
def on_button_pressed(button):
    Thread(target=hold_keys, args=(button,), daemon=True).start()

# Asociar eventos
for button in buttons_list:
    button.when_pressed = lambda b=button: on_button_pressed(b)

# Mantener vivo
pause()
