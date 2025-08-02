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
for name, info in config['buttons'].items():
    buttons[name] = Button(info['pin'], pull_up=pull_up, bounce_time=bounce_time, hold_time=hold_time, hold_repeat=hold_repeat)



outputs = {}
for key, value in config["outputs"].items():
    outputs[key] = value
    
    
all_chars = [char for char in set(outputs.values()) if char is not None] 
    