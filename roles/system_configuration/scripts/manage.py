#!/usr/bin/python3

import syslog
import re
import os
import json
from Xlib import display
from Xlib.ext import randr
from ruamel.yaml.main import round_trip_dump as yaml_dump
from displaymanagement.display import Display

# Yaml commentary
from ruamel.yaml.comments import CommentedMap as OrderedDict

class ZDisplay():

    def __init__(self):
        self.tsRESET_COMMENT_LIST = [None, [], None, None]
        self.INDENTATION = 2
        self.DISPLAY_ID = ':0'
        self.display = display.Display(':0')
        self.screen = self.display.screen(0)
        self.window = self.screen.root

   
    def set_display(self):

        display = Display(self.DISPLAY_ID)
        screen = display.Screens[0]
        
        # Get an active output
        outputs = screen.Outputs
        for output in outputs.values():
            if output.Connected:
                # Change the output position
                X = 1920 
                Y = 0
                output.set_position(X, Y)


    # def get_lid_state(self):
    #     """get_lid_state."""
    #     lid_path = "/proc/acpi/button/lid/LID0/state"
    #     lid_state = "unknown"
    #     if os.path.exists(lid_path):
    #         file = open(lid_path, "r")
    #         lid_state = re.sub(r"state:[\n\t\s]+", "", file.read()).rstrip()
    #         file.close()
    #     return lid_state
    
    # def get_modes(self):
    #     res = randr.get_screen_resources(self.window)
    #     modes = {}
    #     for mode in res._data["modes"]:
    #         object = mode._data
    #         id = object["id"]
    #         modes[id] = object
    #     return json.dumps(modes)
    
    # def get_crtc(self, crtc):
    #     data = randr.get_crtc_info(self.window, crtc, 0)
    #     return json.dumps(data._data)
  
    # def get_outputs(self):
    #     output = self.screen
    #     print(output)

    # def set_order(self):

    #     randr.set_output_primary(self.window, 2)
    #     # randr.set_crtc_config(self.window, 78, 0, 1000, 1000, 0, 115, 0)





    # def get_active_randr_outputs(self):
    #     """get_active_randr_outputs."""
    #     res = randr.get_screen_resources(self.window)
    #     outputs = []
    #     for output in res.outputs:
    #         info = randr.get_output_info(self.window, output, 0)
    #         if info.connection == 0:
    #             outputs.append(info._data)
    #     return json.dumps(outputs)
    
    # def get_current_user(self):
    #     """get_current_user."""
    #     return os.getlogin()
    
    # def create_user_config_dir(self, user):
    #     """create_user_config_dir.
    
    #     :param user:
    #     """
    #     config_dir = "/home/{}/.config/zdisplay".format(user)
    #     if not os.path.exists(config_dir):
    #         os.mkdir(config_dir)
    #     return config_dir
    
    # def create_user_config_file(self, config_dir, lid_state, outputs_info):
    #     """create_user_config_file.
    
    #     :param config_dir:
    #     :param lid_state:
    #     :param outputs_info:
    #     """
    #     file_name_with_path = config_dir + "/" + "_".join(list(map(lambda x: x.name, outputs_info))) + ".cfg"
        
    #     if not os.path.isfile(file_name_with_path):
    #         data = OrderedDict()
    #         order = 0
    #         for output in outputs_info:
    #             data[output.name] = OrderedDict()
    #             data[output.name]["order"] = order
    #             order += 1
    #         f = open(file_name_with_path, "w")
    #         f.write(yaml_dump(data, indent=self.INDENTATION, block_seq_indent=self.INDENTATION))
    #         f.close()
    
    # def print_json(self, data):
    #     """print_json.
    
    #     :param data:
    #     """
    #     print(json.dumps(json.loads(data), indent=2))

if __name__ == "__main__":

    zd = ZDisplay()
    zd.set_display()
    # syslog.syslog(syslog.LOG_INFO, "Lid state: {}".format(zd.get_lid_state()))

    # lid_state = zd.get_lid_state()
    # outputs_info = zd.get_active_randr_outputs()
    # user = zd.get_current_user()
    # config_dir = zd.create_user_config_dir(user)
    # # create_user_config_file(config_dir, lid_state, outputs_info)

    # modes = zd.get_modes()
    # zd.print_json(outputs_info)
    # zd.print_json(modes)

    # zd.print_json(zd.get_crtc(79))
    # zd.print_json(zd.get_crtc(78))
   
    # # zd.get_outputs()
    # # zd.set_order()

