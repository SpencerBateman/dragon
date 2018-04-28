global BASEURL
BASEURL = 'example_project/'
import json
from parser import *
config_data = open (BASEURL + 'config.json').read()
config = json.loads(config_data)
for item in config['load']:
    loadFile(item)
