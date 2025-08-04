import libs.config

def get_action(mapping):
    action = libs.config.mappings[mapping]
    if action == None:
        return None
    if action in libs.config.custom_actions:
        custom_action = action
        action_list = libs.config.custom_actions[custom_action].split("_")
        action = action_list[0]
        libs.config.custom_actions[custom_action] =  "_".join(__shift_list(action_list))
        
    return action


def __shift_list(input_list):
    return input_list[1:] + input_list[:1] 