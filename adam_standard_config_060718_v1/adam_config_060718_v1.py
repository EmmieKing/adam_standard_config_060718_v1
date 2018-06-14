"""
    set up adam configuration paths
"""
import json
import sys
from os.path import expanduser

class setPaths(object):
    #def Paths():
        #global relativePaths
        home = expanduser("~")

        if home.find(':') == 1 : # true for Windows OS
            configDir = home + "\\adam"
            OS = "\\"
        else :
            configDir = home + "/adam"
            OS = "/"

        config_file = configDir + OS + 'adam_config_060718.json'


        with open(config_file, 'r') as f:
            raw_config = json.load(f)
            adam_path = home + OS + raw_config['ADAM_config']['adam_package_path']
            data_path = adam_path + OS + raw_config['ADAM_config']['data_path']
            env_config_path = adam_path + OS + raw_config['ADAM_config']['environment_config_file']
                
    #return relativePaths
        