global BASEURL
BASEURL = 'example_project/'
import json
from parser import *
with open('build.tex', "w") as file:
    file.truncate()
config_data = open (BASEURL + 'config.json').read()
config = json.loads(config_data)
for item in config['load']:
    loadFile(item)
