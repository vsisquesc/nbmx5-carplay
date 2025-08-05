import yaml
import sys
from gpiozero import Button


path = sys.path[0]
with open(path+'/config/settings.yaml', 'r') as f:
    settings = yaml.safe_load(f)
    
with open(path+'/config/controller.yaml', 'r') as f:
    controller = yaml.safe_load(f)


 
    
pull_up = settings["pull_up"]
bounce_time = settings["bounce_time"]
hold_time = settings["hold_time"]
hold_repeat = settings["hold_repeat"]

buttons = {}
for name, pin in settings['gpio'].items():
    buttons[name] = Button(
        pin, 
        pull_up=pull_up, 
        bounce_time=bounce_time,
        hold_time=hold_time, 
        hold_repeat=hold_repeat
    )



inputs = controller["inputs"]
mappings = controller["mappings"]
actions = controller["actions"]
custom_actions = controller["custom_actions"]