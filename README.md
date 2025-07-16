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

<img width="995" height="880" alt="image" src="https://github.com/user-attachments/assets/dff9f4d0-f614-4791-a71d-0fb8072e10b2" />



<img width="1176" height="806" alt="image" src="https://github.com/user-attachments/assets/5fe00806-baef-48d8-850a-18d5c9bdd571" />


<img width="1343" height="611" alt="image" src="https://github.com/user-attachments/assets/1585c820-f7c0-47f3-b4a9-0989a5ce8958" />


