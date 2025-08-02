# nbmx5-carplay
# GPIO Keyboard Emulator for Raspberry Pi

Este proyecto permite usar interruptores conectados a los pines GPIO de una Raspberry Pi para emular pulsaciones de teclado.

0º partir de raspbian lite


1º Clonar React carplay
2º instalar openbox
```bash
   sudo apt install --no-install-recommends xserver-xorg xinit openbox chromium-browser
```
3º  Crear fichero .xinitrc
```bash
    nano ~/.xinitrc
```
4º Definir acciones a ejecutar cuando se lanza  ```startx```
```bash
    openbox &
    exec ~/apps/Carplay.AppImage --no-sandbox > ~/logs/Carplay.appimage.electron.log 2>&1
```
5º  Crear fichero .bash_profile
```bash
    nano ~/.bash_profile
```
6º Definir acciones a ejecutar cuando se lanza  ```startx```
```bash
   if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
        startx -- -nocursor
   fi
```
7º Habilitar login automatico creando el fichero   ```/etc/systemd/system/getty@tty1.service.d/autologin.conf ``` y dandole el siguiente valor
```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin user --noclear %I $TERM

```

8º soldar boton a los pines GPIO3 y ground
9º añadir esto al final de ```/boot/firmware/config.txt```
```bash
   [all]
   #power button
   dtoverlay=gpio-shutdown, gpio_pin=3
```
10º Conectar los cables del controlador de ventana a los pines

11º Crear reglas para el modulo kernel uinput
   - Abre o crea este archuivo
   ```bash
   sudo nano /etc/udev/rules.d/99-uinput.rules
   ```
   - El contenido del fichero debe ser
   ```
   KERNEL=="uinput", MODE="0666"
   ```

12º Habilitar persistencia para el modulo uinput
   - Abre o crea este archuivo
   ```bash
   sudo nano /etc/modules
   ```
   - Añade al final
   ```
   uinput
   ```






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

Guarda y cierra. El script se ejecutará automáticamente cada vez que la Raspberry Pi arranque.

## Notas

- Asegúrate de que el script tenga permisos de ejecución.
- Verifica la ruta del archivo `controller.py` según dónde lo coloques.

<img width="995" height="880" alt="image" src="https://github.com/user-attachments/assets/dff9f4d0-f614-4791-a71d-0fb8072e10b2" />



<img width="1176" height="806" alt="image" src="https://github.com/user-attachments/assets/5fe00806-baef-48d8-850a-18d5c9bdd571" />


<img width="1343" height="611" alt="image" src="https://github.com/user-attachments/assets/1585c820-f7c0-47f3-b4a9-0989a5ce8958" />



