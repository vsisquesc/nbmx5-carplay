import yaml
import sys
from gpiozero import Button


path = sys.path[0]
with open(path+'/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

 
    
pull_up = config["settings"]["pull_up"]
bounce_time = config["settings"]["bounce_time"]
hold_time = config["settings"]["hold_time"]
hold_repeat = config["settings"]["hold_repeat"]
repeat_delay = config['settings']['repeat_delay']

buttons = {}
for name, pin in config['gpio'].items():
    buttons[name] = Button(
        pin, 
        pull_up=pull_up, 
        bounce_time=bounce_time,
        hold_time=hold_time, 
        hold_repeat=hold_repeat
    )



inputs = config["inputs"]
mappings = config["mappings"]
actions = config["actions"]
custom_actions = config["custom_actions"]