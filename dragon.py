import json
from parser import *
BASEURL = 'example_project/'
config_data = open (BASEURL + 'config.json').read()
config = json.loads(config_data)
for item in config['load']:
    loadFile(item)
