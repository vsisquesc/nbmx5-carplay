from signal import pause
import time

import libs.config
import libs.uinput
import libs.actions


# configuración
buttons = libs.config.buttons
device = libs.uinput.build_device(libs.config.actions)
        
# globales
MASK = 0 

def check_btns():
    global MASK
    MASK = (buttons['driver_up'].is_pressed)     | \
           (buttons['driver_down'].is_pressed << 1) | \
           (buttons['passenger_up'].is_pressed << 2) | \
           (buttons['passenger_down'].is_pressed << 3)

        
def dispatchFunction(held = False):
    global MASK
 
    currMask = held << 4 | MASK
    if currMask in libs.config.inputs and libs.config.inputs[currMask]!= None:
        mapping = libs.config.inputs[currMask]
        # print("mapping",mapping)
        action = libs.actions.get_action(mapping)
        # print("action",action)
        if action != None:
            key = libs.config.actions[action]
            print("key",key)
            libs.uinput.type_char(device, key)
    MASK = 0
        


buttons['driver_up'].when_pressed = check_btns
buttons['driver_down'].when_pressed = check_btns
buttons['passenger_up'].when_pressed = check_btns
buttons['passenger_down'].when_pressed = check_btns

buttons['driver_up'].when_released = dispatchFunction
buttons['driver_down'].when_released = dispatchFunction
buttons['passenger_up'].when_released = dispatchFunction
buttons['passenger_down'].when_released = dispatchFunction

buttons['driver_up'].when_held = lambda : dispatchFunction(True)
buttons['driver_down'].when_held = lambda : dispatchFunction(True)
buttons['passenger_up'].when_held = lambda : dispatchFunction(True)
buttons['passenger_down'].when_held = lambda : dispatchFunction(True)

pause()

