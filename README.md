# nbmx5-carplay
# GPIO Keyboard Emulator for Raspberry Pi

Este proyecto permite usar interruptores conectados a los pines GPIO de una Raspberry Pi para emular pulsaciones de teclado.

## Requisitos

- Raspberry Pi OS
- Python 3
- Paquetes necesarios:

```bash
sudo apt update
sudo apt install xdotool
pip install gpiozero pyyaml
```

## Archivos

- `controller.py`: Script principal
- `config.yaml`: Archivo de configuración de pines, teclas y combinaciones

## Uso

Ejecuta el script manualmente con:

```bash
python3 controller.py
```

## Ejecución automática al arrancar

1. Abre el crontab del usuario:

```bash
crontab -e
```

2. Añade esta línea al final (ajustando la ruta):

```bash
@reboot python3 /home/pi/gpio-controller/controller.py &
```

Guarda y cierra. El script se ejecutará automáticamente cada vez que la Raspberry Pi arranque.

## Notas

- Asegúrate de que el script tenga permisos de ejecución.
- Verifica la ruta del archivo `controller.py` según dónde lo coloques.
